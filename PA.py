#This program print out the name of each sandwich that has been made

# List of sandwich orders 
sandwich_orders = ["veggie", "tuna", "Turkey", "Grilled Cheese"]

# Stores the finished sandwiches
finished_sandwiches = []

#Use a while loop to print out the name of each sandwich that has been made
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print all the sandwiches that were made
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")