start = int(input("Enter a start range: "))
end = int(input("Enter a end range: "))

count = 0
if start %2 == 0:
    for j in range(start, end, 2):
        count += j
    print(f"{count} is the summ of even numbers.")
else:
    pass
