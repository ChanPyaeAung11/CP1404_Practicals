dict={}


text = input("Put a sentence here >>> ")
print(text)
splited = text.split()
for i in splited:
    count = dict.get(i, 0)
    dict[i] = count + 1

to_sort = list(dict.keys())
to_sort.sort()

print(to_sort)

max_length = max(len(word) for word in to_sort)
for word in to_sort:
    print("{:{}} : {}".format(word, max_length, dict[i]))
