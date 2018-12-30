class Solution:
    def find_sky_line_grid(self,grid):
        horizontal= list()
        vertical=list()
        for i in grid:
            horizontal.append(self.find_largest_element(i))
        transpose = [[grid[j][i] for j in range(len(grid))] for i in    range(len(grid[0]))]
        for j in transpose:
            vertical.append(self.find_largest_element(j))
        return [horizontal, vertical]  
    
    def find_largest_element(self,arr):
        max=0
        for i in arr:
            if max<i:
                max=i
        return max 

    def maxIncreaseKeepingSkyline(self, grid):
        arr=self.find_sky_line_grid(grid)
        horizontal= arr[0]
        vertical= arr[1]
        increment=0
    
    
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                
                x=horizontal[i]
                y=vertical[j]
            
                min= x if x<y else y
                increment+=0 if grid[i][j]>min else (min-grid[i][j])
            
        return increment
