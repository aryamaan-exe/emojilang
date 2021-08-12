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
        elif char in "✌➕":
            if char == "✌":
                try:
                    value = func.to_int(value)
                except:
                    print("😕❌🔢")
                else:
                    value **= 2
            elif char == "➕":
                try:
                    addend = func.to_int(line[i+1:line.index("👈")])
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
                    value += line[i+1:line.index("👈")]
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
        elif char == "🐰":
            try:
                num = func.to_int(line[i+1:line.index("👈")])
                try:
                    value = func.to_int(value)
                except:
                    pass
                    
                if num == "😕❌🔢":
                    print("😕❌🔢")
                else:
                    value *= num
            except ValueError:
                print("😕❌👈")
        elif char == "➗":
            try:
                divisor = func.to_int(line[i+1:line.index("👈")])
                try:
                    value = func.to_int(value)
                except:
                    pass
                    
                if divisor == "😕❌🔢":
                    print("😕❌🔢")
                else:
                    value /= divisor
            except ValueError:
                print("😕❌👈")
        elif char == "🐇":
            try:
                exponent = func.to_int(line[i+1:line.index("👈")])
                try:
                    value = func.to_int(value)
                except:
                    pass
                    
                if exponent == "😕❌🔢":
                    print("😕❌🔢")
                else:
                    value **= exponent
            except ValueError:
                print("😕❌👈")
        elif char == "🐕":
            try:
                num = func.to_int(line[i+1:line.index("👈")])
                try:
                    value = func.to_int(value)
                except:
                    pass
                    
                if num == "😕❌🔢":
                    print("😕❌🔢")
                else:
                    value %= num
            except ValueError:
                print("😕❌👈")
        elif char in "♊♎":
            try:
                rhs = func.to_int(line[i+1:line.index("👈")])
            except ValueError:
                print("😕❌👈")
            else:
                if rhs == "😕❌🔢":
                    rhs = line[i+1:line.index("👈")]
                
                temp = value
                try:
                    value = func.to_int(value)
                except:
                    pass
                
                if value == "😕❌🔢":
                    value = temp
                
                if value == rhs:
                    value = True if char == "♊" else False
                else:
                    value = False if char == "♊" else True
        elif char in "👨👩":
            if line[i+1] == "⚖":
                try:
                    rhs = func.to_int(line[i+2:line.index("👈")])
                except ValueError:
                    print("😕❌👈")
                else:
                    if rhs == "😕❌🔢":
                        rhs = line[i+2:line.index("👈")]
                    
                    temp = value
                    try:
                        value = func.to_int(value)
                    except:
                        pass
                    
                    if value == "😕❌🔢":
                        value = temp
                    
                    value = True if value > rhs else (True if value == rhs else False)
            else:
                try:
                    rhs = func.to_int(line[i+1:line.index("👈")])
                except ValueError:
                    print("😕❌👈")
                else:
                    if rhs == "😕❌🔢":
                        rhs = line[i+1:line.index("👈")]
                    
                    temp = value
                    try:
                        value = func.to_int(value)
                    except:
                        pass
                    
                    if value == "😕❌🔢":
                        value = temp
                    
                    value = True if value > rhs else False
        elif char in "👦👧":
            if line[i+1] == "⚖":
                try:
                    rhs = func.to_int(line[i+2:line.index("👈")])
                except ValueError:
                    print("😕❌👈")
                else:
                    if rhs == "😕❌🔢":
                        rhs = line[i+2:line.index("👈")]
                    
                    temp = value
                    try:
                        value = func.to_int(value)
                    except:
                        pass
                    
                    if value == "😕❌🔢":
                        value = temp
                    
                    value = True if value > rhs else (True if value == rhs else False)
            else:
                try:
                    rhs = func.to_int(line[i+1:line.index("👈")])
                except ValueError:
                    print("😕❌👈")
                else:
                    if rhs == "😕❌🔢":
                        rhs = line[i+1:line.index("👈")]
                    
                    temp = value
                    try:
                        value = func.to_int(value)
                    except:
                        pass
                    
                    if value == "😕❌🔢":
                        value = temp
                    
                    value = True if value < rhs else False
        elif char == "🐍":
            pycode = line[i+2:line.index("👈")]
            if line[i+1] == "🕐":
                stack.append(eval(pycode))
            elif line[i+1] == "🕑":
                stack.append(exec(pycode))
            else:
                print("😕🐍")

        i += 1
