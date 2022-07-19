tool = 0

def on_button_pressed_b():
    global tool
    tool += 1
    if tool == 3:
        tool = 0
    if tool == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif tool == 1:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global tool
    tool = randint(0, 2)
    if tool == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif tool == 1:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
