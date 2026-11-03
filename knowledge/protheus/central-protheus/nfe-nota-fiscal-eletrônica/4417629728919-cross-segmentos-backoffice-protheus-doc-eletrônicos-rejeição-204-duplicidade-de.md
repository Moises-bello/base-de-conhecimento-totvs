---
article_id: 4417629728919
category: NFe - Nota Fiscal Eletrônica
content_hash: 3ce5c0a588472754dc585a2e664bbd781e16fbbf654235c9444ddd8d23101a97
fetched_at: '2026-06-28T22:40:07.123667+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 204: Duplicidade
  de NF-e [nRec:999999999999999]'
type: support-article
updated_at: '2022-01-03T12:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417629728919-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-204-Duplicidade-de-NF-e-nRec-999999999999999
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00** **min** **Dúvida**Como resolver a rejeição abaixo na nfe?  
Rejeição 204: Duplicidade de NF-e [nRec:999999999999999].  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.17  
Cross Segmentos - TSS - a partir da versão 12

**Solução**  
Para resolução desta rejeição realize os passos a seguir:

1- Na rotina de transmissão de notas **NFe Sefaz (SPEDNFE),** posicione na respectiva nota e acesse **Outras Ações -> Monitor -> Consulta NF.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058287234/mceclip1.png)

Com isso o TSS fará a consulta da situação da nota na Sefaz, após receber o retorno de Autorizado o Uso acesse o **Monitor -> Faixa,** para que a chave e o retorno de autorização alimente as tabelas do Protheus (SF2, SFT e SF3).

Regra de validação da Sefaz:

![](http://www.oobj.com.br/bc/assets/Articles/289/Rej204.PNG)

 

**Importante:** Caso após receber esta rejeição a nota seja retransmitida, pode causar uma nova rejeição que é a 539, segue detalhes de como resolver esta no link abaixo.

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 539 Rejeição: Duplicidade de NF-e com diferença na Chave de Acesso [chNFe: ]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044295914)
