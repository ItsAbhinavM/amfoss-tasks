import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from PySide6.QtGui import QPixmap, QFont

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 500)
        self.setWindowTitle("Pokémon Data Viewer")

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter a Pokémon's name", self)
        label1.setGeometry(50, 5, 300, 70)

        search_button = QPushButton("Search", self)
        search_button.setGeometry(50, 300, 160, 43)
        search_button.clicked.connect(self.fetch_pokemon_data)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)

        self.pokemon_name_label = QLabel("Name:", self)
        self.pokemon_name_label.setGeometry(350, 20, 300, 40)
        self.pokemon_name_label.setFont(QFont("Arial", 14, QFont.Bold))

        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(350, 50, 250, 250)

        self.pokemon_info_label = QLabel(self)
        self.pokemon_info_label.setGeometry(350, 280, 500, 200)
        self.pokemon_info_label.setFont(QFont("Arial", 14))

        self.pokemon_info_label.setWordWrap(True)
        self.pokemon_name_label.setWordWrap(True)

    def fetch_pokemon_data(self):
        pokemon_name = self.textbox.text().strip().lower()
        if pokemon_name:
            api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                # Display the Pokémon's name
                self.pokemon_name_label.setText(f"Name: {data['name'].capitalize()}")
                # Fetch and display the Pokémon's picture
                pixmap_url = data['sprites']['front_default']
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(pixmap_url).content)
                pixmap = pixmap.scaled(450, 550)  # Set the desired size here
                self.pokemon_image_label.setPixmap(pixmap)
                # Display other data (abilities, types, stats)
                abilities = [ability['ability']['name'] for ability in data['abilities']]
                types = [type['type']['name'] for type in data['types']]
                stats = [f"{stat['stat']['name']}: {stat['base_stat']}" for stat in data['stats']]
                self.pokemon_info_label.setText(f"Abilities: {', '.join(abilities)}\nTypes: {', '.join(types)}\nStats: {', '.join(stats)}")
            else:
                self.pokemon_name_label.setText("Pokémon not found")
                self.pokemon_image_label.clear()
                self.pokemon_info_label.clear()
        else:
            self.pokemon_name_label.setText("Please enter a Pokémon name")
            self.pokemon_image_label.clear()
            self.pokemon_info_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())

