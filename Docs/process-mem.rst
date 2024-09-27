============
 process_mem
============

----------------------------------
Display Memory Used by Process(es)
----------------------------------

:Author: Gene C <arch@sapience.com>
:Copyright: 2024-present Gene C 
:Version: process_mem
:Date: 27 September 2024
:Manual section: 1
:Manual group: Linux Tools

SYNOPSIS
========

**process_mem** [-f] [-u user] [Process-Name-1 Process-Name-2 ...]

DESCRIPTION
===========

Argument is a list of process names to examine. If none given then all processes are included.
Default is to only include processes ownder by the current user. The *-u* option allows
other users to be checked and all users can be included by using the user **:all:**

Process names can use regex and may be case insensitve.

OPTIONS
=======

  -h, --help            show this help message and exit
  -u USER, --user USER  username or :all: default (current_user)
  -f, --full            Full report adds shared lib and dirty pages (default False)
  -i, --ignore-case    Process name matching is case insensitive

EXAMPLES
========

Display memory used by current users *bash* and *ssh* processes::

  $ process-mem ssh bash
                   Proc-Name : [num]      rss      vsz      shr
                        bash : [ 28]   204.5M   258.5M   152.8M
                         ssh : [ 18]   183.0M   276.4M   160.8M
                       Total : [ 46]   387.5M   534.9M   313.6M


Display memory used by all processes owned by user *alice* using case insensitive process
matching::

  $ process_mem -u alice -i 'webkit.*'
                   Proc-Name : [num]      rss      vsz      shr
        WebKitNetworkProcess : [  2]   304.5M   133.4G   239.2M
            WebKitWebProcess : [ 45]     9.1G     2.9T     7.9G
                       Total : [ 47]     9.4G     3.1T     8.2G



SEE ALSO
========

ps(1), memusage(1) 

https://github.com/gene-git/process-mem
