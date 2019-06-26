# simple solution with //
def centuryFromYear(year):
    return (year + 99) // 100

# or some list and dict comprehension

def centuryFromYear(year):
    breaks = [range(i, i+101) for i in range(0, 2100, 100)]
    centuries = {c+1:i for c,i in enumerate(breaks)}
    def match(y):
        for item in centuries.items():
            if year in item[1]:
                return item[0]
    return match(year)


