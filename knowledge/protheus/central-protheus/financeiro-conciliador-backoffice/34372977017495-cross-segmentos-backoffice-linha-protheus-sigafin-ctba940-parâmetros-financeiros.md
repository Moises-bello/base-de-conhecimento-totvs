---
article_id: 34372977017495
category: Financeiro - Conciliador Backoffice
content_hash: ea27ee62612e0022d3dd6c4330ea5fe7879b981c4d89818bbcada659334aec92
fetched_at: '2026-06-28T22:37:47.221803+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Parâmetros
  financeiros para bloqueio de alterações de registros conciliados ou inclusões de
  conciliações em períodos fechados
type: support-article
updated_at: '2025-08-22T16:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34372977017495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Par%C3%A2metros-financeiros-para-bloqueio-de-altera%C3%A7%C3%B5es-de-registros-conciliados-ou-inclus%C3%B5es-de-concilia%C3%A7%C3%B5es-em-per%C3%ADodos-fechados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34372976998679) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual os parâmetros financeiros para bloqueio de alterações de registros conciliados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2310  
  
**Solução**  
Quanto as conciliações realizadas nas opções **automática 0023** e **manual 0024** da rotina **Conciliador Backoffice (CTBA940)** existe oparâmetro **MV\_BXCONC** que tem como tem por finalidade permitir cancelamento de baixa conciliada.

**1 = Permite,**

**2 = Não permite.**

Outro parâmetro que existe para o processo seria o **MV\_DATAREC**, porém este só funcionara para o processo **manual 0024**.

Ao informar uma data no **MV\_DATAREC** o sistema passa a não permitir que o usuário realize conciliações manuais dentro do período, ou seja, em que a data dos movimentos seja anterior ao conteúdo do parâmetro.

Exemplo de utilização com um movimento bancário incluído manualmente

1. Informar o conteúdo **20250226** no **MV\_DATAREC**
2. Acessar a rotina de movimentos bancários (**FINA100**)
3. Incluir um movimento a receber no dia **26/02/2025**
4. Acessar a rotina de conciliação manual - **0024 através do****Conciliador*****Backoffice***
5. Preencher os parâmetros informando a data do movimento **26/02/2025**
6. Ao confirmar os filtros o sistema irá exibir uma mensagem dizendo que o período esta fechado para conciliações

Saiba mais:

[Utilização do parâmetro MV\_BXCONC](https://tdn.totvs.com/display/public/PROT/MV_BXCONC)

[Utilização do parâmetro MV\_DATAREC](https://tdn.totvs.com/pages/releaseview.action?pageId=918416598)
