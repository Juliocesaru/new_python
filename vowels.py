def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in input_string if char in vowels)

if __name__ == "__main__":
    user_string = input("Please enter a string: ")
    vowel_count = count_vowels(user_string)
    print(f"The number of vowels in the given string is: {vowel_count}")

Please enter a string: Julio Urueta
The number of vowels in the given string is: 3
