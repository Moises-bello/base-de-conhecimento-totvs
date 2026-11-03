---
article_id: 360047531273
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 98a3d634c4c8d16f25fa62a2c493e81728c6126d1fc722d76803b52f8272172a
fetched_at: '2026-06-28T22:39:57.560653+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - MV_NFSEDIN
  (Desconto Incondicionado)
type: support-article
updated_at: '2025-06-25T21:22:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047531273-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-MV-NFSEDIN-Desconto-Incondicionado
---

**Dúvida**Como habilitar ou desabilitar o Desconto Incondicionado para NFSE?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**O Desconto Incondicionado de uma NFSE **só poderá ser informado apenas através dos campos: C6\_VALDESC e C6\_DESCONT** no item do Pedido de Vendas.  
  
Após preencher ambos os campos, o valor do desconto incondicionado é populado dentro do campo D2\_DESCON na tabela SD2, o qual será utilizado para a montagem do XML de acordo com a configuração do parâmetro MV\_NFSEDIN:  
  
**MV\_NFSEDIN = .T. (Irá levar o desconto no XML);**  
**MV\_NFSEDIN = .F. (Não irá levar o desconto no XML, onde irá zerar a tag, mesmo tendo conteúdo no D2\_DESCON).**  
  
Exemplo da estrutura do parâmetro:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068919333/mceclip0.png)  
  
Obs.: Para surtir efeito a criação/alteração do parâmetro, **DEVE** ser reiniciado o serviço do Protheus.
