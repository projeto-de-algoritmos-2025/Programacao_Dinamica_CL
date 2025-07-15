from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        #matriz
        m, n = len(dungeon), len(dungeon[0])

        #inicializa e adiciona uma linha e coluna extra com infinito
        matriz = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        #definimos a borda (canto inferior direito) da matriz com 1, pois o cavaleiro precisa de pelo menos 1 para sair
        matriz[m][n - 1] = matriz[m - 1][n] = 1  

        #tras pra frente
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                #so pode ir ou para baixo ou para direita
                #se a célula tem um monstro (dungeon[i][j] < 0), precisaremos de mais HP.
                #se tem um bônus de vida (dungeon[i][j] > 0), precisaremos de menos HP.
                HP_minimo = min(matriz[i + 1][j], matriz[i][j + 1]) - dungeon[i][j]

                matriz[i][j] = max(1, HP_minimo)

        return matriz[0][0]

solution = Solution()

dungeon1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(solution.calculateMinimumHP(dungeon1))  # Output esperado: 7

dungeon2 = [[0]]
print(solution.calculateMinimumHP(dungeon2))  # Output esperado: 1
