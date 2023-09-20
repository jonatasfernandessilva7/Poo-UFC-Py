from Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome:str, email:str, matricula:str, notas:[], frequencia:{}, curso:str, semestre:int):
        Pessoa.__init__(nome, email, matricula)
        self._notas = notas
        self._frequencia = frequencia
        self._curso = curso
        self._semestre = semestre
        print("ok")

    @property
    def frequencia(self):
        return self._frequencia