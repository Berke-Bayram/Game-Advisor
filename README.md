# Game Advisor

Game Advisor is a simple application that provides game recommendations based on user-selected genres.
It utilizes the RAWG Video Games Database API to fetch game data and Tkinter for the graphical user interface.

## Features

- Allows users to select a genre from a predefined list.
- Fetches game recommendations from the RAWG API based on the selected genre.
- Displays recommended game details including name, release date, background image, Metacritic score, and supported platforms.

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python installation)

## Usage

1. Upon running the application, a window will appear with a list of genres on the left side.
2. Select a genre from the list.
3. Click the "Generate" button to get a game recommendation based on the selected genre.
4. The recommended game details will be displayed on the right side of the window, including its name, release date, background image, Metacritic score, and supported platforms.

## API Key

To use the application, you need to obtain an API key from [RAWG API](https://rawg.io/apidocs). Once you have the API key, you can use the file `key.py` in the project directory and assign your API key.

`key.py` file:

```python
api = "your_api_key_here"
```

## Notes

- Any unexpected behavior or incorrect match regarding the game category may be related to the data provided by the RAWG API itself. It's recommended to check the documentation provided by RAWG and ensure that the API is being used correctly.
- Please find the documentation at [RAWG API Documentation](https://api.rawg.io/docs/).
- Users are encouraged to refer to the RAWG API documentation for any additional information or updates. If necessary, users can provide supplements to the application to improve its functionality.


