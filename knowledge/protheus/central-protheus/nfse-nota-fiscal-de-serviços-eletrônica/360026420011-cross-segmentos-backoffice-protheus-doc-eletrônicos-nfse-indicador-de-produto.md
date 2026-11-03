---
article_id: 360026420011
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: ad72f1912fb4298b76cfb38852f05401e37fb619e715ae0300fb400beb00f341
fetched_at: '2026-06-28T22:39:57.510254+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Indicador
  de Produto
type: support-article
updated_at: '2025-06-25T14:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026420011-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Indicador-de-Produto
---

**Dúvida**Como configurar o Indicador de Produto para Código de Serviço, Atividade e Tributação para utiliza-lo em NFSE?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Parâmetros deverão estar da seguinte maneira: **MV\_ARQPROD = SBZ** e **MV\_ARQPROP = .T.**É possível usar a rotina **MATA018** (Indicador de Produto) para informar o Código de Serviço, Código de Atividade e Código de Tributação, nos campos BZ\_CODISS, BZ\_CNAE e BZ\_TRIBMUN respectivamente.  
  
**Passo a passo para teste:**  
**1.** Cadastre um produto e preencha o campo Código de Serviço (B1\_CODISS), Código de Atividade (B1\_CNAE) ou Código de Tributação (campo B1\_TRIBMUN);

**2.** Acesse a filial 02, e preencha a "tabela de indicadores de produtos" utilizando o produto cadastrado anteriormente e informe um Código de Serviço, Atividade ou Tributação no campo BZ\_CODISS, BZ\_CNAE ou BZ\_TRIBMUN respectivamente DIFERENTE do que foi cadastrado no produto.
