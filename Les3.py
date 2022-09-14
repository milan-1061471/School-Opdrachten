# Les 3 
# Opdracht 1
print("Internet verbindingsselectie")
internet_vraag_1_str = input("Welke verbinding wilt u gebruiken [4G, 5G, Wifi open]: ")
internet_vraag_1 = internet_vraag_1_str.upper()
if internet_vraag_1 == "WIFI OPEN":
    print("U heeft voor de 'Wifi open' gekozen, wij zijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    internet_vraag2_str = input("Wilt u nog steeds verbinden? [Ja/Nee]: ")
    internet_vraag2 = internet_vraag2_str.upper()
    if internet_vraag2 == "JA":
        print(f"U bent verbonden via <{internet_vraag_1}>!")
    else:
        print("U bent niet verbonden.")
elif internet_vraag_1 == "4G":
    print(f"U bent verbonden via <{internet_vraag_1}>! ")
elif internet_vraag_1 == "5G":
    print(f"U bent verbonden via <{internet_vraag_1}>! ")
else:
    print("Onbekende invoer, u wordt niet verbonden.")

# Opdracht 2
print("Patient exposed to TB.")
question1_str = input("Is the patient Adult or Child? [Adult/Child]: ")
question1 = question1_str.upper()
if question1 == "ADULT":
    print("Adult")
    question2_str = input("Has common TB symptoms? [Yes/No]: ")
    question2 = question2_str.upper()
    if question2 == "YES":
        print("Treat as likely TB patient and perfom full Tb exam.")
    elif question2 == "NO":
        print("Have patient report back if unwell; return in 1 month for checkup.")
    else:
        print("Abort, unknown input. ")
elif question1 == "CHILD":
    question3_str = input("Can TB test be given? [Yes/No]: ")
    question3 = question3_str.upper()
    if question3 == "YES":
        print("Administer TB test.")
        print("Assess TB test results and child's condition.")
    elif question3 == "NO":
        question4_str = input("Child well? [Yes/No]: ")
        question4 = question4_str.upper()
        if question4 == "YES":
            print("6 months preventive isoniazid.")
            print("Have parent bring in if child shows any symptoms.")
        elif question4 == "NO":
            print("Take full history. Examine for TB.")
            print("If TB likely diagnosis treat for TB.")
            print("If other diagnosis more likely, treat as needed and watch for TB symptoms.")
        else:
            print("Abort, unknown input. ")
    else:
        print("Abort, unknown input. ")
else:
    print("Abort, unknown input. ")

# Opdracht 3
print("Shopping Cart")
question5_str = input("Payment Method? [Online/Offline]: ")
question5 = question5_str.upper()
if question5 == "ONLINE":
    print("Place Purchase Order.")
    question6_str = input("Admin User? [Yes/No]: ")
    question6 = question6_str.upper()
    if question6 == "YES":
        print("Enter payment details.")
        print("Place Order.")
    elif question6 == "NO":
        question7_str = input("Approval Rules [Rejected/Approved]: ")
        question7 = question7_str.upper()
        if question7 == "REJECTED":
            print("Purchase order Rejected.")
        elif question7 == "APPROVED":
            print("Enter payment details.")
            print("Place Order.")
        else:
            print("Abort, unknown input. ")
    else:
        print("Abort, unknown input. ")
elif question5 == "OFFLINE":
    print("Place Purchase Order")
    question8_str = input("Admin User [Yes/No]: ")
    question8 = question8_str.upper()
    if question8 == "YES":
        print("Order Created Automatically.")
    elif question8 == "NO":
        question9_str = input("Approval Rules? [Rejected/Approved]: ")
        question9 = question9_str.upper()
        if question9 == "REJECTED":
            print("Purchase Order Rejected.")
        elif question9 == "APPROVED":
            print("Order Created Automatically")
        else:
            print("Abort, unknown input. ")
    else:
        print("Abort, unknown input. ")
else:
    print("Abort, unknown input. ")

# Opdracht 4
print("Welkom bij Mac Donald's")
mac_vraag1_str = input("Burgers of drankjes? [Burgers/Drankjes]: ")
mac_vraag1 = mac_vraag1_str.upper()
if mac_vraag1 == "BURGERS":
    mac_vraag2_str = input("Hamburger, Cheese burger, Big Mac, Quarter Pounder: ")
    mac_vraag2 = mac_vraag2_str.upper()
    if mac_vraag2 == "HAMBURGER":
        print("Hamburger")
    elif mac_vraag2 == "Cheese burger":
        print("Cheese burger")
    elif mac_vraag2 == "Big Mac":
        print("Big Mac")
    elif mac_vraag2 == "QUARTER POUNDER":
        mac_vraag3_str = input("Quarter Pounder met of zonder kaas/ [Met/Zonder]: ")
        mac_vraag3 = mac_vraag3_str.upper()
        if mac_vraag3 == "MET":
            print("Quarter Pounder met kaas")
        elif mac_vraag3 == "ZONDER":
            print("Quarter Pounder zonder kaas")
        else:
            print("Abort, unknown input. ")
    else:
        print("Abort, unknown input. ")
elif mac_vraag1 == "DRANKJES":
    mac_vraag4_str = input("Warme of koude drankjes? [Warm/Koud]: ")
    mac_vraag4 = mac_vraag4_str.upper()
    if mac_vraag4 == "WARM":
        mac_vraag5_str = input("Koffie, Cappucino of Chocolademelk: ")
        mac_vraag5 = mac_vraag5_str.upper()
        if mac_vraag5 == "KOFFIE":
            print("Koffie")
        elif mac_vraag5 == "CAPPUCINO":
            print("Cappucino")
        elif mac_vraag5 == "CHOCOLADEMELK":
            print("Chocolademelk")
        else:
            print("Abort, unknown input. ")
    elif mac_vraag4 == "KOUD":
        mac_vraag6_str = input("Coca Cola, Cola Zero, 7-up, Fanta, Fristi")
        mac_vraag6 = mac_vraag6_str.upper()
        if mac_vraag6 == "COCA COLA":
            print("Coca Cola")
        elif mac_vraag6 == "Cola Zero":
            print("Cola Zero")
        elif mac_vraag6 == "7-up":
            print("7-up")
        elif mac_vraag6 == "Fanta":
            print("Fanta")
        elif mac_vraag6 == "Fristi":
            print("Fristi")
        else:
            print("Abort, unknown input. ")
    else:
        print("Abort, unknown input. ")
        mac_vraag7_str = input("Hier opeten of meenemen? [Opeten/Meenemen]: ")
        mac_vraag7 = mac_vraag7_str.upper()
        if mac_vraag7 == "OPETEN":
            print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant")
        elif mac_vraag7 == "MEENEMEN":
            print("Bedankt voor uw bestelling, goede reis en eet smakelijk")
        else:
            print("Abort, unknown input. ")
else:
    print("Abort, unknown input. ")