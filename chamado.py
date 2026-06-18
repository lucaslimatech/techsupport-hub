from datetime import datetime


class Chamado:
    def __init__(self, id, cliente, titulo, descricao, prioridade="Média", status="Aberto", data_criacao=None):
        self.id = id
        self.cliente = cliente
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.data_criacao = data_criacao or datetime.now().strftime("%d/%m/%Y %H:%M")

    def to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_criacao": self.data_criacao
        }

    @staticmethod
    def from_dict(dados):
        return Chamado(
            id=dados["id"],
            cliente=dados["cliente"],
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            prioridade=dados["prioridade"],
            status=dados["status"],
            data_criacao=dados["data_criacao"]
        )