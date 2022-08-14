'''
    The file used to generate a random yet true and close  
    simulation of the dataset used for training.
'''



import pandas as pd
import random


# helper functions
def generate_randoms(start, stop, limit=60):
    lst = []
    for i in range(limit):
        n = random.uniform(start, stop)
        lst.append(n)
    
    return lst


def generate_final_columns(*lsts):
    final_lst = []
    for lst in lsts:
        for element in lst:
            final_lst.append(element)
    
    return final_lst

# list of features
features = [
    "BRAND",
    "DEVICE_LENGTH",
    "DEVICE_MAJORITY_COMPOSITION",
    "DEVICE_OUTPUT_TYPE",
    "SENSOR_TYPE"
]

# create a dataframe with the features
df = pd.DataFrame(columns=features)

# reference arrays
# brands
thermal_brand = random.choices(
    ['Delphi Automative', 'Hitachi Automotive Systems', 'Avago'],
    k=60
)
prox_brand = random.choices(
    ['Reed Rex', 'Kinequip'],
    k=60
)
ultra_brand = random.choices(
    ['Delphi Automative', 'Siemens', 'Rockwell Automation'],
    k=60
)

# device length
thermal_d_len = generate_randoms(50, 60)
prox_d_len = generate_randoms(30, 40)
ultra_d_len = generate_randoms(40, 50)

# device composition
thermal_comp = ['Ceramic' for i in range(60)]
prox_comp = ['Ferrite' for i in range(60)]
ultra_comp = ['Piezoelectric Crystals' for i in range(60)]

# device op
thermal_op = random.choices(
    ['Analog', 'Digital'],
    k=60
)
prox_op = random.choices(
    ['Analog', 'Digital'],
    k=60
)
ultra_op = ['Analog' for i in range(60)]

# sensor type
thermal_type = ['Thermal' for i in range(60)]
prox_type = ['Proximity' for i in range(60)]
ultra_type = ['Ultrasonic' for i in range(60)]

# final columns
final_brand = generate_final_columns(thermal_brand, prox_brand, ultra_brand)
final_d_len = generate_final_columns(thermal_d_len, prox_d_len, ultra_d_len)
final_d_comp = generate_final_columns(thermal_comp, prox_comp, ultra_comp)
final_d_op = generate_final_columns(thermal_op, prox_op, ultra_op)
final_sens_type = generate_final_columns(thermal_type, prox_type, ultra_type)

# assign columns to pandas
df['BRAND'] = final_brand
df['DEVICE_LENGTH'] = final_d_len
df['DEVICE_MAJORITY_COMPOSITION'] = final_d_comp
df['DEVICE_OUTPUT_TYPE'] = final_d_op
df['SENSOR_TYPE'] = final_sens_type

# pack it as a csv file
df.to_csv('./dataset/device_specs.csv', index=False)

