import car_utils
from car import Car

cars = {}

def main():
    while True:
        print("\n--- Car Management System ---")
        print("1. Add Car")
        print("2. View All Cars")
        print("3. Drive Car")
        print("4. Paint Car")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            # TODO: Agregar un auto nuevo
            new_car = car_utils.create_car_from_input()
            cars[new_car.car_id] = new_car
            print(new_car)
            print("Car added.")

        elif choice == "2":
            # TODO: Ver todos los autos
            car_utils.display_cars(cars)

        elif choice == "3":
            # TODO: Conducir un auto
            car_id = input("Enter car ID:\n")
            miles = float(input("Enter miles to drive:\n"))
            
            if car_id in cars:
                cars[car_id].drive(miles)
                print("Mileage updated.")
                print(cars[car_id])
            else:
                print("Error: Car ID not found.")

        elif choice == "4":
            # TODO: Pintar un auto
            car_id = input("Enter car ID:\n")
            new_color = input("Enter new color:\n")
            
            if car_id in cars:
                cars[car_id].change_color(new_color)
                print("Color updated.")
                print(cars[car_id])
            else:
                print("Error: Car ID not found.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()