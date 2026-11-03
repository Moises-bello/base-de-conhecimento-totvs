---
article_id: 360025945272
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 45e5549b9cf2310d53cadf3cb0398b36dd603091efb459a41d4b48b8bcd47650
fetched_at: '2026-06-28T22:39:56.441001+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Destacar
  o C6_DESCRI na Discriminação dos serviços
type: support-article
updated_at: '2025-07-08T20:04:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025945272-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Destacar-o-C6-DESCRI-na-Discrimina%C3%A7%C3%A3o-dos-servi%C3%A7os
---

**Dúvida**Como usar o conteúdo do C6\_DESCRI na discriminação dos serviço?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para destacar o C6\_DESCRI é necessário a configuração abaixo de parâmetros:  
  
**MV\_NFSEMOD = .T.**  
**MV\_NFEDESC = .F.**  
**MV\_NFESERV = 2**  
  
1. Após isso crie um campo MEMO na tabela SC5. Esse campo será usado para alimentar a tag DescricaoRPS (provedores DSFNET).   
2. Coloque o nome desse campo dentro do parâmetro **MV\_CMPUSR**.  
3. Feito isso emita uma nota preenchendo os campos acima (C6\_DESCRI e campo customizado na SC5).  
  
**IMPORTANTE!**  
*Caso o provedor da prefeitura não seja DSFNET, não é necessário preencher o campo criado na SC5 (passo 3), apenas o C6\_DESCRI.   
**Porém os passos 1 e 2 ainda são necessários.***  
*- [Relação Municípios x Provedor](https://tdn.totvs.com/pages/releaseview.action?pageId=4814340)*
