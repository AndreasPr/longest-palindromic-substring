def longestPalSubstr(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0

    for i in range(1, length):
        low = i - 1
        high = i
        # print("I: ", i)
        # print("Before while Low: ", low)
        # print("Before while High: ", high)
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
                # print("start: ", start)
                # print("maxLength: ", maxLength)
            low -= 1
            high += 1
            # print("While Low: ", low)
            # print("While High: ", high)

        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
            print("Second While Low: ", low)
            print("Second While High: ", high)

    print("Longest palindrome substring is:")
    print(string[start:start + maxLength])

    return maxLength

string = "noandreassaerdnayes"
print("Length is: " + str(longestPalSubstr(string)))
