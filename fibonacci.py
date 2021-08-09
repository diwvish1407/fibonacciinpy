# Write a program to print the Fibonacci series.

numberOfTerms = int(input("Number of terms : "))

firstTerm, secondTerm = 0, 1
count = 0

if numberOfTerms <= 0:
    print("Please enter a positive integer.")

elif numberOfTerms == 1:
    print(numberOfTerms, end=", ")
else:
    while count < numberOfTerms:
        print(firstTerm, end=", ")
        nthTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nthTerm
        count += 1
