import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    machine_on = True

    while machine_on:

        choice = input("What size sandwich would you like? (small/medium/large): ").lower()

        if choice == "off":
            machine_on = False
        elif choice == "report":
            print("Bread: " + str(resources["bread"]))
            print("Ham: " + str(resources["ham"]))
            print("Cheese: " + str(resources["cheese"]))
        elif choice == "small" or choice == "medium" or choice == "large":

            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                print("The cost is $" + str(cost))
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
