class Pessoas:
    def __init__(self,nome:str,cpf:str,senha:str,agencia:str) -> None:
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__senha: str = senha
        self.__agencia: str = agencia
        self.__limite: float = 1000.0

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def senha(self) -> str:
        return self.__senha

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def limite(self) -> float:
        return self.__limite

    def __str__(self) -> str:
        return f'Cliente:{self.nome}\nCpf:{self.cpf}\nSenha:{self.senha}\nAgencia:{self.agencia}\nLimite:{self.limite}'

