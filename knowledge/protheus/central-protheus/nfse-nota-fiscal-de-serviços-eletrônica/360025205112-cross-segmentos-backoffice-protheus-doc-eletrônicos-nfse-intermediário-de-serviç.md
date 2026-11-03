---
article_id: 360025205112
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 61108670debdeeefa4d606e2845e51d35ffd21c0bdd335343ff61d2b4afb4565
fetched_at: '2026-06-28T22:39:56.245212+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE -  Intermediário
  de Serviços
type: support-article
updated_at: '2025-07-18T14:39:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025205112-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Intermedi%C3%A1rio-de-Servi%C3%A7os
---

**Dúvida**Como emitir uma nota com os dados do intermediário do serviço?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Inclua o pedido de vendas preenchendo os campos C5\_CLIINT, C5\_CGCINT e C5\_IMINT:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024124531/mceclip1.png)  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024106412/mceclip2.png)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024106452/mceclip3.png)  
O rdmake vai gerar o grupo de tags abaixo, no XML\_TSS da SPED051:

<intermediario>  
<razao></razao>  
<cpfcnpj></cpfcnpj>  
<inscmun></inscmun>  
</intermediario>

O TSS vai utilizar as tags para compor o XML com base no layout da prefeitura, portanto apenas prefeituras que possuem essas informações no layout webservice, terão esses dados no XML.

Veja o exemplo da prefeitura de São Paulo-SP:

<CPFCNPJIntermediario>  
<CNPJ></CNPJ>  
</CPFCNPJIntermediario>  
<InscricaoMunicipalIntermediario></InscricaoMunicipalIntermediario>

Se os dados do tomador não devem ser enviados no XML, veja a instrução no link abaixo:

**[NFSE sem os dados do tomador do serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017731151-MP-NFSE-Emiss%C3%A3o-de-uma-nota-fiscal-de-servi%C3%A7o-sem-tomador)**
