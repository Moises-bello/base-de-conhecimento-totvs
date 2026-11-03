---
article_id: 4402519785495
category: Faturamento - Cenários de Venda
content_hash: 5882e6de2bca4a95741c2b609428268761218a41dbcf150a3367b863e3e5b41f
fetched_at: '2026-06-28T22:38:33.972393+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada
  da rotina FATA100
type: support-article
updated_at: '2021-06-11T18:37:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402519785495-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-da-rotina-FATA100
---

**Dúvida**Quais são os pontos de entrada existentes na rotina **Regras de Negócio (FATA100)**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Abaixo a lista com os pontos de entrada existentes na rotina **Regras de Negócio (FATA100)**, e seus endereços de documentação no TDN:

**- FT100RNI -** Avaliação dos itens da regra de negócios: <https://tdn.totvs.com/x/9IVn>

**- FT100TOK -** TudoOK Regras do Negócio: <https://tdn.totvs.com/x/OYZn>

**- FT100MNU -** Antecede abertura do Browse: <https://tdn.totvs.com/x/SYRn>

**Obs.:** O ponto de entrada **FT100MRN** - Localizado na função **Ft100RDes**, tratado na função aButtons - aButtons := ExecBlock( "FT100MRN",.F.,.F.,{@aButtons, @oGetD1, @oGetD2, @oGetD3} ), porém, ainda em documentação pela equipe de produto.
