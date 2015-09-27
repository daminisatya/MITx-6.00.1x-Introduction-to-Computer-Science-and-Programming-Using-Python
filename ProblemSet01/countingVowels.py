count = 0
def isVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    return False
for var in s:
    if isVowel(var):
        count += 1
print("Number of vowels:" + " " + str(count))