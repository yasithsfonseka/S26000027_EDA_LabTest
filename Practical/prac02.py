numbers = [12, 7, 5, 3, 8, 10]
print("the numbers are:", numbers)

print("the smallest number is:", min(numbers))
print("the largest number is:", max(numbers))
print("the sum of the numbers is:", sum(numbers))
print("the average of the numbers is:", sum(numbers) / len(numbers))

numbers.sort()
print("the sorted numbers are:", numbers)

numbers.reverse()
print("the numbers in reverse order are:", numbers)

numbers.insert(111, 19)
print("the numbers after inserting 19 at index 111 are:", numbers)

numbers.remove(5)
print("the numbers after removing 5 are:", numbers)

numbers.pop()
print("the numbers after popping the last element are:", numbers)





#///////////////////////////////////////////////////////////////////////

text = input("Enter a sentence: ").lower()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"The Word '{word}' appears {count} times.")