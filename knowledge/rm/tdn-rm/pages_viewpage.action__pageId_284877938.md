---
content_hash: 3fe2202872fdd9f84cd2377748c6f0136a48b5d57d9389b7a7455d8250bb68ed
fetched_at: '2026-06-29T00:08:37.162860+00:00'
page_id: '284877938'
product: rm
source: tdn-rm
title: DT Melhoria na Utilização do Controle de Pedidos de Exames da Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284877938
version: 107
---

# Melhoria na utilização do Painel de Eletivos do Posto de Enfermagem

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina:** | | Unidades de Atendimento |  |  | | --- | | **Rotina envolvida:** | | Controle de Pedido de Exames / Responsável pelo Recebimento do laudo | |
| **Cadastros Iniciais:** | Unidades de Atendimento / Controle de Pedido de Exame deverá possuir um exame com Status 'F' |
| **Tickets relacionados:** | Ticket #[712151](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22712151%22 "712151") |
| **Requisito:** | JIRA Produçãokey,summary,type,created,updated,due,assignee,reporter,priority,status,resolution0c783de1-186e-383b-975c-a1acd7d76cb5MSAU-10531 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A partir dessa implementação, ao utilizar o botão de **Responsável pelo Recebimento do laudo**, é possível visualizar o nome do Responsável pelo recebimento do laudo e também a data em que foi realizada a entrega.

## Procedimento para Utilização

1. Acesse **Unidades de Atendimento/ Controle de Pedidos de Exames**
2. Selecione um exame com Status 'E' e clique duas vezes nele para alterar o status do exame.
3. No combobox '**Executar ação**' e selecionar '**Entregar exame**', clique no botão **Salvar.**
4. O sistema abrirá a tela de **Dados de Registro de Entrega de Exames**.
5. Preencher os dados e clique em **OK**.
6. O sistema voltará para a tela de **Preenchimento de Resultados**, clique em **OK**.
7. O sistema retornará para a tela de **Controle de Pedidos de Exames**, e o status do exame deverá ser 'F'.
8. Selecione o exame que foi alterado no passo anterior e clicar no botão **Responsável de Recebimento do Laudo**.
9. O sistema abrirá a tela **Preenchimento de Resultados**, com o nome do **Responsável pelo recebimento do Laudo**, e a data do recebimento (preenchidos anteriormente).

divs
