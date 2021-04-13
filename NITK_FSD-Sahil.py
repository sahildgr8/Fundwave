data = []    
def LQtoLTM():
    n = len(data)
    total = 0
    date = None
    count = 0
    for i in range(n):
        check = data[i][2]
        if check == "LQ":
            total += int(data[i][0])
            date = data[i][1]
            print(date)
            count +=1
            if count==4:
                print(f"output ({date} , LTM ) :")
                print(total)
                total = 0
                date = None
                count = 0

check = True
while(check):
    l = None
    try:
        l = input()
        data.append(l.split())
    
    except EOFError as e:
        check = False
LQtoLTM()
#print(data)