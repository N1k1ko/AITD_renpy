define gg = Character("N1k1_ko", color="#0099cc")
define Azari = Character("[name_azari]", color="#0099cc")
define name_azari = "???"

define stackoverflow = False
define good = 0
define find = False

define slowdissolve = Dissolve(1.0)



label start:
    play music "audio/main.mp3" fadeout 1
    scene bg room
    with slowdissolve
    pause 1
    "{i}Очередной рабочий день. Скоро дедлайн, а мы ещё многое должны сделать. Надеюсь сегодня всё пройдёт без проблем.{/i}"
    "{i}Я N1k1_ko, недавно выпустился, а уже устроился в качестве разработчика в отличное местечко с интересным проектом. И это история о том, как всё что могло пойти не так - пошло не так.{/i}"
    "{i}А впрочем, может и не пошло.{/i}"
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
    play music "audio/coffee.mp3" fadeout 1
    pause .5
    "{i}Наконец-то добрался.{/i}"

    show azari
    with slowdissolve
    pause .5
    Azari "Доброе утро, N1k1_ko! Как добрался в этот раз?"
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
    "{i}Это Азарий, мой наставник. Он всегда готов мне помочь советом или решением, если что-то случится - всё таки это его работа, до тех пор пока я не слишком опытен.{/i}"
    "{i}Однако, готов поспорить, что и в будущем он сможет подсказать, если дела будут совсем плохи.{/i}"

    scene bg table_800
    with slowdissolve
    play music "audio/work.mp3" fadeout 1
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

label go_coffee:
    scene bg coffee_light
    with slowdissolve
    play music "audio/coffee.mp3" fadeout 1
    pause .5

    show azari surprised
    with slowdissolve
    pause .5
    menu:
        Azari "О, N1k1_ko, как обстоят дела?"

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
            play music "audio/work.mp3" fadeout 1
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
            "{i}Хмм, ещё одна не из простых задача, отложу её пока.{/i}"

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
            play music "audio/work.mp3" fadeout 1
            pause .5
            jump sit
    return

label sit:
    scene bg table_1145
    with slowdissolve
    "{i}По-любому это какой-то пустяк, нужно лишь немного посидеть и идея сама придёт в голову.{/i}"
    
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

label problem2:
    menu:
        gg "Что же мне делать?"

        "Поискать решение на stackoverflow" if stackoverflow:
            jump stackoverflow
        "Продолжить сидеть":
            jump sit2
        "Пойти в кафетерий":
            "{i}Пойду поищу Азария.{/i}"
            jump go_coffee2

    return

label stackoverflow:
    scene bg table_1700
    with slowdissolve
    pause .5
    menu:
        "{i}О, неплохое решение, но немного не то.{/i}"

        "Взять на заметку" if stackoverflow:
            $good+=1
            $find = True
            $ stackoverflow = False
            "{i}Возьму пока на заметку, может найду что-то подходящее.{/i}"
            jump problem2
        "Нагло скопировать и сидеть дальше":
            "{i}Времени осталось совсем немного, придётся прибегнуть к этому. Позже разберусь и подправлю.{/i}"
            jump sit2
    return

label go_coffee2:
    scene bg coffee_light
    with slowdissolve
    play music "audio/coffee.mp3" fadeout 1
    pause .5

    show azari smile
    with slowdissolve
    pause .5

    menu:
        Azari "N1k1_ko, ну-с, как оно?"

        "Сказать что нашёл" if find:
            $good+=1
            gg "Есть одна вещь, я поискал на stackoverflow, но ничего нужного не нашёл."
            Azari "Блин, времени осталось немного, но давай вместе посмотрим."
            scene bg table_1715
            with slowdissolve
            pause .5
            show azari surprised
            with slowdissolve
            pause .5
            Azari "Ого, да, тут даже мне придётся постараться."
            show azari smile
            with slowdissolve
            Azari "Оставь это на меня, а пока пошли по домам, рабочее время уже вышло."
            gg "Хорошо."
            jump pre_end
        "Рассказать о проблеме" if not find:
            $good+=1
            gg "Да вот, проблемка одна возникла."
            Azari "А на stackoverflow искал?"
            gg "Нет."
            Azari "Поторопись, главное нагло не копируй!"
            $ stackoverflow = False
            play music "audio/work.mp3" fadeout 1
            jump stackoverflow
        "Соврать":
            gg "Всё супер, столько всего сделал."
            show azari angry
            with slowdissolve
            Azari "Да? А мне кажется что ты что-то темнишь - по глазам вижу."
            gg "Да неет, просто лампы светят ярко..."
            "{i}И действительно, Азарий, пусть и не сильно, но был выше меня, от чего приходилось поднимать голову.{/i}"
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
            Azari "Ну, раз всё, как ты говоришь, отлично - продолжай в том же духе, осталось совсем немного!"
            play music "audio/work.mp3" fadeout 1
            jump sit2
    return

label sit2:
    scene bg table_1715
    with slowdissolve
    pause .5
    "{i}Так, мы люди гордые, мы со всем справимся сами!{/i}"
    scene bg table_2015
    with slowdissolve
    pause .5
    "Прошло 3ч."
    "{i}Фух, закончил. А ведь говорил мне Азарий, чтоб не кранчил...{/i}"
    jump pre_end
    return

label pre_end:
    scene bg street
    with slowdissolve
    play music "audio/main.mp3" fadeout 1
    pause .5
    "{i}Вот и подошёл к концу мой рабочий день.{/i}"
    scene bg tram
    with slowdissolve
    pause 1
    "{i}Снова общак.{/i}"
    scene bg bus
    with slowdissolve
    pause 1
    scene bg street
    with slowdissolve
    pause 1
    scene bg room
    with slowdissolve
    pause .5
    "{i}И наконец-то дома. Завтра - последний день перед сдачей проекта.{/i}"
    scene bg room
    with Fade(1,1,1)
    pause 1
    gg "Кх... Кх..."
    "{i}Чёрт, всё-таки простыл... А время уже 12.{/i}"
    "{i}Надо бы позвонить Азарию, предупредить.{/i}"
    play sound "audio/w8.mp3"
    pause 9
    gg "Азарий, я простыл. Как там всё?"
    if good == 3:
        jump good
    elif good > 0:
        jump neutral
    else:
        jump bad
    return

label good:
    show azari smile
    with slowdissolve
    Azari "Ничего, всё в порядке, мы как раз закончили. Отдыхай."
    Azari "И кстати, зови меня Аза."
    "{i}Фух, успели. Теперь и правда можно отдохнуть.{/i}"
    image logo g = Text("Хороший конец", size=72)
    scene bg nothing
    with slowdissolve
    show logo g:
        xalign .5
        yalign .5
    with slowdissolve
    "В итоге проект был сдан в лучшем виде и в срок."
    "Азарий и главный герой стали не только хорошими коллегами, но и друзьями."
    jump end
    return
label neutral:
    show azari smile
    with slowdissolve
    menu:
        Azari "N1k1_ko, не вовремя ты конечно, последний рубеж уже, можешь выйти удалённо?"

        "Работать из дома":
            gg "Кх, хорошо, сделаю что смогу."
            Azari "Спасибо, лишние руки нам не помешают!"
            image logo ng = Text("Хороший нейтральный конец", size=72)
            scene bg nothing
            with slowdissolve
            show logo ng:
                xalign .5
                yalign .5
            with slowdissolve
            "В итоге проект был сдан в лучшем виде и в срок."
            "Азарий уже доверяет главному герою, еще немного и с ним можно будет стать друзьями."
            jump end
        "Ничего не делать":
            gg "Извини, вообще, кх, никак"
            "{i}Соврал...{/i}"
            Azari "Ладно, постараемся без тебя справиться, поправляйся!"
            image logo nb = Text("Плохой нейтральный конец", size=72)
            scene bg nothing
            with slowdissolve
            show logo nb:
                xalign .5
                yalign .5
            with slowdissolve
            "В итоге проект был закончен и сдан вовремя, но его еще придётся доработатывать."
            "Азарий еще не уверен, насчёт главного героя, но продолжает возлагать на него большие надежды."
            jump end
    return
label bad:
    show azari angry
    with slowdissolve
    Azari 'О, смотрите кто объявился! Из-за твоих "всё просто супер" мне сейчас до ночи сидеть и половину переделывать!'
    Azari "А я ведь столько надежд на тебя возлагал... Впредь за тобой буду глаз да глаз..."
    play sound "audio/deny.mp3"
    hide azari
    with Dissolve(3)
    "{i}Лишь бы не вышвырнули..."
    image logo b = Text("Плохой конец", size=72)
    scene bg nothing
    with slowdissolve
    show logo b:
        xalign .5
        yalign .5
    with slowdissolve
    "В итоге проект был сдан, пускай и в срок, но не в самом лучшем виде."
    "Азарий стал меньше доверять главному герою. И придётся приложить не мало усилий чтоб это исправить."
    jump end
    return

label end:
    scene bg end
    with slowdissolve
    pause 30
    return