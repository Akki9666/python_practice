def nums1(n):
    for i in range(n):
    	return i
print(nums1(5))

def nums2(n):
    for i in range(n):
    	yield i
print(tuple(nums2(5)))