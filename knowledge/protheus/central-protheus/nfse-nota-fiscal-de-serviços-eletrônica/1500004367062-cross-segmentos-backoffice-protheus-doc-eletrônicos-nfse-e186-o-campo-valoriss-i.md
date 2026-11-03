---
article_id: 1500004367062
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1e1d38d2373e0739cc53b9d02ac84336108f6df136009e7f737b583bf64dd728
fetched_at: '2026-06-28T22:39:56.242188+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE -  E186: O
  campo valorIss informado incorretamente'
type: support-article
updated_at: '2025-07-08T19:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004367062-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E186-O-campo-valorIss-informado-incorretamente
---

**Dúvida**Ao transmitir um RPS para prefeituras que trabalham com o provedor GINFES ocorre a rejeição abaixo:  
*"E186: O campo valorIss informado incorretamente".*  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A GINFES apresenta a orientação abaixo para a rejeição E186: **O valor do campo ValorIss é calculado multiplicando a base de cálculo pelo valor da alíquota.**  
  
O rdmake NFSEXMLENV usa o conteúdo do campo CD2\_VLTRIB para destacar no XML o Valor de ISS.  
Esse calculo deve estar correto (Aliquota x Base de Calculo) e com arredondamento, pois a GINFES espera esse arredondamento.  
  
Instruções para arredondamento do valor do ISS: [MP - FIS - Arredondamento de ISS Padrão ABNT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027191731-MP-FIS-Arredondamento-de-ISS-Padr%C3%A3o-ABNT)
