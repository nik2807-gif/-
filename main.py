user_input = input("Скажи щось: ")

if user_input.lower() == "привіт":
    print("Привіт! Як справи?")
    
    # Крок 2: Чекаємо на відповідь про стан справ
    status = input() 
    
    if status.lower() == "нормально":
        print("В мене теж!")
    else:
        print("Бідняга, сподіваюсь, скоро все налагодиться.")