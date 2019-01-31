require 'byebug'
class TinyURL
  def initialize
    @prefix = "http://tinyurl.com/"
    @hash = {}
  end

  def encode(longurl)
    key = longurl.to_i(36)
    @hash[key] = longurl
    return @prefix+key.to_s 
  end

  def decode(shorturl)
    code = shorturl.split('/')[-1]
    @hash[code.to_i]
  end
end


obj = TinyURL.new
key=obj.encode("https://leetcode.com/problems/design-tinyurl")
p key
p obj.decode(key)