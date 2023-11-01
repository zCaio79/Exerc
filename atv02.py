import os

class Professor:
    def __init__(self, nome):
        self.nome = nome

class Curso:
    def __init__(self, nomecurso):
        self.nomecurso = nomecurso
        self.professor = None

    def designar_professor(self, professor):
        self.professor = professor

    def verCurso(self):
        print("Curso: ",self.nomecurso,"\nProfessor: ",self.professor)

os.system('cls')
professor1 = Professor("Dieimes")
curso1 = Curso("Programação")
curso1.designar_professor(professor1.nome)

curso1.verCurso()


