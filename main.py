from window import Window, Point, Line, Cell

def main():
    window = Window(800, 600)
    cell = Cell(window)
    cell.has_left_wall = False
    cell.draw(120, 120, 240, 240)

    cell = Cell(window)
    cell.has_right_wall = False
    cell.draw(150, 150, 300, 300)

    cell = Cell(window)
    cell.has_top_wall = False
    cell.draw(60, 120, 120, 180)
    
    cell = Cell(window)
    cell.has_bottom_wall = False
    cell.draw(300, 90, 310, 100)

    window.wait_for_close()

main()