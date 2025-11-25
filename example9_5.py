text = input()
text_temp = text[1:len(text)]

if not text.startswith('@'):
    print("Incorrect")
  
elif not text.islower() and not text_temp.isdigit():
    print("Incorrect")

elif text.count('@') > 1:
    print("Incorrect")

elif text.count('_'):
    print("Incorrect")

elif len(text) < 5 or len(text) > 15:
    print("Incorrect")

else:
    print("Correct")