function palindrome(s) {
  return isPalindrome(s, 0, s.length - 1);
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

console.log(palindrome("not a palindrome"));
