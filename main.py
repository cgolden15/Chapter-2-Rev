questions = ["1. ___ is called the command prompt. ", "2. \_ creates a new line. ", "3. A single line comment starts with the symbol ___ ", "4. How do you import the turtle ", "5. What is the command to change the turtles color? ", "6. What is the highest number i will be in 'for i in range(5):' ", "7. What is the command to change the turtles speed? ", "8. What three letter word lets you define a function? ", "9. How would you call a function named 'hello'? ", "10. Does Indentation matter in Python? ", "11. ___________ a function means you are using the function in your program. ", "12. Is Python case sensitive? ", "13. What number do i loops start at? ", "14. How would you move tracy forward 100 pixles? ", "15. Who is the "]

answers = [">>>", "n", "#", "import turtle", 'turtle.color("")', "4", "turtle.speed()", "def", "hello()", "yes", "calling", "yes", "0", "turtle.forward(100)"]

qs = len(questions)

for i in range(qs):
  ans = input(questions[i])
  if ans == answers[i]:
    print('Correct!')
  else:
    print(f"Incorrect! The correct answer is {answers[i]}")
