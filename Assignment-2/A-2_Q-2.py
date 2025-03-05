'''Ques-2: Explain how the `continue` statement works in a loop. What are some
scenarios where using `continue` is more beneficial than restructuring
the loop?'''
'''Ans: When a continue statement is executed:

1.It skips the remaining code in the current iteration.
2.It advances the loop to the next iteration, whether it's the next item in a for loop or the next check for the condition in a while loop.

Scenarios Where continue is Beneficial:
1.Avoiding Nested Conditions: Instead of adding multiple if-else conditions, you can use continue to avoid unnecessary indentation and make your code cleaner. This is particularly useful when you have a lot of conditions to check at the start of the loop, and you want to skip the rest of the loop if a condition is met.
2.Skipping Over Invalid Data: In scenarios where you are processing data (e.g., in a list or a file), you might encounter invalid data. Instead of restructuring the loop logic or adding extra nested conditions to handle invalid data, continue can skip over those invalid entries quickly.
3.Filtering and Early Exiting Loop: If you need to filter out certain items early in the loop, continue allows you to skip further unnecessary checks for that iteration and move directly to the next one. This helps in reducing the complexity of the loop and improving readability.
'''


l=[1,3,9,4,6,4,2,3]
for i in l:
    if (i%3!=0):
        continue
    print(i)
    