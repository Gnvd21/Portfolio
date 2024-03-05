
digits = "8459761203"
nums = "5439"

def input_check(nums,digits):
    if len(digits) == 10 and len(nums) <=10000:
        func1(nums,digits)
    else:
        print("One or more input have incorrect number of values.")

def func1(num, digit):
    steps = 0
    in_a = 0
    in_b = 0
    for n in num:
        in_b = func2(n,digit)
        steps += step_count(in_a, in_b)
        in_a = in_b
        print ("steps" + str(steps))
    return steps    
        
def func2(Num,digit) ->int :
    index: int = 0
    for d in digit:
        if Num == d:
            return index
        else:
            index += 1
            
def step_count(a, b):
    A = max(a, b)
    B = min(a, b)
    Res = A - B
    return Res
#test()
#func1(nums, digits)
input_check(nums,digits)
