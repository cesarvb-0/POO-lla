from dataclasses import dataclass, field
from typing import List

# Clase Persona
@dataclass
class Persona:
    nombre: str
    correo: str

    def presentarse(self):
        return f"Hola, soy {self.nombre}, mi correo es {self.correo}"


# Clase Empleado (hereda de Persona)
@dataclass
class Empleado(Persona):
    salario: float

    def calcular_bono(self) -> float:
        return 0.0  # Se sobrescribe en subclases

# Desarrollador (hereda de empleado)
@dataclass
class Desarrollador(Empleado):
    lenguaje_principal: str

    def calcular_bono(self, proyecto=None) -> float:
        bono = self.salario * 0.10
        if proyecto and len(proyecto.tareas) > 5:
            bono += self.salario * 0.01
        return bono

    def presentarse(self):
        return f"Soy desarrollador en {self.lenguaje_principal} y me llamo {self.nombre}"


#  Analista (hereda de empleado)
@dataclass
class Analista(Empleado):
    senior_o_junior: str

    def calcular_bono(self) -> float:
        bono = self.salario * 0.08
        if self.senior_o_junior.lower() == "senior":
            bono += self.salario * 0.03
        return bono

    def presentarse(self):
        return f"Soy analista {self.senior_o_junior}, mi nombre es {self.nombre}"


# Gerente (hereda de empleado)
@dataclass
class Gerente(Empleado):
    empleados_a_cargo: List[Empleado] = field(default_factory=list)

    def agregar_empleado(self, e: Empleado):
        if e == self:
            print("Error: un gerente no puede agregarse a sí mismo.")
            return
        if e in self.empleados_a_cargo:
            print("Error: este empleado ya está en el equipo.")
            return
        self.empleados_a_cargo.append(e)

    def remover_empleado(self, e: Empleado):
        if e in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(e)

    def listar_equipo(self):
            nombres = []
            for emp in self.empleados_a_cargo:
                nombres.append(emp.nombre)
            return nombres


    def calcular_bono(self) -> float:
        return self.salario * 0.15

    def presentarse(self):
        return f"Soy el gerente {self.nombre} y tengo {len(self.empleados_a_cargo)} empleados a cargo"



# Clase Tarea (composición dentro de Proyecto)
@dataclass
class Tarea:
    id: int
    descripcion: str
    horas_estimadas: int
    asignado_a: Empleado = None   # Puede no estar asignada todavía


# Clase Proyecto
@dataclass
class Proyecto:
    nombre: str
    presupuesto: float
    tareas: List[Tarea] = field(default_factory=list)
    contador_tareas: int = 0

    def agregar_tarea(self, descripcion: str, horas_estimadas: int):
        if horas_estimadas < 0:
            print("Error: no se permiten horas negativas en una tarea.")
            return None
        self.contador_tareas += 1
        tarea = Tarea(self.contador_tareas, descripcion, horas_estimadas)
        self.tareas.append(tarea)
        return tarea

    def asignar_empleado(self, tarea_id: int, empleado: Empleado):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.asignado_a = empleado
                return
        print("Error: tarea no encontrada.")


# Clase Empresa
@dataclass
class Empresa:
    empleados: List[Empleado] = field(default_factory=list)
    proyectos: List[Proyecto] = field(default_factory=list)

    def agregar_empleado(self, e: Empleado):
        self.empleados.append(e)

    def crear_proyecto(self, nombre: str, presupuesto: float) -> Proyecto:
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto

    def asignar_empleado_a_proyecto(self, proyecto: Proyecto, tarea_id: int, empleado: Empleado):
        proyecto.asignar_empleado(tarea_id, empleado)




developer = Desarrollador("Ana", "ana@gmail.com", 3000, "Python")
analista = Analista("Luis", "luis@gmail.com", 2500, "senior")
gerente = Gerente("Marta", "marta@gmail.com", 5000)

# Gerente agrega empleados
gerente.agregar_empleado(developer)
gerente.agregar_empleado(analista)

# Crear empresa y proyecto
empresa = Empresa()
empresa.agregar_empleado(developer)
empresa.agregar_empleado(analista)
empresa.agregar_empleado(gerente)

proyecto = empresa.crear_proyecto("Sistema de Ventas", 20000)
tarea1 = proyecto.agregar_tarea("Diseñar base de datos", 10)
tarea2 = proyecto.agregar_tarea("Programar backend", 20)

# Asignar empleados a tareas
empresa.asignar_empleado_a_proyecto(proyecto, tarea1.id, analista)
empresa.asignar_empleado_a_proyecto(proyecto, tarea2.id, developer)

# Ejemplos de prints
print(developer.presentarse())
print("Bono developer:", developer.calcular_bono(proyecto))
print(analista.presentarse())
print("Bono analista:", analista.calcular_bono())
print(gerente.presentarse())
print("Equipo gerente:", gerente.listar_equipo())
print("Bono gerente:", gerente.calcular_bono())