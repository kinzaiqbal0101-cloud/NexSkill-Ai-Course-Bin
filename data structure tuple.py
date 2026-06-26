nums=(1,2,3)
temp_list=list(nums)
temp_list[0]=99
nums=tuple(temp_list)
print(nums)