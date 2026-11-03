---
article_id: 22378175934359
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: b419002b6563ce5516caa3c9abbeb6281d21770fd8c13573305f4dbfaacd8cfc
fetched_at: '2026-06-28T22:37:56.214173+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA241 - Como gerar
  o calculo de vencimento dos impostos PCC/IRRF a partir da data de vencimento real
  do título (E2_VENCREA)
type: support-article
updated_at: '2024-03-28T11:48:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22378175934359-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA241-Como-gerar-o-calculo-de-vencimento-dos-impostos-PCC-IRRF-a-partir-da-data-de-vencimento-real-do-t%C3%ADtulo-E2-VENCREA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22378167863319) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar o borderô com o calculo de vencimento dos impostos PCC/IRRF a partir da data de vencimento real do título (E2\_VENCREA) ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - REINF - A partir da versão 12.1.33  
  
**Solução**Para este processo utiliza o parâmetro **MV\_BDVCIMP** = .T.   
  
Se o **MV\_BDVCIMP** = **.T.,** o calculo de vencimento dos **impostos PCC/IRRF** será a partir da data de vencimento real do título **(E2\_VENCREA)**, por exemplo:

* Nota fiscal com vencimento real 05/10/XX, incluso no borderô na data 30/09/XX, o vencimento do imposto será calculado a partir no mês de outubro, logo seu vencimento ocorrerá no mês de novembro.

  | Imposto | Vencimento |
  | --- | --- |
  | PIS | 20/11/XX |
  | COFINS | 20/11/XX |
  | CSLL | 20/11/XX |
  | IRRF | 10/11/XX |

  Se o **MV\_BDVCIMP = .F.** (Default), o calculo de vencimento dos impostos **PCC/IRRF** será a partir da data de geração do borderô, por exemplo:

  + Nota fiscal com vencimento real 05/10/XX, incluso no borderô na data 30/09/XX, o vencimento do imposto será calculado a partir no mês de setembro, logo seu vencimento ocorrerá no mês de outubro.

    | Imposto | Vencimento |
    | --- | --- |
    | PIS | 20/10/XX |
    | COFINS | 20/10/XX |
    | CSLL | 20/10/XX |
    | IRRF | 10/10/XX |

    **Saiba mais:**   
    [Borderô de Impostos (FINA241 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312165366)
