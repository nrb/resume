#!/bin/bash
# Small script so I can view PDFs on Linux or OS X using the `make view` command.


OPEN_CMD=""

case $(uname) in
    Linux) OPEN_CMD='xdg-open' ;; 
    Darwin) OPEN_CMD='open' ;;
esac

$OPEN_CMD resume.pdf
