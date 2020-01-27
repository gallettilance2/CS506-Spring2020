def draw_road(length=10, axis="horizontal"):
    VALID = ["horizontal", "vertical"]
    if axis not in VALID:
        # raise error
        raise ValueError("your axis is undefined")
    if length <0:
        raise ValueError("your length is undefined")

    if axis=="horizontal":
        return draw_road_horizontal(length)
    else:
        for i in range(length):
            print("||")
    print()
    return

def draw_road_horizontal(length):   
    for i in range(length):
        print("=", end="")
    return
