def calculate_area(base,height):
    area=(1/2)*base*height
    return area


def calculate_area1(length,width):
    area=length*width
    return area


shape=input("Enter the shapes:")
if(shape=="triangle"):
    base=float(input("Enter the base of the triangle:"))
    height=float(input("Enter the height of the triangle:"))
    print(f"The area of the triangle is {calculate_area(base,height)}")

elif(shape=="rectangle"):
    lenght=int(input("Enter the length of the rectangle:"))
    width=int(input("Enter the width of the rectangle:"))
    print(f"The area of rectangle is {calculate_area1(lenght,width)}")
else:
    print("Shapes are not found")