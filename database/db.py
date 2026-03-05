import sqlite3
import json
from typing import Optional, List, Dict, Any


class Database:
    """SQLite database handler for character sheets"""

    def __init__(self, db_path: str = "db.sqlite"):
        """Initialize the database connection and create tables if needed
        
        Args:
            db_path: Path to the SQLite database file"""

        self.db_path = db_path
        self.connection = None
        self.cursor = None

        self.init_db()


    def init_db(self):
        """Initialize the database connection and create tables if they don't exist"""

        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            
            # Create characters table if it doesn't exist
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS characters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    character_sheet TEXT NOT NULL
                )
            """)
            
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise


    def get_all_characters(self) -> List[Dict[str, Any]]:
        """Get all characters from the database
        
        Returns:
            List of dictionaries containing character data"""

        try:
            self.cursor.execute("SELECT id, name, character_sheet FROM characters")
            rows = self.cursor.fetchall()
            
            characters = []
            for row in rows:
                character_id, character_name, character_sheet_json = row
                try:
                    character_data = json.loads(character_sheet_json)
                except json.JSONDecodeError:
                    character_data = {}
                
                characters.append({
                    "id": character_id,
                    "name": character_name,
                    "data": character_data
                })
            
            return characters
        except sqlite3.Error as e:
            print(f"Error retrieving characters: {e}")

            return []


    def get_character_by_id(self, character_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific character by ID
        
        Args:
            character_id: The character ID
            
        Returns:
            Dictionary containing character data or None if not found"""

        try:
            self.cursor.execute("SELECT id, name, character_sheet FROM characters WHERE id = ?", (character_id,))
            row = self.cursor.fetchone()
            
            if row:
                character_id, character_name, character_sheet_json = row
                try:
                    character_data = json.loads(character_sheet_json)
                except json.JSONDecodeError:
                    character_data = {}
                
                return {
                    "id": character_id,
                    "name": character_name,
                    "data": character_data
                }
            
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving character: {e}")

            return None


    def insert_character(self, character_name: str, character_data: Dict[str, Any]) -> Optional[int]:
        """Insert a new character into the database
        
        Args:
            name: Character name
            character_data: Dictionary containing character data
            
        Returns:
            The ID of the inserted character or None if failed"""

        try:
            character_sheet_json = json.dumps(character_data)
            self.cursor.execute(
                "INSERT INTO characters (name, character_sheet) VALUES (?, ?)",
                (character_name, character_sheet_json)
            )
            self.connection.commit()

            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting character: {e}")
            return None


    def update_character(self, character_id: int, character_name: str, character_data: Dict[str, Any]) -> bool:
        """Update an existing character in the database
        
        Args:
            char_id: The character ID
            name: Character name
            character_data: Dictionary containing character data
            
        Returns:
            True if successful, False otherwise"""

        try:
            character_sheet_json = json.dumps(character_data)
            self.cursor.execute(
                "UPDATE characters SET name = ?, character_sheet = ? WHERE id = ?",
                (character_name, character_sheet_json, character_id)
            )
            self.connection.commit()

            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating character: {e}")

            return False


    def delete_character(self, character_id: int) -> bool:
        """Delete a character from the database
        
        Args:
            char_id: The character ID
            
        Returns:
            True if successful, False otherwise"""

        try:
            self.cursor.execute("DELETE FROM characters WHERE id = ?", (character_id,))
            self.connection.commit()

            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting character: {e}")

            return False


    def close(self):
        """Close the database connection"""

        if self.connection:
            self.connection.close()


    def __del__(self):
        """Ensure database connection is closed when object is destroyed"""

        self.close()
