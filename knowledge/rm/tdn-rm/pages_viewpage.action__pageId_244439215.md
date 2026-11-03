---
content_hash: 9cca6d3ae7ccfb8641e51166bba1b0637047051b5e293c77125dc53ce7989a7d
fetched_at: '2026-06-29T00:08:14.049528+00:00'
page_id: '244439215'
product: rm
source: tdn-rm
title: TTRNGN_DT_Baixa_Cancelamento_do_Item_de_Baixa_do_Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244439215
version: 111
---

# Baixa - Cancelamento do Item de Baixa do Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa - Cancelamento do Item de Baixa do Lançamento |
| **Situação/Requisito:** | Ao realizar o cancelamento de baixa de um lançamento baixado via arquivo de retorno bancário, o campo CNABCODRETORNO na tabela FLAN continua preenchido. |
| **Solução/Implementação:** | Ao cancelar um item de baixa que seja referente a baixa por Retorno Bancário, o campo Código de Retorno será atualizando assumindo o valor nulo. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FINTRF000255 |

divs
