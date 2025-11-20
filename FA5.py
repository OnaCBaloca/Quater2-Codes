destinations=[]
print("Enter five destinations:")
for i in range(5):
    place = input(f"Destination {i+1}: ")
    destinations.append(place)


print("Original Travel Itinerary:")
for i, place in enumerate(destinations, start=1):
    print(f"{i}. {place}")
    
print("Let's update your 2nd and 5th destinations.")
second = input("\nEnter a new destination for position 2: ")
destinations[1] = second 

fifth = input("Enter a new destination for position 5: ")
destinations[4] = fifth  


print("\nUpdated Travel Itinerary:")
for i, place in enumerate(destinations, start=1):
    print(f"{i}. {place}")