function rotate(s, len) {
  for (let i = 0; i < len; i++) {
    s = s[s.length - 1] + s.substr(0, s.length - 1);
  }
  return s;
}

console.log(rotate("Hello", 4));
