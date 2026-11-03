---
article_id: 4405266726551
category: Faturamento - Cadastros
content_hash: 642fad0d2de8718535b4013a378b31a2bc00c413280f729e2b957e18634b61a2
fetched_at: '2026-06-28T22:38:36.840033+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Help FT150ECFiltro
type: support-article
updated_at: '2021-07-29T21:07:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405266726551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Help-FT150ECFiltro
---

**Dúvida**Ao salvar amarração da Categoria x Produto FATA150, ocorre Help FT150ECFiltro  
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - A partir da versão 12.  
  
**Solução**![help.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405266652183/help.JPG)

Para não ocorrer o help é necessário cadastrar o produto, primeiro Categoria Pai para posteriormente cadastrar na Categoria Filha, ou não utilizar a configuração:

- Parâmetro MV\_LJECOMM=.T.;  
- Complemento do Produto SB5 configurado no campo E-Commerce **B5\_ECFLAG** igual Ativo;  
- Categoria Pai e Filha configurado no campo E-Commerce **ACU\_ECFLAG** igual Ativo.
