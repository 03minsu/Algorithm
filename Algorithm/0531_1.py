array = [[0]*6 for i in range(5)]
#  [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(array)
for x in range(6):
    print(x,end=" ")

print("\n")
for i in array :
    for j in i:
        print(j,end=" ")
    print()

money = 1000
count = 1
num = 0
while True:
    print("\n   맨시티 VS 첼시 \n    스코어 예측")
    i = int(input("맨시티 : "))
    if(i == 404): 
        score = input("결과 입력 좌 맨시티 : 우 첼시 ").split(":")
        print("경기 결과",score[0],score[1])
        A = int(score[0])
        B = int(score[1])
        if(score[0] > score[1]):
            
            print("맨시티 승")
            print("당첨자는 ",array[A][B],"명 총 상금 : ",moneySUM,"원","인 당 배당금 : ",int(moneySUM/int(array[A][B])),"원")
        elif(score[0] == score[1]):
            print("무승부")
            print("당첨자는 ",array[A][B],"명 총 상금 : ",moneySUM,"원","인 당 배당금 : ",int(moneySUM/int(array[A][B])),"원")
        else:
            
            print("첼시 승")
            print("당첨자는 ",array[A][B],"명 총 상금 : ",moneySUM,"원","인 당 배당금 : ",int(moneySUM/int(array[A][B])),"원")
        break
    j = int(input("첼시 : "))
    
    num += 1
    moneySUM = money*num
    print("참가자 ",num,"명 총 배당액 : ",moneySUM,"원")
    array[i][j] += count

    for x in range(6):
        print(x,end=" ")

    print("\n")
    for i in array :
        for j in i:
            print(j,end=" ")
        print()