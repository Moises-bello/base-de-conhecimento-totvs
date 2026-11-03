---
article_id: 360018530772
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fa29f8ec2081eda34081e912da762d97b2d383b2f667bca00556a4694ffbd9d7
fetched_at: '2026-06-28T22:38:31.310771+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Nota sobre os campos C9_BLINF e C9_BLTMS
type: support-article
updated_at: '2021-04-28T15:55:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018530772-MP-FAT-Nota-sobre-os-campos-C9-BLINF-e-C9-BLTMS
---

**Dúvida**

Nota sobre os C9\_BLINF e C9\_BLTMS.  
   
 **Ambiente**

Microsiga Protheus -  a partir da versão 11.  
   
**Solução**

O campo **C9\_BLINF** traz a informação do bloqueio, exemplo, se C9\_BLCRED for igual a "01", C9\_BLINF receberá **"Bloqueio de Credito por Valor."**; enquanto o campo **C9\_BLTMS**traz o tipo de bloqueio do TMS, se é **10 - Comercial** ou **20- Operacional**.

Ambos os campos não são utilizados pelo módulo de faturamento, desta forma não possuirão informações se o pedido foi gerado neste módulo.

Os campos em questão são utilizados pelo módulo de **TMS (TMSXFUNA)**, quaisquer dúvidas sobre os mesmos, contatar a equipe de Protheus Logística.
