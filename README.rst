.. SPDX-License-Identifier: GPL-2.0-or-later

###########
process-mem
###########

Overview
========

process_mem : Command line tool to display process(es) memory usage

I sometimes find the need to get the memory being consumed by a specific application.
This simplifies that by summing up the memory used by all process with the same name.

Example

::

    $ process-mem ssh bash
                   Proc-Name : [num]      rss      vms      shr
                        bash : [ 28]   204.5M   258.5M   152.8M
                         ssh : [ 18]   183.0M   276.4M   160.8M
                       Total : [ 46]   387.5M   534.9M   313.6M

Which shows there are 28 bash process running and 18 ssh. Total resident memory is 388 MB.

Next example uses regex with case ignored. ::

    $ ./process-mem  -i 'webkit.*'
                   Proc-Name : [num]      rss      vms      shr
        WebKitNetworkProcess : [  2]   304.5M   133.4G   239.2M
            WebKitWebProcess : [ 45]     9.1G     2.9T     7.9G
                       Total : [ 47]     9.4G     3.1T     8.2G

Key features
============

* Simple way to get total memory used by an application across all it's processes.
* Can use regex to match process name
* Can choose user to match.

New / Interesting
=================

**1.5.0**

* Code Reorg
* Switch packaging from hatch to uv
* Testing to confirm all working on python 3.14.2
* License GPL-2.0-or-later

**Older**

* All git tags are signed with arch@sapience.com key which is available via WKD
  or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
  The key is included in the Arch package and the source= line with *?signed* at the end can be used
  to verify the git tag.  You can also manually verify the signature

* Add regex matching for process names.


###############
Getting Started
###############

process_mem application
=======================

Usage
-----

To use it, open a terminal and run :

 .. code-block:: bash

   process-mem [process-name process-name ...]

Options
-------

By default it displayes process owned by current user.
This can be changed with the *-u* open followed by *username*. You can also use *:all:* to see
all users.

positional arguments: 

   list of process names to check. If omitted, all processes are examined.
   A process name may be a regex expression.

* (*-h, --help*) 

   show help message and exit

* (*-u,--user*)      
   
   Limit to processes ownder by specified user or *:all:* 
   Defaults to current user.

* (*-i, --ignore-case*)

   Case insensitive matching of process names

* (*-f, --full*)

   Full report : adds shared lib and dirty pages (False)

* (*-sm, --sort-mem)

   Sort by resident memory usage instead of process name.

* (*sr, --sort-rev)

  Reverse the sort.

* (*-v, --vers*)

   Display version and exit

Installation
============

Available on
 * `Github`_
 * `Archlinux AUR`_

On Arch you can build using the provided PKGBUILD in the packaging directory or from the AUR.
To build manually, clone the repo and :

.. code-block:: bash

       rm -f dist/*
       /usr/bin/python -m build --wheel --no-isolation
       root_dest="/"
       ./scripts/do-install $root_dest

When running as non-root then set root_dest a user writable directory

Dependencies
============

* Run Time :

  * python          (3.13 or later)
  * python-psutil   

* Building Package:

  * git
  * uv
  * uv-build        (aka python-uv-build)
  * rsync
  * docutils        (aka python-docutils - to generate man page)

Philosophy
==========

We follow the *live at head commit* philosophy as recommended by
Google's Abseil team [1]_.  This means we recommend using the
latest commit on git master branch. 


License
=======

Created by Gene C. and licensed under the terms of the GPL-2.0-or-later license.

* SPDX-License-Identifier: GPL-2.0-or-later
* SPDX-FileCopyrightText: © 2024-present  Gene C <arch@sapience.com>

.. _Github: https://github.com/gene-git/process_mem
.. _Archlinux AUR: https://aur.archlinux.org/packages/process_mem

.. [1] https://abseil.io/about/philosophy#upgrade-support


