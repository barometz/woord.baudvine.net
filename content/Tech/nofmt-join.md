Title: nofmt::join
Tags: projects, c++
Lang: en
Date: 2023-08-28
Status: published

*This post is three parts journey, one part self-indulgence, and one part
this-might-be-useful-to-you. In short: I ported `fmt::join` to work with
`<format>`. You can find it at
[barometz/nofmt-join](https://github.com/barometz/nofmt-join).*

At work, we're hoping to switch some things from the excellent
[{fmt}](https://fmt.dev) library to the now standardized `<format>`. The one
largely inspired the other, so the porting burden won't be too much, and we get
to drop a dependency in a hundred different builds - some of which in turn
depend on each other, so there's some transitive lock-in with the version.

Package management mistakes aside, `<format>` lacks one thing I love from fmt:
[`fmt::join`](https://fmt.dev/latest/api.html#_CPPv4I0EN3fmt4joinE9join_viewIN6detail10iterator_tI5RangeEEN6detail10sentinel_tI5RangeEEERR5Range11string_view).

## What is `fmt::join`?

It looks a lot like Python's
[`str.join`](https://docs.python.org/3/library/stdtypes.html#str.join) at first
glance:

```c++
std::array names { "Atalant", "Yorden", "Nicholas" }; 
fmt::print("{}", fmt::join(names, ", "));
// prints "Atalant, Yorden, Nicholas"
```

Except it also works with other types fmt knows how to format:

```c++
std::list shoe_sizes { 39, 45, 43 };
fmt::print("{}", fmt::join(shoe_sizes, " & "));
// prints "39 & 45 & 43"
```

That by itself is convenient but not too exciting - you can do it in about ten
lines:

<details>
<summary>join.cpp (28 lines)</summary>
```c++
#include <iostream>
#include <list>
#include <string>
#include <sstream>

template<typename Range>
std::string join(Range&& range, std::string_view separator)
{
  std::stringstream result;
  // Stop if the range is empty.
  if (range.size() != 0) {
    // Write the first element to the output stream.
    result << *range.begin();
    auto next = std::next(range.begin());
    // Then, for each following element,
    for (auto it = next; it != range.end(); it++) {
      // Write the separator and element to the output stream.
      result << separator << *it;
    }
  }
  return result.str();
}

void fn()
{
  std::list shoe_sizes { 39, 45, 43 };
  std::cout << join(shoe_sizes, " & ");
}
```
</details>

But what makes `fmt::join` special is this:

```c++
std::array mac { 0x56, 0x10, 0x00, 0x67, 0x11, 0xEE };
fmt::print("{:02x}", fmt::join(mac, ":"));
// prints "56:10:00:67:11:EE"
```

That's right: you get to apply a format specifier (`:02x` in the example) to
each of the joined elements. Nothing's actually converted to a string before it
passes through `fmt::format` or `fmt::print`.

## `<format>` & join

So `<format>` doesn't include the `join` function template. It's tremendously
useful and not *entirely* trivial to write. It wasn't included in the [original
`<format>`
proposal](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2093r1.html)
- maybe the author wanted to limit the scope to ease acceptance, or maybe they
didn't want a conflict with an older [proposal for
std::join](https://www.open-std.org/JTC1/SC22/WG21/docs/papers/2013/n3594.html).
At any rate, I decided I wanted to port `fmt::join` to work with `<format>`.

## Porting

### The proof of concept
With this sort of thing it's helpful to start with a proof of concept - don't
worry too much about being tidy or having a well-organized commit history, just
get the thing running. So I pulled up a checkout of fmt I already had, and
copied the `fmt::join` function template itself. That doesn't build, clearly, so
I copied the type it returns:

```c++
template <typename It, typename Sentinel, typename Char>
struct arg_join {
  It begin;
  Sentinel end;
  std::basic_string_view<Char> sep;
};
```

It turns out that `fmt::join` doesn't do all that much - it takes your
parameters and turns it into a view of the range (delimited by `begin` and
`end`) plus a view of the separator. The real work happens in the formatter
defined for `arg_join`, which I'll get to later.

Copying the formatter isn't enough, though - there are still dependencies on
other fmt internals. Some of those provide C++ library features which were added
after C++11, while others are just fmt-internal. The former I can replace with
whatever's available in C++20 (since that's my porting target). Others, I copy
over until it builds.

### For real

Satisfied that everything fits together, I check out the latest release of fmt -
8.1.1 at the time - and get to work:

1. Copy all the chunks I copied during my proof of concept into my own header.
2. Add comments to each function and struct to indicate what file and line it's
   from.
3. Commit that as a baseline.
4. Make all the changes I made before to get it to compile in its new context.
5. Build.
6. .. doesn't work. Drat, still missing more bits.
7. Rebase to modify the first commit, `goto` 2.

After a little while of this I realized 8.1.1's `fmt::join` is more tightly
coupled with the fmt internals than whatever I'd previously been working with,
and so...

### For real, for real.

I went back to fmt 7.1.3, the latest release of fmt 7. This turned out to be
*much* simpler to port than what I'd started with: apart from `arg_join` and its
formatter, `fmt::join` 7.1.3 had no dependencies that I couldn't easily replace
with C++ standard library functions.

1. Copy `arg_join`, `fmt::formatter<arg_join<...>>`, and `fmt::join` from
   `fmt/format.h`.
2. [Commit
   that](https://github.com/barometz/nofmt-join/commit/8029add7e05c68d359173576d35c4ffc95f6c782)
   as a baseline.
3. Update everything to use the C++ standard library and adapt it to its new
   namespace.
4. [Commit
   that](https://github.com/barometz/nofmt-join/commit/fa6eaa9ba2ea5adecd0b4a6370dd5a21a71af709).

The end result, including tests and CI, is at
[barometz/nofmt-join](https://github.com/barometz/nofmt-join).

## How it works

As mentioned above, the "real work" happens in the formatter for `arg_join`:

<details>
<summary>std::formatter for arg_join (23 lines)</summary>
```c++
template <typename It, typename Sentinel, typename Char>
struct std::formatter<arg_join<It, Sentinel, Char>, Char>
    : std::formatter<typename std::iterator_traits<It>::value_type, Char> {
  template <typename FormatContext>
  auto format(
    const nofmt::arg_join<It, Sentinel, Char>& value,
    FormatContext& ctx)
      -> decltype(ctx.out()) {
    using base =
      formatter<typename std::iterator_traits<It>::value_type, Char>;
    auto it = value.begin;
    auto out = ctx.out();
    if (it != value.end) {
      out = base::format(*it++, ctx);
      while (it != value.end) {
        out = std::copy(value.sep.begin(), value.sep.end(), out);
        ctx.advance_to(out);
        out = base::format(*it++, ctx);
      }
    }
    return out;
  }
};
```
</details>

The core of which looks a lot like `join.cpp` above:

```c++
// Get the formatter for the elements' type
using base = formatter<typename std::iterator_traits<It>::value_type, Char>;
// Do nothing if the range is empty (begin == end)
if (it != value.end) {
  // Format the first element using the element formatter, passing on the
  // format context (which holds the format specifiers, among other things)
  out = base::format(*it++, ctx);
  while (it != value.end) {
    // Then, for each element, append the separator
    out = std::copy(value.sep.begin(), value.sep.end(), out);
    ctx.advance_to(out);
    // And format the element itself.
    out = base::format(*it++, ctx);
  }
}
```

## Next up: fmt 8

There's a reason fmt 8's `fmt::join` is less easy to port: it uses more
fmt-internal machinery which (if I'm reading the comments correctly) is intended
to improve compilation times. That sounds pretty good to me, so [I do want to
get back to that](https://github.com/barometz/nofmt-join/issues/2) at some
point. I *would* want to demonstrate the benefit in that case, because the
current implementation of `nofmt::join` is pleasantly small.
