#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error, data) => {
  if (error) { console.log(error); }
});
