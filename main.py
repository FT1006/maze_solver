from window import Window, Point, Line

def main():
    window = Window(800, 600)
    l = Line(Point(100, 100), Point(200, 200))
    window.draw_line(l, "red")
    window.wait_for_close()

main()