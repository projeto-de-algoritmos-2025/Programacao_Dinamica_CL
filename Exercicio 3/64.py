from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        #so pode vir da esquerda
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        #so pode vir de cima
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        #preenchendo a matriz
        for i in range(1, m):
            for j in range(1, n):
                #escolhemos o menor custo entre:
                                  # vir de cima # vir da esquerda
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # retorna o menor caminho para a ultima celula
        return grid[-1][-1]  

sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum([[1,2,3],[4,5,6]]))
