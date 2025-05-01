class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # limits = how many elements we an take from the grid[i]
        # k = how many tot elements we can summ 
        # get the max from the grid
        heap  = []
        op  = []
        summ = 0
        
        for  i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = -1*( grid[i][j] )
            
        for i in range(len(grid)):
            heapify(grid[i])
            for j in range(limits[i]):
                maxm = (heappop(grid[i]))
                heappush(op,maxm)
        while k
            summ += abs(heappop(op))
        return summ

    

                   

        
        # heapify(heap)
        # print(heap)
        # for i in range(limits[i]) :
        #     maxm = abs(heappop(heap))
        #     summ += maxm
        #     k -=1 
        #     if k == 0 :
        #         return summ
        # for i in range(k):
        #     maxm = abs(heappop(heap))
        #     
        # return maxm


        # maxm = []
        # summ = 0
        # for i in range(len(grid)):
        #     grid[i].sort(reverse=True)
        #     j = 0
        #     while limits[i] > 0 :
        #         maxm.append((grid[i][j]))
        #         j += 1
        #         limits[i]-=1
     
        # maxm.sort(reverse=True)
        # i = 0
        # while k :
        #     summ += maxm[i]
        #     i += 1
        #     k-=1
        # return summ
        # return 0





