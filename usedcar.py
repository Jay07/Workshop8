from car import Car

def main():
    # bus = Car(180)
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    # print(bus)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("Limo fuel =", limo.fuel)
    limo.drive(115)
    print("Limo odo =", limo.odometer)
    print(limo)

main()
