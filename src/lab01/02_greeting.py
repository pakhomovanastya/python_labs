a = input('a:')
b = input('b:')
a,b = float(a.replace(',','.')),float(b.replace(',','.'))
summ=a+b
avg=(a+b)/2
print('summ=',round(summ,2),'; avg=',round(avg,2))
