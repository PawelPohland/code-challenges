"use strict";

function getNumbers1(startNum = 2000, endNum = 3200) {
  const numbers = [];

  for (let number = startNum; number <= endNum; number++) {
    if (number % 7 === 0 && number % 5 !== 0) {
      numbers.push(number);
    }
  }

  return numbers.join(",");
}

const numbers1 = getNumbers1();
console.log(numbers1);

console.log();
// ************************************************************ //

// using generator
function* getNumbers2(startNum = 2000, endNum = 3200) {
  for (let number = startNum; number <= endNum; number++) {
    if (number % 7 === 0 && number % 5 !== 0) {
      yield number;
    }
  }
}

const generator = getNumbers2();
const numbers2 = [...generator].join(",");
console.log(numbers2);

// ************************************************************ //
// with using while loop:

// const generator = getNumbers2();
// const numbers = [];

// let number = generator.next();
// while (!number.done) {
//   numbers.push(number.value);
//   number = generator.next();
// }
// console.log(numbers.join(","));

// ************************************************************ //
// with for-of loop

// const generator = getNumbers2();
// const numbers = [];

// for (let number of generator) {
//   numbers.push(number);
// }
// console.log(numbers.join(","));
