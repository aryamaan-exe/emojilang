def to_int(s):
    r = ""
    m = {"⭕": "0",
    "🕐": "1",
    "🕑": "2",
    "🕒": "3",
    "🕓": "4",
    "🕔": "5",
    "🕕": "6",
    "🕖": "7",
    "🕗": "8",
    "🕘": "9"}

    for c in s:
        if c not in "⭕🕐🕑🕒🕓🕔🕕🕖🕗🕘":
            return "😕❌🔢"

        r += m[c]

    return int(r)

def out(s):
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(s)