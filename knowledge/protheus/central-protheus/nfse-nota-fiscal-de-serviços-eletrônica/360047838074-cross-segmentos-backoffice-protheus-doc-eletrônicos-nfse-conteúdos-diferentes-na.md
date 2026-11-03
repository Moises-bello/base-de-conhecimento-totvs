---
article_id: 360047838074
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 197ffd610f1de60f44c198321e635f31dbcfc4418cce0861a209cfee19ef8100
fetched_at: '2026-06-28T22:39:56.407067+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Conteúdos
  diferentes nas tags <dadosAdicionais> e <descricaoServico> (Florianópolis)
type: support-article
updated_at: '2025-07-14T21:13:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047838074-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Conte%C3%BAdos-diferentes-nas-tags-dadosAdicionais-e-descricaoServico-Florian%C3%B3polis
---

**Dúvida**Como configurar para que sejam destacadas informações diferentes nas tags <dadosAdicionais> e <descricaoServico> para a prefeitura de Florianópolis?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para usar informações distintas, terá que deixar os parâmetros da seguinte maneira abaixo:  
  
MV\_CMPUSR = EM BRANCO (sem conteúdo)  
MV\_NFEDESC = .T.  
MV\_NFESERV = 1  
  
Feito isso, serão informados os conteúdos das tags nos respectivos campos:  
  
**<dadosAdicionais>** -> Através do **X5\_DESCRI**, Descrição do Código de Serviço na tabela genérica (60)  
**<descricaoServico>** -> Através do campo **C5\_MENNOTA**no Pedido de Vendas  
  
Exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070324154/mceclip0.png)
