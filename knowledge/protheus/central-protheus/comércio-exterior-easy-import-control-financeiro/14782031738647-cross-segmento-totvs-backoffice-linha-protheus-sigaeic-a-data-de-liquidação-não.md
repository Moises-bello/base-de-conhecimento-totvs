---
article_id: 14782031738647
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 28f20e756a376621c577044ec8851b100f31576a5360bdc813d28d48fd7f71cd
fetched_at: '2026-06-28T22:39:44.470240+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -  A data de liquidação
  não pode ser menor que a Data da Invoice.
type: support-article
updated_at: '2023-05-24T19:44:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14782031738647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-A-data-de-liquida%C3%A7%C3%A3o-n%C3%A3o-pode-ser-menor-que-a-Data-da-Invoice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**A data de liquidação não pode ser menor que a Data da *Invoice*.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14781918281239)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – *Easy Export Control* – A partir da versão 12.1.33  
  
**Solução**

Verifique a data da emissão da *Invoice* do processo dentro da rotina de "**Desembaraço - EICDI502**"**,** no campo **"W9\_DT\_EMIS"**. Caso o mesmo esteja preenchido com data superior a data de liquidação, o sistema irá apresentar a mensagem em questão.

Tal validação é efetuada pelo **SIGAEIC** pois não faz parte da Regra de Negócio do Módulo a Liquidação ocorrer antes mesmo da Emissão da *Invoice*1 - Acesse SIGAEIC - Atualizações - Desembaraço - Manutenção:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14818169060247)  
  
2 - Posicione sobre o processo de Desembaraço, selecione Alterar ou Visualizar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14818211400855)

3 - Em Outras ações -> selecione *Invoices:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14820226445463)*

4 - Em outras ações novamente, selecione  visualizar e confirmar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14818323548439)  
  
5 - Em Manutenção de *Invoices*, verifique a data preenchida na emissão da *Invoice* campo **W9\_DT\_EMIS:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14818381788439)

**Exemplo do processo:**

*![Gravar-2023-05-24-15-26-02-947.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/14818133757079)*
