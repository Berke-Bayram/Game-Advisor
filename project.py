# Modules and Files
from tkinter import *
import requests
import random
from key import api

# Constants
BACKGROUND = "#474F7A"
BUTTON_COLOR = "#81689D"
LISTBOX_COLOR = "#1F2544"

class App:
    def __init__(self):
        # Class attributes
        self.api_key = api
        self.listbox = None
        self.text_box = None

        # Create the window
        self.window = Tk()
        self.width = 1000
        self.height = 560
        self.window.title('Game Advisor')
        self.window.config(bg=BACKGROUND)
        self.window.resizable(width=False, height=False)

        self.initiate_window()
        self.handleGUI()

        self.window.mainloop()


    def initiate_window(self):
        # Centralize the window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = int((screen_width / 2) - (self.width / 2))
        y = int((screen_height / 2) - (self.height / 2))

        self.window.geometry("{}x{}+{}+{}".format(self.width, self.height, x, y))


    def handleGame(self):
        url = "https://api.rawg.io/api/games"
        response = requests.get(url, params={
            "key": self.api_key,
            "genre": self.listbox.get(self.listbox.curselection()),
            "page_size": 40
        })
        # Choose a random game among all results
        results = response.json()["results"]
        result = random.choice(results)
        # If there is no result, try again
        while result == None:
            result = random.choice(response.json()["results"])
        return result


    def handleGUI(self):
        self.window.config(padx=125)

        # Title Label
        title_label = Label(text="Game Advisor", font=("Cooper Black", 20, "normal"), fg="azure", bg=BACKGROUND)
        title_label.pack()

        left_frame = Frame(self.window, bg=BACKGROUND)
        left_frame.pack(side=LEFT)

        right_frame = Frame(self.window, bg=BACKGROUND)
        right_frame.pack(side=RIGHT)

        # Genre Label
        genre = Label(left_frame, text="Genres", font=("Cooper Black", 16, "normal"), fg="azure", bg=BACKGROUND)
        genre.grid(row=1, column=0)

        # Category Listbox
        self.listbox = Listbox(left_frame, height=7, font=("Lucida Sans Regular", 12, "bold"), bg=LISTBOX_COLOR, fg="white")
        self.listbox.grid(row=2, column=0, pady=10)
        categories = ["Action", "RPG", "Indie", "Adventure", "Simulation", "Strategy"]
        for item in categories:
            self.listbox.insert(END, item)

        # Play Label
        play_label = Label(right_frame, text="Give this one a try!", font=("Cooper Black", 20, "normal"), fg="azure", bg=BACKGROUND)
        play_label.grid(row=0, column=2, padx=10)
        
        # Text Widget
        self.text_box = Text(right_frame, height=12, width=40, font=("Lucida Sans Regular", 16, "normal"), bg=BUTTON_COLOR, fg="white")
        self.text_box.grid(row=1, column=2, padx=(40, 0), pady=(20, 0))
        
        # Generate Button
        generate = Button(left_frame, 
                          text="Generate", 
                          font=("Lucida Sans Regular", 12, "normal"), 
                          bg=BUTTON_COLOR, 
                          fg="white",
                          command=self.text_insert)
        generate.grid(row=4, column=0)


    def text_insert(self):
        # Get the recommended game from the method
        game = self.handleGame()

        # Clear the text and insert the new one
        self.text_box.delete(1.0, END)
        game_string = f"""Game ID: {game["id"]}\nName: {game["name"]}\nReleased: {game["released"]}\n
Image: {game["background_image"]}\n\nMetacritic Score: {game["metacritic"]}/100\n"""
        
        platforms = game["platforms"]
        platform_names = "Platforms: "
        for element in platforms:
            platform_names += f"{element['platform']['name']}/"
        
        result_string = game_string + platform_names

        self.text_box.insert(END, result_string)


App1 = App()
