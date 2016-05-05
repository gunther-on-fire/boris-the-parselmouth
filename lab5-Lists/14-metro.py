N = int(input('Количество пассажиров: '))
In_Time = list(map(int,input('Время входа n-ого пассажира в метро: ').split()))
In_Time = In_Time[:N]

Out_Time = list(map(int,input('Время выхода n-ого пассажира из метро: ').split()))
Out_Time = Out_Time[:N]

T = int(input('Отслеживаемый момент времени: '))
count = 0

for i in range(N):
	if T >= In_Time[i] and T <= Out_Time[i]:
		count += 1
	
print(count)