import random

WORDS = ("superman", "batman", "robbin", "hulk", "wonderwomen",  "spiderman", "wolverine", "goku", "gohan", "vagita", "naruto", "cpt america", "antman", "one above all",  "living tribunal", "The Mighty Thor",  "Michael the Arc Angel")
secretword = random.choice(WORDS)
correct = secretword
jumble = ""
failureCount = 6
lettersGuessed = ""
print(
"""
      Welcome to JUMPER!!!

      Guess the letters to make a word.
     
      """
      )
while failureCount > 0:
    
    
    print("Guess the letter in secret word:")
    if (failureCount == 6):
        print(''' 
                ___
               /___|
               \   /
                \ /
                 0    "Hi im jumper"
                /||    i love to  read scriptures when i sky jump!
                / |
                    
            ^^^^^^^^^     
                                        ''')
    elif (failureCount == 5):
        print(f''' 
                ___
               /__ y
               \   /
                \ /
                 0       "{failureCount} turns remaining!"
                /|!       7 And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, 
                / 5        for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them.
                    
            ^^^^^^^^^     
''')
    elif (failureCount == 4):
        print(f'''  
               /___|
               \   /
                \ /
                 0       "{failureCount} turns remaining!"
                /||       24 That by him, and through him, and of him, the worlds are and were created, and the inhabitants thereof are begotten sons and daughters unto God.
                / |
                    
            ^^^^^^^^^     
''')
    elif (failureCount == 3):
        print(f''' 
                ___
               \   /
                \ /
                 0
                /||     "{failureCount} turns remaining!"
                / |     39 For behold, this is my work and my glory—to bring to pass the immortality and eternal life of man.
                    
            ^^^^^^^^^     
''')
    elif (failureCount == 2):
        print(f'''    
               \   /
                \ /
                 0
                /||      "{failureCount} turns remaining!"
                / |      He [Jesus Christ] has given His life that even in our weakness, we may overcome our mistakes through repentance and obedience to His gospel.
                    
            ^^^^^^^^^     
''')
    elif (failureCount == 1):
        print(f''' 
                \ /
                 0
                /||      "{failureCount} turns remaining!"
                / |       Men must follow Christ, be baptized, receive the Holy Ghost, and endure to the end to be saved, 
                    
            ^^^^^^^^^     
        ''')
    elif (failureCount == 0):
        print(f''' 
                 x
                /||       "{failureCount} turns remaining!"
                / |        "God is love." 
                    
              ^^^^^^^^^     
''')
    guess = input("Your guess: ")
    if guess in secretword:
        print(f"correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incoorect. there are no {guess} in the secret word. {failureCount} turn(s) left.")


    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0
    for letter in secretword:
        if letter in lettersGuessed:
            print(f"{letter}", end = "")
        else:
            print("_", end = "")

            wrongLetterCount += 1
    if wrongLetterCount == 0:
        print(f"congratualtions! the secret word was: {secretword}. you won! winner!")
        print("winner!")
        print("winner!")
        print("winner!")
        print("winner!")
        print("winner!")
        print("winner!")
        print("")
        print("")
        print("")
        print("")

        break
    