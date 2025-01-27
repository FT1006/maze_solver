from window import Window, Point, Line, Cell

def main():
    window = Window(800, 600)
    c1 = Cell(window)
    c1.has_right_wall = False
    c1.draw(50, 50, 150, 150)

    c2 = Cell(window)
    c2.has_left_wall = False
    c2.draw(150, 50, 250, 150)

    c1.draw_move(c2)

    a1 = Cell(window)
    a1.has_bottom_wall = False
    a1.draw(350, 50, 450, 150)
    
    a2 = Cell(window)
    a2.has_top_wall = False
    a2.draw(350, 150, 450, 250)

    a1.draw_move(a2)


    window.wait_for_close()

main()