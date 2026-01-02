var firstName = prompt("Enter your first name please:");
var lastName = prompt("Enter your last name please:");
var age = prompt("How old are you?");
var height = prompt("what is your height (in cm) ?");
var petName = prompt("what is your pet's name?");
alert("Thank you for your answers!");


// Logic



// Four Conditions
var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;



// NAME CONDITION

if (firstName[0] === lastName[0]){
    nameCond = true;
}else {
    nameCond = false;
}


// AGE CONDITION

if (age > 28 && age < 30){
    ageCond = true;
}else {
    ageCond = false;
}

// HEIGHT CONDITION

if (height >= 170){
    heightCond = true;
}else {
    heightCond = false;
}

// PET CONDITION

if (petName[petName.length -1] === "y"){
    petCond = true;
}else {
    petCond = false;
}

// FINAL DECISION

if (nameCond && ageCond && heightCond && petCond){
    console.log("Welcome Spy!");
}else {
    console.log("Nothing to see here.");
}


