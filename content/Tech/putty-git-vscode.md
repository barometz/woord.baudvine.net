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
I've personally used it with KiTTY. The only difference there is some of the
file names change (`plink.exe` becomes `klink.exe`, for example).

## SSH keypairs in PuTTY

I'm assuming you have some sense of how asymmetric keypairs are used with SSH,
but for completeness this section will briefly describe how they work with
PuTTY.

## Git






[PuTTY]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
