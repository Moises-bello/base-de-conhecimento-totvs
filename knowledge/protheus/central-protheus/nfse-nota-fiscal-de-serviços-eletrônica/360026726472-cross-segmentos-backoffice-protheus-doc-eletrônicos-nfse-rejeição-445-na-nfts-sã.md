---
article_id: 360026726472
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 30a6abcccb4fba9bd6629a0c22103f8f52199a3ed88a3c8786d0280ddd29b746
fetched_at: '2026-06-28T22:39:58.437397+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  445 na NFTS São Paulo.
type: support-article
updated_at: '2021-10-06T18:09:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026726472-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-445-na-NFTS-S%C3%A3o-Paulo
---

**Dúvida**Como solucionar a rejeição "445 - Prestador autorizado à emissão da NFS-e desde XX/YY/ZZZ. Os serviços tomados ou intermediados com emissão de NFS-e não devem ser declarado".  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A rejeição 445 ocorre na NFTS de São Paulo, porque está sendo transmitido uma nota com o prestador de São Paulo-SP.  
As NFTSs de prestadores de São Paulo-SP que foram emitidas eletronicamente, não podem ser transmitidas para prefeitura pelo tomador do serviço.  
Para que essa nota não seja considerada no range de transmissão, é necessário a parametrização abaixo:  
  
MV\_NFTOMSE=3550308  
No rodapé do documento de entrada, na pasta 'Nota Fiscal Eletronica', preencha os campos **Número** e **Cód.verificação** com os dados da nota fiscal.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026415592/mceclip1.png)  
  
Com essa parametrização, a nota com prestador de São Paulo-SP que foi emitida eletronicamente, não será considerada no range de transmissão da NFTS.
