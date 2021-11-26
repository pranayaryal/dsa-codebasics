
expenses = [2200, 2350, 2600, 2130, 2190]
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']


# 1. In Feb, how many dollars you spent extra compare to January?

print(f'Diff between Jan and Feb: {expenses[1] - expenses[0]}')

# 2. Find out your total expense in first quarter
# (first three months) of the year.
print(f'''Expense in first quarter: {expenses[0] +
    expenses[1] + expenses[2]}''')

# 3. Find out if you spent exactly 2000 dollars in any month
for exp in expenses:
    if exp == 2000:
        print(f'You spent exactly 2000 dollars in {exp}')
        break

# 4. June month just finished and your expense is 1980 dollar.
# Add this item to our monthly expense list
expenses.append(1980)
print(expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] -= 200
print(expenses)

# 1. Length of the list
print(f'Length of the list heros is: {len(heros)}')
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and
# replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros.remove('thor')
heros.remove('hulk')
heros.insert(1, 'doctor strange')
print(heros)
# 5. Sort the heros list in alphabetical order (Hint.
# Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)
print(heros.__hash__)
print(list.__dir__(heros))
