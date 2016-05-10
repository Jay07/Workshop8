from guitar import Guitar

guitar = Guitar("guitar", 1922, 100.50)

age = guitar.get_age(1922)
vintage = guitar.is_vintage(1922)

print(age)
print(vintage)