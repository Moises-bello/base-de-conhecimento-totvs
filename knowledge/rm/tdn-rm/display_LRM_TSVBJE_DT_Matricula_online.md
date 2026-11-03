---
content_hash: 1854db5a95e9df55bd7aaf252b1f26d2e967f606da88c7f49bc83705282d770f
fetched_at: '2026-06-29T00:06:01.432665+00:00'
page_id: '198938251'
product: rm
source: tdn-rm
title: TSVBJE_DT_Matricula_online
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVBJE_DT_Matricula_online
version: 1
---

# MATRÍCULA ONLINE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula online* | *Matrícula online* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Geração de lançamento** | *Geração de lançamento* | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado com um usuário válido no portal;*  *2) Aluno matriculado em pelo menos em uma turma/disciplina;*  *3) Aluno com contrato com parcelas com lançamento gerado e em aberto.* |
| **Parâmetro(s):** | *1) Educacional | RM Portal | RM Portal - Matrícula | Contrato Financeiro 1/3 | Disponível para impressão MARCADO;*  *2) Parâmetro: Educacional | RM Portal | RM Portal - Matrícula | Contrato Financeiro 1/3 | Visualizar/alterar plano de pagamento MARCADO.* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server* |
| **Tabelas utilizadas:** | *SLAN, SPARCELA.* |
| **Sistema(s) operacional(is):** | *Windows 7* |
| **Versões/Release:** | *11.82.39.116* |

## Descrição

Otimização da matrícula online para informar ao aluno quando não for possível alterar o contrato de matrícula pelo Portal quando existirem lançamentos gerados.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(11.82.39.116)* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1) No TOTVS Educacional acesse **Menu | Configurações | RM Portal | RM Portal - Matrícula | Contrato Financeiro 1/3.**

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Disponível para impressão |
| **Tipo:** | Booleano (True/False) |
| **Cont. Por.:** | False |
| **Descrição:** | Este parâmetro define que o contrato ficará disponível para impressão no portal ou não. |

2) No TOTVS Educacional acesse **Menu | Configurações | RM Portal | RM Portal - Matrícula | Contrato Financeiro 1/3.**

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Visualizar/alterar plano de pagamento |
| **Tipo:** | Booleano (True/False) |
| **Cont. Por.:** | False |
| **Descrição:** | Este parâmetro define que se será possível ou não alterar e visualizar o plano de pagamento. |

## Procedimento para Utilização

1. Logar no portal do aluno;
2. Acessar Educacional | Acadêmico | Matrícula online;
3. Avançar até a etapa de seleção de Turma/Disciplina;
4. Desmarcar uma matrícula em uma Turma/Disciplina e avançar;
5. Finalizar a matrícula;
6. Como o aluno possui lançamentos, o sistema exibirá uma mensagem informativa para o usuário, o instruindo que já foram geradas cobranças para o plano de pagamento que é necessário ele procurar a secretaria.
