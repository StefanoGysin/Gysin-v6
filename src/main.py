# isso e um testS
from core.assistant import Assistant
from interfaces.gui import GysinIAGUI
from utils.logger import setup_logger
from interfaces.gui import GysinIAGUI

def main():
    logger = setup_logger()
    assistant = Assistant()
    app = GysinIAGUI()
    
    logger.info("Iniciando Gysin IA")
    app.run()

if __name__ == "__main__":
    main()