#calculate cuboid
def inputTake():
    try:
        l, w, h=list(map(int, input("Enter lenght, width, height : ").split()))
    except Exception as e:
        print("Please enter correct number.")
    return l, w, h
def calculate():
    stop='no'
    while(True):
        if stop.lower()=='no':
            l, w, h = inputTake()
            print("Cuboid volume is: ",l*w*h)
        elif stop.lower()=='yes':
            break
        else:
            print("Something else.")
        stop=input("If Stop program than Type Yes: ")
            
calculate()


