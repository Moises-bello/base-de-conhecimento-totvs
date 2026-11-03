---
article_id: 360028813892
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 4d0866d72983e62d229e3e1c5f58b97e7b762ef1c009d06f2f5b8cc41b93893c
fetched_at: '2026-06-28T22:39:49.990900+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Campo Previsão
  Entrega (W6_PRVENTR)
type: support-article
updated_at: '2022-04-27T21:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028813892-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Campo-Previs%C3%A3o-Entrega-W6-PRVENTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao preencher manualmente o campo **Prev. Desem.** (W6\_PRVDESE), automaticamente é calculado o campo **Prev. Entrega** (W6\_PRVENTR), onde ajustar a quantidade de dias para este campo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 11.80  
  
**Solução**Ao preencher manualmente o campo **Prev. Desem.** (W6\_PRVDESE) será verificado o L.Time Tran.(Y6\_LT\_TRA) para calcular automaticamente a data apresentada no campo Prev. Entrega (W6\_PRVENTR).

Sendo assim, para ajuste dos dias, verifique na rotina de Desembaraço, na aba Embarque o destino informado:

​![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030175112/mceclip0.png)

Após acesse em Tabelas \ Portos/Aeroportos(EIC090):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030175212/mceclip1.png)  
​

Busque o destino informado no Desembaraço, selecione alterar e informe os dias no campo L.Time Tran.(Y6\_LT\_TRA):

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030175452/mceclip4.png)  
​
