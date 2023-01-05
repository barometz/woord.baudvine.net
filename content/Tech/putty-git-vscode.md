Title: Using PuTTY & Pageant with Git and VS Code
Tags: tooling
Lang: en
Status: draft

[PuTTY] is a common choice for an SSH client on Windows. Despite this, most
manuals for setting up integration with tools like Git and VS Code seem to
focus on OpenSSH. So what do I do when I have my SSH public/private keys set
up in PuTTY, and want to reuse those instead of setting up separate keys for
the OpenSSH that ships with Git on Windows?

This guide is written for PuTTY as that's probably what most people use, but
I've personally used it with [KiTTY]. The only difference there is some of the
file names change (`plink.exe` becomes `klink.exe`, for example).

I'm assuming you already have an SSH keypair set up. If not, see the
documentation for [PuTTYgen] (to generate keypairs) and optionally [Pageant]
(to keep keys loaded in the background).

## Git

The full PuTTY toolbox includes [Plink], "a command-line connection tool
similar to UNIX ssh". Git has an option [core.sshCommand] to select an
alternative command for SSH connections. That makes this a very simple affair:

```
git config --global core.sshCommand '"C:/path to/plink.exe"'
```

## VS Code

With the "Remote - SSH" extension, Visual Studio Code can open folders and
files on a remote host over SSH. Again, Plink can be provided as an
alternative SSH client. Because of how the extension tries to verify it's a
real OpenSSH client, this requires a little futzing:

Create a file `ssh.bat` with the following contents:
```bat
REM trick VS Code into believing this is an OpenSSH client
echo OpenSSH
"C:\path to\plink.exe" -ssh $*
```

In VS Code, find the option `remote.SSH.path` and set it to the full path to
`ssh.bat`.

VS Code stores its SSH configuration in an ssh-config file in the format used by
the OpenSSH client. It then passes the `Host` name to the SSH client, which - if
it were OpenSSH - would read the SSH client config file and load settings from
there. PuTTY and Plink don't understand that, but Plink does support using PuTTY
session names:

- Configure your host in PuTTY (say, hostname `example.com`, user `dominic`,
  session name `Example`).
- Create a new remote SSH host in VS Code. For the SSH command, just enter `Example`.
- Connect to the new remote host through VS Code to test it.

That's it! 

This was tested with KiTTY 0.76.1.2, Visual Studio Code 1.74.2, and Remote - SSH 0.94.0.

[PuTTY]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[PuTTYgen]: https://the.earth.li/~sgtatham/putty/0.78/htmldoc/Chapter8.html#pubkey
[Pageant]: https://the.earth.li/~sgtatham/putty/0.78/htmldoc/Chapter9.html#pageant
[Plink]: https://the.earth.li/~sgtatham/putty/0.78/htmldoc/Chapter7.html#plink
[core.sshCommand]: https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand
[GIT_SSH]: https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables#_miscellaneous
[KiTTY]: http://www.9bis.net/kitty/
