#Багринцев Даниил Михайлович
#2 вариант
fir_num, sec_num, third_num = map(int, input("Enter the numbers ").split())
if (fir_num>=1 and fir_num <=3):
	print(fir_num,"Подходит")
else:
	print(fir_num,"Не подходит")

if (sec_num>=1 and sec_num <=3):
	print(sec_num,"Подходит")
else:
	print(sec_num,"Не подходит")

if (third_num>=1 and third_num <=3):
	print(third_num,"Подходит")
else:
	print(third_num,"Не подходит")
