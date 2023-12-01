import re

if __name__ == "__main__":
    # part 1:
    # break input into lines, find digits, concatenate the first and last ones,
    # cast all concatenated numbers to ints, then sum
    print(sum(map(lambda digits: int(digits[0] + digits[-1]),
              map(lambda line: re.findall(r"[0-9]", line),
                  open("1/trebuchet.txt", "r").read().splitlines()))))
    
    digits = {
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9",
    }
    
    regex = re.compile('[0-9]|' + '|'.join(digits.keys()))
    
    def getdigit(d: str) -> str:
        return digits[d] if d in digits else d
    
    def getOverlapping(line: str) -> list[str]:
        result = []
        i = 0
        while i < len(line):
            m = regex.search(line, i)
            if m is None:
                return result
            result.append(line[m.start() : m.end()])
            i = m.start() + 1
        return result
    
    # part 2:
    # break into lines, find digits OR digit names, convert any spelled-out
    # digits into actual digits, concatenate and sum as in part 1
    print(sum(map(lambda d: int(d[0] + d[-1]),
                  map(lambda strs: [getdigit(strs[0]), getdigit(strs[-1])],
                      map(lambda line: getOverlapping(line),
                          open("1/trebuchet.txt", "r").read().splitlines())))))
