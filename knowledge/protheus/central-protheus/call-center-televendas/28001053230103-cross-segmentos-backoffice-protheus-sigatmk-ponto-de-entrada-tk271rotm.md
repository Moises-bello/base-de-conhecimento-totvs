---
article_id: 28001053230103
category: Call Center - Televendas
content_hash: 717d5da51cb8da5dc4a61641f39a1f1d1f77d916e7bcbccc8e77fc4302d906da
fetched_at: '2026-06-28T22:41:30.267355+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Ponto de entrada TK271ROTM
type: support-article
updated_at: '2024-11-22T19:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28001053230103-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Ponto-de-entrada-TK271ROTM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28001066516503) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o exemplo do ponto de entrada TK271ROTM?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões  
  
**Solução**O ponto de entrada serve para permitir a personalização de novas rotinas no *browse* inicial da rotina de atendimento Call Center. (É possível incluir no máximo duas novas rotinas customizadas)

**Rotina:** TMKA271

Exemplo:

```
#INCLUDE 'PROTHEUS.CH'

User Function TK271ROTM()

    Local aRotina := {} //Adiciona Rotina Customizada aos botoes doBrowse
    aAdd( aRotina, { 'Customizacao' ,'U_XXX001', 0 , 7 })

Return aRotina

User Function XXX001()
    MsgAlert( 'Executando Rotina Customizada')
Return Nil
```

**Resultado:**

![](https://totvssuporte.zendesk.com/attachments/token/VCPDq9UNEMgckH1DVZavPRzIj/?name=image.png)

**Saiba mais:**

[**TK271ROTM - Personalização de novas rotinas**](https://tdn.totvs.com/x/mZJn)

[**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Limitação no ponto de entrada TK271ROTM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034699774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Limita%C3%A7%C3%A3o-no-ponto-de-entrada-TK271ROTM?source=search)
