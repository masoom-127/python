a = int(input("Enter a number: "))
i = 1

# Loop 1
print("First loop:")
while i < a:
    print("my sir g")
    i += 1

# Reset i for next loop
i = 1
print("Second loop:")
while i < a:
    print(i)
    i += 1

# Reset a and i for next loop
a = int(input("Enter a number again: "))
i = 1
print("Third loop:")
while a > i:
    print(i)
    a -= 1

# Reset i and a for next loop
a = int(input("Enter a number again: "))
i = 1
print("Fourth loop:")
while i < a:
    if a % 2 == 1:
        print(i)
    i += 1  # Needed increment!

# Reset i and a again
a = int(input("Enter a number again: "))
i = 1
print("Fifth loop:")
while a > i:
    if a % 2 == 1:
        print(i)
    a -= 1
