# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character("[name]", color="#c8ffc8")
define Azari = Character("[name_azari]", color="#c8ffc8")
define name_azari = "???"

define stackoverflow = False
define good = 0
define find = False

define slowdissolve = Dissolve(1.0)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    python:
        name = renpy.input("Ваше имя:")
        name = name.strip()

    "{i}Очередной рабочий день. Скоро дедлайн, а мы ещё многое должны сделать. Надеюсь сегодня всё пройдёт без проблем.{/i}"
    "{i}Я [name], недавно выпустился, а уже устроился в качестве разработчика в отличное местечко с интересным проектом. И это история о том, как всё что могло пойти не так - пошло не так.{/i}"

    scene bg street
    with slowdissolve
    pause .5
    "{i}Морозно сегодня, лишь бы не продуло...{/i}"

    scene bg bus
    with slowdissolve
    pause 1
    scene bg tram
    with slowdissolve
    pause 1

    scene bg coffee_light
    with slowdissolve
    pause .5
    "{i}Наконец-то добрался.{/i}"

    show azari
    with slowdissolve
    pause .5
    Azari "Доброе утро, [name]! Как добрался в этот раз?"
    gg "Чуть коньки не откинул в холодном общаке. Точно когда-нибудь так слягу с болезнью..."
    Azari "Возьмёшь как обычно?"
    gg "Нет, сегодня побольше кофе - много работы предстоит."
    Azari "Смотри много не кранчи, а то и впрямь до добра не доведёт..."
    gg "Тут уж как пойдёт..."
    Azari "Кстати, а почему ты не перейдёшь на удалёнку? Для этого же есть всё и не придётся терпеть общак."
    gg "Не могу я работать там, где находится моя кровать - сразу появляется желание всё бросить и ничего не делать. Не для того я столько времени пытался попасть сюда, чтоб быть вышвырнутым в первый же год."
    show azari smile
    with slowdissolve
    Azari '{i}"Не работать там, где находится твоя кровать"{/i} - хорошо сказано, надо бы запомнить!'
    gg "Ладно, в перерыве ещё пересечёмся."
    Azari "Если что-то не выходит, спрашивай - подскажу!"
    hide azari
    with slowdissolve

    $ name_azari = "Азарий"
    "{i}Это Азарий, мой наставник и уже друг. Он всегда готов мне помочь советом или решением, если что-то случится - всё таки это его работа, до тех пор пока я не слишком опытен.{/i}"
    "{i}Однако, готов поспорить, что и в будущем он сможет подсказать, если дела будут совсем плохи.{/i}"

    scene bg table_800
    with slowdissolve
    pause .5
    "{i}Чтож, пора начинать работать.{/i}"

    scene bg table_1130
    with slowdissolve
    pause .5
    "Прошло 3,5ч."
    "{i}Чёёёрт, ну и как это реализовать?! Ой, надо бы почаще смотреть на часы, а то, в отличии от меня, у Азария мало времени чтобы ещё и мне помогать.{/i}"

    menu:
        "{i}Может пойти поискать его?{/i}"

        "Пойти в кафетерий":
            jump go_coffee
        "Продолжать сидеть на месте":
            jump sit
    return

label problem2:
    menu:
        gg "Что же мне делать?"

        "Поискать рещёние на stackoverflow" if stackoverflow:
            $ stackoverflow = False
            menu:
                "{i}О, неплохое решение, но немного не то.{/i}"

                "Взять на заметку":
                    $good+=1
                    $find = True
                    "{i}Возьму пока на заметку, может найду что-то подходящее.{/i}"
                    jump problem2
                "Нагло скопировать":
                    "{i}Ай, ладно, просто скопирую и в процессе подправлю.{/i}"
                    jump problem2

        "Продолжить сидеть":
            ""
        "Пойти в кафетерий":
            "{i}Пойду поищу Азария.{/i}"
            jump go_coffee2

    return

label go_coffee:
    scene bg coffee_light
    with slowdissolve
    pause .5

    show azari surprised
    with slowdissolve
    pause .5
    menu:
        Azari "О, [name], как обстоят дела?"

        "Сказать":
            $ good+=1
            gg "Да, вот, не знаю как одну тему реализовать."
            Azari "Ты уже искал на том же stackoverflow как можно сделать?"
            $ stackoverflow = True
            gg "Нет."
            show azari smile
            with slowdissolve
            Azari "Поищи, скорее всего кто-то это сделал уже за тебя. Главное не скатывай не задумываясь, а разберись и желательно напиши по-своему."
            gg "Чтобы я без тебя делал..?"
            Azari "Для этого и нужны наставники."
            hide azari
            with slowdissolve

            scene bg table_1145
            with slowdissolve
            pause .5
            "{i}Что же, посмотрим...{/i}"
            pause .5
            "{i}О, так вот как...{/i}"

            scene bg table_1245
            with slowdissolve
            pause .5
            "Прошёл 1ч."
            "{i}Отлично, и даже не так много времени заняло.{/i}"

            scene bg table_1445
            with slowdissolve
            pause .5
            "Прошло 2ч."
            "{i}Хмм, ещё одна не из простых задача, отложу её пока{./i}"

            scene bg table_1645
            with slowdissolve
            pause .5
            "Прошло ещё 2ч."
            "{i}Так, надо бы вернуться к тому что я отложил.{/i}"
            jump problem2

        "Соврать":
            gg "Всё более чем шикарно!"
            show azari angry
            with slowdissolve
            Azari "Правда? А то ты выглядишь так, будто искал меня."
            gg "Да-да, всё окей."
            Azari "Ну смотри, чтоб мне не пришлось доделывать за тебя..."
            hide azari
            with slowdissolve

            "{i}М-да, не хватило смелости спросить...{/i}"
            scene bg table_1145
            with slowdissolve
            pause .5
            jump sit
    return

label sit:
    scene bg table_1145
    with slowdissolve
    "{i}По-любому это какой-то пустяк, нужно лишь немного посидеть и идея сама придёт в голову{/i}"
    
    scene bg table_1445
    with slowdissolve
    pause .5
    "Прошло 3ч."
    "{i}Фух, еле как разобрался с этим, пусть и с костылями, но главное что работает и что я сделала это сам, ведь так..?{/i}"

    scene bg table_1645
    with slowdissolve
    pause .5
    "Прошло ещё 2ч."
    "{i}Ааа, и как я ЭТО должен сделать?!{/i}"
    jump problem2
    return

label go_coffee2:
    scene bg coffee_light
    with slowdissolve
    pause .5

    show azari smile
    with slowdissolve
    pause .5

    menu:
        Azari "[name], ну-с, как оно?"

        "Сказать что нашёл" if find:
            ""
        "Рассказать о проблеме" if not find:
            ""
        "Соврать":
            gg "Всё супер, столько всего сделал."
            show azari angry
            with slowdissolve
            Azari "Да? А мне кажется что ты что-то темнишь - по глазам вижу."
            gg "Да неет, просто лампы светят ярко"
            "{i}И действительно, Азарий, пусть и не сильно, но был выше меня, от чего приходилось поднимать голову{/i}"
            show azari smile
            with slowdissolve
            Azari "Ладно, ладно, давай убавим его, всё равно вечер уже."
            hide azari
            with slowdissolve
            pause .5
            scene bg coffee_dark
            with slowdissolve
            pause .5
            show azari smile
            with slowdissolve
            ""

    return
label sit2:
    
    return