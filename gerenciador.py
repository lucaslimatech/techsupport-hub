import json
import os
from chamado import Chamado


class GerenciadorChamados:
    def __init__(self, arquivo="chamados.json"):
        self.arquivo = arquivo
        self.chamados = []
        self.carregar_chamados()

    def carregar_chamados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as arquivo_json:
                try:
                    dados = json.load(arquivo_json)
                    self.chamados = [Chamado.from_dict(item) for item in dados]
                except json.JSONDecodeError:
                    self.chamados = []
        else:
            self.chamados = []

    def salvar_chamados(self):
        with open(self.arquivo, "w", encoding="utf-8") as arquivo_json:
            dados = [chamado.to_dict() for chamado in self.chamados]
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)

    def gerar_id(self):
        if not self.chamados:
            return 1

        maior_id = max(chamado.id for chamado in self.chamados)
        return maior_id + 1

    def abrir_chamado(self, cliente, titulo, descricao, prioridade):
        novo_chamado = Chamado(
            id=self.gerar_id(),
            cliente=cliente,
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade
        )

        self.chamados.append(novo_chamado)
        self.salvar_chamados()

        return novo_chamado

    def listar_chamados(self):
        return self.chamados

    def buscar_chamado_por_id(self, id_chamado):
        for chamado in self.chamados:
            if chamado.id == id_chamado:
                return chamado

        return None

    def atualizar_status(self, id_chamado, novo_status):
        chamado = self.buscar_chamado_por_id(id_chamado)

        if chamado:
            chamado.status = novo_status
            self.salvar_chamados()
            return True

        return False

    def alterar_prioridade(self, id_chamado, nova_prioridade):
        chamado = self.buscar_chamado_por_id(id_chamado)

        if chamado:
            chamado.prioridade = nova_prioridade
            self.salvar_chamados()
            return True

        return False

    def excluir_chamado(self, id_chamado):
        chamado = self.buscar_chamado_por_id(id_chamado)

        if chamado:
            self.chamados.remove(chamado)
            self.salvar_chamados()
            return True

        return False
