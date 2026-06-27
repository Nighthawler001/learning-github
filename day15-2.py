constraints = {
    'patient_id': True,
    'age': False,
    'gender': True,
    'diagnosis': False
}

for key,value in constraints.items():
    print(key,value)