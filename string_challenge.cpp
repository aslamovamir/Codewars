// String Challenge
// INCOMPLETE!!!
// Have the function StringChallenge(str) take the str parameter being passed and determine if a palindrome 
// can be created by swapping two adjacent characters in the string. If it is possible to create a palindrome,
// then your program should return the palindrome, if not then return the string -1. The input string will only
// contain alphabetic characters. For example: if str is "rcaecar" then you can create a palindrome by swapping
// the second and third characters, so your program should return the string racecar which is the final 
// palindromic string.
  
// Examples

// Input: "anna" 
// Output: anna
// Input: "kyaak" 
// Output: kayak

#include <iostream>
#include <string>
using namespace std;
#include <map>


string StringChallenge(string str) {

  int l = 0;
  int r = str.length()-1;

  string front;
  string back;
  while (l < r) {
    if (str[l] == str[r]) {
      front += str[l];
      back += str[r];
    } else {
      if (l != 0) {
        if (str[l-1]  == str[r])
      }
    }
  }

}

int main(void) { 
   
  // keep this function call here
  cout << StringChallenge(coderbyteInternalStdinFunction(stdin));
  return 0;
    
}
