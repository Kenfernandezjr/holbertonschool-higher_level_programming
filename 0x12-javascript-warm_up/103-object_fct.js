#!/usr/bin/node

const myObject1 = {
  type: 'object',
  value: 12
};
console.log(myObject1);
myObject1.incr = function () {
  myObject1.value++;
};
myObject1.incr();
console.log(myObject1);
myObject1.incr();
console.log(myObject1);
myObject1.incr();
console.log(myObject1);
