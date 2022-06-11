Title: Blogstack
Tags: web, software
Lang: en
Status: published

Can't have a website without talking about how it's made.

woord.baudvine.net is part of a larger effort to simplify my online
infrastructure situation:

- Disentangle baudvine.net from Google Workspaces.
- Move stuff under a single domain.
- Let go of the excellent dvanb.nl domain, which is more attached to my first
  name than I am.
- Drop the VPS I'm not really using for anything but a static site no one reads.

*Woord* is hosted at [nearlyfreespeech.net](https://www.nearlyfreespeech.net/),
one of the most stick-with-what-you-know services I've had the pleasure of
using. NFSN provides hosting without a subscription fee, making you pay only for
the resources you use - which works out beautifully for the "static site with
five readers" scenario.

TLS certificates are provided by [Let's Encrypt](https://letsencrypt.org/). I
[wrote about setting this up for Lighttpd]({filename}lighty-certbot.md) before
when I ran my own web server, but it's much simpler with NFSN: I logged in
through SSH, ran a script that was already there, accepted some terms and
conditions, and now woord.baudvine.net has HTTPS.

The site is cobbled together by [Pelican](http://docs.getpelican.com/), a static
site generator that takes Markdown and ReStructuredText documents as input. I
don't have to worry about the security woes of a dynamic site, and I get to type
my stuff in the same markup language I'm already familiar with.

The theme is a [modified version of the Sober
theme](https://github.com/barometz/pelican-sober). I fixed some bugs, and added
some odds and ends like Open Graph tags and article translation links. I don't
know a whole lot about typography & co so I'm not touching any of tat.

Generation and deployment is automated with [a GitHub
workflow](https://github.com/barometz/woord.baudvine.net/blob/main/.github/workflows/publish.yml),
although I can just as easily run that from a local checkout. I try to avoid
writing big CI scripts - the more I can debug without pushing to GitHub, the
better.