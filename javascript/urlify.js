function urlify(s, len) {
  let str = s.substr(0, len);
  final_str = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] == " ") {
      final_str += "%20";
    } else {
      final_str += str[i];
    }
  }
  return final_str;
}

console.log(urlify("MR JOHN SMITH    ", 13));
