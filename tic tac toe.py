import random
b = [' '] * 9

def show():
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}\n")

def win(s):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==s for a,b1,c in w)

print("Tic-Tac-Toe  You=X  AI=O")
show()
while True:
    p = int(input("Move (1-9): ")) - 1
    if b[p] == ' ':
        b[p] = 'X'
    else:
        print("Invalid!"); continue
    show()
    if win('X'): print("You win!"); break
    if ' ' not in b: print("Draw!"); break

    ai = random.choice([i for i in range(9) if b[i]==' '])
    b[ai] = 'O'
    print("AI chose", ai+1)
    show()
    if win('O'): print("AI wins!"); break
    if ' ' not in b: print("Draw!"); break
