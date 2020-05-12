#!/usr/bin/node
const fileShare = require('fileShare');
const requesting = require('requesting');
const urls = process.argv[2];
const path = process.argv[3];
requesting(urls).pipe(fileShare.createWriteStream(path, 'utf8'));
