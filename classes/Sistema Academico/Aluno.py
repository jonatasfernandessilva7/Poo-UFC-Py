class Aluno:

    __nome = None
    __email = None
    __matricula = None
    _notas = None
    _frequencia = None
    _curso = None
    _semestre = None

    def __init__(self, nome:str, email:str, matricula:str, notas:[], frequencia:{}, curso:str, semestre:int):
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula
        self._notas = notas
        self._frequencia = frequencia
        self._curso = curso
        self._semestre = semestre
        print("ok")

    @property
    def frequencia(self):
        return self._frequencia