from models.data import users
from utils.crud import show_users, add_new_user, search_user, remove_user, update_user

if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:

        print("Menu:")
        print("0. Zakończ program")
        print("1. wyświetl co u znajomych")
        print("2. dodaj użytkownika")
        print("3. znajdź użytkownika")
        print("4. usuń użytkownika")
        print("5. modyfikuj użytkownika")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "2":
            show_users(users)
            add_new_user(users)
        if menu_option == "3":
            search_user(users)
        if menu_option == "4":
            remove_user(users)
        if menu_option == "5":
            update_user(users)


