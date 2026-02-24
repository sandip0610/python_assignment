# Text Analysis Functions

def count_words(text):
    w = text.split()
    return len(w)  #return no of words

def count_vowels(text):
    v = "aeiouAEIOU"
    c = 0
    for ch in text:
        if ch in v:
            c = c + 1
    return c #return no of vowels

def count_consonants(text):
    v = "aeiouAEIOU"
    c = 0
    for ch in text:
        if ch.isalpha() and ch not in v:
            c = c + 1
    return c #constant count

def reverse_text(text):
    r = ""
    for i in range(len(text) - 1, -1, -1):
        r = r + text[i]
    return r #reversed

def is_palindrome(text):
    s = text.lower().replace(" ", "")
    r = reverse_text(s)
    return s == r #palindrome check

def remove_vowels(text):
    v = "aeiouAEIOU"
    r = ""
    for ch in text:
        if ch not in v:
            r = r + ch
    return r  #vowel remove

def word_frequency(text):
    w = text.lower().split()
    d = {}
    for x in w:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    return d

def longest_word(text):
    w = text.split()
    lw = ""
    for x in w:
        if len(x) > len(lw):
            lw = x
    return lw

def analyze_text(text):
    print("=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    
    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print("Longest word:", lw, "(" + str(len(lw)) + " letters )")

    print("Word Frequency:")
    wf = word_frequency(text)
    for k in wf:
        print(k + ":", wf[k])



t = input("Enter text: ")
analyze_text(t)