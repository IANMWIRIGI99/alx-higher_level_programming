#!/usr/bin/node
'use strict';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let count = 0; count < process.argv[2]; count++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
