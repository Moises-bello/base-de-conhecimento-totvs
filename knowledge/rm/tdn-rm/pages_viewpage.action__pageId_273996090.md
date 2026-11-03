---
content_hash: e6a45a7b1c2825c561f92d7ac93d1dfe8681423fa9d612ffd6a618b1d6bbdab3
fetched_at: '2026-06-29T00:08:32.689328+00:00'
page_id: '273996090'
product: rm
source: tdn-rm
title: 697886 CONTROLADORIA01-80 DT Importação Saldo Anterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273996090
version: 109
---

# Importação de Saldo Anterior Via Conceito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | Conceito |
| **Situação/Requisito:** | Ao executar a importação de saldo anterior, via conceito, é apresentado um erro que impede a conclusão do processo. |
| **Solução/Implementação:** | Foi necessário modificar a importação de saldo anterior para que o campo IDSALDOEXERCICIO, da tabela CSALDOEXERCICIO, seja preenchido. Ele faz parte da chave primária, por isso seu preenchimento é obrigatório. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
