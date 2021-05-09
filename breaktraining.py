colors = {'deep': 4, 'brush': 'aqua'}
existances = {'freedom': 'Absolute', 'sanity': 15}
parameters = [colors, existances]
for parameter in parameters:
    for key, value in parameter.items():
        if key == 'deep' and value != 4:
            break
        if key == 'freedom':
            print(f'Your freedom is {value}')
key, value = parameters[0].items()
print(key, value)
colors['deep'] = 5
key, value = parameters[0].items()
print(key, value)
