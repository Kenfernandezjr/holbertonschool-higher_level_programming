#!/bin/bash
# Validate Json contents and post them to filename
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
