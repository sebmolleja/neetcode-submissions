class TrieNode():

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.full_word = ""
    
    def addWord(self, word):
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
        node.is_end = True
        node.full_word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()
        directions = [(-1, 0), (1, 0), (0, -1), (0,1)]

        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        def dfs(row, col, node):
            visited.add((row, col))

            if node.is_end:
                result.add(node.full_word)
            
            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col

                if (new_row, new_col) in visited:
                    continue
                
                if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    continue
                
                char = board[new_row][new_col]
                if char in node.children:
                    dfs(new_row, new_col, node.children[char])
            
            visited.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root.children[board[r][c]])
        
        return list(result)

            

        