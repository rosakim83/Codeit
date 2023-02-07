def is_palindrome(word):
    list_word = list(word)
    reverse_list_word = list_word[::-1]
    if list_word == reverse_list_word:
        return True
    else:
        return False


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))