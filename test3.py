

# def numbers():
#     print("testing....")
#     for i in range(1,21):
#         if i is not 11 and i is not 13:
#         # if i is not in [11,13]
#             print(i)



def lowest():
    nums = [12,234,123,56,678,45,7,3,567,2423,56,-2,345,6752,-34,345,0,0,2]

    lowest = nums[0]
    for i in nums:
        if i<lowest:
            lowest=i
    
    print(f"the lowest number is: {lowest}")


# numbers()
lowest()
