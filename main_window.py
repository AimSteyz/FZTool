import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QFileDialog, QLabel, QFrame, QTextEdit
from PyQt5.QtCore import Qt
from history_processor import process_history_file

# Create a small window with file selection and sort button
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties (width and height)
        self.setWindowTitle("FZUSB Tool")
        window_width = 1600
        window_height = 800
        self.setFixedSize(window_width, window_height)

        # Center the window on the screen
        self.center_window()

        # Set dark gray background color using stylesheet
        self.setStyleSheet("background-color: #2E2E2E;")  # Dark gray background

        # Create file label to show selected file path
        self.file_label = QLabel("No file selected", self)
        self.file_label.setStyleSheet("color: white;")

        # Create a button to select a file
        self.file_button = QPushButton("Select File", self)
        self.file_button.setStyleSheet("background-color: #4E4E4E; color: white;")
        self.file_button.clicked.connect(self.open_file_dialog)

        # Create a sort button
        self.sort_button = QPushButton("Sort", self)
        self.sort_button.setStyleSheet("background-color: #4E4E4E; color: white;")
        self.sort_button.clicked.connect(self.sort_files)

        # Create a text area to display sorted content
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)  # Make it read-only to display sorted content
        self.text_area.setStyleSheet("background-color: #1E1E1E; color: white;")

        # Vertical layout for the left side (file selection and sort)
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.file_label)
        left_layout.addWidget(self.file_button)
        left_layout.addWidget(self.sort_button)
        left_layout.addStretch()  # Push the buttons to the top for vertical centering

        # Create a vertical line separator
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: white;")

        # Horizontal layout to split left and right sections
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(line)  # Add the separator
        main_layout.addWidget(self.text_area)  # Text area for displaying sorted content

        # Set the layout for the window
        self.setLayout(main_layout)

    # Center the window on the screen
    def center_window(self):
        # Get the geometry of the screen
        screen_geometry = QDesktopWidget().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calculate the top-left corner position to center the window
        x = (screen_width - self.width()) // 2
        y = (screen_height - self.height()) // 2

        # Move the window to the center
        self.move(x, y)

    # Method to open a file dialog and select a file
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_path:
            self.file_label.setText(f"Selected file: {file_path}")
            self.selected_file = file_path  # Store the selected file path

    # Action when sort button is clicked
    def sort_files(self):
        if hasattr(self, 'selected_file'):
            # Call the history processing function and get the formatted output
            sorted_content = process_history_file(self.selected_file)
            self.text_area.setText(sorted_content)  # Display sorted content in text area
        else:
            self.text_area.setText("No file selected!")


# Main function to run the application
def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
