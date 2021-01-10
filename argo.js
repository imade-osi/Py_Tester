// Given an M by N grid, we have an actor that always starts in the top left cell.
// There is a goal cell in the bottom right hand corner we want to reach.
// The actor may only move down, or to the right (no up, left or diagonal movements).
// Given those constraints, there are a finite number of paths that the actor may take.
// Can we create an algorithm that determines the number of paths from the actor's original
// position, to the goal cell?
//  _______________
// |_X_|_ _|_ _|_ _|
// |_ _|_ _|_ _|_ _|
// |_ _|_ _|_ _|_O_| 


// optimized solution
//identify the number of steps to reach goal(5)
//create return 2d array
//use factoriaztion logic with number of steps (2) and length of paths (5)
//2 * 2 * 2 * 2 * 2
//calculate the factorized number 
//return that number 


// function path_count();

// const number_of_steps = (N + M) - 1
// var directions = 2

// for (i = 0; i < number_of_steps; i++);
// directions *= 2

// return directions

var items = [
    { name: 'Edward', value: 22 },
    { name: 'Sharpe', value: 30 },
    { name: 'And', value: 45 },
    { name: 'The', value: -12 },
    { name: 'Magnetic', value: 13 },
    { name: 'Zeros', value: 37 }
];

// sort by value
items.sort(function (a, b) {
    return a.value - b.value;
});


// sort by name
items.sort(function (a, b) {
    var nameA = a.name.toUpperCase(); // ignore upper and lowercase
    var nameB = b.name.toUpperCase(); // ignore upper and lowercase
    if (nameA < nameB) {
        return -1;
    }
    if (nameA > nameB) {
        return 1;
    }

    // names must be equal
    return 0;
});




