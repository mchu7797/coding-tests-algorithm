T = int(input())
testcase = []

for _ in range(T):
    testcase.append(int(input()))
    
for case in testcase:
    cents = case
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    
    while(cents >= 25):
        cents = cents - 25
        quarter = quarter + 1
    while(cents >= 10):
        cents = cents - 10
        dime = dime + 1
    while(cents >= 5):
        cents = cents - 5
        nickel = nickel + 1
    while(cents >= 1):
        cents = cents - 1
        penny = penny + 1
    
    print(quarter, dime, nickel, penny)
