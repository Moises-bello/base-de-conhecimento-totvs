---
content_hash: 079d0c00c8bd83045c163e01778101c03d0d1a4cd992edf000d466862d2a4c87
fetched_at: '2026-06-29T00:08:49.567683+00:00'
page_id: '331844454'
product: rm
source: tdn-rm
title: DT Recebimento via Cheque na Sessão de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331844454
version: 2
---

# Recebimento via Cheque na Sessão de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Sessão de Caixa.* | *Sessão de Caixa.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Lançamentos* | *Lançamentos* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Lançamentos, Cadastro de Conta/Caixa* |
| **Parâmetro(s):** | *N/A* |
| **Tickets relacionados** | *<https://totvssuporte.zendesk.com/agent/tickets/438616>* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-437 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **Sql-Server e Oracle** |
| **Tabelas Utilizadas:** | *FLAN, FBOLETO, FLANBAIXA, FSESSAOCAIXA, FLOGSESSAOCAIXA, FCXA* |
| **Sistema(s) Operacional(is):** | *MS-Windows* |

## Descrição

Implementado na sessão de caixa a funcionalidade de efetuar um recebimento via cheque para os lançamentos a receber.

Obs.: A permissão de Recebimento via cheque da sessão de caixa é diferente da permissão do cadastro de lançamento.

## Procedimento para Utilização

**Exemplo:**

       1.            Defina no cadastro de "Perfil" o acesso ao "Recebimento via Cheque" da sessão de caixa

       2.            Na tela de sessão de caixa, foi disponibilizado o botão "Recebimento via Cheque"

       3.            Será chamada a tela de Recebimento de cheque para que o operador de caixa possa definir os parâmetros.

       4.            Ao efetuar a baixa de um lançamento que possui cheque emitido será pergunta ao operador se ele deseja baixar o lançamento com cheque recebido.

       5.            Baixar o lançamento com cheque recebido
