from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTabWidget, QLineEdit
from PySide6.QtGui import QCloseEvent, QAction
from functools import partial

from character_sheet import CharacterSheet
from database.db import Database
from version import APP_INFO
from ui.main_window_ui import Ui_CharacterManagerMainWindow

class MainWindow(QMainWindow, Ui_CharacterManagerMainWindow):
    """Class for the main window of the application"""

    def __init__(self, db: Database):
        super().__init__()
        
        self.setupUi(self)

        # Store database reference
        self.db = db
        
        # Dictionary to map tab indices to character IDs
        # Format: {tab_index: character_id}
        self.tab_to_character_id = {}
        
        # Dictionary to map character IDs to CharacterSheet instances
        # Format: {character_id: CharacterSheet}
        self.character_sheets: dict[int, CharacterSheet] = {}

        # Setup
        # Initialize UI components
        self.initialize_components()

        # Connect menu action signals
        self.connect_menu_action_signals()

        # Initialize tabs from database
        self.character_sheet_tab_widget.clear()
        self.load_characters()


    def initialize_components(self):
        """Initialize UI components"""
        
        # File menu actions
        self.action_new_character_sheet: QAction = self.action_new_character_sheet
        self.action_save_character_sheet: QAction = self.action_save_character_sheet
        self.action_save_all_character_sheets: QAction = self.action_save_all_character_sheets
        self.action_delete_current_character_sheet: QAction = self.action_delete_current_character_sheet
        self.action_exit: QAction = self.action_exit

        # Help menu actions
        self.action_about: QAction = self.action_about

        # Character sheet tab widget
        self.character_sheet_tab_widget: QTabWidget = self.character_sheet_tabWidget


    def connect_menu_action_signals(self):
        """Connect signals for menu actions"""

        # File menu
        self.action_new_character_sheet.triggered.connect(self.init_empty_character_sheet)
        self.action_save_character_sheet.triggered.connect(self.save_character_sheet)
        self.action_save_all_character_sheets.triggered.connect(self.save_all_character_sheets)
        self.action_delete_current_character_sheet.triggered.connect(self.delete_current_character_sheet)
        self.action_exit.triggered.connect(self.close_application)

        # Help menu
        self.action_about.triggered.connect(self.show_about)
    

    def show_about(self):
        """Show the about message box"""
        about_text = f"""
<b>{APP_INFO['name']}</b><br>
Verzió: {APP_INFO['version']}<br>
Kiadás dátuma: {APP_INFO['release_date']}<br>
<br>
<b>Készítő:</b> {APP_INFO['creator']}<br>
"""
        QMessageBox.about(self, "Névjegy", about_text)


    def load_characters(self):
        """Load all characters from the database and create tabs for each"""
        
        characters = self.db.get_all_characters()
        
        if not characters:
            # If no characters in database, create an empty character sheet
            self.init_empty_character_sheet()
        else:
            # Load each character from the database
            for character in characters:
                character_id = character["id"]
                character_name = character["name"]
                character_data = character["data"]
                
                # Create a new CharacterSheet instance with the data
                character_sheet = CharacterSheet(character_data)
                
                # Add it to the tab widget
                tab_index = self.character_sheet_tab_widget.addTab(character_sheet, character_name)
                
                # Map tab index to character ID
                self.tab_to_character_id[tab_index] = character_id
                self.character_sheets[character_id] = character_sheet
                
                # Connect the name change signal
                name_line_edit: QLineEdit = character_sheet.findChild(QLineEdit, "name_lineEdit")
                if name_line_edit:
                    name_line_edit.textChanged.connect(partial(self.on_character_name_change, tab_index))


    def init_empty_character_sheet(self):
        """Initialize an empty character sheet"""

        # Create a new CharacterSheet instance
        character_sheet = CharacterSheet()
        
        # Add it to the tab widget
        tab_index = self.character_sheet_tab_widget.addTab(character_sheet, "Új karakter")
        
        # For new characters, we don't have a character_id yet
        # We'll set it to None until it's saved to the database
        self.tab_to_character_id[tab_index] = None
        self.character_sheets[id(character_sheet)] = character_sheet
        
        # Store the character_sheet reference with the tab for later access
        self.character_sheet_tab_widget.setTabText(tab_index, "Új karakter")
        
        # Find the lineEdit in this specific sheet and connect its signal
        name_line_edit: QLineEdit = character_sheet.findChild(QLineEdit, "name_lineEdit")
        if name_line_edit:
            name_line_edit.textChanged.connect(partial(self.on_character_name_change, tab_index))


    def save_character_sheet(self):
        """Save the currently selected character sheet tab"""
        
        current_index = self.character_sheet_tab_widget.currentIndex()
        if current_index < 0:
            return
        
        # Get the character sheet widget for the current tab
        tab_widget = self.character_sheet_tab_widget.widget(current_index)
        
        # Find the CharacterSheet instance that owns this tab
        character_sheet = None
        old_id = None
        for id, character_sheet_instance in self.character_sheets.items():
            if character_sheet_instance == tab_widget:
                character_sheet = character_sheet_instance
                old_id = id
                break
        
        if not character_sheet:
            QMessageBox.warning(self, "Hiba", "Nem található karakter.")
            return
        
        # Get the character data
        character_data: dict = character_sheet.get_character_data()
        character_name: str = character_data.get("name", "Új karakter")
        
        # Check if this is a new character (character_id is None)
        character_id = self.tab_to_character_id.get(current_index)
        
        if character_id is None:
            # Insert new character into database
            character_id = self.db.insert_character(character_name, character_data)

            if character_id:
                self.tab_to_character_id[current_index] = character_id

                # Remove old id and add new one
                if old_id in self.character_sheets:
                    del self.character_sheets[old_id]

                self.character_sheets[character_id] = character_sheet

                # Update tab title
                self.character_sheet_tab_widget.setTabText(current_index, character_name)

                QMessageBox.information(self, "Siker", f"'{character_name}' sikeresen mentve!")
            else:
                QMessageBox.warning(self, "Hiba", "Karakter mentése sikertelen.")
        else:
            # Update existing character
            if self.db.update_character(character_id, character_name, character_data):
                # Update tab title
                self.character_sheet_tab_widget.setTabText(current_index, character_name)

                QMessageBox.information(self, "Siker", f"'{character_name}' sikeresen frissítve!")
            else:
                QMessageBox.warning(self, "Hiba", "Karakter frissítése sikertelen.")


    def save_all_character_sheets(self):
        """Save all character sheet tabs"""
        
        saved_count = 0
        failed_count = 0
        
        for tab_index in range(self.character_sheet_tab_widget.count()):
            tab_widget = self.character_sheet_tab_widget.widget(tab_index)
            
            # Find the CharacterSheet instance
            character_sheet = None
            old_id = None
            for id, character_sheet_instance in self.character_sheets.items():
                if character_sheet_instance == tab_widget:
                    character_sheet = character_sheet_instance
                    old_id = id
                    break
            
            if not character_sheet:
                failed_count += 1
                continue
            
            # Get the character data
            character_data: dict = character_sheet.get_character_data()
            character_name: str = character_data.get("name", "Új karakter")
            
            # Check if this is a new character
            character_id = self.tab_to_character_id.get(tab_index)
            
            if character_id is None:
                # Insert new character
                character_id = self.db.insert_character(character_name, character_data)

                if character_id:
                    self.tab_to_character_id[tab_index] = character_id

                    # Remove old id and add new one
                    if old_id in self.character_sheets:
                        del self.character_sheets[old_id]

                    self.character_sheets[character_id] = character_sheet
                    self.character_sheet_tab_widget.setTabText(tab_index, character_name)
                    saved_count += 1
                else:
                    failed_count += 1
            else:
                # Update existing character
                if self.db.update_character(character_id, character_name, character_data):
                    self.character_sheet_tab_widget.setTabText(tab_index, character_name)
                    saved_count += 1
                else:
                    failed_count += 1
        
        if failed_count == 0:
            QMessageBox.information(self, "Siker", f"{saved_count} karakter sikeresen mentve!")
        else:
            QMessageBox.warning(self, "Hiba", f"{saved_count} karakter sikeresen mentve! Hibák: {failed_count}")


    def delete_current_character_sheet(self):
        """Delete the currently selected character sheet tab"""

        current_index = self.character_sheet_tab_widget.currentIndex()
        if current_index < 0:
            return
        
        character_id = self.tab_to_character_id.get(current_index)
        
        # Show confirmation dialog
        tab_text = self.character_sheet_tab_widget.tabText(current_index)
        reply = QMessageBox.question(
            self,
            "Karakter törlése",
            f"'{tab_text}' törölve lesz! Biztos, hogy folytatod?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Delete from database if it has a character_id
            if character_id is not None:
                if self.db.delete_character(character_id):
                    self.character_sheet_tab_widget.removeTab(current_index)

                    if character_id in self.character_sheets:
                        del self.character_sheets[character_id]

                    if current_index in self.tab_to_character_id:
                        del self.tab_to_character_id[current_index]
                    
                    # If no tabs left, create an empty one
                    if self.character_sheet_tab_widget.count() == 0:
                        self.init_empty_character_sheet()
                    
                    QMessageBox.information(self, "Siker", f"'{tab_text}' sikeresen törölve!")
                else:
                    QMessageBox.warning(self, "Hiba", "Karakter törlése sikertelen.")
            else:
                # For new unsaved characters, just remove the tab
                self.character_sheet_tab_widget.removeTab(current_index)
                
                # If no tabs left, create an empty one
                if self.character_sheet_tab_widget.count() == 0:
                    self.init_empty_character_sheet()


    def on_character_name_change(self, tab_index: int, label: str):
        """Handle changes to the character name

        - Update the tab title when the character name is changed
        - tab_index: The index of the tab to update
        - label: The new character name"""

        self.character_sheet_tab_widget.setTabText(tab_index, label)


    def close_application(self):
        """Close the application"""

        QApplication.quit()


    def closeEvent(self, event: QCloseEvent):
        """Handle the window close event (X button in title bar)"""

        event.accept()
        QApplication.quit()