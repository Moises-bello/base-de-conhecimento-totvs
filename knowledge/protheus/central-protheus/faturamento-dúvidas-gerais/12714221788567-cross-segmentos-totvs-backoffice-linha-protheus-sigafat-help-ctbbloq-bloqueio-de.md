---
article_id: 12714221788567
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e1c2ff938ce35649834f06ca3dbd933f832d84b1792957d4d2e675e2ef476bc6
fetched_at: '2026-06-28T22:38:33.103641+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT  - HELP CTBBLOQ
  / Bloqueio de Calendário Contábil '
type: support-article
updated_at: '2025-01-10T19:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12714221788567-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-HELP-CTBBLOQ-Bloqueio-de-Calend%C3%A1rio-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar bloqueio de Calendário Contábil (HELP CTBBLOQ) ?  
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT – todas as versões.  
  
**Solução**  
É possível bloquear movimentação contábil no modulo faturamento usando a rotina **Moeda x Calendário x Tipo de Saldo (CTBA011)**Abaixo um exemplo de operação   
  
1) Incluir um Lp 610 com a sintaxe SD2->D2\_TOTAL;  
2) Acessar a rotina CTBA011 e bloquear o processo 007 (geração de nota de saída);  
3) Incluir uma NF no sistema com contabilização habilitada. O sistema vai emitir o Help CTBBLOQ  
  
![](https://totvssuporte.zendesk.com/attachments/token/U5CjFGQa7Br0bMG1I72d6pHDz/?name=image.png)
