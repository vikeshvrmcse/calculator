import math
pi=math.pi

def choiseArea():
    global selArea
    selArea=int(input("Select option given above : "))
    print("")

def showVariousArea():
    print("")
    print("Different Area is:")
    various_area=["1.Area of Circle", "2.Area of Triangle","3.Area of Sphere","4.Area of Cylinder","5.Area of Cone","6.Are you want exit now!"]
    for i in various_area:
        print(i)

def showVariousWeight():
    print("")
    print("Different Weight is:")
    various_weight = ["1.Weight of Disk", "2.Weight of sphere", "3.Weight of triangular prism", "4.Weight of Cuboid","5.Are you want exit now!"]
    for i in various_weight:
        print(i)


def choiseWeight():
    print("")
    global selWeight
    selWeight=int(input("Select option given above : "))

print("Different operation in application")

def mainOperShow():
    oper = ["1.Different area", "2.Different weight", "3.Exit"]
    for k in oper:
        print(k)
mainOperShow()

def mainOperChoose():
    global var
    var = int(input("Choose above option : "))
mainOperChoose()

def mainOper():
    if(var==1):
        def variousArea():
            showVariousArea()
            choiseArea()
            if selArea == 1:
                rad = float(input("Enter radius of circle in meter : "))
                print("Radius and Area of Circle is : ", rad, " , ", pi * (rad ** 2), "m2")
                variousArea()
            elif selArea == 2:
                side_1 = float(input("Enter side of triangle in meter : "))
                side_2 = float(input("Enter side of triangle in meter : "))
                side_3 = float(input("Enter side of triangle in meter : "))
                s = (side_1 + side_2 + side_3) / 2
                tr_area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
                print("Area of triangle in meter square", tr_area)
                variousArea()
            elif selArea == 3:
                sp_rad_a = float(input("Enter radius of sphere in meter : "))
                print("Radius and Area of Sphere is : ", sp_rad_a, " , ", 4*pi * (sp_rad_a ** 2), "m2")
                variousArea()
            elif selArea == 4:
                cy_rad_a = float(input("Enter radius of cylinder in meter : "))
                hei_a = float(input("Enter height of cylinder in meter : "))
                print("Radius Height and Area of Cylinder is : ", cy_rad_a, " , ", hei_a," and ",2 * pi * cy_rad_a * hei_a, "m2")
                variousArea()
            elif selArea == 5:
                co_rad_a = float(input("Enter radius of cone in meter : "))
                co_hei_a = float(input("Enter height of cone in meter : "))
                co_s=(co_rad_a**2)+(co_hei_a**2)
                print("Radius, Height and Area of Cone is : ",co_rad_a," , ",co_hei_a," and ",co_s)
                variousArea()
            elif selArea == 6:
                print("Switch direct main operation.")
                mainOperShow()
                mainOperChoose()
                mainOper()
            else:
                print("")
                print("Andha hai kya laude...!!!")
                print("")
                variousArea()
        variousArea()
    elif(var==2):
        def variousWeight():
            showVariousWeight()
            choiseWeight()
            if selWeight == 1:
                cy_rad = float(input("Enter radius of disk in meter : "))
                hei = float(input("Enter height of disk in meter : "))
                cy_den = float(input("Enter density of disk material in kg/m3: "))
                cy_volume = (pi * (cy_rad ** 2) * hei)
                cy_weight = (cy_den * cy_volume * 9.8)
                print("Weight of disk in newton : ", cy_weight)
                print("")
                variousWeight()
            elif selWeight == 2:
                sp_rad = float(input("Enter radius of sphere in meter : "))
                sp_volume = (4 / 3) * (sp_rad ** 3)
                sp_den = float(input("Enter density of spherical material in kg/m3: "))
                sp_weight = sp_volume * sp_den
                print("Weight of sphere in newton : ", sp_weight)
                print("")
                variousWeight()
            elif selWeight == 3:
                p_side_1 = float(input("Enter side of triangle prism in meter : "))
                p_side_2 = float(input("Enter side of triangle prism in meter : "))
                p_side_3 = float(input("Enter side of triangle prism in meter : "))
                p_hei = float(input("Enter height or thick of triangle prism in meter : "))
                p_den = float(input("Enter density of triangular prism material in kg/m3 : "))
                p_s = (p_side_1 + p_side_2 + p_side_3) / 2
                p_tr_area = math.sqrt(p_s * (p_s - p_side_1) * (p_s - p_side_2) * (p_s - p_side_3))
                p_volume = p_tr_area * p_hei
                p_weight = p_den * p_volume
                print("Weight of triangular prism in newton : ", p_weight)
                print("")
                variousWeight()
            elif selWeight == 4:
                length = float(input("Enter length of cuboid in meter : "))
                width = float(input("Enter width of cuboid in meter : "))
                height = float(input("Enter height of cuboid in meter : "))
                cu_den = float(input("Enter density of cuboid material in kg/m3 : "))
                cu_volume = length * width * height
                cu_weight = cu_volume * cu_den
                print("Weight of cuboid material in newton : ", cu_weight)
                print("")
                variousWeight()
            elif selWeight == 5:
                print("")
                print("Switch direct main operation.")
                mainOperShow()
                mainOperChoose()
                mainOper()
            else:
                print("")
                print("Andha hai kya laude...!!!")
                print("")
                variousWeight()
        variousWeight()
    elif var == 3:
        print("Thanks for use this application")
    else:
        print("")
        print("Andha hai kya laude...!!!")
        print("")
        mainOperShow()
        mainOperChoose()
        mainOper()
mainOper()