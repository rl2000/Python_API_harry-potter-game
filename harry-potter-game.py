import random
import requests


def random_character():
    response = requests.get('http://hp-api.herokuapp.com/api/characters/students')
    harryPotter = response.json()
    #print(len(harryPotter))
    character_number = random.randint(1, 10)
    return {
        'name': harryPotter[character_number]['name'],
        'house': harryPotter[character_number]['house'],
        'eyeColour': harryPotter[character_number]['eyeColour']
    }



def run():
    questions_counter = 0
    my_score_counter = 0
    computer_score_counter = 0



    for questions in range(3):
        questions_counter = questions_counter+1
        print('------------------------------------------')
        print('Round {}'.format(questions_counter))
        print('------------------------------------------')

        my_character = random_character()
        print('You were given {}'.format(my_character['name']))

        player_choice = input('which stat do you want to choose? (house or eyeColour): ')


        computer_character = random_character()
        print('The computer chose {}'.format(computer_character['name']))

        my_stat = my_character[player_choice]
        computer_stat = computer_character[player_choice]

        my_score = 0
        computer_score = 0

        if my_stat == computer_stat:
            my_score = my_score + 1
            my_score_counter = my_score_counter + my_score
            computer_score_counter = computer_score_counter + computer_score
            print('Wohoo! You scored 1 point here!')

            print('Your total score: {} '.format(my_score_counter))
            print('Computers total score: {} '.format(computer_score))
        #print('You are doing great!')
        else:
            if my_stat != computer_stat:
                computer_score = computer_score + 1
                computer_score_counter = computer_score_counter + computer_score
                print('Sorry, you lost 1 point!')
                print('------------------------------------------')
                print('Your total score: {}'.format(my_score_counter))
                print('Computers total score: {}'.format(computer_score_counter))

    print('------------------------------------------')
    if my_score_counter > computer_score_counter:

        print('CONGRATULATIONS! You are a WINNER')
    else:
        print('BAD LUCK! You LOST')


    #print('You score is: {}'.format(my_score_counter))
    #print('Computer score is: {}'.format(computer_score_counter))
run()
