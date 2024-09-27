.. SPDX-License-Identifier: MIT

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
                   Proc-Name : [num]      rss      vsz      shr
                        bash : [ 28]   204.5M   258.5M   152.8M
                         ssh : [ 18]   183.0M   276.4M   160.8M
                       Total : [ 46]   387.5M   534.9M   313.6M

Which shows there are 28 bash process running and 18 ssh. Total resident memory is 388 MB.

Key features
============

 * Works for any user
 * Displays total memory used

New / Interesting
=================

 - initial release

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

positional arguments: list of process names to check. If omitted, all processes are examined.

 - *-h, --help* 

    show help message and exit

 - *-u,--user*      
   
    Limit to processes ownder by specified user or *:all:* 
    Defaults to current user.

 - *-f, --full*

    Full report : adds shared lib and dirty pages (False)


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

  * python          (3.11 or later)

* Building Package:

  * git
  * hatch           (aka python-hatch)
  * wheel           (aka python-wheel)
  * build           (aka python-build)
  * installer       (aka python-installer)
  * rsync
  * docutils        (aka python-docutils - to generate man page)

Philosophy
==========

We follow the *live at head commit* philosophy. This means we recommend using the
latest commit on git master branch. We also provide git tags. 

This approach is also taken by Google [1]_ [2]_.

License
=======

Created by Gene C. and licensed under the terms of the MIT license.

 * SPDX-License-Identifier: MIT
 * SPDX-FileCopyrightText: © 2024-present  Gene C <arch@sapience.com>

.. _Github: https://github.com/gene-git/process_mem
.. _Archlinux AUR: https://aur.archlinux.org/packages/process_mem

.. [1] https://github.com/google/googletest  
.. [2] https://abseil.io/about/philosophy#upgrade-support


