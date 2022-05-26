"""from turtle import Turtle, Screen

mc_mikay = Turtle()
mc_mikay.shape("turtle")
mc_mikay.color("orange")
mc_mikay.fd(100)
mc_mikay.rt(-90)
mc_mikay.fd(100)
print(mc_mikay)

my_screen = Screen()
my_screen.exitonclick()
print(my_screen.canvwidth)"""

from prettytable import PrettyTable, MSWORD_FRIENDLY, ORGMODE
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.set_style(ORGMODE)
table.align = "l"
print(table)
