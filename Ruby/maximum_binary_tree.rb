class TreeNode
  attr_accessor :left,:right,:val
  def initialize(val) 
    @val = val 
    @left = nil 
    @right = nil 
  end
end




def maximum(nums)
  left = 0 
  right = nums.length 
  helper(nums,left,right)
end


def helper(nums,left,right)
  if left == right
    return nil 
  end 
  max = nums[left...right].max 
  max_i = nums.index(max)
  root = TreeNode.new(max)
  root.left = helper(nums,left,max_i)
  root.right = helper(nums,max_i+1,right)
  return root 
end


p maximum([3,2,1,6,0,5])