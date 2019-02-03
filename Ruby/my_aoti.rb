def my_atoi(str)
  str.strip!
  hash = {
      "0"=> 0,
      "1"=> 1,
      "2"=> 2,
      "3"=> 3,
      "4"=> 4,
      "5"=> 5,
      "6"=> 6,
      "7"=> 7,
      "8"=> 8,
      "9"=> 9,
      }
  str_num = ""
  str.chars.each_with_index do |ch,idx|
      if (ch == '+' || ch == '-') && idx == 0
          str_num += ch 
      elsif hash.key?(ch)
          str_num += ch
      else
          break
      end
  end
  p str_num
  res = 0 
  if str_num[0] == '-' || str_num[0] == '+'
      length = str_num.length - 2 
  else 
      length = str_num.length - 1
  end 
  str_num.chars.each do |ch|
     next if ch == '-' or ch == '+'
     temp = hash[ch]
     res += temp * (10 ** length)
     length -=1
  end
   res *= -1  if str_num[0] == '-'
   return res if (-2147483648) <= res && res <=(2147483647)
   if res < (-2147483648)
       return -2147483648
   else 
       return 2147483647
   end
end