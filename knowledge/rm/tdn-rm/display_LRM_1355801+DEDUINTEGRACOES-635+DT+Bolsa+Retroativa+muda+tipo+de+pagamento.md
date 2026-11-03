---
content_hash: 8af5e6102bfb84f62ffcb74cc4f0673b4cac1720d16fea814ffa9e5bcaabc5f1
fetched_at: '2026-06-29T00:08:43.794467+00:00'
page_id: '306843645'
product: rm
source: tdn-rm
title: 1355801 DEDUINTEGRACOES-635 DT Bolsa Retroativa muda tipo de pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/1355801+DEDUINTEGRACOES-635+DT+Bolsa+Retroativa+muda+tipo+de+pagamento
version: 98
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Bolsa retroativa |
| **Situação/Requisito:** | A coluna 'FLAN.cnabcodretorno' é atualizada para 'null' quando o procedimento de inclusão de bolsa retroativa é realizado.  A coluna não devesse ser atualizada, uma vez que a bolsa retroativa serve de complemento para o lançamento. Se o mesmo foi pago no banco, a bolsa retroativa não deveria apagar esse registro. |
| **Solução/Implementação:** | Melhoria no processo de inclusão de bolsa retroativa para que os campos CNABCODRETORNO,CNABSTATUS da FLAN não sejam alterados, pois após a inclusão da bolsa estes campos devem permanecer com o mesmo valor de antes da inclusão da bolsa. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
