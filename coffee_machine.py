class CoffeeMachine:
    state = 'choosing an action'  # default state

    def user_input(self, choice):
        if self.state == 'choosing an action':
            if choice == 'buy':
                self.state = 'buying a coffee'
                self.user_input(choice=input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>'))
            elif choice == 'remaining':
                self.remaining()
            elif choice == 'fill':
                self.state = 'adding water'
                self.user_input(choice=input('Write how many ml of water do you want to add:\n>'))
            elif choice == 'take':
                print(f'\nI gave you ${self.money}\n')
                self.money = 0
            elif choice == 'exit':
                self.state = 'exit'
        elif self.state == 'buying a coffee':
            self.action_buy(choice)
            self.state = 'choosing an action'  # recover state back to default
        elif self.state == 'adding water':
            self.water += int(choice)
            self.state = 'adding milk'
            self.user_input(choice=input('Write how many ml of milk do you want to add:\n>'))
        elif self.state == 'adding milk':
            self.milk += int(choice)
            self.state = 'adding coffee beans'
            self.user_input(choice=input('Write how many grams of coffee beans do you want to add:\n>'))
        elif self.state == 'adding coffee beans':
            self.beans += int(choice)
            self.state = 'adding cups'
            self.user_input(choice=input('Write how many disposable cups of coffee do you want to add:\n>'))
        elif self.state == 'adding cups':
            self.cups += int(choice)
            self.state = 'choosing an action'  # back to default state

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def action_buy(self, coffee_type):
        if coffee_type == '1':
            # if "enough" do "reduction"
            if self.enough(250, 16, 0, 1):
                self.reduction(250, 16, 0, 1, 4)
        elif coffee_type == '2':
            if self.enough(350, 20, 75, 1):
                self.reduction(350, 20, 75, 1, 7)
        elif coffee_type == '3':
            if self.enough(200, 12, 100, 1):
                self.reduction(200, 12, 100, 1, 6)
        elif coffee_type == 'back':
            print()

    def reduction(self, water, beans, milk, cups, money):
        self.water -= water
        self.beans -= beans
        self.cups -= cups
        if milk != 0:  # if milk is used
            self.milk -= milk
        self.money += money
        print('I have enough resources, making you a coffee!\n')

    def enough(self, water, beans, milk, cups):
        self.state = 'choosing an action'
        if self.water < water:
            print('Sorry, not enough water!\n')
            return False
        elif self.beans < beans:
            print('Sorry, not enough beans!\n')
            return False
        elif self.cups < cups:
            print('Sorry, not enough cups!\n')
            return False
        elif self.milk < milk:
            print('Sorry, not enough milk!\n')
            return False
        else:
            return True

    def remaining(self):
        print()
        print('The coffee machine has:')
        print(self.water, ' of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money\n')


coffee_machine = CoffeeMachine()
while True:
    coffee_machine.user_input(input('Write action (buy, fill, take, remaining, exit):\n>'))
    if coffee_machine.state == 'exit':
        break
