#!/bin/bash
# Script to use post and -F to return information as a form
curl -sX POST "$1" -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD"
