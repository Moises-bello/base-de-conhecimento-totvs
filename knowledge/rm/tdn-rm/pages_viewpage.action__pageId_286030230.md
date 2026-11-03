---
content_hash: 244d5cd400881f9d5bbff8a9d17c18698bb4a987508b65c58f77217127303ff7
fetched_at: '2026-06-29T00:08:39.989524+00:00'
page_id: '286030230'
product: rm
source: tdn-rm
title: 347757 FINANCEIRO01-1646_Campo_Projeto_movimento_para_lançamento_financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286030230
version: 105
---

# LEVAR CAMPO PROJETO DO RATEIO POR CENTRO DE CUSTO DO MOVIMENTO PARA LANÇAMENTO FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Criação de lançamento financeiro a partir do movimento. |
| **Situação/Requisito:** | No rateio por centro de custo do movimento/item o valor do campo **Projeto** não era levado para o lançamento financeiro quando o campo Tarefa não informado. |
| **Solução/Implementação:** | Melhoria no Rateio por Centro de Custo do Movimento/Item – Integrações Financeira, retirada dependência para os campos “Tarefa” e “Projeto” do rateio, se qualquer um dos campos for preenchido no item ou no movimento, este será carregado para o Lançamento Financeiro.  OBS: parâmetro do tipo de movimento **Usa Rateio de Tarefa** deve ser diferente de "Não Usa". |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 347757. |
| **Requisito:** | FINANCEIRO01-1646 |

divs
