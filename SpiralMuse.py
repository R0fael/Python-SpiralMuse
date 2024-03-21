
import turtle
import tkinter as tk
import tkinter.messagebox as box
import random



## Base Color Choices
colors = {
    'light gray': (211, 211, 211),
    'light steel blue': (176, 196, 222),
    'medium blue': (0, 0, 205),
    'royal blue': (65, 105, 225),
    'deep sky blue': (0, 191, 255),
    'cyan': (0, 255, 255),
    'turquoise': (64, 224, 208),
    'teal': (0, 128, 128),
    'aquamarine': (127, 255, 212),
    'sea green': (46, 139, 87),
    'spring green': (0, 255, 127),
    'forest green': (34, 139, 34),
    'lime': (0, 255, 0),
    'olive drab': (107, 142, 35),
    'dark khaki': (189, 183, 107),
    'khaki': (240, 230, 140),
    'yellow': (255, 255, 0),
    'gold': (255, 215, 0),
    'tan': (210, 180, 140),
    'saddle brown': (139, 69, 19),
    'orange': (255, 165, 0),
    'firebrick': (178, 34, 34),
    'maroon': (128, 0, 0),
    'light salmon': (255, 160, 122),
    'tomato': (255, 99, 71),
    'crimson': (220, 20, 60),
    'light coral': (240, 128, 128),
    'pink': (255, 192, 203),
    'hot pink': (255, 105, 180),
    'medium violet red': (199, 21, 133),
    'violet': (238, 130, 238),
    'magenta': (255, 0, 255),
    'orchid': (218, 112, 214),
    'dark violet': (138, 0, 211),
    'medium purple': (147, 112, 219)
    }


bgcolor1 = 'gray85'
bgcolor2 = 'powder blue'
wincolor = 'azure2'



##### Turtle #######

def draw_spiral(sides, colorselect, colordrift):

    # Turtle Configuration
    turtle.colormode(255)
    turtle.setup(width=1280, height=960)
    t = turtle.Pen()
    t.speed(0)
    turtle.bgcolor("black")
    t.hideturtle()



    ##### Spiral #####

    start_r, start_g, start_b = colors[colorselect]
    color_r, color_g, color_b = start_r, start_g, start_b

    rangemax = 360


    ## Functions for growth and noise
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


    ## Drawing loop
    for i in range(rangemax):
        t.pencolor(color_r, color_g, color_b)
        t.forward(i * 3/sides + i)
        t.left(360/sides + 1)   #degrees for a corner turn + 1 to make it spiral
        t.width(i*sides/200)
        color_r = start_r + growth(start_r, rangemax, i) + noise(start_r)
        color_g = start_g + growth(start_g, rangemax, i) + noise(start_g)
        color_b = start_b + growth(start_b, rangemax, i) + noise(start_b)
        #  print(color_r, color_g, color_b)       # For color performance analysis


    turtle.done()






####### tkinter window ############


## tkinter window to interact

window = tk.Tk()
window.title('Spiral Control')
window.geometry('850x800')
window.configure(bg=wincolor)

# tkinter Configuration
font1 = ('Arial', '12', 'bold')
font2 = ('Times', '12' , 'normal')
font3 = ('calibre', 10, 'normal')


# Description Frame

frame_descript = tk.Frame(window, 
                       bg=bgcolor2,
                       padx=10, pady=5,
                       relief=tk.RIDGE, borderwidth=5)
frame_descript.grid(row=0, column=0, padx=10, pady=(10,0), sticky=tk.N)

tk.Label(frame_descript,
         text='Spiral Muse', bg=bgcolor2, height=1,      # height in lines, not pixels
         pady=5,
         font=font1).grid(row=0)

description1 = (
    'Generate colored spiral designs (against a black background) '
    'starting with a base polygonal shape (triangle, square, '
    'pentagon, etc.) and a base color. The base polygonal shape '
    'is specified by the number of sides (3, 4, 5,...up to 10). \n'
)
description2 = (
    '\nThe color can be allowed to DRIFT away from the base '
    'color as the spiral twists and expands outward, '
    'creating an unfolding effect. '
    'This can be set using an integer number '
    'from 2 to 8, where 2 represents a lot of drift and 8 '
    'represents only a little. Think of this number as the degree '
    'of color STABILITY, the opposite of DRIFT. '
    'Regardless, a little amount of random variation is automatically '
    'added to the color, creating an organic look. '
)
mess_descript1 = tk.Message(master=frame_descript,
            text=description1,
            bg=bgcolor2,
            width=500,
            padx=5)
mess_descript1.grid(row=1)

img = tk.PhotoImage(file = 'Green_Color_Spiral.png')
small_img = tk.PhotoImage.subsample(img, x=5, y=5)
tk.Label(frame_descript,
      image=small_img, bg=bgcolor2).grid(row=2)
mess_descript2 = tk.Message(master=frame_descript,
            text=description2,
            bg=bgcolor2,
            width=500,
            padx=5)
mess_descript2.grid(row=3)


# Sides Select Frame
sides = 3

frame_sides = tk.Frame(window, 
                       bg=bgcolor2,
                       padx=10, pady=5,
                       relief=tk.RIDGE, borderwidth=5)
frame_sides.grid(row=1, column=0, padx=10, pady=0)
tk.Label(frame_sides,
         text='Base Polygon Sides', bg=bgcolor2, height=1,      # height in lines, not pixels
         padx=10, pady=5,
         font=font1).grid(row=0, column=0, sticky=tk.E)
sidemessage = ('How many sides would you like for the base polygon? '
               'Select a number from 3 to 10.'
)
mess1 = tk.Message(master=frame_sides,
            text=sidemessage,
            bg=bgcolor2,
            width=500,
            padx=5)
mess1.grid(row=1, columnspan=2)


##def sides_submit():
##    global sides
##    sides = str(sides_entry.get())
##    box.showinfo('', f'Your Selection is {sides}.')
##    print("The number of sides is: " + sides)
##    

sides_entry = tk.Entry(frame_sides, width=2)
sides_entry.insert(0, str(sides))
##sides_btn = tk.Button(frame_sides, text='Submit', command=sides_submit)

sides_entry.grid(row=0, column=1, sticky='W')
##sides_btn.grid(row=2, column=1)



# Color Drift Frame
colordrift = 8

frame_drift = tk.Frame(window,
                       bg=bgcolor2,
                       padx=10, pady=5,
                       relief=tk.RIDGE, borderwidth=5)
frame_drift.grid(row=2, column=0, padx=10, pady=0)
tk.Label(frame_drift,
         text='Color Drift', bg=bgcolor2, height=1,     # height in lines, not pixels
         padx=10, pady=5,
         font=font1).grid(row=0, column=0, sticky=tk.E)
driftmessage = ('Determine color stability.  Select the amount to which the spiral color '
                'is prevented from '
                'drifting away from the base color, where 8 represents a lot of stability '
                'and 2 allows for a lot of drift.'
)
mess3 = tk.Message(master=frame_drift,
                   text=driftmessage,
                   bg=bgcolor2,
                   width=500,
                   padx=5)
mess3.grid(row=1, columnspan=2)

##def drift_submit():
##    global colordrift
##    colordrift = str(drift_entry.get())
##    box.showinfo('', f'Your Selection is {colordrift}.')
##    print("The color drift is: " + colordrift)
##    window.quit()

drift_entry = tk.Entry(frame_drift, width=2)
drift_entry.insert(0, str(colordrift))
##drift_btn = tk.Button(frame_drift, text='Submit', command=drift_submit)

drift_entry.grid(row=0, column=1, sticky='W')
##drift_btn.grid(row=2, column=1)



# Color Select Frame

colorselect = 'medium purple'

frame_colorselect = tk.Frame(window,
                            bg=bgcolor2,
                             padx=10, pady=25, relief=tk.RIDGE, borderwidth=5)
frame_colorselect.grid(row=0, column=1, rowspan=4, pady=(10,0))
tk.Label(frame_colorselect,
         text='Base Polygon Color', bg=bgcolor2, height=1,     # height in lines, not pixels
         pady=5,
         font=('Arial', '12', 'bold')).pack(side=tk.TOP)
colormessage = 'Select a base (inner) color for the spiral.\nDefault (highlighted in white)\n is the last one.\n'
label2 = tk.Label(master=frame_colorselect,
                  text=colormessage, bg=bgcolor2, pady=5).pack()
listbox = tk.Listbox(frame_colorselect, selectbackground='ghost white', height=len(colors), borderwidth=5)

for i, key in enumerate(colors.keys()):
    listbox.insert(i, '  ' + key)
    listbox.itemconfig(i, bg=key)

listbox.select_set(len(colors) - 1)   # Sets the last element

##def dialog():
##    global colorselect
##    colorselect = str(listbox.get(listbox.curselection())).strip()
##    box.showinfo('', f'Your Selection is {colorselect}.')
##    print(colorselect)
##
##btn = tk.Button(frame_colorselect, text = "Choose", command = dialog)

listbox.pack()
##btn.pack(side=tk.RIGHT, padx=10)



##### Proceed Frame ######

frame_proceed = tk.Frame(window,
                         bg=bgcolor2,
                         padx=10, pady=5,
                         relief=tk.RIDGE, borderwidth=5)
frame_proceed.grid(row=3, column=0, pady=0)

tk.Label(frame_proceed,
         text='Proceed with Drawing?', bg=bgcolor2, height=1,     # height in lines, not pixels
         pady=5,
         font=('Arial', '12', 'bold')).pack(side=tk.TOP)


##### Proceed Function #####

counter = 0

def proceed_submit():
    global sides
    global colorselect
    global colordrift
    global counter

    if counter > 0:                   # Skips clear on 1st iteration
        turtle.Screen().clear()       # Deletes all drawings and turtles
    counter += 1

    # Exception handling for sides
    sides = sides_entry.get()
    if not sides.isdigit():
        box.showwarning('', 'The sides entry must be an integer.  Select again.')
        return
    sides = int(sides)
    if sides < 3 or sides > 10:
        box.showwarning('', 'The selected number of sides is out of range.  Select again.')
        return
    
    # Getting color
    colorselect = str(listbox.get(listbox.curselection())).strip()

    # Exception handling for stability/drift
    colordrift = drift_entry.get()
    if not colordrift.isdigit():
        box.showwarning('', 'The stability/drift entry must be an integer.  Select again.')
        return
    colordrift = int(colordrift)
    if colordrift < 2 or colordrift > 8:
        box.showwarning('', 'The stability/drift selection is out of range.  Select again.')
        return

    mess_proceed = f'''Your Selection is...\t\t\t
Sides:\t\t{sides}
Base Color:  {colorselect}
Stability/Drift:\t{colordrift}
'''
    
    box.showinfo('', mess_proceed)
    draw_spiral(sides, colorselect, colordrift)

##### End Proceed Function #####
                         
tk.Button(frame_proceed, text='Proceed', command=proceed_submit).pack()

##### End Proceed Frame #####




##### Window mainloop #######

window.mainloop()





