class TimeMap
  def initialize
    @map = Hash.new {|h,k| h[k]= Hash.new}
  end

  def set(key,value,timestamp)
    @map[key][timestamp]=value 
  end

  def get(key,timestamp)
    if @map.key?(key)
      temp = @map[key]
      if @temp.key?(timestamp)
        return @temp[timestamp]
      else
        latest_timestamp = @map.keys.max
        return @temp[latest_timestamp]
      end
    else
      return ""
    end
  end
end
