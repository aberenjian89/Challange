function rollTheString(s, roll) {
  // Write your code here
  let alphabet = {
    a: "b",
    b: "c",
    c: "d",
    d: "e",
    e: "f",
    f: "g",
    g: "h",
    h: "i",
    i: "j",
    j: "k",
    k: "l",
    l: "m",
    m: "n",
    n: "o",
    o: "p",
    p: "q",
    q: "r",
    r: "s",
    s: "t",
    t: "u",
    u: "v",
    v: "w",
    w: "x",
    x: "y",
    y: "z",
    z: "a"
  };
  str = s;
  let i = 0;
  while (i < roll.length) {
    let res = roll[i];
    console.log(res);
    let j = 0;
    while (j < res) {
      console.log(alphabet[str[j]]);
      // s[j] = alphabet[s[j]];
      str = str.replace(j, alphabet[str[j]]);
      j += 1;
    }
    console.log(s);
    i += 1;
  }
  return s;
}

console.log(rollTheString("abc", [3, 2, 1]));
