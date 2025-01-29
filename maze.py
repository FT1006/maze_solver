from window import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None,
        ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.move_count = 0

    
    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))

       
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        if self._win is None:
            return
        top_left_x = self.x1 + i * self.cell_size_x
        top_left_y = self.y1 + j * self.cell_size_y
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y
        self._cells[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()

    def _animate(self):
        time.sleep(0.05)
        self._win.redraw()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(0, 0)
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_neighbors = []
            if i+1 < self.num_cols and self._cells[i+1][j] and not self._cells[i+1][j].visited:
                possible_neighbors.append([i+1, j]) # right
            if i-1 >= 0 and self._cells[i-1][j] and not self._cells[i-1][j].visited:
                possible_neighbors.append([i-1, j]) # left
            if j+1 < self.num_rows and self._cells[i][j+1] and not self._cells[i][j+1].visited:
                possible_neighbors.append([i, j+1]) # bottom
            if j-1 >= 0 and self._cells[i][j-1] and not self._cells[i][j-1].visited:
                possible_neighbors.append([i, j-1]) # top
            if len(possible_neighbors) == 0:
                self._draw_cells(i, j)
                return
            next = random.choice(possible_neighbors)
            
            if next == [i+1, j]:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            elif next == [i-1, j]:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif next == [i, j+1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            elif next == [i, j-1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            
            self._break_walls_r(next[0], next[1])
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        
        print("Starting to solve the maze...")
        if self._solve_r(0, 0):
            print("Maze solved in {} moves.".format(self.move_count))
            return True
        print("Could not solve the maze.")
        return False
            
    def _solve_r(self, i, j):
        self._animate()
        self.move_count += 1
        direction = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        for dir in direction:
            if dir[0] >= 0 and dir[0] < self.num_cols and dir[1] >= 0 and dir[1] < self.num_rows:
                if dir[0] == i + 1 and dir[1] == j and not self._cells[i][j].has_right_wall:
                    if not self._cells[i+1][j].visited:
                        self._cells[i][j].draw_move(self._cells[i+1][j])
                        if self._solve_r(i+1, j):
                            return True
                        else:
                            self._cells[i][j].draw_move(self._cells[i+1][j], True)
                if dir[0] == i and dir[1] == j + 1 and not self._cells[i][j].has_bottom_wall:
                    if not self._cells[i][j+1].visited:
                        self._cells[i][j].draw_move(self._cells[i][j+1])
                        if self._solve_r(i, j+1):
                            return True
                        else:
                            self._cells[i][j].draw_move(self._cells[i][j+1], True)
                if dir[0] == i - 1 and dir[1] == j and not self._cells[i][j].has_left_wall:
                    if not self._cells[i-1][j].visited:
                        self._cells[i][j].draw_move(self._cells[i-1][j])
                        if self._solve_r(i-1, j):
                            return True
                        else:
                            self._cells[i][j].draw_move(self._cells[i-1][j], True)
                if dir[0] == i and dir[1] == j - 1 and not self._cells[i][j].has_top_wall:
                    if not self._cells[i][j-1].visited:
                        self._cells[i][j].draw_move(self._cells[i][j-1])
                        if self._solve_r(i, j-1):
                            return True
                        else:
                            self._cells[i][j].draw_move(self._cells[i][j-1], True)
        return False