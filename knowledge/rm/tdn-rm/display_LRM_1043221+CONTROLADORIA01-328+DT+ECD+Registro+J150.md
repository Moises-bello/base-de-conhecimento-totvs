---
content_hash: d7a08bd66715a1dc1af6e2464ff73c97129d12fa2d7cd77ff0d7d96ee6a56925
fetched_at: '2026-06-29T00:08:40.855445+00:00'
page_id: '286512119'
product: rm
source: tdn-rm
title: 1043221 CONTROLADORIA01-328 DT ECD Registro J150
type: documentation
url: https://tdn.totvs.com/display/LRM/1043221+CONTROLADORIA01-328+DT+ECD+Registro+J150
version: 104
---

# ECD Registro J150

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | ECD Registro J150 |
| **Situação/Requisito:** | Na geração da ECD valor de receita positivo é gerado com valor negativo no registro J150, por meio da ferramenta demonstração contábil. |
| **Solução/Implementação:** | A rotina responsável por gerar o registro J150 não estava levando em consideração, no momento de gerar o indicador da situação do valor ('P' ou 'N'), o valor processado pelas expressões existentes na DRE.  Ex: Se o valor processado pela expressão for 1000,00 então o indicador da situação deve ser 'P', porém ser ele for -1000,00 o indicador deve ser 'N'. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
