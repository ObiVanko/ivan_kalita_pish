from Homework.Lab1.main import squares_before

def unique_elements(sentence: str):
    return sorted(set(sentence.split()))

def element_frequencies(string: str):
    unique = set(string)
    answer = dict()
    for i in unique:
        count = 0
        for j in string:
            if i == j:
                count += 1
        answer.update({i: count})
    return answer

def lists_intersection(list1: list, list2: list):
    return sorted(set(list1) & set(list2))

def squares_dictionary(n: int):
    return dict(map(lambda x: [x[0], x[1][0]], squares_before(n).items()))

def anagram(string1: str, string2: str):
    return True if (element_frequencies(string1) == element_frequencies(string2)) else False

print(unique_elements("apple banana apple orange banana kiwi"))
print(element_frequencies("abracadabra"))
print(lists_intersection([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
print(squares_dictionary(5))
print(anagram("listen", "silent"))
