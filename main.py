print("Wellcome to the Roller coaster! ")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the Roller coaster! ")
    bill = 0
    age = int(input("What is your age? "))
    while age > 120:
        int(input("Wrong age! What is your age? "))
    if age < 12:
        bill += 5
        print("Child tickets are $5. ")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7. ")
    elif 45 <= age <= 55:
        print("Have a free ride on us!. ")
    else:
        print("Adult tickets are $12. ")
        bill += 12

    photo = input("Do you want a photo taken? Y or N. ")
    while photo != "Y" and photo != "N":
        photo = input("Please insert Y or N! ")
    if photo == "Y":
        print("Photo costs $3. ")
        bill += 3

    print(f"Your total bill is: ${bill}. ")
else:
    print("Sorry, you have to grow taller before you can ride. ")
