import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from database.db import Database

def main() -> int:
    """Main entrypoint"""

    # Initialize app
    app = QApplication(sys.argv)
    
    # Initialize database
    db = Database("hkm.db")
    
    # Create main window with database reference
    main_window = MainWindow(db)
    main_window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())