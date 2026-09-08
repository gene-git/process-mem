.. SPDX-License-Identifier: GPL-2.0-or-later

===========
process-mem
===========

Overview
========

process_mem : Command line tool to display process(es) memory usage

I sometimes find the need to get the memory being consumed by a specific application.
This simplifies that by summing up the memory used by all process with the same name.

Example::

    $ process-mem ssh bash
                   Proc-Name : [num]      rss      vms      shr
                        bash : [ 28]   204.5M   258.5M   152.8M
                         ssh : [ 18]   183.0M   276.4M   160.8M
                       Total : [ 46]   387.5M   534.9M   313.6M

Which shows there are 28 bash process running and 18 ssh. Total resident memory is 388 MB.

Next example uses regex with case ignored.::

    $ ./process-mem  -i 'webkit.*'
                   Proc-Name : [num]      rss      vms      shr
        WebKitNetworkProcess : [  2]   304.5M   133.4G   239.2M
            WebKitWebProcess : [ 45]     9.1G     2.9T     7.9G
                       Total : [ 47]     9.4G     3.1T     8.2G

Signed Source
-------------

All git tags are signed with arch@sapience.com key which is available via WKD
or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
The key is included in the Arch package and the source= line with *?signed* at the end can be used
to verify the git tag.  You can also manually verify the signature

Key features
============

* Simple way to get total memory used by an application across all it's processes.
* Can use regex to match process name
* Can choose user to match.

Recent Changes
==============

**1.7.0**

* Use meson / meson python for build / package management.
* Periodic code review


Getting Started
===============

Usage
-----

To use it, open a terminal and run::

   process-mem [process-name process-name ...]

Options
-------

By default it displayes process owned by current user.
This can be changed with the *-u* open followed by *username*. You can also use *:all:* to see
all users.

All available options::

    usage: process-mem [-h] [-u USER] [-f] [-i] [-v] [-sm] [-sr] [pnames ...]

    pnames             process names to check (all processes if not provided)

    -h, --help         show this help message and exit
    -u, --user USER    username or :all: default (gene)
    -f, --full         Full report adds shared lib and dirty pages (False)
    -i, --ignore-case  Case insensitive process names match(False)
    -v, --vers         Display version
    -sm, --sort-mem    Sort by resident memory use instead of process name
    -sr, --sort-rev    Sort in reverse order

Installation
============

Available on

* `Github <https://github.com/gene-git/process_mem>`_
* `Archlinux AUR <https://aur.archlinux.org/packages/process_mem>`_

On Arch you can build using the provided PKGBUILD in the packaging directory or from the AUR.
To build manually, clone the repo and::

        ./scripts/do-build
        ./scripts/do-install <destination directory>


Dependencies
============

* Run Time :

  * python          (3.14 or later)
  * python-psutil   

* Building Package:

  * git
  * meson
  * meson-python        (aka python-uv-build)
  * rsync

License
=======

Created by Gene C. and licensed under the terms of the GPL-2.0-or-later license.

* SPDX-License-Identifier: GPL-2.0-or-later
* SPDX-FileCopyrightText: © 2024-present  Gene C <arch@sapience.com>



