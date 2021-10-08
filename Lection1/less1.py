print('Как тебя зовут ?')
name = input()

#----- next

print('Раз знакомству, ' , name, ' ! ', sep='')

age = int(input('Сколько тебе лет, ' + name  + '?'))

print('А я думал, тебе', age + 1, end='')

x = age + 1

if x >= 11 and x <= 19:
	print('лет')
elif x % 10 ==1:
	print('год')
elif x % 10 >= 2 and x % 10 <= 4:
	print('года')
else:
	print('лет')



print('!..')
