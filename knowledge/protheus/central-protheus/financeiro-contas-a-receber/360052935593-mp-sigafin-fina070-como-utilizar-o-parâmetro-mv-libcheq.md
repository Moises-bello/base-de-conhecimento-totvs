---
article_id: 360052935593
category: Financeiro - Contas a Receber
content_hash: caee822eb02526827539f2c9c4334438a8440f67438e47434316d49c6ec3a437
fetched_at: '2026-06-28T22:38:15.024110+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA070 - Como utilizar o parâmetro MV_LIBCHEQ
type: support-article
updated_at: '2021-04-28T15:16:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052935593-MP-SIGAFIN-FINA070-Como-utilizar-o-par%C3%A2metro-MV-LIBCHEQ
---

**Dúvida**Como utilizar o parâmetro MV\_LIBCHEQ?  
  
 **Ambiente**Microsiga Protheus – Financeiro – FINA070 – A partir da versão 11.80  
  
**Solução**Caso seja configurado o parâmetro **MV\_LIBCHEQ** com o conteúdo em **S**:  
  
Baixa automática - Motivo **NORMAL** - Informando o número do cheque:  
O sistema gera a movimentação bancária no momento da baixa.  
  
Baixa automática - Motivo **NORMAL** - Sem informar o número do cheque:  
Após a baixa do título o sistema fica aguardando o usuário Juntar um cheque a mesma para que o sistema possa gerar a movimentação bancária (do cheque).

Baixa automática - Motivo **DEBITOCC** - campo cheque desabilitado:  
O sistema gera a movimentação bancária no momento da baixa.  
  
Se configurado o parâmetro **MV\_LIBCHEQ** com o conteúdo em **N**:  
Baixa automática - Motivo **NORMAL** - Informando o número do cheque:  
O sistema gera a movimentação bancária no momento da liberação do cheque.  
  
Baixa automática - Motivo **NORMAL** - Sem informar o número do cheque:  
Após a baixa do título o sistema fica aguardando o usuário Juntar um cheque a mesma, e posteriormente liberar o cheque para que o sistema possa gerar a movimentação bancária (do cheque).  
  
Baixa automática - Motivo **DEBITOCC** - campo cheque desabilitado:  
O sistema gera a movimentação bancária no momento da baixa.
