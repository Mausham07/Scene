# importing from draw2d to call the inbuilt functions
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.


    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, scene_width, scene_height):
    #Draw the sky and all the objects in the sky.
        
    draw_rectangle(canvas, 0, scene_height /3,
    scene_width, scene_height, width=0, fill="sky blue")
  
    diameter = 80
    space = 5
    interval = diameter + space
    x = 620
    y = 370


    for i in range(1):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="yellow", fill="yellow")
        x += interval
        y -= interval

    # calling draw_cloud function to draw the clouds
    draw_cloud(canvas, 400, 420)
    draw_cloud(canvas, 350, 380)
    draw_cloud(canvas, 450, 380)
    draw_cloud(canvas, 50, 450)
    draw_cloud(canvas, 0, 400)
            
            


def draw_ground(canvas, scene_width, scene_height):
    #Draw the ground and all the objects on the ground.
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # here creating, giving values to create the house in the scene
    house_center_x = 400
    house_bottom = 100
    house_height = 330

    # calling draw_house to draw the house
    draw_house(canvas, house_center_x, house_bottom, house_height)


    # giving values to draw the fence for the vertical ones
    fence_center_x = 50
    interval = 100
    while fence_center_x <= 800:
        bottom = 75
        height = 200

        draw_fence_vertical(canvas, fence_center_x, bottom, height)

        fence_center_x += interval

    #giving values to draw the fence for the horizontal ones
    fence_center_y = 85
    interval = 50
    while fence_center_y <= 200:
        left_x = 0
        right_x = 800

        draw_fence_horizontal(canvas, fence_center_y, left_x, right_x)
        fence_center_y += interval
    
    # giving values to draw the trees in loop so that they can have multiple trees
    tree_center_x = 20
    interval = 110
    while tree_center_x <= 800:
        tree_bottom = 20
        tree_height = 180

        #calling draw_pine function to draw tree
        draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

        tree_center_x = tree_center_x + interval

# defining the function which can draw the fence in vertical line    
def draw_fence_vertical(canvas, center_x, bottom, height):

    fence_starting_x = center_x - 10
    fence_ending_x = center_x + 10

    # calling in-built function draw_rectangle to draw the fence in vertical
    draw_rectangle(canvas, fence_starting_x, bottom, fence_ending_x, height, outline="white", fill="white")


#defining the funciton which can draw the fence in the horizontal line
def draw_fence_horizontal(canvas, center_y, left, right):
    fence_starting_y = center_y - 10
    fence_ending_y = center_y + 10

    # calling in-built function draw_rectangle to draw fence in horizontal
    draw_rectangle(canvas, left, fence_starting_y, right, fence_ending_y, outline="white", fill="white")


#defining the function to draw the house
def draw_house(canvas, center_x, bottom, height):

    #adjusting height and width for the base of house
    house_width = height / 5
    house_height = height / 2
    house_starting_x = center_x - house_width
    house_ending_x = center_x + house_width
    house_starting_y = bottom + house_height

    draw_rectangle(canvas, house_starting_x, house_starting_y, house_ending_x, bottom, fill="brown3")

    draw_rectangle(canvas, 370, 100, 430, 170, outline="ivory3", fill="ivory2")

    #adjusting height and width for the skirt of house
    skirt_width = height / 3
    skirt_height = height - house_height
    skirt_starting_x = center_x - skirt_width
    skirt_ending_x = center_x + skirt_width
    skirt_starting_y = height

    draw_polygon(canvas, center_x, skirt_starting_y, skirt_starting_x, house_starting_y, skirt_ending_x, house_starting_y, fill="brown4")


#   defining the function that can draw the pine trees
def draw_pine_tree(canvas, center_x, bottom, height):
    
    trunk_width = height / 6
    trunk_height = height / 4
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# defining the function which can draw the cloud
def draw_cloud(canvas, center_starting_x, center_starting_y):
    starting_point_x = center_starting_x - 100
    starting_point_y = center_starting_y - 50
    ending_point_x = center_starting_x + 100
    ending_point_y = center_starting_y + 50

    #calling inbuilt function to draw cloud as oval
    draw_oval(canvas, starting_point_x, starting_point_y, ending_point_x, ending_point_y, width=1, outline="white",fill="white")


# Call the main function so that
# this program will start executing.
main()