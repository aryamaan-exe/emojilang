import sys, func

stack = []
value = ""
comment = False

with open(sys.argv[1], encoding="utf-8") as f:
    code = f.read()

code = code.split("🥱")
for line in code:
    i = 0
    while i < len(line):
        char = line[i]
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
            if char == "✌":
                try:
                    value = func.to_int(value)
                except:
                    print("😕❌🔢")
                else:
                    value **= 2
            elif char in "👩‍👦👩‍👧👨‍👦👨‍👧":
                try:
                    addend = func.to_int(line[i+3:line.index("👈")])
                    try:
                        value = func.to_int(value)
                    except:
                        pass
                    if addend == "😕❌🔢":
                        print("😕❌🔢")
                        
                    else:
                        value += addend
                except ValueError:
                    print("😕❌👈")
                except TypeError:
                    value += line[i+3:line.index("👈")]
                
                i += 3
        elif char == "✂":
            try:
                minuend = func.to_int(line[i+1:line.index("👈")])
                try:
                    value = func.to_int(value)
                except:
                    pass
                if minuend == "😕❌🔢":
                    print("😕❌🔢")
                else:
                    value -= minuend
            except ValueError:
                print("😕❌👈")
        elif char == "🐍":
            pycode = line[i+2:line.index("👈")]
            if line[i+1] == "🕐":
                stack.append(eval(pycode))
            elif line[i+1] == "🕑":
                stack.append(exec(pycode))
            else:
                print("😕🐍")

        i += 1
