import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def build_fuzzy_system():
    # -------- Input Variables --------
    soil_moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'soil_moisture')
    temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

    # -------- Output Variable --------
    irrigation = ctrl.Consequent(np.arange(0, 101, 1), 'irrigation')

    # -------- Membership Functions --------
    soil_moisture['dry'] = fuzz.trimf(soil_moisture.universe, [0, 0, 40])
    soil_moisture['moderate'] = fuzz.trimf(soil_moisture.universe, [30, 50, 70])
    soil_moisture['wet'] = fuzz.trimf(soil_moisture.universe, [60, 100, 100])

    temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 20])
    temperature['medium'] = fuzz.trimf(temperature.universe, [15, 25, 35])
    temperature['high'] = fuzz.trimf(temperature.universe, [30, 40, 40])

    humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 40])
    humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
    humidity['high'] = fuzz.trimf(humidity.universe, [60, 100, 100])

    irrigation['low'] = fuzz.trimf(irrigation.universe, [0, 0, 40])
    irrigation['medium'] = fuzz.trimf(irrigation.universe, [30, 50, 70])
    irrigation['high'] = fuzz.trimf(irrigation.universe, [60, 100, 100])

    # -------- Rules --------
    rules = [
        ctrl.Rule(soil_moisture['dry'], irrigation['high']),
        ctrl.Rule(soil_moisture['moderate'] & temperature['high'] & humidity['low'], irrigation['high']),
        ctrl.Rule(soil_moisture['moderate'] & temperature['medium'] & humidity['medium'], irrigation['medium']),
        ctrl.Rule(soil_moisture['moderate'] & temperature['low'] & humidity['high'], irrigation['low']),
        ctrl.Rule(soil_moisture['wet'], irrigation['low']),
        ctrl.Rule(temperature['high'] & humidity['low'], irrigation['high']),
        ctrl.Rule(temperature['low'] & humidity['high'], irrigation['low']),
        ctrl.Rule(temperature['medium'] & humidity['medium'], irrigation['medium'])
    ]

    control_system = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(control_system)
