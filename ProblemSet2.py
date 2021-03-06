
//Problem 1

Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses

Examples
Input: 3
Output: 5


function BracketCombinations(num) { 

  // code goes here  
  count = 0;
  n = 2**(2*num);
  for (iperm=0; iperm<n; iperm++){
    sum = 0;
    i = iperm;
    for (dig = 2*num; dig > 0; dig --){
      bit = i % 2;
      i -= bit;
      i /= 2;
      sum = sum + (bit == 0?1:-1);
      if(sum<0){break; };
    };
    count += (sum ==0)?1:0;
  };
  return count; 
}
   
// keep this function call here 
console.log(BracketCombinations(readline()));

