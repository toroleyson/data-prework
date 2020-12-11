Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
>>> saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
>>> 
>>> spells = 0
>>> if (len(gandalf) == len(saruman)):
    print ("Duel of socerers:")
    spells = len(gandalf)
else:
    "Sorcerers don't have the same number of spells"

    
Duel of socerers:
>>> gandalf_wins = 0
>>> saruman_wins = 0
>>> ties = 0
>>> 
>>> for i in range (0,spells):
    if gandalf[i] > saruman[i]:
        gandalf_wins = gandalf_wins + 1
    elif saruman[i] > gandalf[i]:
        saruman_wins = saruman_wins + 1
    else:
        ties = ties + 1

        
>>> print ("Gandalf wins:", gandalf_wins)
Gandalf wins: 6
>>> print ("Saruman wins:", saruman_wins)
Saruman wins: 4
>>> print ("Ties:", ties)
Ties: 0
>>> if gandalf_wins > saruman_wins:
    print ("Result of the duel: Gandalf wins")
elif saruman_wins > gandalf_wins:
    print ("Result of the duel: Saruman wins")
else:
    print ("Result of the duel: Tie")

    
Result of the duel: Gandalf wins
>>> 
