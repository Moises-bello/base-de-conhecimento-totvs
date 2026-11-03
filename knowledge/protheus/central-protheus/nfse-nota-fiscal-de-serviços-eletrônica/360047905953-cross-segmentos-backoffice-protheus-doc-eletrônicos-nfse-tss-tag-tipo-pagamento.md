---
article_id: 360047905953
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1dbbdffac48ee9a4c66d6b4ebe73c8693492c92759d56f91174c0ec9d1bf3f3d
fetched_at: '2026-06-28T22:39:58.594350+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: TAG  <tipo_pagamento>
  (IPM)'
type: support-article
updated_at: '2025-06-04T14:47:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047905953-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-TAG-tipo-pagamento-IPM
---

**Dúvida**Como é configurado o conteúdo da TAG **<tipo\_pagamento>** para prefeituras com provedor IPM?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A tag <tipo\_pagamento> varia de acordo com o conteúdo do campo **E4\_COND** na rotina de **Condições de Pagamentos (MATA360)**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070007313/mceclip0.png)  
  
As possibilidades são:

**<tipo\_pagamento> = 1 (À VISTA)**  
Deverá utilizar a condição igual à 00  
Exemplo: 00  
  
**<tipo\_pagamento> = 2 (À PRAZO)**  
Deverá utilizar alguma condição contendo vírgula (",")  
Exemplo: 00,10,20  
  
**<tipo\_pagamento> = 3 (NA APRESENTAÇÃO)**Deverá utilizar uma condição maior que 00  
Exemplos: 07  
  
Obs.:   
I. O fonte IPM inverte a ordem dos conteúdos que recebe do rdmake NFSEXMLENV para se enquadrar na layout das prefeituras.  
II. Para o município de Bento Gonçalves/RS é chumbado sempre como <tipo\_pagamento> = 2, por conta de uma exigência da prefeitura.
