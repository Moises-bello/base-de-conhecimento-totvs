---
article_id: 360028249211
category: Escrita Fiscal - Impostos - ISS
content_hash: 0404de416939086fa79c3a76957cff65a1d622e0d011bed14bae99a269eb7672
fetched_at: '2026-06-28T22:39:35.268037+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Utilizando à rotina
  FISA052 para Notas Fiscais de Entrada
type: support-article
updated_at: '2022-09-15T12:03:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028249211-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Utilizando-%C3%A0-rotina-FISA052-para-Notas-Fiscais-de-Entrada
---

**Dúvida*****Como utilizar o ISS na rotina FISA052 para Notas fiscais de entrada?***  
  
**Ambiente**Protheus -> Versões: A partir da versão 11.80.

**Solução**Cliente tem alguns municípios cadastrados para utilizar a FISA052, contudo, quando toma serviços, precisa que a alíquota na base de cálculo seja a alíquota padrão do ISS, como fazer?

Configurações:

**Parâmetros:** MV\_ISSXMUN = .T.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028187731/mceclip1.png)

Exemplo:

**Exe. Serviço** (B1\_MEPLES) =  2=LES - Local de Exceção do Serviço.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028190372/mceclip0.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409764079511/mceclip0.png)

**Documento de entrada:** Aba Apuração ISS / INSS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028196971/mceclip3.png)

Link com demais informações:

<https://tdn.totvs.com/pages/releaseview.action?pageId=654295834>
