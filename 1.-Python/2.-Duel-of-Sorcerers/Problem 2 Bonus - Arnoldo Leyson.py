Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import statistics
>>> 
>>> POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}
>>> gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
>>> saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
>>> spells = 0
>>> if (len(gandalf) == len(saruman)):
    print ("Duel of socerers:")
    spells = len(gandalf)
else:
    "Sorcerers don't have the same number of spells"

    
Duel of socerers:
>>> gandalf_power = []
>>> saruman_power = []
>>> for i in range (0,spells):
    gandalf_power.append (POWER[gandalf[i]])
    saruman_power.append (POWER[saruman[i]])

    
>>> gandalf_wins = 0
>>> saruman_wins = 0
>>> ties = 0
>>> 
>>> for i in range (0,spells):
    while (gandalf_wins <3):
        if gandalf_power[i] > saruman_power[i]:
            gandalf_wins = gandalf_wins + 1
            saruman_wins = 0
        elif saruman_power[i] > gandalf_power[i]:
            saruman_wins = saruman_wins + 1
            gandalf_wins = 0
        else:
            ties = ties + 1

            
>>> print ("Gandalf wins:", gandalf_wins)
Gandalf wins: 3
>>> print ("Saruman wins:", saruman_wins)
Saruman wins: 0
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
>>> print ("Average spell power of Gandalf:", sum(gandalf_power)/len(gandalf_power))
Average spell power of Gandalf: 39.0
>>> print ("Average spell power of Saruman:", sum(saruman_power)/len(saruman_power))
Average spell power of Saruman: 30.5
>>> print ("Standar deviation of the spell power of Gandalf:", statistics.pstdev(gandalf_power,))
Standar deviation of the spell power of Gandalf: 15.132745950421556
>>> print ("Standar deviation of the spell power of Saruman:", statistics.pstdev(saruman_power,))
Standar deviation of the spell power of Saruman: 15.56438241627338
>>> 
