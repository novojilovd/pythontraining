def build_person(first_name, last_name, middle_name = ''):
    person = {'first': first_name, 'second': middle_name, 'third': last_name}
    return person

musician = []
musician.append(build_person('jimi', 'hendrix'))
musician.append(build_person('jimi', 'ivanovich', 'hendrix'))
print(musician)
