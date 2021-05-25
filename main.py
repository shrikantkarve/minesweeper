import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy

kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MineSweeperGrid(GridLayout):
    # grid dimensions in terms of number of cells
    # Each cell is a button
    def __init__(self, **kwargs):
        super(MineSweeperGrid, self).__init__(**kwargs)

        self.cols = 25
        self.rows = 25
        
        self.btn = []
        for row in range(self.rows):
            self.btn.append([
                Button(
                    text ="",
                    font_size ="20sp",
                    background_normal = "unopened_square.png"
                    #background_down = None
                ) for x in range(self.cols)])
        for row in range(self.rows):
            for col in range(self.cols):
                self.add_widget(self.btn[row][col])

        
class MineSweeperApp(App):
    def build(self):
        return MineSweeperGrid()

    def callback(self, event):
        print("Button pressed")

if __name__ == '__main__':
    MineSweeperApp().run()

#print("Hi")