from console import main_screen
import os

if __name__ == "__main__":
    if not os.path.exists(os.path.join(os.getcwd(), "outputs")):
        os.mkdir(os.path.join(os.getcwd(), "outputs"))
    exc = True
    while exc:
        exc = main_screen()
