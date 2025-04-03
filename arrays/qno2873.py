#  maximum valueofanordered triplet-i
def maximum(number):
    res=0
    N = len(number)
    left = number[0]
    for j in range(1,N):
        if number[j]>left:
            left = number[j]
        for k in range(j+1,N):
            res = max (res, (left-number[j]) * number[k])
    print("the greatest value is ", res)
number = [12,6,1,2,7]

# lets take a list of number . According to question , we have to find the maximum value of an ordered triplet
# where i<j<k and the formula is (number[i]-number[j]) * number[k]. to obtain the maximum value the value of i 
# indexed must be maximum  j must be minimum and k must be maximum. We can also use three loops to obtain 
# the max value but the time complxity will be O(n3). To reduce the complexity, i fixed the i and move the
# pointer j and make the comparison between i and j . 