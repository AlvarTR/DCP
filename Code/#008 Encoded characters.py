"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def encodeCharacters(string):
    #letterArray = [""] # + list(string.ascii_lowercase)
    #for char in range(ord("a"), ord("z")+1):
    #    letterArray.append( chr(char) )
    if not string:
        return 0

    minCode, maxCode = 1, 26
    decodedMessages = 1 #It supposes at least 1 decode is possible

    return decodedMessages

if __name__ == "__main__":
    print(encodeCharacters(""))
