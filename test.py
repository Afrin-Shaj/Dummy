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
