sub = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
       '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', '/', '.', ',', ' ', '~', '`', ';', ':', '{', '}', '[', ']',
       '?', '<', '>', '"', '\'', '\\', '|']
def findorder(character):
    order=-1
    for c in sub:
        if c == character:
            order = sub.index(c)
            return order

def replace(order,step):
    while order+step >= len(sub):
        step-=len(sub)
    print(sub[order + step], end="")

print("Enter the step: ", end="")
step = input()
step = int(step)
print("Enter the message: ", end="")
msg = input()
for x in msg:
    replace(findorder(x),step)
