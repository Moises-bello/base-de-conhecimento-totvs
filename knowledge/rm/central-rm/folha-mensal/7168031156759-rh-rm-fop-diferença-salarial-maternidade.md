---
article_id: 7168031156759
category: Folha Mensal
content_hash: 147af0a84bbf250d4686aa140203da8f9640fb2b06946dcb3df78f8493083c19
fetched_at: '2026-06-28T22:46:59.150289+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença salarial maternidade
type: support-article
updated_at: '2025-01-07T19:46:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7168031156759-RH-RM-FOP-Diferen%C3%A7a-salarial-maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:45 min****Dúvida**Como realizar a diferença de salário para funcionária que está afastada por licença maternidade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O sistema não possui uma rotina e um código de cálculo para funcionário que está afastado por licença maternidade, então deve -se criar um evento sem código de cálculo e vincular o mesmo no campo **evento de diferença** dentro do evento de  código de cálculo 17 - Salário Maternidade e calcular a diferença.  
  
![](https://totvssuporte.zendesk.com/attachments/token/Izwjp3z9dwSsRRXA4pEtAZTeo/?name=image.png)

**Importante**  
Esta parametrização leva corretamente tanto no E-SOCIAL, quanto na SEFIP que não está preparada para aceitar licença maternidade, sem que o evento esteja informado dentro do código de cálculo 17.
