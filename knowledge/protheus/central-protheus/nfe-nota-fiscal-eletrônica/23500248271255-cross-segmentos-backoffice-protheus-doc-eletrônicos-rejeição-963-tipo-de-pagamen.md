---
article_id: 23500248271255
category: NFe - Nota Fiscal Eletrônica
content_hash: d9cf3c77fbb28627ba1b1a05a7148b08de2a2c0a817d99b8f075438b8f4db791
fetched_at: '2026-06-28T22:40:07.167021+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 963: Tipo
  de pagamento não aceita o grupo de cartões ou boletos. [nOcor:999]'
type: support-article
updated_at: '2025-06-11T11:46:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23500248271255-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-963-Tipo-de-pagamento-n%C3%A3o-aceita-o-grupo-de-cart%C3%B5es-ou-boletos-nOcor-999
---

**Dúvida**

Como solucionar a rejeição abaixo ?

Rejeição 963: Tipo de pagamento não aceita o grupo de cartões ou boletos. [nOcor:999]

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Se Meio de Pagamento (tag: tPag) for diferente de 03, 04, 10, 11, 12, 13, 15, 17 e 18:  
Não pode ser preenchido o grupo de cartões (tag: card).  
   
![](https://atendimento.tecnospeed.com.br/hc/article_attachments/22107999297175)  
   
Na prática, o que isso significa?  
  
A Rejeição 963 pode ocorrer quando uma NF-e for emitida com a tag tPag\_YA02 diferente de 03, 04, 10, 11, 12, 13, 15, 17 e 18 e for informado o grupo de cartões.   
   
Para resolver a **Rejeição: Tipo de pagamento não aceita o grupo de cartões ou boletos. [nOcor:999]**, verifique se o grupo de cartões foi informado para um tipo de pagamento diferente de 03, 04, 10, 11, 12, 13, 15, 17 e 18, caso sim, o mesmo deverá ser removido.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23500249468951)  
   
Verifique a documentação abaixo para alterar a forma de pagamento:  
   
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-tPag-forma-de-pagamento-duplicata-fatura?source=search)**
