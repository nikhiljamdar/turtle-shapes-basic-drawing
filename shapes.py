from turtle import Turtle , Screen
import random
tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "slateGray", "SeaGreen" ]

def draw_shap(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range (3,11):
    tim.color(random.choice(colors))
    draw_shap(shape_side_n)





screen = Screen()
screen.exitonclick()