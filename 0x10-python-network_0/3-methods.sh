#!/bin/bash
# Script that display all HTTP methods
curl -s -i -X OPTIONS "$1" | grep "Allow: " | cut -d : -f2
