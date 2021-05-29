#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program uses user defined functions


def address(name, street_number, street_name,
            city, province, postal_code, apartment_number=None):

    address = name + "\n"
    if apartment_number is not None:
        address = address + apartment_number + "-"
    address = address + street_number
    address = address + " " + street_name
    address = address + "\n" + city
    address = address + " " + province
    address = address + "  " + postal_code

    return address


def main():
    # this function gets information of the user
    apartment_number = None

    name = input("Enter your name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "Yes":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")

    if apartment_number != None:
        mailing_address = address(name, street_number, street_name, city,
                                  province, postal_code, apartment_number)
    else:
        mailing_address = address(name, street_number, street_name, city,
                                  province, postal_code)

    print("")
    print(mailing_address)


if __name__ == "__main__":
    main()
