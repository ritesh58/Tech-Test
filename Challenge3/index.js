var parseIn = require('./Test');

// JSON object
const object = {
  "a":{
    "b":{
      "c":"d",
    }
  }
};

// Calls function parseIn in Test.js----
let result = parseIn(object, "a/b/c"); 
// Print out the result
console.log(`Value = ${result}`)