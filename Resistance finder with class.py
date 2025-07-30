# Creating the class for the resistance finder

class resistance:

    def __init__(self):
        self.color_finder = ["black","brown","red","orange","yellow","green","blue","violet","gray","white"]

    # Function for finding the color code

    def finding_color_code(self):
        while True:

            a = input("Enter the resistance to find its color code :")
            
            if a.isdigit():

                c1 = int(a[0])
                c2 = int(a[1])
                c3 = int(len(a) - 2)

                if c3 > 9:
                    print("Sorry,large input\n") 
                    continue
                else:
                    print("The color code is ",self.color_finder[c1],"|",self.color_finder[c2],"|",\
                    self.color_finder[c3],"\n")
                    pass
            else:
                print("Wrong input\n")
                continue

            z = input("Do you want to continue? (y or n) ").lower()

            if z == "n":
                break

    # Function for finding the resistance

    def finding_resistance(self):

        while True:

            a = input("Enter the three colors  :").lower()
            b = input("\t\t\t:").lower()
            c = input("\t\t\t:").lower()

            if a and b and c in self.color_finder:

                c1 = self.color_finder.index(a)
                c2 = self.color_finder.index(b)
                c3 = self.color_finder.index(c)

                resistance = c1 + (10*c2) + 10**c3

                print("\nThe resistance is ",resistance)
                pass

            else:
                print("Enter a valid input!\nThe colors are ",self.color_finder)
                continue

            z = input("Do you want to continue? (y or n) ").lower()

            if z == "n":
                break

    # The main function

    def main(self):

        while True:
            print("\n What do you want to do? \n1.Find the color code\n2.Find the resistance\n3.Exit")
            a = int(input("Enter your choice : "))

            if a == 1:
                self.finding_color_code()

            elif a == 2:
                self.finding_resistance()

            elif a == 3:
                print("Thank you for using!")
                break

            else:
                print("Enter a valid input.")
                continue

rs = resistance()
rs.main()
