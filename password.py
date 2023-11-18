import random
import traceback

class RandomPassword():
    def __init__(self):
        self.letters = ["Q", "W", "E", "R", "T", "Y", "U", "O", "P", "A", "S", "D", "F",
                        "G", "H", "J", "K", "L", "I", "Z", "X", "C", "V", "B", "N", "M"]
        
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def password(self):
        try:

            #? "self.result" stores the generated password.
            self.result = []

            #? Choose 4 random letters from "self.letters".
            for i in range(1,5):
                self.result.append(random.choice(self.letters))

            #? Choose 4 random digits from "self.letters".
            for j in range(1,5):
                self.result += random.choice(self.digits)

            #! Shuffle the new password to make sense.
            random.shuffle(self.result)

            try:
                if self.result:

                    #? Get rid of the the list bracets, quotes and commas. 
                    simplify = str(self.result).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace(",", "")

                    print(simplify)

            except Exception:
                error_traceback = traceback.format_exc()
                print(error_traceback)

        except Exception:
            error_traceback = traceback.format_exc()
            print(error_traceback)

new_password = RandomPassword()
new_password.password()
