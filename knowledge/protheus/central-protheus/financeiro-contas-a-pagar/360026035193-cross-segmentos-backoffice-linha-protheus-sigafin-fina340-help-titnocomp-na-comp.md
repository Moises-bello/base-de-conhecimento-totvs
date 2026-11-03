---
article_id: 360026035193
category: Financeiro - Contas a Pagar
content_hash: ca5a0eed6c7900d07854d73fbaacc66ce675b2d0317f60e28c8aeed8515481bf
fetched_at: '2026-06-28T22:38:09.660654+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - HELP: TITNOCOMP
  na compensação'
type: support-article
updated_at: '2025-11-06T15:04:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026035193-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-HELP-TITNOCOMP-na-compensa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**  
No módulo Financeiro, ao acessar a rotina de compensação e estornar uma compensação  apresenta a mensagem HELP: TITNOCOMP Esse título não possui registro de compensação para estornar.

![titinoi.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360040465754/titinoi.JPG)

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Financeiro - Todas as versões

**Causa**Um dos motivos que ocorre essa mensagem é que os títulos são de origem de outro módulo e no campo  **E5\_HISTOR**, está gravado **Compes. Autom. Adiantamento**.

**![](https://totvssuporte.zendesk.com/attachments/token/ehiCGDWjDFqtmS5p7N4rQuGfj/?name=Microsoft+SQL+Server+Management+Studio_6.jpg)**

**Solução**Realizar a exclusão pelo modo de origem, determinado no campo **E5\_ORIGEM**

​​
