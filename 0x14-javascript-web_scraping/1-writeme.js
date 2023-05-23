#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('File path and string not included');
  process.exit(1);
}

const content = process.argv[3];
const filePath = process.argv[2];
fs.writeFile(filePath, content, 'utf8', (error) => {
  if (error) {
    console.error(error);
    return;
  }
});
