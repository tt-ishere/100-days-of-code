# from turtle import Turtle, Screen
#
# tt = Turtle()
# tt.shape('turtle')
# tt.color('DarkViolet')
# tt.fd(100)
# print(tt)
#
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'

print(table)
