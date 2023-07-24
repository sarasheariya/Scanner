def lex(text):
    out = []
    nextToken = None
    i = 0
    o = ''

    while i < len(text): #Take all the characters from the character stream
        o = text[i] #store the character here 

        if o == ' ': #if it's space .. ignore it
            pass

        elif o == '#': #if it's comment .. ignore it
            break

        elif o == '=': 
            nextToken = "ASSIGN_OP"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == '/':
            nextToken = "DIVISION_OP"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == '*':
            nextToken = "MULTIPLY_OP"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == '+':
            nextToken = "PLUS_OP"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == '-':
            nextToken = "MINUS_OP"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == ';':
            nextToken = "SEMICOLON"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == '(':
            nextToken = "LPAREN"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == ')':
            nextToken = "RPAREN"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        elif o == '\n':
            nextToken = "EndOfLine"
            out.append((o, nextToken))
            print(o + " --> " + nextToken)

        if o.isdigit(): #if it's digit store it in token and if the next character is also digit .. store them together until done
            token = o
            j = i + 1
            while j < len(text) and text[j].isdigit():
                token += text[j]
                j += 1
            nextToken = "DIGIT_CODE"
            out.append((token, nextToken))
            print(token + " --> " + nextToken)

            i = j - 1

        #if it's char store it in token and if the next character is also char .. store them together until done
        if ((o >= 'A' and o <= 'Z') or (o >= 'a' and o <= 'z')):
            token = o
            j = i + 1
            while j < len(text) and ((text[j] >= 'A' and text[j] <= 'Z') or (text[j] >= 'a' and text[j] <= 'z')):
                token += text[j]
                j += 1
            if j >= len(text) or not ((text[j] >= 'A' and text[j] <= 'Z') or (text[j] >= 'a' and text[j] <= 'z')):
                out.append((token, "VAR_CODE"))
                print(token + " --> " + "VAR_CODE")

            i = j - 1

        i += 1
    return out
if __name__ == "__main__":
    print(lex(input("Enter a stream of characters (Ending with semicolon): ")))
