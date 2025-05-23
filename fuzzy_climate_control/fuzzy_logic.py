import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def get_fuzzy_result(room_temp, outside_temp, comfort_pref, hour, energy_cost):
    # Girdi tanımları
    room = ctrl.Antecedent(np.arange(10, 36, 1), 'room_temp')
    outside = ctrl.Antecedent(np.arange(-10, 41, 1), 'outside_temp')
    comfort = ctrl.Antecedent(np.arange(1, 11, 1), 'comfort_pref')
    saat = ctrl.Antecedent(np.arange(0, 25, 1), 'hour')
    enerji = ctrl.Antecedent(np.arange(0.1, 1.1, 0.1), 'energy_cost')

    # Çıktı tanımları
    heat = ctrl.Consequent(np.arange(0, 101, 1), 'heating')
    cool = ctrl.Consequent(np.arange(0, 101, 1), 'cooling')

    # Üyelik fonksiyonları
    room['cold'] = fuzz.trimf(room.universe, [10, 10, 20])
    room['comfortable'] = fuzz.trimf(room.universe, [18, 22, 26])
    room['hot'] = fuzz.trimf(room.universe, [24, 35, 35])

    outside['very_cold'] = fuzz.trimf(outside.universe, [-10, -10, 5])
    outside['cold'] = fuzz.trimf(outside.universe, [0, 10, 20])
    outside['warm'] = fuzz.trimf(outside.universe, [15, 25, 35])
    outside['hot'] = fuzz.trimf(outside.universe, [30, 40, 40])

    comfort['cool'] = fuzz.trimf(comfort.universe, [1, 1, 5])
    comfort['neutral'] = fuzz.trimf(comfort.universe, [3, 5, 7])
    comfort['warm'] = fuzz.trimf(comfort.universe, [6, 10, 10])

    saat['night'] = fuzz.trimf(saat.universe, [0, 0, 6])
    saat['morning'] = fuzz.trimf(saat.universe, [5, 9, 12])
    saat['afternoon'] = fuzz.trimf(saat.universe, [11, 15, 18])
    saat['evening'] = fuzz.trimf(saat.universe, [17, 21, 24])

    enerji['low'] = fuzz.trimf(enerji.universe, [0.1, 0.1, 0.5])
    enerji['medium'] = fuzz.trimf(enerji.universe, [0.3, 0.6, 0.9])
    enerji['high'] = fuzz.trimf(enerji.universe, [0.7, 1.0, 1.0])

    heat['low'] = fuzz.trimf(heat.universe, [0, 0, 40])
    heat['medium'] = fuzz.trimf(heat.universe, [30, 50, 70])
    heat['high'] = fuzz.trimf(heat.universe, [60, 100, 100])

    cool['low'] = fuzz.trimf(cool.universe, [0, 0, 40])
    cool['medium'] = fuzz.trimf(cool.universe, [30, 50, 70])
    cool['high'] = fuzz.trimf(cool.universe, [60, 100, 100])

    # Kurallar
    rule1 = ctrl.Rule(room['cold'] & outside['very_cold'] & comfort['warm'], (heat['high'], cool['low']))
    rule2 = ctrl.Rule(room['comfortable'] & comfort['neutral'], (heat['low'], cool['low']))
    rule3 = ctrl.Rule(room['hot'] & comfort['cool'], (heat['low'], cool['high']))
    rule4 = ctrl.Rule(room['cold'] & enerji['high'], (heat['medium'], cool['low']))
    rule5 = ctrl.Rule(room['hot'] & outside['hot'] & enerji['low'], (heat['low'], cool['high']))
    rule6 = ctrl.Rule(room['comfortable'] & outside['cold'] & comfort['warm'], (heat['medium'], cool['low']))
    rule7 = ctrl.Rule(room['hot'] & saat['afternoon'], (heat['low'], cool['high']))
    rule8 = ctrl.Rule(room['cold'] & saat['night'], (heat['high'], cool['low']))
    rule9 = ctrl.Rule(room['comfortable'] & enerji['low'], (heat['low'], cool['low']))
    rule10 = ctrl.Rule(room['hot'] & enerji['high'], (heat['low'], cool['medium']))

    # Sistem kurulumu
    system = ctrl.ControlSystem([
        rule1, rule2, rule3, rule4, rule5,
        rule6, rule7, rule8, rule9, rule10
    ])

    sim = ctrl.ControlSystemSimulation(system)

    # Girdileri ayarla
    sim.input['room_temp'] = room_temp
    sim.input['outside_temp'] = outside_temp
    sim.input['comfort_pref'] = comfort_pref
    sim.input['hour'] = hour
    sim.input['energy_cost'] = energy_cost

    # Hesapla
    sim.compute()

    return sim.output['heating'], sim.output['cooling']

