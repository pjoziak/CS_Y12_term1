import random

data = [
    ["Application", "System", "Feature", "Mobile App", "Website"],
    ["yields", "shows", "displays", "throws", "renders"],
    ["invalid response", "error", "warning", "exception"],
    ["when button was", "when page was", "when the window was", "then page link was"],
    ["clicked", "visited", "opened", "showed", "refreshed"]
]


def generate_sentence(sentencepieces: list[list[str]]) -> str:
    return " ".join(random.choice(sentencepiece) for sentencepiece in sentencepieces)


def is_yes(s: str):
    return s.lower() in ['yes', 'y', 'yeah', 't', '']


def check_continue():
    userinput = input('Do you want next sentence? [y/n] ')
    return is_yes(userinput)


def print_msg_box(msg, indent=1, width=None):
    lines = msg.split('\n')
    if not width:
        width = max(map(len, lines)) + 2 * indent
    box = f'╔{"═" * width}╗\n'
    box += ''.join([f'║{line.center(width)}║\n' for line in lines])
    box += f'╚{"═" * width}╝'
    print(box)


def main():
    print_msg_box("Customer complaints generator")
    print('', end="\n\n")
    cont = True
    while cont:
        print_msg_box(generate_sentence(data))
        cont = check_continue()


if __name__ == '__main__':
    main()
