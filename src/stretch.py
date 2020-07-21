# Print out all of the strings in the following array that represent a number divisible by 3:
# ```

# ```
# The expected output for the above input is:
# ```
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# ```
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

stringnums = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]


starts = [
    {"one": 1},
    {"tw": 2},
    {"th": 3},
    {"fo": 4},
    {"fi": 5},
    {"six": 6},
    {"seven": 7},
    {"eigh": 8},
    {"nine": 9},
    {"ten": 10},
    {"eleven": 11},
    {"twelve": 12},
    {"hundred": 100}
    ]

ends =[
    {"teen": 1},
    {"ty": 0}
]

def check(word):
    startvalue = None
    for start in starts:
        for key, value in start.items():
            if word.startswith(key):
                startvalue = value
    
    endvalue = None
    for end in ends:
        for key, value in end.items():
            if word.endswith(key):
                endvalue = value
                if key == "teen":
                    return int(f"{endvalue}{startvalue}")
                elif key == "ty":
                    return int(f"{startvalue}{endvalue}")
    return startvalue
# print(check("ninety")) 

for s in stringnums:
    words =  s.split(" ")
    arr = [] 
    for w in words:
        # print(check(w))
        arr.append(check(w))
    total = 0
    hundred = 0
    if len(arr) > 1:
        if arr[1] == 100:
            hundred = arr[0] * arr[1]
            total = hundred
        else:
            for num in arr:
                total += num
    else:
        total = arr[0]
        
    if total % 3 == 0:
        print(s)
        
    # print(total)
    # print(arr)