---
article_id: 360026216773
category: Folha Mensal
content_hash: e61491700043c2f81eb1ea1442ac32e8eb9a7e83c9df878548e0a2c32151f995
fetched_at: '2026-06-28T22:46:59.529572+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Funcionários demitidos não aparecem na folha analítica
type: support-article
updated_at: '2025-01-20T21:40:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026216773-RH-RM-FOP-Funcion%C3%A1rios-demitidos-n%C3%A3o-aparecem-na-folha-anal%C3%ADtica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**  
Ao gerar a folha analítica não são impressos funcionários demitidos, sendo que estes funcionários possuem movimentação na competência devido ao pagamento de rescisão complementar.    
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**   
Esse incidente ocorre pois a **data do último movimento** informada no cadastro da rescisão do funcionário é anterior a data do pagamento da rescisão complementar.   
  
**Solução**Para que o funcionário seja impresso na folha analítica, será necessário alterar a data do último movimento informando a data de pagamento da rescisão complementar neste campo:  
  
![print.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040637914/print.png)
