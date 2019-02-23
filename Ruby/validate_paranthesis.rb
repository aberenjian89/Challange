def validate(str)
	stack = []
	hash = {
		']':'[',
		')':'(',
		'}':'{'
	}

	str.chars.each do |ch|
		if ch == '(' || ch == '{' || ch == '['
			stack << ch 
		elsif !stack.empty? && stack.last == hash[ch.to_sym]
			stack.pop 
		else 
			stack << ch 
		end
	end
	stack.empty?
end

p validate('[{}()]')


