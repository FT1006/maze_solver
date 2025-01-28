from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(
            self,
            line,
            fill_color="black",
    ):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(
            self,
            p1,
            p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2
        )

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        if self._win is None:
            return
        self._x1 = top_left_x
        self._y1 = top_left_y
        self._x2 = bottom_right_x
        self._y2 = bottom_right_y
        if self.has_left_wall:
            line = Line(Point(top_left_x, top_left_y), Point(top_left_x, bottom_right_y))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(bottom_right_x, top_left_y), Point(bottom_right_x, bottom_right_y))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(top_left_x, top_left_y), Point(bottom_right_x, top_left_y))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(top_left_x, bottom_right_y), Point(bottom_right_x, bottom_right_y))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
       
        start = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        end = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        move =  Line(start, end)
        
        fill_color = "red"
        if undo:
            fill_color = "grey"
        self._win.draw_line(move, fill_color)

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
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
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                self._cells[i].append(Cell(self._win))
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        top_left_x = self.x1 + i * self.cell_size_x
        top_left_y = self.y1 + j * self.cell_size_y
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y
        self._cells[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()

    def _animate(self):
        time.sleep(0.05)
        self._win.redraw()

        