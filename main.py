from window import Window, Point, Line, Cell
from maze import Maze

def main():
    width = 800
    height = 600
    window = Window(width, height)
    cell_size_x = 100
    cell_size_y = 100
    num_rows = height // cell_size_x - 1
    num_cols = width // cell_size_y - 1
    maze = Maze(50, 50, num_rows, num_cols, cell_size_x, cell_size_y, window)
    maze.solve()
    window.wait_for_close()

main()