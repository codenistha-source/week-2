speed_of_light=300000000

def main():
    mass=int(input("enter the mass in kg:"))
    energy=mass*speed_of_light**2
    print(f"E={energy}")

main()