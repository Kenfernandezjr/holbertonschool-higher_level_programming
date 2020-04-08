#!/bin/bash
# takes a URL as an argument, replace header information on value 98
curl -H "X-HolbertonSchool-User-Id:98" "$1"
