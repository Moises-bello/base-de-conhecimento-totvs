---
article_id: 360057421093
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: df9cb7c8f2fc0fc2ce15a012b9ce9630981697d1734da45a329db7cacb1c4979
fetched_at: '2026-06-28T22:39:57.593578+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - NFTS SÃO
  PAULO: Erro 617 - Prestador de SP sem CCM'
type: support-article
updated_at: '2025-06-25T21:15:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057421093-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-NFTS-S%C3%83O-PAULO-Erro-617-Prestador-de-SP-sem-CCM
---

**Dúvida**Ao transmitir uma NFTS para prefeitura de São Paulo - SP, ocorre o erro abaixo:  
**617 - Prestador de SP sem CCM. O ISS deverá ser retido.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094058594/mceclip1.png)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A prefeitura de São Paulo - SP valida os dados do emitente da nota, portanto ao cadastrar o fornecedor (SA2), é importante se certificar de que todos os dados estão corretos.  
  
Esse erro pode ocorrer, quando por exemplo o prestador é de outro município e alguma informação no endereço aponta para São Paulo-SP.  
  
**Exemplo:**  
Prestador de Campinas, porém está com um CEP incorreto de São Paulo - SP.  
  
Se todos os dados estão corretos e o erro ainda permanece, é importante realizar uma consulta junto a prefeitura para entender o motivo da rejeição.
