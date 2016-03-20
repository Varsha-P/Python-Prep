from collections import Counter
# Tally occurrences of words in a list
words = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counts = Counter(words).most_common(2)
print(counts)
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

#Counter({'blue': 3, 'red': 2, 'green': 1})

# Find the ten most common words in Hamlet
'''import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]'''