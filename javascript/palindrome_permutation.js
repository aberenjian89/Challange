// 1. Find Permutation
// 2. Check to see if the palindrom they are palindrome

function palindrom_permutation(s) {
  // Find Permutation
  let result = [];
  Permutation(" ", s, result);
  for (let i = 0; i < result.length; i++) {
    if (isPalindrome(result[i], 0, result[i].length - 1)) {
      return true;
    }
  }

  return false;
}

function Permutation(str, s, result) {
  if (s.length <= 0) {
    result.push(str);
  }

  for (let i = 0; i < s.length; i++) {
    Permutation(str + s[i], s.substr(0, i) + s.substr(i + 1), result);
  }
  return result;
}

function isPalindrome(str, start, end) {
  if (start > end) {
    return false;
  }
  if (str[start] != str[end]) {
    return false;
  }
  isPalindrome(str, start + 1, end - 1);
  return true;
}

console.log(palindrom_permutation("hello"));
