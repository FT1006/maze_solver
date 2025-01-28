from window import Cell
import time

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
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
        self._break_entrance_and_exit()
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
        time.sleep(0.00)
        self._win.redraw()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(0, 0)
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)

