# src/main.py
from core.assistant import Assistant
from interfaces.gui import GysinIAGUI
from utils.logger import setup_logger

def main():
    logger = setup_logger()
    assistant = Assistant()
    app = GysinIAGUI()
    
    logger.info("Iniciando Gysin IA")
    app.run()

if __name__ == "__main__":
    main()