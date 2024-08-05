import another_module
# print(another_module.another_variable)

# timmy = turtle.Turtle() # use method Turtle from module turtle

from turtle import Turtle, Screen # this imports the Turtle class instead of the entire turtle module
# timmy = Turtle() # timmy is the object in this case
# print(timmy)

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(10)
# car.speed, so car is object, speed is attribute, period acts as stopper
# car.stop() uses the stop() method on car
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

from prettytable import PrettyTable
table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
tab = PrettyTable(table[0])
print(tab)