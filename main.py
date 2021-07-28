import sys, func

stack = []
value = ""
comment = False

with open(sys.argv[1], encoding="utf-8") as f:
    code = f.read()

code = code.split("🥱")
for line in code:
    for char in line:
        i = 0
        if char == "🤮":
            if line[i + 1] == "↩":
                stack.append(value)
            else:
                try:
                    res = ""
                    j = 1
                    while line[i + j] != "👈":
                        res += line[i + j]
                        j += 1
                    
                    stack.append(res)
                except:
                    print("😕❌👈")

            

        elif char == "🧐":
            value = stack.pop()
        elif char == "😤":
            print(value)
            func.out(str(value))
        elif char in "✌👩‍👦👩‍👧👨‍👦👨‍👧":
            try:
                value = func.to_int(value)
            except:
                print("😕❌🔢")
            else:
                if char == "✌":
                    value **= 2
                elif char in "👩‍👦👩‍👧👨‍👦👨‍👧":
                    try:
                        value += func.to_int(line[i+1:line.index("👈")])
                    except ValueError:
                        print("😕❌")
                    except TypeError:
                        value += line[i+1:line.index("👈")]

        i += 1