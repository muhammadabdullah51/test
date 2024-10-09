def grop_anagram(strs):
    anagrams = {}
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
        # print(anagrams)

    return [v for v in anagrams.values() if len(v) > 1]

print(grop_anagram(['tea', 'eat', 'ate', 'bat', 'tab']))



def numToWord(num):
    if num == 0:
        return 'zero'
    below_twenty = ['', 'one', 'two', 'three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thriteen', 'fourteen', 'fifteen', 'sixteen','seventeen', 'eighteen','nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    thousands = ['', 'thousand']
    def func(n):
        if n < 20:
            return below_twenty[n]
        elif n < 100:
            return tens[n // 10] + ('' if n%10==0 else ' ' + below_twenty [n%10] )
        elif n < 1000:
            return below_twenty[n // 100] + ' hundred ' + ('' if n%100==0 else ' and ' + func(n%100))
        else:
            for i, words in enumerate(thousands):
                if n < 1000**(i+1):
                    return func(n // 1000**i) + ' ' + thousands[i] + ('' if n%1000**i==0 else ' and ' + func(n%1000**i))
    return func(num).strip()
print(numToWord(2024))