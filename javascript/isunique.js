function isunique(str) {
  // Assuming 128 Uniqu Assci Character
  if (str.length > 128) {
    return false;
  }
  let char_set = new Array(128);
  let index = null;
  for (let i = 0; i < str.length; i++) {
    index = str[i].charCodeAt() % 128;
    if (char_set[index]) {
      return false;
    } else {
      char_set[index] = true;
    }
  }
  return true;
}

// If string has unique character
console.log(isunique("Hello"));
