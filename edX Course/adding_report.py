def adding_report(str_par):
    total = 0
    items = ""
    while True:
        user_input = input('Enter an integer or "Q": ').lower()
        if user_input.isdigit():
            total = int(user_input) + total
            if str_par == "A":
                items = items + user_input + "\n"
            else:
                pass
        elif user_input.lower().startswith("q"):
            if str_par == "A":
                print("Items:\n" + items)
                print("Total:\n" + str(total))
                break
            elif str_par == "T":
                print(total)
                break
            else:
                pass
        else:
            print(user_input, " is invalid input")


adding_report("A")
adding_report("T")
