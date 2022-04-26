#### Lists
from mockdata import mock_catalog

def test_1():
    print("basic python lists")

    nums = [1,2,3,89,56,3456,123,456]

    #read
    print(nums[0])
    print(nums[3])

    #add
    nums.append(42)
    nums.append(-1)

    #remove by element
    nums.remove(56)

    #remove by index
    del nums[0]

    print(nums)

    #loop
    for n in nums:
        print(n)

def test_2():
    print("sum numbers")

    prices = [12.23,345,123.2,542,65,123.2,0.223,-23, 123.2,6,171,5678]

    # for and print every number
    total = 0
    smallest =prices[0]
    largest = prices[0]
    for x in prices:
        total+=x

        if x<smallest: 
            smallest=x
        
        if x>largest:
            largest=x

    print(total)
    # print(f"The smallest number is: {smallest}")
    # print(f"The largest number is: {largest}")

        

def test_3():
    
    print("cheapest product")
    solution = mock_catalog[0]
    for prod in mock_catalog:
        # print(prod["title"])

        if prod["price"]< solution["price"]:
          solution = prod

    print(f"The cheapest product is: {solution['title']} -  ${solution['price']}")

# testing for catalog total
def test_4():
    total = 0
    for x in mock_catalog:
        total += x["price"]
        

    print(total)
        
    
#call
# test_1()
# test_2()
# test_3()
# test_4()