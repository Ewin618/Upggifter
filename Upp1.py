storlek = int(input("Skriv in ett positivt udda heltal: "))

start = storlek
stop = 0
steg = -1

for i in range(start,stop,steg):
    #print(" " * (storlek - i) + "*" * i)
    print(f"{("*" * i):>{storlek}}")
    
