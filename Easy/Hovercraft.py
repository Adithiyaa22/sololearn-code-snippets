# Cost to build one hovercraft
cost_per_craft = 2100000       # 1 hovercraft = 100000 then 10 hovercraft = 1000000

# Selling price of one hovercraft 
selling_price = 3000000

customers = int(input())

total_cost = cost_per_craft * customers

# Calculate total revenue from sales
total_revenue = customers* selling_price

# Determine profit or loss
if total_revenue > total_cost:
    print("Profit")
elif total_revenue == total_cost:
    print("Broke Even")
else:
    print("Loss") 