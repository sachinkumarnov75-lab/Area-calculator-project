# ==================
# Area Calculator 📐
# ==================
import math

while True:
    print("Area Calculator 📐")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    try:
        shape = int(input("Which shape: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        break
   
    if shape == 1:
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = 0.5 * base * height
        print(f"The area is {area}")
    
    elif shape == 2:
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = length * width
        print(f"The area is {area}")
    
    elif shape == 3:
        side = float(input("Side: "))
        area = side ** 2
        print(f"The area is {area}")
    
    elif shape == 4:
        radius = float(input("Radius: "))
        area = math.pi * radius ** 2
        print(f"The area is {area}")
    
    elif shape == 5:
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        
