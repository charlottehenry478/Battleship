from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

human = HumanPlayer()
human.printGuessGrid()
human.printShipGrid()
human.placeShips("D")
human.printShipGrid()

computer = ComputerPlayer()
computer.printGuessGrid()
computer.printShipGrid()
computer.placeShips("D")
computer.printShipGrid()