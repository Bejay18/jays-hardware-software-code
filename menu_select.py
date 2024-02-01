def execute_display(menu_dict):
    for items, values in menu_dict.items():
        print("{} . {}".format(items, values.capitalize()))
    menu_selection = list (menu_dict.keys())
    selection = "#"

    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid entry")

    return selection, menu_dict[selection]

def menu_display():
    menu_dict = {
        '1':'Decimal_to_Binary',
        '2':'Binary_to_Decimal',
        'X':'Exit_Progress'
    }
    return menu_dict

def main():
    while selection != 'X'
        sel, choice = execute_display(menu_display())
        print("You selected {} and want to convert {}".format(sel, choice))
    return menu_dict
if selection == 'X'
    break



if __name__=="__main__":
    main()
