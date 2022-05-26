
import random
#rock,paper, pencil, scissior
def game(comp,user):
    if comp== user:
        return None
    elif comp=='rock':
        if user=='paper':
            return True
        elif user=='pencil':
            return False
        elif user=='scissor':
            return False
    elif comp=='paper':
        if user=='rock':
            return False
        elif user=='pencil':
            return True
        elif user=='scissor':
            return False
    elif comp=='pencil':
        if user=='rock':
            return True
        elif user=='paper':
            return False
        elif user=='scissor':
            return True
    elif comp=='scissor':
        if user=='rock':
            return True
        elif user=='paper':
            return False
        elif user=='pencil':
            return False
print("comp turn:rock(rock),paper(paper),pencil(pencil),scissor(scissor)?") 
radNo = random.randint(1,4)

if radNo==1:
    comp='rock'
elif radNo==2:
    comp='paper'
elif radNo==3:
    comp= 'pencil'
elif radNo==4:
    comp='scissor'

user= input("user's turn:rock(rock),paper(paper),pencil(pencil),scissor(scissor)?") 
a= game(comp,user)

print(f"computer choose {comp}")
print(f"you choose {user}")
if a==None:
    print("the game is tie")
elif a:
    print("you win")
else:
    print("you loose")
