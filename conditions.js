//Write a function that takes an array of numbers as input and returns the sum of all the numbers
function sumnumbers(array){
    let result = 0;
    for(let num of array){
        result+=num;
    }
    return result;
  }
  console.log(sumnumbers([1,2,3,4,]));


// Write a function that takes two numbers as input and returns true if their sum is greater than 100,
// And false otherwise




function sum_greater_than_100(sum){
    sum=0
    for(i in sum){
        if(i>=100){
            return true
        }
        else{
            return false
        }
    }
}
const a=20
const b=80
const sum=a+b
console.log(sum_greater_than_100(sum))
// Write a function that takes a string as input and returns the number of vowels in the string
function number_vowels(string){
    var count_vowels=0
    vowels=["a","e","i","o","u"]
    for(let vowels in string){
        if(string.includes(vowels)){
            return  string.count_vowels++
        }
        else{
            return
        }
    }
    return count_vowels
}
const string="linah"
console.log(number_vowels(string))
// Write a function that takes in a array of numbers as a parameter and returns the second largest number in the array
function second_largest_number(array) {
    let second_largest_number=0
    return array[array.length - 2];
    }
    const array=[20,30,40,50,70]
    console.log(second_largest_number(array))
    // Write a function that takes a string as a parameter and returns true if the string is a palindrome and false otherwise
    function palindrome(string1){
        return true
    }
const string1="nose"
console.log(palindrome(string1))
























