import turtle
import tkinter as tk
import tkinter.messagebox as box
from tkinter.font import Font
import random
colors = {'light gray': (211, 211, 211), 'light steel blue': (176, 196, 222), 'medium blue': (0, 0, 205), 'royal blue': (65, 105, 225), 'deep sky blue': (0, 191, 255), 'cyan': (0, 255, 255), 'turquoise': (64, 224, 208), 'teal': (0, 128, 128), 'aquamarine': (127, 255, 212), 'sea green': (46, 139, 87), 'spring green': (0, 255, 127), 'forest green': (34, 139, 34), 'lime': (0, 255, 0), 'olive drab': (107, 142, 35), 'dark khaki': (189, 183, 107), 'khaki': (240, 230, 140), 'yellow': (255, 255, 0), 'gold': (
    255, 215, 0), 'tan': (210, 180, 140), 'saddle brown': (139, 69, 19), 'orange': (255, 165, 0), 'firebrick': (178, 34, 34), 'maroon': (128, 0, 0), 'light salmon': (255, 160, 122), 'tomato': (255, 99, 71), 'crimson': (220, 20, 60), 'light coral': (240, 128, 128), 'pink': (255, 192, 203), 'hot pink': (255, 105, 180), 'medium violet red': (199, 21, 133), 'violet': (238, 130, 238), 'magenta': (255, 0, 255), 'orchid': (218, 112, 214), 'dark violet': (138, 0, 211), 'medium purple': (147, 112, 219)}
bgcolor1 = 'gray85'
bgcolor2 = 'powder blue'
wincolor = 'azure2'


def draw_spiral(sides, colorselect, colordrift, dir_of_rot, degree_of_rot):
    turtle.colormode(255)
    turtle.setup(width=1280, height=960)
    t = turtle.Pen()
    t.speed(0)
    turtle.bgcolor("black")
    t.hideturtle()
    start_r, start_g, start_b = colors[colorselect]
    color_r, color_g, color_b = start_r, start_g, start_b
    rangemax = 360

    def growth(start, rangemax, i):
        if start < 128:
            growthmax = (255 - start)//colordrift
            result = i//(int(rangemax/growthmax) + 1)
        else:
            growthmax = start//colordrift
            result = -1 * (i//(int(rangemax/growthmax) + 1))
        return result

    def noise(start):
        if start < 128:
            noisemax = (255 - start)//colordrift
            result = random.randint(0, noisemax)
        else:
            noisemax = start//colordrift
            result = random.randint(-noisemax, 0)
        return result
    for i in range(rangemax):
        t.pencolor(color_r, color_g, color_b)
        t.forward(i * 3/sides + i)
        if dir_of_rot == 'right':
            t.right(360/sides + degree_of_rot)
        else:
            t.left(360/sides + degree_of_rot)
        t.width(i*sides/200)
        color_r = start_r + growth(start_r, rangemax, i) + noise(start_r)
        color_g = start_g + growth(start_g, rangemax, i) + noise(start_g)
        color_b = start_b + growth(start_b, rangemax, i) + noise(start_b)
    t.forward(((rangemax+1) * 3/sides + (rangemax+1))/2)
    turtle.done()


window = tk.Tk()
window.title('Spiral Muse - Spiral Control')
window.geometry('900x800')
window.configure(bg=wincolor)
Arial10 = Font(family="Arial", size=10, weight="normal")
Arial11 = Font(family="Arial", size=11, weight="normal")
Arial12 = Font(family="Arial", size=12, weight="normal")
Arial20 = Font(family="Arial", size=20, weight="bold")
Verd10 = Font(family="Verdana", size=10, weight="normal")
Verd12 = Font(family="Verdana", size=12, weight="normal")
Verd14 = Font(family="Verdana", size=14, weight="bold")
Verd20 = Font(family="Verdana", size=20, weight="bold")
window.option_add('*Dialog.msg.font', 'Verdana 12')
frame_descript = tk.Frame(window, bg=bgcolor2, padx=10, pady=5,
                          relief=tk.RIDGE, borderwidth=5).grid(row=2, column=1)
tk.Label(frame_descript, text='Spiral Muse', bg=bgcolor2,
         height=1, pady=5, font=Verd20).grid(row=0, columnspan=2)
mess_descript1 = tk.Message(master=frame_descript, text='Generate colored spiral designs (against a black background) starting with a base polygonal shape (triangle, square, pentagon, etc.) and a base color. The base polygonal shape is specified by the number of sides (3, 4, 5,...up to 10).',
                            bg=bgcolor2, width=580, padx=5, font=Verd10).grid(row=1, columnspan=2)
img = tk.PhotoImage(file='Green_Color_Spiral.png')
small_img = tk.PhotoImage.subsample(img, x=5, y=5)
tk.Label(frame_descript, image=small_img, bg=bgcolor2).grid(row=2, column=0)
mess_descript2 = tk.Message(master=frame_descript, text='The color can be allowed to DRIFT away from the base color as the spiral twists and expands outward, creating an unfolding effect. This can be set using an integer number from 2 to 8, where 2 represents a lot of drift and 8 represents only a little. Think of this number as the degree of color STABILITY, the opposite of DRIFT. Regardless, a little amount of random variation is automatically added to the color, creating an organic look. ', bg=bgcolor2, width=350, padx=5, font=Verd10).grid(row=2, column=1)
sides = 3
frame_sides = tk.Frame(window, bg=bgcolor2, padx=10,
                       pady=5, relief=tk.RIDGE, borderwidth=5).grid(row=1, column=0, padx=10, pady=0)
tk.Label(frame_sides, text='Base Polygon Sides', bg=bgcolor2, height=1,
         padx=10, pady=5, font=Verd14).grid(row=0, column=0, sticky=tk.E)
tk.Message(master=frame_sides, text='How many sides would you like for the base polygon?Select a number from 3 to 10.',
           bg=bgcolor2, width=580, padx=5, font=Verd10).grid(row=1, columnspan=2)
sides_entry = tk.Entry(frame_sides, width=2, font=Verd12).insert(
    0, str(sides)).grid(row=0, column=1, sticky='W')
colordrift = 8
frame_drift = tk.Frame(window, bg=bgcolor2, padx=10, pady=5, relief=tk.RIDGE,
                       borderwidth=5).grid(row=2, column=0, padx=10, pady=0)
tk.Label(frame_drift, text='Color Drift', bg=bgcolor2, height=1,
         padx=10, pady=5, font=Verd14).grid(row=0, column=0, sticky=tk.E)
mess3 = tk.Message(master=frame_drift,
                   text='Determine color stability.  Select the amount to which the spiral color is prevented from drifting away from the base color, where 8 represents a lot of stability and 2 allows for a lot of drift.', bg=bgcolor2, width=580, padx=5, font=Verd10).grid(row=1, columnspan=2)
drift_entry = tk.Entry(frame_drift, width=2, font=Verd12).insert(
    0, str(colordrift)).grid(row=0, column=1, sticky='W')
degree_of_rot = 1
frame_rot = tk.Frame(window, bg=bgcolor2, padx=10, pady=5, relief=tk.RIDGE,
                     borderwidth=5).grid(row=3, column=0, padx=10, pady=0)
tk.Label(frame_rot, text='Direction of Rotation', bg=bgcolor2, height=1,
         padx=10, pady=5, font=Verd14).grid(row=0, column=0, sticky=tk.E)
tk.Label(frame_rot,
         text='Degree of Rotation', bg=bgcolor2, height=1, padx=10, pady=5, font=Verd14).grid(row=0, column=2, sticky=tk.E)
dir_entry = tk.Entry(frame_rot, width=5, font=Verd12).insert(
    0, str(dir_of_rot)).grid(row=0, column=1, padx=(0, 20), sticky='W')
deg_entry = tk.Entry(frame_rot, width=2, font=Verd12).insert(
    0, str(degree_of_rot)).grid(row=0, column=3, sticky='W')

mess_rot = tk.Message(master=frame_rot, text='Select the direction of rotation, either \'left\' or \'right\', and the degree of rotation, an integer number from 1 to 20.',
                      bg=bgcolor2, width=580, padx=5, font=Verd10).grid(row=1, columnspan=4)
colorselect = 'medium purple'

frame_colorselect = tk.Frame(
    window, bg=bgcolor2, padx=10, pady=5, relief=tk.RIDGE, borderwidth=5)
frame_colorselect.grid(row=0, column=1, rowspan=5, pady=(10, 0))

tk.Label(frame_colorselect, text='Base Polygon Color', bg=bgcolor2,
         height=1, pady=5, font=Verd14).pack(side=tk.TOP)

# Add description message
colormessage = ('Select a base (inner) color for the spiral. '
                'The default (highlighted in white) is the last one.'
                )
mess_colorselect = tk.Message(master=frame_colorselect,
                              text=colormessage,
                              bg=bgcolor2,
                              width=200,
                              pady=5,
                              font=Verd10
                              ).pack()

# Create listbox
listbox = tk.Listbox(frame_colorselect,
                     selectbackground='ghost white',
                     height=len(colors),
                     borderwidth=5,
                     font=Verd10,
                     # keep listbox selection from being deselected by other selections
                     exportselection=False
                     )

# Add items to listbox
for i, key in enumerate(colors.keys()):
    listbox.insert(i, '  ' + key)
    listbox.itemconfig(i, bg=key)

# Select the last element as default
listbox.select_set(len(colors) - 1)
listbox.pack()


# Proceed Frame -----------------------------------------

frame_proceed = tk.Frame(window,
                         bg=bgcolor2,
                         padx=10,
                         pady=5,
                         relief=tk.RIDGE,
                         borderwidth=5)
frame_proceed.grid(row=4, column=0, pady=0)

tk.Label(frame_proceed,
         text='Proceed with Drawing?',
         bg=bgcolor2,
         height=1,     # height in lines, not pixels
         padx=0,
         pady=5,
         font=Verd14
         ).grid(row=0, column=0)


# Proceed Function
counter = 0


def proceed_submit():
    global sides
    global colorselect
    global colordrift
    global dir_of_rot
    global degree_of_rot
    global counter

    if counter > 0:                   # Skips clear on 1st iteration
        turtle.Screen().clear()       # Deletes all drawings and turtles
    counter += 1
    sides = sides_entry.get()
    if not sides.isdigit():
        box.showwarning(
            '', 'The sides entry must be an integer.  Select again.')
        return
    sides = int(sides)
    if sides < 3 or sides > 10:
        box.showwarning(
            '', 'The selected number of sides is out of range.  Select again.')
        return
    colorselect = listbox.get(listbox.curselection()).strip()
    colordrift = drift_entry.get()
    if not colordrift.isdigit():
        box.showwarning(title='Selections',
                        message='The stability/drift entry must be an integer.  Select again.')
        return
    colordrift = int(colordrift)
    if colordrift < 2 or colordrift > 8:
        box.showwarning(title='Selections',
                        message='The stability/drift selection is out of range.  Select again.')
        return
    dir_of_rot = dir_entry.get()
    if not (dir_of_rot == 'left' or dir_of_rot == 'right'):
        box.showwarning(title='Selections', message=(
            'The Direction of Rotation entry must be either ''\'left\' or \'right\'.  Select again.'))
        return
    degree_of_rot = deg_entry.get().strip()
    if not degree_of_rot.isdigit():
        box.showwarning(title='Selections',
                        message='The Degree of Rotation entry must be an integer.  Select again.')
        return
    degree_of_rot = int(degree_of_rot)
    if degree_of_rot < 1 or degree_of_rot > 20:
        box.showwarning(
            title='Selections', message='The Degree of Rotation is out of range.  Select again.')
        return

    mess_proceed = f'''Your Selection is...\t\t\tBase Color:\t{colorselect}Sides:\t\t{sides}Stability/Drift:\t{colordrift}Direction of Rotation:\t{dir_of_rot}Degree of Rotation:\t{degree_of_rot}'''


box.showinfo('', mess_proceed)
draw_spiral(sides, colorselect, colordrift, dir_of_rot, degree_of_rot)
tk.Button(frame_proceed, text='Proceed', command=proceed_submit,
          font=Verd12).grid(row=0, column=1, padx=20)

window.mainloop()
