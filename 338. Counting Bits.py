class Solution:
    def countBits(self, num):
        if num==0:
            return [0]
        ans=[0,1]
        for i in range(2,num+1):
            ans.append(ans[i//2]+i%2)
        return ans
""""""
sln=Solution()
print(sln.countBits(5))


