---
content_hash: 8c5d89e17a20c57a5cd8f2c0671a20ea7142457e28706ad607adb446dcd9774a
fetched_at: '2026-06-29T00:08:50.832921+00:00'
page_id: '334341536'
product: rm
source: tdn-rm
title: 1773603 EDUCACIONAL01-3814 DT Importacao Multa Pergamum Sem Vinculo
type: documentation
url: https://tdn.totvs.com/display/LRM/1773603+EDUCACIONAL01-3814+DT+Importacao+Multa+Pergamum+Sem+Vinculo
version: 89
---

# IMPORTAR MULTAS GERADAS NO PERGAMUM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Importar multas geradas no Pergamum |
| **Situação/Requisito:** | Foi identificado uma inconsistência na importação de multas geradas pelo Pergamum, o sistema não encontrava os usuários para a geração dos lançamentos das multas. |
| **Solução/Implementação:** | Foi identificado que a situação ocorreu devido a uma alteração feita pelo Pergamum que mudou o campo de retorno do código da pessoa que está vinculado ao TOTVS Educacional, assim o Educacional perdia o vínculo da multa. Foi feito ajuste para que o sistema receba corretamente a multa vinculando a pessoa correta. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
