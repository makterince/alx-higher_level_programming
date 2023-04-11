#!/usr/bin/node
function secondBigNum (...nums) {
  nums.sort((a, b) => b - a);
  return (nums[1]);
}
const argumen = process.argv.splice(2);
if (argumen.length === 1 || argumen.length === 0) {
  console.log(0);
} else {
  console.log(secondBigNum(...argumen));
}
