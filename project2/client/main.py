from requests import get, post

def show_game(game):
    if "status" in game and game["status"]=="error":
        print("НЕт такой игры")
        return None
    print(
        f"title: {game['title']}, "+
        f"genre: {game['genre']}, "+
        f"platform: {game['platform']}, "+
        f"date_of_release: {game['date']}"
    )
def show_games():
    for game in games:
        show_game(game)
    print("\n \n")

def main():
    MENU_TEXT="1. Посмотреть все игры\n2. Найти игру по названию\n3. Добавить игру\n4.Выйти"
    while True:
        user_input=str(input(f"Введите пункт меню: "))
        if user_input=="1":
            show_game