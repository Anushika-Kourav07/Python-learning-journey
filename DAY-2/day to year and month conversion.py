# days to year and month conversion
day = int(input('Enter number of days: '))

# days to year conversion
year = day / 365
print(f'{day} days are equal to {year:.2f} years.')

# days to month conversion
month = day / 30.4
print(f'{day} days are equal to {month:.2f} month.')
