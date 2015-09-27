countBob = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        countBob += 1
print("Number of times bob occurs is: ") + str(countBob)