input_data = open('input.txt', 'r') # Открываем для чтения (литера 'r') файл и кладем его в переменную
S = input_data.read() # Читаем в другую переменную содержимое всего файла
S= int(S)
out=str(int(S/6))+" "+str(int(2*S/3))+" "+str(int(S/6))

output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
# Записываем результат сложения и не забываем преобразовать его в строку (иначе будет ошибка)
output_data.write(out)

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()