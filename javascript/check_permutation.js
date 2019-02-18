function check_permutation(s1, s2) {
  if (s1.length != s2.length) {
    return false;
  }

  let char_set = new Array(128);
  index = null;
  for (let i = 0; i < s1.length; i++) {
    index = s1[i].charCodeAt() % 128;
    if (char_set[index] == undefined) {
      char_set[index] = 1;
    } else {
      char_set[index] += 1;
    }
  }

  for (let i = 0; i < s2.length; i++) {
    index = s2[i].charCodeAt() % 128;
    if (char_set[index] == undefined || char_set[index] - 1 < 0) {
      return false;
    } else {
      char_set[index] -= 1;
    }
  }

  return true;
}

function check_permutation_v2(s1, s2) {
  if (s1.length != s2.length) {
    return false;
  }

  return sort(s1) == sort(s2);
}

function sort(str) {
  return str
    .split("")
    .sort()
    .join("");
}

console.log(check_permutation("abc", "cba"));
console.log(check_permutation("abc", "vba"));
console.log(check_permutation("aabc", "abc"));
console.log(check_permutation("aabc", "abca"));

console.log(check_permutation_v2("abc", "cba"));
console.log(check_permutation_v2("abc", "vba"));
console.log(check_permutation_v2("aabc", "abc"));
console.log(check_permutation_v2("aabc", "abca"));
