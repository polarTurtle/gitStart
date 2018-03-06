strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for n in strings:
	sentence = sentence+' '+n
print(sentence.strip())
print(' '.join(strings))