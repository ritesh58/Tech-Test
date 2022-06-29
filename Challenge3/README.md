Problem:
    We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.

    Example Inputs

    object = {“a”:{“b”:”{“c”:”d”}”}}
    key = a/b/c

    object = {“x”:{“y”:”{“z”:”a”}”}}
    key = x/y/z
    value = a

Solution:

    I am using node.js for this solution. 
    Created a function inside package Test.js. This function named "parseIn" will accept two arguments.
    First argument is full json object and second one is path of the key whose value needs to be fetched.
    This function is called from main(index.js) file

Testing: 

    For automation testing, Implementing mocha framework would be my preffered choice but because of limited time I have chosen manual testing
    Run the program by running command "npm test". Value will be shown in console
    Invalid json and empty key will throw an error

