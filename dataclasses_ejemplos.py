from dataclasses import dataclass, field, asdict
import operaciones
from typing import List

@dataclass(frozen=True)
class Persona:
    nombre: str
    edad: int = field(default = 35)

    def retornar_edad_por_2(self) -> int:
        return self.edad * 2
    
@dataclass
class Puesto:
    nombre: str
    persona: Persona

class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona2 = Persona2("Pedro", 22)
persona1 = Persona("Juan")

puesto1 = Puesto("Desarrollador",persona1)

"""print(operaciones.resta(persona2.edad, persona1.edad))"""

@dataclass
class Grupo:
    personas: List[Persona] = field(default_factory=list)

grupo1 = Grupo()

grupo1.personas.append(persona1)

print(grupo1.personas)