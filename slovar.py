floppa_0 = {'type':'Fiery', 'color':'White'}
print(f"You meet {floppa_0['type']} Floppa")
print(f"It is {floppa_0['color']} Floppa")
floppa_0['Age'] = 14
floppa_0['Shield'] = True
print(floppa_0)
if floppa_0.get('Attack') == None:
    print("Floppa dont attac")
    floppa_0['Attack'] = 10
    print("But...\n")
    print("Floppa hit you\n")
    print(f"\tYou get {floppa_0['Attack']} damage")
