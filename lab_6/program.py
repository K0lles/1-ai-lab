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
