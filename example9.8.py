n = int(input())
text = input()
decoded_text = ""

for i in range(len(text)):
    if ord(text[i])-n > 122 or ord(text[i])-n < 97:
        decoded_text += chr(ord(text[i])-n + 26)
    else:
        decoded_text += chr(ord(text[i])-n)
#97 122
print(decoded_text)