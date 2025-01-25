from math import *

while 1 < 2 :

	a = int(input('enter a ==> '));
	b = int(input('enter b ==> '));
	c = int(input('enter c ==> '));
	e = 2.7182818285;
	delta = ((b**2)-4*a*c)
	x1 = ((-1*b+sqrt(delta))/(2*a))
	x2 = ((-1*b-sqrt(delta))/(2*a))
	x0 = ((-1*b)/(2*a))

	print('∆  = b²-4ac = ',b,'² - 4 ×',a,'×',c,'=' ,delta);
	if delta > 0 :
		q_1 = str(input('do u want to see the solutions (yes/no) => '))
		if q_1 == 'yes' :
			print('x1 = ', x1)
			print('x2 = ', x2)
		if q_1 == 'no' :
			print('okay...')
	elif delta == 0 :
		q_2 = str(input('do u want to see the solutions (yes/no) => '))
		if q_2 == 'yes' :
			print('x0 = ', x0)
		if q_2 == 'no' :
			print('okay...')
	else :
		print('there is no solution')
