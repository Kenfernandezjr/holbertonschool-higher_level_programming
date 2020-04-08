#!/bin/bash
# Write and and output in curl 
curl -so /dev/null -w "%{http_code}" "$1"
