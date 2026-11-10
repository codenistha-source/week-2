def main():
    bill=float(input("Enter the bill amount:"))
    tip_percent=float(input("enter the tip percent:"))

    tip=bill*(tip_percent/100)
    total=bill+tip

    print(f"tip ampunt:Rs{tip:.2f}")
    print(f"total amount:Rs{total:.2f}")

main()