import pyautogui

def click_back_to_game():
    # Ścieżka do pliku z obrazem przycisku "Back to Game"
    button_image_path = "images/back_to_game_button.png"

    # Wyszukiwanie przycisku "Back to Game" na ekranie
    button_location = pyautogui.locateOnScreen(button_image_path)
    if button_location:
        button_x, button_y, button_width, button_height = button_location
        button_center_x = button_x + button_width // 2
        button_center_y = button_y + button_height // 2

        # Kliknij w przycisk "Back to Game"
        pyautogui.click(button_center_x, button_center_y)
    else:
        print("Przycisk 'Back to Game' nie został znaleziony.")