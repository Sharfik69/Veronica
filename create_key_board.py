import json

def get_button(label, color, payload = ""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def new_key_board(labels_for_keyboard): #принимаем двумерный массив
    buttons_row = []
    for i in labels_for_keyboard:
        new_row = []
        for j in i:
            if j.isdigit(): #если элемент массива является число, то для него делаем зеленый цвет
                new_row.append(get_button(label = j, color = "positive"))
            elif j == 'Отмена' or j == 'Назад': #если элемент является словом, которое возвращает на шаг назад, делаем его красным цветом
                new_row.append(get_button(label = j, color = "negative"))
            else: #иначе в синий цвет
                new_row.append(get_button(label = j, color = "primary"))
                

        buttons_row.append(new_row)
            
    keyboard = {
        "one_time": False,
        "buttons": buttons_row
    }

    keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))

    return keyboard
