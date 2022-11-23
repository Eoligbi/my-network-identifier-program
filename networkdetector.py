user_input = int(input("Enter your four digit number"))

list_of_airtel_numbers = ["0702", "0802","0808","0908", "0704"]
list_of_mtn_numbers = ["0806", "0803", "0816", "0814" "0813"]
list_of_glo_numbers = ["0815","0807", "0905", "0807", "0805"]
list_of_etisalat_numbers = ["0809","0818", "0817","0818"]

if user_input in list_of_airtel_numbers:
    print("Your phone number is Airtel Network")
elif user_input in list_of_mtn_numbers:
    print("Your number is an MTN Network")
elif user_input in list_of_glo_numbers:
    print("Your phone number is a Glo Network")
elif user_input in list_of_etisalat_numbers:
    print("Your Phone number is an Etisalat Network")
else:
    print("Not on any Network")
