class RestaurantFrame:
    def __init__(
        self,
        name,
        cuisine,
        address,
        hours,
        menu,
        reservation,
        rating,
        specials,
        contact,
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
    name, cuisine, address, hours, menu, reservation, rating, specials, contact
):
    restaurant = RestaurantFrame(
        name, cuisine, address, hours, menu, reservation, rating, specials, contact
    )
    restaurants_db.append(restaurant)
    print(f"Ресторан '{name}' додано до бази даних.")


def find_restaurant_by_name(name):
    for restaurant in restaurants_db:
        if restaurant.name == name:
            return restaurant
    return None


# Реалізуємо рекурсивний пошук за типом кухні
def find_restaurants_by_cuisine(cuisine, restaurants=None, index=0):
    if restaurants is None:
        restaurants = []
    if index >= len(restaurants_db):
        return restaurants
    if restaurants_db[index].cuisine == cuisine:
        restaurants.append(restaurants_db[index])
    return find_restaurants_by_cuisine(cuisine, restaurants, index + 1)


# Приклади використання програми
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
    "Ресторан 2",
    "Японська",
    "Адреса 2",
    "10:00 - 23:00",
    ["Суші", "Роли"],
    False,
    4.0,
    "Знижка на суші",
    ("987-654-3210", "email2@example.com"),
)

restaurant = find_restaurant_by_name("Ресторан 1")
if restaurant:
    print(f"Назва: {restaurant.name}")
    print(f"Тип кухні: {restaurant.cuisine}")
    # Виведення інших атрибутів

italian_restaurants = find_restaurants_by_cuisine("Італійська")
if italian_restaurants:
    print("Італійські ресторани:")
    for italian_restaurant in italian_restaurants:
        print(italian_restaurant.name)
