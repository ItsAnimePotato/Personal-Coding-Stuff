//learn vars
let name = "itsanimepotato";
console.log(name);

//learn const
const interestRate = 0.3;
console.log(interestRate);

//learn typing
let age = 30;
let isApproved = false;
let firstName = undefined;
let lastName = null;

//learn object
let person = {
  name: "amogus",
  age: 23,
};

console.log(person.name);
console.log(person.age);

//learn arrays
let selectedColors = ["red", "green", "blue"];
console.log(selectedColors);
console.log(selectedColors[0]);
console.log(selectedColors.length);
selectedColors[3] = 23;
console.log(selectedColors);
console.log(selectedColors.length);

//learn funcs

function greet(name) {
  console.log("hello " + name);
}

greet(name);

function greetFull(firstName, lastName) {
  console.log("hello " + firstName + " " + lastName);
}

greetFull("frist", "lsat");

//learn other funcs
function square(number) {
  return number * number;
}

let number = square(2);

console.log(number);
console.log(square(3));
