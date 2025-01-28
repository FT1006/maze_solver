from window import Window, Point, Line, Cell, Maze

def main():
    width = 800
    height = 600
    window = Window(width, height)
    cell_size_x = 40
    cell_size_y = 40
    num_rows = width // cell_size_x
    num_cols = height // cell_size_y
    maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, window)
    maze._create_cells()
    window.wait_for_close()

main()