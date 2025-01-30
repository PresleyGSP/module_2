# SIMPLE DATA TYPES
"""
name = 'Presley'
print("name:", name, "type:", type(name))
his_license = 'valid'
print("has license:", his_license, "type:", type(his_license))
current_year = 2025
print("this year", current_year, "type:", type(current_year))
current_year = current_year + 1
print(current_year)
print("next_year:", current_year, "type:", type(current_year))

# MATHEMATICAL OPERATIONS
GST = 0.05
PST = 0.07
honda = 7000
p_tax = 7000 * PST
g_tax = 7000 * GST
sum = honda + p_tax + g_tax
print("Purchase Price:", honda, "Provincial Tax:", PST, "Federal Tax:", GST, "Total:", sum)
print(f"Purchase Price: ${honda:,.2f} Provincial Tax: ${PST:,.2f} Federal Tax: ${GST:,.2f} Total: ${sum:,.2f} ")

# LISTS
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(numbers))
print(numbers)
numbers.insert(5, 'Presley')
print(numbers)
numbers.remove(9)
print(numbers)
letters = ['A', 'B', 'C']
combined_list = numbers + letters
print(combined_list)

# TUPLE
provinces = ('MB','SK','AB','ON')
print(type(provinces))
print(provinces)
"""
# DICTIONARIES
coins = {
    'nickel': .05, 
    'dime': .10, 
    'quarter': .25
}
print(type(coins))
print(coins)
print(coins['nickel'])
coins['nickel'] = 5
coins['dime'] = 10
coins['quarter'] = 25
print(coins)
coins['loonie'] = 100
coins['toonie'] = 200
print(coins)
