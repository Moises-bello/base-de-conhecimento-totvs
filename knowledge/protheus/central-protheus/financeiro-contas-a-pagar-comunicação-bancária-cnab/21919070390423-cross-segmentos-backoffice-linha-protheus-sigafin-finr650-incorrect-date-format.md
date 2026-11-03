---
article_id: 21919070390423
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 56f85ec7b65a9d3fd3f691901b86706984f7819c31465aabd81cdf25334c2854
fetched_at: '2026-06-28T22:37:56.386397+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR650 - Incorrect
  date format on REPORTPRINT(FINR650.PRX)
type: support-article
updated_at: '2024-03-12T19:59:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21919070390423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR650-Incorrect-date-format-on-REPORTPRINT-FINR650-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21919070322583) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a geração do relatório FINR650 - Relatório de Retorno CNAB, ocorre o error.log Incorrect date format on REPORTPRINT(FINR650.PRX)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o parâmetros de bancos (**FINA130**) está com o campo **EE\_TIPODAT** incorreto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21919076340119)

**Solução**Na rotina parâmetros de bancos (**FINA130**) se faz necessário avaliar as posições de data do **arquivo de retorno** utilizada e qual formato se ajusta na condição abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21919070328215)

Posteriormente realizar a geração do relatório.

**Saiba mais:**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
