from typing import Optional
from componente import Componente

class Robot:
    def __init__(
        self,
        codice: str,
        modello: str,
        applicazione: str,
        peso_massimo_componenti_kg: float,
        stato: str,
        ) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti: list[componente] = []
        
        def peso_componenti(self) -> float:
            totale = 0.0
            for componente in self.componenti:
                totale += componente.peso_kg
            return totale
        
        def cerca_componente(self.codice: str) -> Optional[Componente]:
            for componente in self.componenti:
                if componente.codice == codice:
                    return componente
                
        def aggiungi_componente(self, componente: Componente) -> None:
            if self.cerca:componente(componente.codice) is not None:ù
            raise ValueError(
                f"Componente {componente.codice } gia presente"
                f"Nel robot {self.codice} ")
            nuovo_peso = self.peso_componenti() + componente.peso_kg
            if nuovo_peso > self.peso_massimo_componenti_kg :
                raise  ValueError(
                    f"peso massimo superato")
            self.componenti.append(componente)
            
        def rimuovi_comnponente(self, codice:str) -> Optional[Componente]:
            componente = self.cerca_componente(codice)
            if componente is not None:
                self.componenti.remove(componente)
                return componente
            
        def componenti_sotto_perso(self, peso_massimo: float) -> list[componente]:
            return [
                componente
                for componente in self.componenti
                if componente.peso_kg <= peso_massimo:
                ]
        