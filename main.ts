let tool = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    tool += 1
    if (tool == 3) {
        tool = 0
    }
    
    if (tool == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (tool == 1) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    tool = randint(0, 2)
    if (tool == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (tool == 1) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
