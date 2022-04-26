

def test_dict():
    print("testing dictionary")

    me = {
        "first_name": "Von",
        "last_name": "Abrea",
        "age": 33,
        "address": {
            "num": 42,
            "street": "Evergreen",
            "city": "Springfield",
        }
    }

    print(me["first_name"] + " " + me["last_name"])

    # modify
    # me["age"] = me["age"] + 1

    # add new keys
    me["color"] = "blue"

    # remove age
    # del me["age"]
    # me["age"].pop

    # print the address
    address = me["address"]
    print(address["street"] + " #" +
          str(address["num"]) + "," + address["city"])

    print(f"{address['street']} #{address['num']}, {address['city']}")

    # last, first
    print(f"{me['last_name']}, {me['first_name']}")

    # Hi my name is ____ ___, and I am _ years old.
    print(
        f"Hi my name is {me['first_name']} {me['last_name']}, and I am {me['age']} years old.")

    # print a key that does not exist
    try:
        print(me["height"])
    except:
        print("errorrrrrrr.")

    # validate keys in dictionary
    if "height" in me:
        print(me["height"])

    print(me)


test_dict()
