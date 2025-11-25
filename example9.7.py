

text = input()
text_new = text
total_old = 0
total_new = 0
replace_text = 'eyopaxcETOPAHXCBM'
replace_to_text = 'еуорахсЕТОРАНХСВМ'

for i in range(len(text)):
    total_old += ord(text[i])

for i in range(len(text_new)):
    for j in range(len(replace_text)):
        if replace_text[j] == text_new[i]:
            text_new = text_new.replace(replace_text[j],replace_to_text[j])


for i in range(len(text_new)):
    total_new += ord(text_new[i]) 

               
print(f"Старая стоимость: {total_old*3}🐝")    
print(f"Новая стоимость: {total_new*3}🐝")    

