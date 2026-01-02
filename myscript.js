function helloYou(name) {
    console.log("Hello, " + name + "!");
}

var rooster = [];

function addNew() {
    var name = prompt("Enter name to add:");
    rooster.push(name);
}

function remove(){
    var remname = prompt("Enter name to remove:");
    var index = rooster.indexOf(remname);
    rooster.splice(index, 1);
}

function displayRooster() {
    console.log("Current Rooster: " + rooster);
}

var start = prompt("would you like to start the rooster app? (y/n)")
var request ="empty";

if (start === "y") {
    while (request !== "quit") {
        request = prompt("What would you like to do? (add, remove, display, quit)");
        if (request === "add") {
            addNew();
        } else if (request === "remove") {
            remove();
        } else if (request === "display") {
            displayRooster();
        }
        else {
            alert("invalid request, will quit now")
            request = "quit";
        }
    }
    console.log("Thanks for using the rooster app!");
}

alert("This is the end of the script. please refresh to start over.");