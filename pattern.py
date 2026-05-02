list=[0,0,0,
      0,0,0,
      0,0,0]

user="X"

def board():
    count==0
    for i in range(3):
        for j in range(3):
            if list[count]==0:
                print("-- |",end=" ")
            else:
                print(list[count],end=" ")
        print()
def playGame():
    return int(input("select a space between 1 to 9:"))

    globals()['list'][num-1]=user
    if user=="X":
        user()["user"]="o"
    else:
        user="X"

while True:
    board()
    playGame()

    