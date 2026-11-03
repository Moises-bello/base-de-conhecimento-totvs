---
article_id: 20341148594455
category: PMS - Projetos
content_hash: 27a29b473fb723a19629955795a02a4083c523cc1e5a68f647c08d6451e04c12
fetched_at: '2026-06-28T22:37:15.956097+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Ponto de Entrada PMA110INC
type: support-article
updated_at: '2024-02-26T18:07:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20341148594455-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Ponto-de-Entrada-PMA110INC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20341148587159) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como usar o Ponto de Entrada PMA110INC?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

Esse ponto de entrada ocorre após a confirmação dos perguntes na rotina "PMSA110 - Preparar projetos", ele pode deixar o projeto ser gerado a partir do orçamento ou a partir de algum pergunte bloqueá-lo.

**Exemplo de uso:**

```
#INCLUDE 'PROTHEUS.CH'
#INCLUDE 'PRTOPDEF.CH'

User Function PMA110INC()
    Local nA := 1
    Local nB := 2
    Local lRet := .T.  // Não gera projeto (True)  

    If (nA < nB)  
        lRet := .F. // Gera projeto (False)  
    EndIf  
Return(lRet)
```

**Saiba mais:**

[**PMA110INC - Cancela geração de projeto**](https://tdn.totvs.com/x/t69n)
