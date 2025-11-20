#function to convert km to miles
def convert_km_to_miles(km):
    miles = km * 0.621371
    return miles

print(convert_km_to_miles(5))   # Expect 3.106855
print(convert_km_to_miles(10))  # Expect 6.21371