from pie_shop import order_potato_pie
from potato_pie import bake, decorate

buyer_name = input()
potato_quantity = int(input())

order_potato_pie(buyer_name, potato_quantity)
bake(potato_quantity - 2)
decorate(4)