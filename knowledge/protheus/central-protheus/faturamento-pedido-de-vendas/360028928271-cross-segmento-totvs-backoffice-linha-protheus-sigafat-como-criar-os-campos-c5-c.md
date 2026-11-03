---
article_id: 360028928271
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: cbc4f79ae4417680ae13ce0c6b2778c69061e8bc4ea272a2f6e3f69675d82a17
fetched_at: '2026-06-28T22:38:38.412439+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat  - Como criar
  os campos C5_CLIRET e C5_LOJARET/ F2_CLIRET e F2_LOJARET?
type: support-article
updated_at: '2022-12-23T20:38:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028928271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Como-criar-os-campos-C5-CLIRET-e-C5-LOJARET-F2-CLIRET-e-F2-LOJARET
---

**Dúvida**

Como criar os campos **C5\_CLIRET** e **C5\_LOJARET**/ **F2\_CLIRET** e **F2\_LOJARET**?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

Os campos **C5\_CLIRET, C5\_LOJARET, F2\_CLIRET, F2\_LOJARET** são usados para identificar o cliente de retirada no **Pedido de Venda (Mata410)** e no **Documento de Saída (Mata461)**.

Com estes campos informados será gerado o grupo de Retirada no XML de transmissão da nota fiscal, conforme o link:

**[http://tdn.totvs.com/display/public/PROT/TUID30\_DT\_NFE\_Campos\_Cliente\_Retirada](http://tdn.totvs.com/display/PROT/NfeSefaz+-+Cliente+de+Retirada+e+Cliente+de+Entrega)**

Para criação dos campos C5\_CLIRET, C5\_LOJARET, F2\_CLIRET, F2\_LOJARET é necessário atualizar o dicionário e base de dados (UPDDISTR ):

**<https://suporte.totvs.com/portal/p/10098/download?e=688783>**

Para maiores detalhes sobre a utilização do UPDDISTR ler a documentação abaixo:

**<http://tdn.totvs.com/pages/viewpage.action?pageId=181965468>**
