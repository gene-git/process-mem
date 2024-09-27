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

OPTIONS
=======

  -h, --help            show this help message and exit
  -u USER, --user USER  username or :all: default (current_user)
  -f, --full            Full report adds shared lib and dirty pages (default False)


EXAMPLES
========

Display memory used by current users *bash* and firefox processes:

    process_mem  bash firefox

Display memory used by all processes owned by user *alice* :

    process_mem -u alice 


SEE ALSO
========

ps(1), memusage(1) 

https://www.sapience.com/
