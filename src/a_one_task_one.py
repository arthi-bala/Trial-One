"""
A function to reverse the words in a sentence.

In such a way that Without changing order of the words.
Input:
>>> "Hi this is just to check the reverse words function"
Output:
>>> iH siht si tsuj ot kcehc eht esrever sdrow noitcnuf
"""


def reverse_words(input_str: str) -> str:
    """
    Reverse the words in a sentence without changing the order of the words.

    Args:
        input_str (str): The input sentence to be reversed.
    Returns:
        str: The sentence with words reversed.
    """
    string_array = input_str[::-1].split(" ")[::-1]
    return " ".join(string_array)

print(reverse_words("Hi this is just to check the reverse words function"))
