---
content_hash: 42db93214e065e0647ec8c8365b609fe3c88d493b49ed0b115745067f03ac636
fetched_at: '2026-06-29T00:08:42.246097+00:00'
page_id: '287065483'
product: rm
source: tdn-rm
title: 1356396 DEDUINTEGRACOES-412 DT Erro na inclusão de parcela em contrato com
  bolsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287065483
version: 104
---

# ERRO NA INCLUSÃO DE PARCELA EM CONTRATO COM BOLSA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Concessão de Bolsa Futura |
| **Situação/Requisito:** | Sistema não está verificando corretamente a existência de bolsas no contrato do aluno quando a bolsa é por parcela. |
| **Solução/Implementação:** | Ajuste na verificação de existência de bolsa no contrato a partir da concessão a fim de que, as bolsas nos contratos por parcelas, tenham o seu período convertidos para datas pois a concessão de bolsas sempre é feita por datas. Em resumo, quando existir algum período coincidente entre a concessão de bolsa e a bolsa no contrato do aluno, a bolsa não será concedida. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
