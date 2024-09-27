#
# rst2man provided by python-docutils
#

default: process-mem.1.gz

process-mem.1: process-mem.rst
	rst2man --strict --no-raw --no-generator --no-datestamp $< $@

process-mem.1.gz: process-mem.1
	gzip -f $<
