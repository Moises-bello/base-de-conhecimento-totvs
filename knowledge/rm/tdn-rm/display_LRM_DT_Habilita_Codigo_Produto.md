---
content_hash: 3b86b64a9fc13f160a118f260606f24c00f3a470fe205ec4a86b39b855160618
fetched_at: '2026-06-29T00:06:04.331586+00:00'
page_id: '200908595'
product: rm
source: tdn-rm
title: DT_Habilita_Codigo_Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Habilita_Codigo_Produto
version: 11
---

# Habilitar código do produto

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Sáude |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Lançamento na conta do paciente | |
| **Requisito (ISSUE):** | [PCREQ-6796](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6796 "PCREQ-6796") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

A melhoria permite que o usuário possa copiar o conteúdo que consta no valor do campo código do produto. O código do produto estará sempre habilitado nas ações de edição, visualização e inclusão de registros.

Para os casos de visualização dos registros, o campo código do produto não estará disponível para digitação apenas será possível a cópia da informação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *da versão 12.1.7*.

1. Aplique o patch do chamado e execute uma vez a rotina**lançamento da conta do paciente.**

## Procedimento para Utilização

1. Acesse o menu **Faturamento / Particular e Convênios / Lançamentos na Conta do Paciente**.
2. Pesquise um atendimento.
3. Selecione a parcial desejada.
4. Acesse a guia **MATMED**.
5. Clique no botão **Incluir**, digite o código do produto (CODIGOPRD). O sistema realizará a busca da descrição do produto caso exista.
