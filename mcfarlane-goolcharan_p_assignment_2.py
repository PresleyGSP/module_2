# SIMPLE DATA TYPES
name = 'Presley'
print("name:", name, "type:", type(name))
his_license = 'valid'
print("has license:", his_license, "type:", type(his_license))
current_year = 2025
print("this year", current_year, "type:", type(current_year))
current_year = current_year + 1
print("next_year:", current_year, "type:", type(current_year))

# MATHEMATICAL OPERATIONS
GST = 0.05
PST = 0.07
honda = 7000
p_tax = 7000 * PST
g_tax = 7000 * GST
total = honda + p_tax + g_tax
print("Purchase Price:", honda, "Provincial Tax:", PST, "Federal Tax:", GST, "Total:", total)
print(f"Purchase Price: ${honda:,.2f} Provincial Tax: ${PST:,.2f} Federal Tax: ${GST:,.2f} Total: ${total:,.2f} ")

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

# SETS
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(type(even_numbers))
print(even_numbers)
multiples_of_five = {5, 10, 15, 20}
print(multiples_of_five)
unique_values= even_numbers.union(multiples_of_five)
print(unique_values)
common_values = even_numbers.intersection(multiples_of_five)
print(common_values)
only_in_evens = even_numbers.difference(multiples_of_five)
print(only_in_evens)
only_in_fives = multiples_of_five.difference(even_numbers)
print(only_in_fives)