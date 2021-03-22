from tabulate import tabulate

table = [['First Name', 'Last Name', 'Profession', 'Age'], ['Leah', 'Pushparaj', 'Stage One', '6'], ['Nathan', 'Pushparaj', 'Nursary', '2']]
print(tabulate(table))
print()
print()
print(tabulate(table, headers="firstrow"))
print()
print()
print(tabulate(table, tablefmt='fancy_grid'))
print()
print()
print(tabulate(table, tablefmt='grid'))
