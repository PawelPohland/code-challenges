"use strict";

// n! = 1 * 2 * ... * (n - 1) * n
function factorial1(number) {
  let result = 1;

  for (let i = 1; i <= number; i++) result *= i;

  return result;
}

// n! = 1 * 2 * ... * (n - 2) * (n-1)! * n
function factorial2(number) {
  if (number <= 1) return 1;

  return factorial2(number - 1) * number;
}

// using generator
function* factorial3(number) {
  if (number <= 1) {
    yield 1;
  }

  let result = 1;

  for (let i = 1; i <= number; i++) {
    result *= i;
    yield result;
  }
}

// ****************************************************************** //

const readline = require("readline");

const userInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

userInput.question("Enter a number: ", (userNumber) => {
  const number = Number.parseInt(userNumber, 10);

  console.log(`${number}! = ${factorial1(number)}`);
  console.log(`${number}! = ${factorial2(number)}`);

  const factorials = [...factorial3(number)];
  console.log(`${number}! = ${factorials[factorials.length - 1]}`);

  userInput.close();
});
