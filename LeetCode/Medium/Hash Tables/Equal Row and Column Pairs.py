class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        lines = {}
        count = 0
        for row in range(len(grid)):
            if tuple(grid[row]) in lines:
                lines[tuple(grid[row])] += 1
            else:
                lines[tuple(grid[row])] = 1
        transposed_matrix = list(map(list, zip(*grid)))
        for row in range(len(transposed_matrix)):
            if tuple(transposed_matrix[row]) in lines:
                count += lines[tuple(transposed_matrix[row])]
        return count
