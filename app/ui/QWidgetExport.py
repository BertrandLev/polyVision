from PyQt6.QtWidgets import (QWidget, QVBoxLayout)

class ExportTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout = QVBoxLayout()
        
        # Add widgets to the Selection tab
        self.setLayout(layout)