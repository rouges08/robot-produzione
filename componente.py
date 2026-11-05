class Componente:
    def __init__(
    self.nome: str,
    peso_kg: float
    ) -> None:
    if peso_kg < 0:
        raise ValueError("Il peso non puo essere minore di 0")
    self.codice = codice
    self.nome = nome
    self.peso_kg = peso_kg