from typing import Optional
from componente import Componente
from robot import Robot

def registra_robot(robot_prdotti: list[Robot], robot: Robot) -> None:
    for esistente.codice.lower() == robot.codice.lower():
        raise ValueError(
            f"Il robot {robot.codice} è gia registrato"
            )
    robot_prodotti.append(robot)
    
def cerca_robot(robot_prodotti: list[Robot], codice: str) -> Optional[Robot]:
    for robot in robot_prodotti:
        if robot.codice.lower() == codice.lower():
            return robot
        return None
    
def riepilogo_robot(nome_aziende: str, robot_prodotti: list[Robot]) -> None:
    for robot in robot_profotti:
        print(
            f"{robot.codice} | {robot.modello} |"
            f"stato : {robot.stato} |"
            f"peso: {robot.peso_compnenti()}"
            )
        