print("Welcome to KBC Game")
print("\n Rules for the Game" 
      "\n Question will be provided on the Screen" \
      "\n Five question will be provided to you" \
      "\n If you give two wrong answer " \
      "\n You will be eliminated from the Game" \
      "\n If you give Correct answer of First Question Then you will win 10,000." \
      "\n If you give Correct answer of Second Question Then you will win 30,000." \
      "\n If you give Correct answer of Third Question Then you will win 50,000." \
      "\n If you give Correct answer of Fourth Question Then you will win 1,00,000." \
      "\n If you give Correct answer of Fifth Question Then you will win 2,00,000.")

Question = ["Who is Prime Minister of India"]
print(Question)
Answer   = ["Narendra Modi"]
Choice   = str(input(""))
print(Choice)
for n in Answer:
    if Choice in Answer:
        print("Your Answer is Correct. You Won 10,000")
        print(Choice+10000)
    else:
        print("no")