d = {
    "hello": "здравей",
    "goodbye": "довиждане",
    "please": "моля",
    "thank you": "благодаря"
}



while True: 
    print("Въведете опция: ")
    print("1. Търсене на дума")
    print("2. Добавяне на дума")
    print("3. Преглед на съдържание")
    print("4. Изтриване на дума")
    print("5. Изход")
    choice = int(input())
    if choice == 1:
        word = input("Въведете дума на английски: ".strip().lower())
        if word in d:
            print(f"Превод на {word}: {d[word]}")
        else:
            print(f"Думата {word} не е намерена в речника")
            translation = input(f"Въведете превод на {word}: ".strip())
            d[word] = translation
            print(f"Думата {word} е добавена с превод: {translation}")
    elif choice == 2:
        word = input(f"Въведете дума за добавяне на английски: ".strip())
        if word in d:
            print(f"Думата {word} вече съществува в речника с превод {d[word]}")
        else:
            translation = input(f"Въведете превод на {word}: ".strip())
            d[word] = translation
            print(f"Думата {word} е добавена с превод: {translation}")
    elif choice == 3:
        print("Съдържанието на речника е: ")
        for eng,bg in d.items():
            print(f"{eng} - {bg}")
    elif choice == 4:
        word_del = input("Въведете дума която да се изтрие: ")
        if word_del in d:
            del d[word_del]
            print(f"Думата {word_del} е изтрита успешно от речника ")
        else:
            print(f"Думата {word_del} не е намерена в речника")
    elif choice == 5:
        print("Изход от програмата")
        break


