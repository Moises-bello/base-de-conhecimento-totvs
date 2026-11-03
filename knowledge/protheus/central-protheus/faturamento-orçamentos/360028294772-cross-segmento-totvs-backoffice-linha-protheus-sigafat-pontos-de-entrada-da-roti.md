---
article_id: 360028294772
category: Faturamento - Orçamentos
content_hash: eb20a44d1229b161a9fc23195be8b87fc63aa838379a1e8efe4bf5a792d4c9bf
fetched_at: '2026-06-28T22:38:24.942459+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de entrada
  da rotina MATA416
type: support-article
updated_at: '2021-09-06T19:57:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028294772-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-da-rotina-MATA416
---

**Dúvida**

Quais são os pontos de entrada existentes na rotina de Aprovação de Orçamento (MATA416)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  todas as versões

**Solução**

Abaixo a lista com os pontos de entrada existentes na rotina de de Aprovação de Orçamento, e seus endereços de documentação no TDN:

**- MA416FIL** **-** Executado antes da apresentação do Browse e utilizado como filtro do usuário: **<https://tdn.totvs.com/x/GIVn>**

**- MA416COR** **-** Alterar cores do browser do cadastro: **<https://tdn.totvs.com/x/F4Vn>**

**- MA416MNU** **-** Antes da abertura do Browse, caso Browse inicial da rotina esteja habilitado, ou antes da apresentação do Menu de opções, caso Browse inicial esteja desabilitado: **<https://tdn.totvs.com/x/GYVn>**

**- MATA416A** **-** Acionado no início da execução da rotina: **<https://tdn.totvs.com/x/MYVn>**

**- MTA416PV** **-** Executado apos o preenchimento do aCols na Baixa do Orcamento de Vendas: **<https://tdn.totvs.com/x/i4Vn>**

**- MTA416BX** **-** No processamento da baixa orçamento de venda, MA416PROC(). É usado para selecionar os itens a serem baixados e autorizar a baixa do orçamento: **<https://tdn.totvs.com/x/ioVn>**

**- MT416FIM** **-** Após o termino da efetivação do Orçamento de Venda: **<https://tdn.totvs.com/x/aIVn>**

**- MA415LEG -** Alterar textos da legenda de status do orçamento: **<https://tdn.totvs.com/x/FIVn>**
