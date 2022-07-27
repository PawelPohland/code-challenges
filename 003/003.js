"use strict";

function genDictionary(maxKey) {
  const dictionary = new Map();

  for (let k = 1; k <= maxKey; k++) {
    dictionary.set(k, k * k);
  }

  return dictionary;
}

// ****************************************************************** //

function main(max_key) {
  const dictionary = genDictionary(max_key);
  console.log(dictionary);
}

const readline = require("readline");

const userInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

userInput.question("Enter a number: ", (userNumber) => {
  main(userNumber);

  userInput.close();
});
