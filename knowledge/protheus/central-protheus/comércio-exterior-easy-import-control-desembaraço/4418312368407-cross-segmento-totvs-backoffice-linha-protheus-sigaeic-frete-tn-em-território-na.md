---
article_id: 4418312368407
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 41004b90102669ff267e6630547bbce6d8c82a167fbfb873c842ab80a8fff8b1
fetched_at: '2026-06-28T22:39:50.074606+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Frete TN em território
  nacional
type: support-article
updated_at: '2022-04-11T14:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418312368407-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Frete-TN-em-territ%C3%B3rio-nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como lançar o frete TN em Território Nacional?  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução** O valor do frete deve ser lançado no desembaraço na sua totalidade na aba transporte campo Vl. Frete CC (W6\_VLFRECC) e no campo Vl. Frete TN (W6\_VLFRETN) o valor do Frete nacional.   
Na capa da invoice nos campos Frete Incl. (W9\_FREINC ) como "2-Não" e *Int'l Freigh* (W9\_FRETEIN) o valor do frete a ser pago.  
  
Exemplo frete incoterm CPT:

```
Valor Frete CC US$ 1.800,00 - Deve ser lançado no valor total  
Valor Frete TN US$ 1.700,00 - Valor a ser abatido dos US$ 1.800,00  
Restará US$ 100,00 a pagar
```

Em Atualizações-> Desembaraço -> Manutenção, posicione no processo e selecione alterar, na Aba transporte:

![](https://totvssuporte.zendesk.com/attachments/token/WzZMtOzz9B1z7xmTlWGTLxdYE/?name=inline-692568107.png)

Outras ações-> Invoice:

![](https://totvssuporte.zendesk.com/attachments/token/20ydRZR8eVwDCp3z34n8m3wzt/?name=inline-1399956139.png)

Ao gerar o câmbio, este será sobre o preço dos itens somando o frete a ser pago.

![](https://totvssuporte.zendesk.com/attachments/token/wZA8S6AhoxJr5bZQLX0IwP9sG/?name=inline1735839954.png)
