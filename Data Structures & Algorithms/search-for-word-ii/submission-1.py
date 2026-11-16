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
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()
        directions = [(-1, 0), # Up
            (1, 0), # Down
            (0, 1), # Right
            (0, -1) # Left
        ]

        def dfs(row, col, node):
            # 1. Mark current cell as visited
            visited.add((row, col))

            # 2. Check whether we've completed a word
            if node.is_end:
                result.add(node.full_word)
            
            # 3. Explore four neighbors
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
            
                # Check bounds
                if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    continue

                # Check visited
                if (new_row, new_col) in visited:
                    continue

                # Check Trie child
                char = board[new_row][new_col]
                if char not in node.children:
                    continue

                # Recursively explore valid neighbors
                dfs(new_row, new_col, node.children[char])

            # 4. Unmark current cell
            visited.remove((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                
                if char in root.children:
                    dfs(r, c, root.children[board[r][c]]) 

        return list(result)



        