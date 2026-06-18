# TechSupport Hub

Sistema de gerenciamento de chamados desenvolvido em Python, criado para simular uma rotina real de suporte técnico em uma empresa de tecnologia.

O projeto permite cadastrar, listar, buscar, atualizar e excluir chamados, utilizando persistência de dados em arquivo JSON. Ele foi desenvolvido como parte de um ecossistema de portfólio voltado para vagas de estágio em tecnologia, com foco em Python, lógica de programação, suporte técnico, automação, dados, APIs e testes.

---

## Sobre o projeto

O **TechSupport Hub** é uma aplicação de terminal que simula um sistema simples de Help Desk.

A proposta é representar uma situação comum em empresas: o registro e acompanhamento de chamados de suporte técnico. Cada chamado possui informações como cliente, título, descrição, prioridade, status e data de criação.

Este projeto foi pensado para evoluir gradualmente, começando com uma versão simples em terminal e depois avançando para banco de dados, API REST, dashboard, relatórios e testes automatizados.

---

## Objetivo

O principal objetivo deste projeto é praticar e demonstrar conhecimentos fundamentais de Python aplicados a um problema real de negócio.

Com ele, é possível demonstrar habilidades como:

- Lógica de programação
- Programação orientada a objetos
- Manipulação de arquivos
- Persistência de dados em JSON
- Organização de código em módulos
- Estruturação de um CRUD
- Tratamento de erros
- Simulação de fluxo de suporte técnico
- Preparação para evolução com banco de dados, API e dashboard

---

## Funcionalidades

A versão atual do sistema permite:

- Abrir novo chamado
- Listar todos os chamados cadastrados
- Buscar chamado por ID
- Atualizar status do chamado
- Alterar prioridade do chamado
- Excluir chamado
- Salvar chamados em arquivo JSON
- Carregar chamados salvos ao iniciar o sistema

---

## Dados de um chamado

Cada chamado possui os seguintes campos:

| Campo | Descrição |
|---|---|
| ID | Identificador único do chamado |
| Cliente | Nome do cliente ou solicitante |
| Título | Resumo curto do problema |
| Descrição | Detalhamento do problema relatado |
| Prioridade | Nível de urgência do chamado |
| Status | Situação atual do atendimento |
| Data de criação | Data e horário em que o chamado foi aberto |

---

## Prioridades disponíveis

O sistema trabalha com quatro níveis de prioridade:

| Prioridade | Descrição |
|---|---|
| Baixa | Problema simples, sem grande impacto |
| Média | Problema comum, com impacto moderado |
| Alta | Problema importante, exige atenção rápida |
| Crítica | Problema urgente, com alto impacto operacional |

---

## Status disponíveis

Os chamados podem ter os seguintes status:

| Status | Descrição |
|---|---|
| Aberto | Chamado registrado, ainda sem resolução |
| Em andamento | Chamado está sendo analisado ou tratado |
| Resolvido | Problema foi solucionado |
| Fechado | Chamado finalizado |

---

## Tecnologias utilizadas

- Python
- JSON
- Programação Orientada a Objetos
- Manipulação de arquivos
- Git
- GitHub

---

## Conceitos praticados

Durante o desenvolvimento deste projeto, foram aplicados conceitos importantes para quem está iniciando na área de tecnologia:

- Criação de classes
- Criação de métodos
- Instanciação de objetos
- Organização do projeto em arquivos separados
- Uso de listas e dicionários
- Leitura e escrita de arquivos
- Conversão de objetos para dicionários
- Conversão de dicionários para objetos
- Validação de entrada do usuário
- Uso de estruturas condicionais
- Uso de laços de repetição
- Separação de responsabilidades entre arquivos



## Estrutura do projeto

    text
techsupport-hub/
│
├── main.py
├── chamado.py
├── gerenciador.py
├── chamados.json
└── README.md