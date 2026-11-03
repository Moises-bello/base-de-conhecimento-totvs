---
article_id: 360027568111
category: Escrita Fiscal - Impostos - ISS
content_hash: d9165c543baeecb82e2fbb7d8b87b73615d0a6423908f55db380376d068e1c7c
fetched_at: '2026-06-28T22:39:35.207049+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como utilizar a alíquota
  padrão do ISS e FISA052?
type: support-article
updated_at: '2021-09-17T12:08:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027568111-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-utilizar-a-al%C3%ADquota-padr%C3%A3o-do-ISS-e-FISA052
---

**Dúvida**  
Cliente quando toma serviços utiliza a FISA052 para alíquotas diferenciadas, como prestador, precisa que o sistema calcule a alíquota padrão conforme o parâmetro MV\_ALIQISS?  
  
**Ambiente**

Protheus - MATA410 - A partir da versão 11.80  
  
**Solução**

Cliente tem alguns municípios cadastrados cadastrados para utilizar a FISA052, contudo, quando presta serviço ele precisa que a alíquota na base de cálculo seja a alíquota padrão do ISS, como fazer?

Para utilizar a alíquota padrão do ISS (MV\_ALIQISS) é necessário validar os seguintes campos:

C5\_ESTPRES = VAZIO

C5\_MUNPRES = VAZIO

B1\_MEPLES = EP - estabelecimento do prestador.
