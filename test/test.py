let storedUser = "admin";
let storedPassword = "admin123";

let inputUser = "admin";
let inputPassword = "admin123";

let login = false;

if(inputUser == storedUser){

   if(inputPassword == storedPassword){
       login = true;
   }

}

console.log("Login:", login);

let command = "alert('security test')";

let runCommand = command;

eval(runCommand);

let accessLevel = "admin";

if(accessLevel == "admin"){
   console.log("Full access granted");
}



let numbers = [5,10,15,20,25];
let total = 0;
let i = 0;

console.log("Starting calculation");

while(i < numbers.length){

   let value = numbers[i];

   console.log("Current number:", value);

   total = total + value;

   if(value == 20){
       console.log("Special number found");
   }

   i = i + 1;
}

let average = total / numbers.length;

console.log("Total:", total);
console.log("Average:", average);

let result = average + 5;

console.log("Final result:", result);
