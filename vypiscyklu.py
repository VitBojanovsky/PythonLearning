'''Vypis cisel od 50 do 150 po 3'''
start = 50;
stop = 150;
jump = 5;
i = 0
'''
i = start;
print("Cyklus 1");
while i <= stop: 
    print(i);
    i += jump;

print("Cyklus 2");
i = start;
for i in range(start, stop, jump):
    print(i);
'''

start = stop;
stop = 50;
i = start;

print("Cyklus 1");
i = start;
while i >= stop:
    print(i);
    i -= jump;

i = start;
for i in range(start,stop,-jump):
    print(i);


