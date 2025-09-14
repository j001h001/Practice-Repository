nums = (5, 10) + (15, 20)
if 3 in nums:
    print ("Spring")
elif max(nums) > 50:
    print ("Summer")
elif sum(nums) > 100:
    print ("Fall")
elif (min(nums) + 5) > 15:
    print ("Winter")
elif nums.count(5) < 3:
    print ("Spring")