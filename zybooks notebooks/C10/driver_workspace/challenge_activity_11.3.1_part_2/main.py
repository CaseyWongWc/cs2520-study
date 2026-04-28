from airline_desk import check_in, check
traveler_name = input()
luggage_quantity = int(input())

check_in(traveler_name, luggage_quantity)
check(luggage_quantity)