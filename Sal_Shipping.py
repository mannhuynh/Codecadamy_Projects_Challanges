# """ 
# Sal's Shipping
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
# Sal wants to make sure that every single one of his customers has the best, 
# and most affordable experience shipping their packages. 
# In this project, you’ll build a program that will take the weight of a package 
# and determine the cheapest way to ship that package using Sal’s Shippers.

# Sal’s Shippers has several different options for a customer to ship their package. 
# They have ground shipping, which is a small flat charge plus a rate based on the weight of your package.
# Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. 
# They recently also implemented drone shipping, which has no flat charge, 
# but the rate based on weight is triple the rate of ground shipping.

# Here are the prices:

# Ground Shipping:
# Weight of Package	                        Price per Pound		Flat Charge
# 2 lb or less	                            $1.50	            $20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	            $20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	            $20.00
# Over 10 lb	$4.75	$20.00

# Drone Shipping
# Weight of Package	                        Price per Pound		Flat Charge
# 2 lb or less	                            $4.50	            $0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	            $0.00
# Over 6 lb but less than or equal to 10 lb	$12.00	            $0.00
# Over 10 lb	                                $14.25	            $0.00

# Premium Ground Shipping
# Flat charge: $125.00

# Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# """

def ground_shipping(weight):
  if weight <= 2:
    ground_cost = 1.50 * weight + 20
  elif 2 < weight <= 6:
    ground_cost = 3.00 * weight + 20
  elif 6 < weight <= 10:
    ground_cost = 4.00 * weight + 20
  else:
    ground_cost = 4.75 * weight + 20
  #print(ground_cost)
  return ground_cost
  
premium_cost = 125.00

ground_shipping(8.4)

def drone_shipping(weight):
  if weight <= 2:
    drone_cost = 4.50 * weight
  elif 2 < weight <= 6:
    drone_cost = 9.00 * weight
  elif 6 < weight <= 10:
    drone_cost = 12.00 * weight
  else:
    drone_cost = 14.25 * weight
  #print(drone_cost)
  return drone_cost

drone_shipping(1.5)

def cheapest_shipping(weight):
  ground_cost = ground_shipping(weight)
  drone_cost = drone_shipping(weight)
  cheapest_cost = min(ground_cost, premium_cost, drone_cost)
  #print(cheapest_cost)
  if cheapest_cost == ground_cost:
    print("You should ship using ground shipping, it will cost " +  str(cheapest_cost))
  elif cheapest_cost == drone_cost:
    print("You should ship using drone shipping, it will cost " +  str(cheapest_cost))
  else:
    print("You should ship using premium shipping, it will cost " +  str(cheapest_cost))
cheapest_shipping(41.5)
