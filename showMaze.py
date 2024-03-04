import tkinter

window = tkinter.Tk()


def visblock():
    block = tkinter.Label(window)
    block.image = tkinter.PhotoImage(file="redDot.png")
    block['image'] = block.image
    return block
# These act like walls

def invisblock():
    block = tkinter.Button(window)
    block.image = tkinter.PhotoImage(file="redDot.png")
    block['image'] = block.image
    return block
# These act like empty spaces"""

maze = [[visblock(), visblock(), visblock(), visblock()],
        [visblock(), invisblock(), invisblock(), visblock()],
        [invisblock(), invisblock(),visblock(), invisblock()],
        [visblock(), invisblock(), invisblock(), invisblock()],
        [visblock(),visblock(), visblock(), visblock()]]

for i, block_row in enumerate(maze):
    for j, block in enumerate(block_row):
        block.grid(row=i, column=j)

window.mainloop()
