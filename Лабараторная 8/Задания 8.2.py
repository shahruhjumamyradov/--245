s = 'Преобразовать строку так, чтобы буквы каждого слова в ней были отсортированы по алфавиту'.lower().split(' ')
for i in range(len(s)):
     __s=(i) = ''.join(sorted(s[i]))
print(' '.join(s))
