# # import numpy as np
#
#
# # Функція приналежності "повільно"
# def slow_membership(speed):
#     if speed <= 40:
#         return 1.0
#     elif speed > 40 and speed < 60:
#         return (60 - speed) / 20
#     else:
#         return 0.0
#
#
# # Функція приналежності "середньо"
# def medium_membership(speed):
#     if speed <= 40 or speed >= 100:
#         return 0.0
#     elif speed > 40 and speed <= 70:
#         return (speed - 40) / 30
#     elif speed > 70 and speed < 100:
#         return (100 - speed) / 30
#
#
# # Функція приналежності "швидко"
# def fast_membership(speed):
#     if speed >= 100:
#         return 1.0
#     elif speed > 60 and speed < 100:
#         return (speed - 60) / 40
#     else:
#         return 0.0
#
#
# # База правил
# def fuzzy_system(speed):
#     # Визначення ступеня належності кожному терміну лінгвістичної змінної
#     slow = slow_membership(speed)
#     print(slow)
#     medium = medium_membership(speed)
#     print(medium)
#     fast = fast_membership(speed)
#     print(fast)
#
#     # Визначення результату на основі бази правил
#     # Правило 1: Якщо швидкість повільна, то рекомендовано збільшити швидкість.
#     increase_speed = max(slow, 0)
#     print(f"increase-speed: {increase_speed}")
#
#     # Правило 2: Якщо швидкість середня, то рекомендовано тримати поточну швидкість.
#     maintain_speed = max(medium, 0)
#     print(f"maintain_speed: {maintain_speed}")
#
#     # Правило 3: Якщо швидкість швидка, то рекомендовано знизити швидкість.
#     decrease_speed = max(fast, 0)
#     print(f"decrease_speed: {decrease_speed}")
#
#     # Визначення вагованого середнього результату
#     weighted_sum = (increase_speed * 50 + maintain_speed * 100 + decrease_speed * 150)
#     print(f"weighted_sum: {weighted_sum}")
#     sum_of_weights = (increase_speed + maintain_speed + decrease_speed)
#     print(sum_of_weights)
#     if sum_of_weights == 0:
#         return 0
#     else:
#         crisp_value = weighted_sum / sum_of_weights
#         return crisp_value
#
#
# speed = 90  # Швидкість автомобіля у км/год
# result = fuzzy_system(speed)
# print(f"Рекомендована швидкість: {result} км/год")

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Вхідні та вихідні дані
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
desired_temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'desired_temperature')
heat_cool = ctrl.Consequent(np.arange(-100, 101, 1), 'heat_cool')

# Функції належності
temperature.automf(3)
desired_temperature.automf(5)
heat_cool['cool'] = fuzz.trimf(heat_cool.universe, [-100, -50, 0])
heat_cool['no_change'] = fuzz.trimf(heat_cool.universe, [-25, 0, 25])
heat_cool['heat'] = fuzz.trimf(heat_cool.universe, [0, 50, 100])

# База правил
rule1 = ctrl.Rule(temperature['poor'] | desired_temperature['poor'], heat_cool['cool'])
rule2 = ctrl.Rule(temperature['average'] | desired_temperature['average'], heat_cool['no_change'])
rule3 = ctrl.Rule(temperature['good'] | desired_temperature['good'], heat_cool['heat'])

# Створення системи керування
heat_cool_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
temperature_control = ctrl.ControlSystemSimulation(heat_cool_ctrl)

# Введення даних та обчислення
temperature_value = 35
desired_temperature_value = 50

temperature_control.input['temperature'] = temperature_value
temperature_control.input['desired_temperature'] = desired_temperature_value
temperature_control.compute()
print("Рівень подачі тепла/охолодження:", temperature_control.output['heat_cool'])
