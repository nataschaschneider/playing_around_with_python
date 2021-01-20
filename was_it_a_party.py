#Was it a party?

items=["shot drinking","vomiting","bathroom sex","Irish goodbye","crying"]


def ask():
    global score
    score=0
    for item in items:
        x=input(f"""Was there {item}? y/n:""")
        if x=="y":
            score=score+1
    return score

ask()

if score >= 3:
    print("Hell yeah, it was a party!!!")
else:
    print("You really don't know how to have fun.")
