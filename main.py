import pygetwindow as gw
from click_back_to_game import click_back_to_game

def bring_minecraft_to_front():
    minecraft_window_name = "Minecraft* 1.19.4 - Singleplayer"
    
    minecraft_window = gw.getWindowsWithTitle(minecraft_window_name)
    if minecraft_window:
        minecraft_window[0].activate()
    else:
        print("Okno gry Minecraft nie zostało znalezione.")
bring_minecraft_to_front()
click_back_to_game()