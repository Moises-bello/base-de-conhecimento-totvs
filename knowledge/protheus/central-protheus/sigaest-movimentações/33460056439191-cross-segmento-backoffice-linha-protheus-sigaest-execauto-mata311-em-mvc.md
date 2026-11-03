---
article_id: 33460056439191
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 8fa4199ebf100b98d3a0c3d112d32d3f6b831a2395a07f9a462c8eed40866bf3
fetched_at: '2026-06-28T22:38:55.526205+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ExecAuto MATA311 em
  MVC
type: support-article
updated_at: '2025-07-14T18:07:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33460056439191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ExecAuto-MATA311-em-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33460056426647) Tempo aproximado para leitura: **00:01:10min**  
  
**Dúvida**  
Qual o exemplo de ExecAuto da MATA311 em MVC ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Abaixo temos um exemplo do ExecAuto da MATA311 em MVC:

```
#Include 'Protheus.ch'
#include 'Parmtype.ch'

User Function MATA311()
      Local aParam   := PARAMIXB
      Local lRet     := .T.
      Local oModel311

      If aParam <> Nil 
            oModel311 := aParam[1]
            cIdPonto  := aParam[2]
            cIdModel  := aParam[3]

            IF oModel311 <> NIL .AND. cIdPonto == 'MODELPOS'
                  Alert ("Passou pelo PE!")
            EndIF
      Else
            Alert("PARAMIXB NULO!")
      EndIf 
Return (lRet)
```

**Veja também:** [Pontos de Entrada para fontes Advpl desenvolvidos utilizando o conceito MVC](https://tdn.totvs.com/x/x-1n)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
