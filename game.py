import random

playing_game = True
players = ['everybody']

for player in players:
    player = input('what is your players name? (type done to move on to the game) ')
    if player == 'done':
        break;
    players.append(player)

print('how this game works: everyone gets a beer and a shot. if you are selected randomly from the list of players you take a shot and do the action requested. game the fuck on.')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

while playing_game == True:
    actions = [
    'read this silently, moo at random first person that laughs has to drink',
    'explain why you dont wear womens clothing',
    'act like a turtle who is running from the cops',
    'bark',
    'you must ask the group to go potty the rest of the night',
    'make a rule',
    'Eat A Teaspoon Of Either Mustard, Soy Sauce Or Hot Sauce, but you aren\'nt allowed to know which one it is',
    'PICTIONARY... you have 60 seconds to draw a picture, if no one guesses what it is, you must face away from the group for a whole round',
    'pretend to be the person on your right for 10 minutes',
    'Sing a song chosen by the group while eating spoonfuls of peanut butter',
    'take a drink of your beer but with trex arms',
    'you can not say yes like or no or you have to take a drink',
    'pass a field sobriety test or take 2 shots',
    'talk in an accent for the next 3 rounds',
    'serenade the person to your left and it has to be in jibberish',
    'do your best impression of a baby being born',
    'put four ice cubes down your pants',
    'Make up a 30 second opera about a person or people in the group and perform it.',
    'spin in circles for 30 seconds, last one standing wins and gives out 2 drinks',
    'everyone text this person, last text recieved has to drink 1',
    'open a bag of snacks using only your mouth(no hands or feet allowed)',
    'talk like kermit the frog for 2 rounds',
    'smoke break.... return in 10',
    'break an egg over your head',
    'make up a rap about koalas'

     ]
    pause = input("press enter to continue...type stop to quit")
    print(random.choice(players))
    print(random.choice(actions))
    if pause == 'stop':
        playing_game = False
