import random
# GET GUESS
def get_guess():
    return list(input("what is your guess: "))

# Generate Computer Code 123
def genearte_code():
    digits = [str(num) for num in range(10)]
    
    # Shuffle the digits
    random.shuffle(digits)
    # then grab the first three
    return digits[:3]

# Genearte the clues

def genearte_clues(code, user_guess):
    if user_guess==code:
        return "CODE CRACKED!"
    
    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues
    
# RUN GAME LOGIC

print("Welcome code breaker")

secret_code = genearte_code()

clue_report = []

while clue_report != "CODE CRAKED!":

    guess =get_guess()

    clue_report = genearte_clues(guess,secret_code)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
