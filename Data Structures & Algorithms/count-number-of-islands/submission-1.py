class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def traverse(r,c):   
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return

            if grid[r][c] == '0':
                return
            else:
                grid[r][c] = '0'
            
            # for row in grid:
            #     print(row)
            # print()

            traverse(r,c+1) 
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    traverse(r,c)   
                    islands += 1                 
        
        return islands