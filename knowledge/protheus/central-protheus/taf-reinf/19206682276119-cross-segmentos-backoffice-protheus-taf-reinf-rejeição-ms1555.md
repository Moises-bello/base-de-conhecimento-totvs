---
article_id: 19206682276119
category: TAF - REINF
content_hash: 11bc3b304e08a138b7d238e3f8b293fd524f71634ccd255889ae893551c81191
fetched_at: '2026-06-28T22:41:34.810780+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição  MS1555
type: support-article
updated_at: '2023-11-22T12:07:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19206682276119-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1555
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19206729398039) Tempo aproximado para leitura:  00:05:00 min****Ocorrência**Ao transmitir os  eventos do bloco 40  ocorre a rejeição abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206713522455)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Causa**Esse problema  ocorre porque a receita está apontando a ausência das  informações  do país (exterior) no cadastro do participante, requisito relacionado a  natureza de rendimento. Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206706376599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206744198551)

**Solução**

Para solucionar esse problema  existe duas opções.

**Opção 1 -** Trocar a natureza de rendimento informada no documento  para  uma natureza que não efetue essa validação.  Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206713534359)

**Opção 2-**  Caso o participante  seja do exterior,  deve ser feito o preenchimento da aba exterior no cadastro do **Participante** (**TAFA053**)

Os principais campos que deve ser preenchidos são:

Tipo Pessoa EX (**C1H\_PEEXE** ): Para participantes residentes no exterior com a opção = "3 - Outros"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206706383639)

Tipo Pessoa Exterior (**C1H\_PEEXE**) como 1 - Pessoa Jurídica ou 2- Pessoa física

![F8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19206744205207)

Em seguida acesse documento, altere o participante, volte para o participante correto apure e transmita o evento novamente.
