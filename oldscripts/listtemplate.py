langs = ['C', 'C++', 'Pascal', 'Pascal++']
num = [0, 1, 2, 3]
print(num[0-3]) # -3 position into num is 1
print(langs[num[0-3]]) # 1 position into langs is 'C++'
langs[3] = 'Python'
print(langs)
langs.append('Pascal++')
print(langs)
langs.insert(5, 'Go')
print(langs)
# del langs[5]
# print(langs)
# forgotenlang = langs.pop()
langs.remove('Pascal++')
print(sorted(langs))
langs.reverse()
print(langs)
# print(forgotenlang)
print(len(langs))
