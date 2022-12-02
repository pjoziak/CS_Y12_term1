import random


def roll_dice():
    return random.choice(range(1, 7))


def validate_input(i: str):
    try:
        converted = int(i)
        return 1 <= converted <= 6
    except TypeError:
        return False


def get_player_guess(player: str) -> int:
    while True:
        guess = input(f'What is your guess, {player}? ')
        if validate_input(guess):
            return int(guess)
        else:
            print(f'You should enter one of the numbers [1, 2, ..., 6], you entered {guess}')


def player_turn(player):
    guess = get_player_guess(player)
    dice = roll_dice()
    print(f'Your guess was {guess}, the dice rolled {dice}')
    if guess == dice:
        return 3
    if guess - dice % 2 == 0:
        return 1
    return -2


def validate_continue(s: str) -> bool:
    return not s.lower().startswith('n')


def check_continue_adding_players() -> bool:
    return validate_continue(input('Do you want to add more players? [y/n] '))


def check_continue_game() -> bool:
    return validate_continue(input('Do you want to play more? [y/n] '))


def start_game():
    players = {}
    next_player = True
    while next_player:
        player = input('Enter new player\'s name: ')
        players[player] = []
        next_player = check_continue_adding_players()
    return players


def summarize_scores(players: dict[str, list[int]]) -> None:
    for player, scores in players.items():
        print(f'{player} obtained {sum(scores)} points ({sum(scores) / len(scores):.2f} on average)')


def play_game():
    players = start_game()
    cont = True
    while cont:
        for player in players:
            score = player_turn(player)
            players[player].append(score)
        cont = check_continue_game()
    summarize_scores(players)


if __name__ == '__main__':
    play_game()
