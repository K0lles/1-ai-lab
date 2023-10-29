from collections import defaultdict


class RestaurantFrame:
    def __init__(
        self,
        name,
        cuisine,
        address,
        hours,
        menu,
        reservation,
        rating=None,
        specials=None,
        contact=None,
    ):
        self.name = name
        self.cuisine = cuisine
        self.address = address
        self.hours = hours
        self.menu = menu
        self.reservation = reservation
        self.rating = rating
        self.specials = specials
        self.contact = contact


restaurants_db = []


def add_restaurant(
    name,
    cuisine,
    address,
    hours,
    menu,
    reservation,
    rating=None,
    specials=None,
    contact=None,
):
    restaurant = RestaurantFrame(name, cuisine, address, hours, menu, reservation, rating, specials, contact)
    restaurants_db.append(restaurant)
    print(f"Ресторан '{name}' додано до бази даних.")


# Приклади використання програми з урахуванням невизначеності
add_restaurant(
    "Ресторан 1",
    "Італійська",
    "Адреса 1",
    "8:00 - 22:00",
    ["Піца", "Паста"],
    True,
    4.5,
    "Спеціальна акція",
    ("123-456-7890", "email1@example.com"),
)
add_restaurant(
    "Ресторан 2", "Японська", "Адреса 2", "10:00 - 23:00", ["Суші", "Роли"], False
)
add_restaurant(
    "Ресторан 3",
    "Італійська",
    "Адреса 1",
    "8:00 - 22:00",
    ["Піца", "Паста", "Суші"],
    True,
    4.0,
    "Спеціальна акція",
    ("123-456-7890", "email1@example.com"),
)


def find_restaurants_by_multiple_criteria(criteria, excluded=None) -> tuple[set, set]:
    if excluded is None:
        excluded = []

    matching_restaurants = set()

    if len(criteria) == len(excluded):
        print("Не знайдено жодних співпадінь.")
        return set(), set()

    for key, value in criteria.items():
        if not key in excluded:
            has_intersection = False
            for restaurant in restaurants_db:
                if getattr(restaurant, key, None) == value:
                    has_intersection = True
                    matching_restaurants.add(restaurant)
            if not has_intersection:
                print(f"Збігів за критерієм {key} не знайдено. Його виключено із пошуку.")
                excluded.append(key)

    if matching_restaurants:
        return matching_restaurants, set(criteria.keys()) - set(excluded)

    if not matching_restaurants:
        return find_restaurants_by_multiple_criteria(criteria=criteria, excluded=excluded)


search_criteria = {"cuisine": "Італійська", "rating": 4.0, "address": "Адреса 1"}


matching_multiple_criteria_restaurants, searching_criteria = find_restaurants_by_multiple_criteria(search_criteria)
if matching_multiple_criteria_restaurants:
    print("Ресторани, що відповідають критеріям пошуку:")
    print(searching_criteria)
    for restaurant in matching_multiple_criteria_restaurants:
        print(restaurant.name)
