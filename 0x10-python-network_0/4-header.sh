#!/bin/bash
# takes a URL as an argument, replace header information on value 98
curl -sH "X-HolbertonSchool-User-Id:98" "$1"
