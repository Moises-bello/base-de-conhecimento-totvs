---
content_hash: b82236400d75a3c64de9e2f5ae462dd10f4dc826781635b4847fbb7dd84df1d5
fetched_at: '2026-06-29T00:10:13.312670+00:00'
page_id: '455804831'
product: rm
source: tdn-rm
title: DT Cancelar transação com cartão Getnet
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=455804831
version: 5
---

# CANCELAR TRANSAÇÃO COM CARTÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnic** | | Solicitar Cancelamento de Transação - Getnet / Ajuste de Transação - Getnet | Solicitar Cancelamento de Transação - Getnet / Ajuste de Transação - Getnet | |
| **Parâmetro(s):** | 02.02.02.03 - Cartão de Crédito/Débito |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-10377> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.24 |

## Descrição

Criado processo para realizar o cancelamento da transação de cartão na visão de transações com cartão de crédito/débito.

Este processo somente solicitará o cancelamento da transação com cartão das transações realizadas no modelo IFrame Getnet, e caso o status da transação esteja como "Pagamento Confirmado" e "Pagamento Concluído". Ao solicitar o cancelamento da transação o status da transação no TOTVS Gestão Financeira será alterada para "Cancelamento Pendente", sendo necessário executar o processo de "Ajustar transação - Getnet" como mostrado acima.

**Configuração**

O processo de "Cancelar transação com cartão" deve ser habilitado no perfil do usuário.
