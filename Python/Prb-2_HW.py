N = int(input())
tempList = []
twoDList = []
mx = -1e9+7;
ansIdx = -1;
for idx in range (N):
    values = input();
    tempList = values.split();
    sum = 0;
    for idx in range(len(tempList)):
        tempList[idx] = int(tempList[idx])
      #  print(tempList[idx])
        sum += tempList[idx]
    # print(sum)
    twoDList.append(tempList)
    if sum>mx:
        mx = sum;
        ansIdx = idx
    # print(mx)
        
print(mx,twoDList[ansIdx]);


        
        