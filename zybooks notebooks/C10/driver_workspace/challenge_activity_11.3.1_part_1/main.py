from pie_shop import buy_apple_pie
from apple_pie import bake
customer_name = input()
num_apples = int(input())
buy_apple_pie(customer_name, num_apples)
bake(num_apples)