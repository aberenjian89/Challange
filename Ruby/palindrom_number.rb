def palindrom_number(num)
  return false if num < 0 
  n = num 
  res = []
  while n >= 10 
    mod = n%10 
    n = n/10
    res << mod 
  end
  res << n
  p res
  total = 0
  res.reverse.each_with_index do |number,idx|
    total += number * (10 ** idx) 
  end
  p total
  return total == num 
end


p palindrom_number(-121)