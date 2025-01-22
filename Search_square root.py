class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        Low = 0
        High = x
    
        
        while(Low<=High):
            Averge= (High+Low)//2
                
            if(Averge*Averge==x):
                return Averge
            elif(Averge*Averge<x):
                Low = Averge+1
            else:
                High =Averge-1
        return High

                
solution=Solution()
Number=int(input("Enter the number"))
result=solution.mySqrt(Number)
print(f"The square root of the number is {result}")