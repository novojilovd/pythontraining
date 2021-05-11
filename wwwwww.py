names = {
    'channel1_to_post': ['text1', 'text2'],
    'channel2_to_post': ['other_text1', 'other_text2'],
}
d = {}
for name in names.keys():
    for t in names[name]:
        d[t.lower()] = name.lower()
print(d)
