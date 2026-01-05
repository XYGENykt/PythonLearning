abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов", "Захаров"}

#Возвращает множество элементов abons, которые не встречаются в debtors
non_debtors = abons.difference(debtors)
print(non_debtors)

#возвращает объединенное множество
union = abons.union(debtors)
print(union)

#возвращает множество, состоящее из элементов кот. встречаются там и там
intersection = abons.intersection(debtors)
print(intersection)

#возвращает те элементы которые не принадлежат обоим одновременно
symmetric_diff = abons.symmetric_difference(debtors)
print(symmetric_diff)