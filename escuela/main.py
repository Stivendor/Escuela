from models.estudiante import Estudiante
from models.profesor import Profesor

if __name__ == "__main__":
    e1 = Estudiante("Ana", 20, "2025A001")
    p1 = Profesor("Carlos", 40, "Matemáticas")
    
    #metodos de prueba

    print(e1.presentarse())
    print(p1.presentarse())