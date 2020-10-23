def Volume(radius):
    volume=1.33*3.14*radius**3
    return volume

print("enter diameter")
diameter=int(input())
radius=diameter/2
volume=Volume(radius)
print(volume)
