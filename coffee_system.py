class CoffeeOrderSystem:
    def __init__(self):
        self.list_of_drinks = ['Ice latte', 'Green tea', 'Black coffee', 'Cappuccino', 'Americano', 'Thai tea']
        self.orders = []

    def show_menu(self):
        print("Menu:")
        for index, drink in enumerate(self.list_of_drinks, start=1):
            print(f"{index}. {drink}")

    def take_order(self):
        self.show_menu()
        try:
            choice = int(input("Enter the number of the drink you'd like to order: "))
            if choice < 1 or choice > len(self.list_of_drinks):
                print("Invalid choice. Please select a valid drink.")
                return
            drink = self.list_of_drinks[choice - 1]
            self.orders.append(drink)
            print(f"You've ordered {drink}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_orders(self):
        if not self.orders:
            print("No orders yet.")
        else:
            print("Current orders:")
            for index, order in enumerate(self.orders, start=1):
                print(f"{index}. {order}")

    def run(self):
        while True:
            print("\nWelcome to the Coffee Order System!")
            print("1. Take Order")
            print("2. View Orders")
            print("3. Exit")
            choice = input("Select an option (1/2/3): ")
            
            if choice == '1':
                self.take_order()
            elif choice == '2':
                self.view_orders()
            elif choice == '3':
                print("Thank you for using the Coffee Order System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    coffee_system = CoffeeOrderSystem()
    coffee_system.run()
