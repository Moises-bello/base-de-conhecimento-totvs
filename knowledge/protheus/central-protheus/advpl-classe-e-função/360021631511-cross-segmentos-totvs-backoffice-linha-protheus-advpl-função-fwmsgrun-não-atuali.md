---
article_id: 360021631511
category: ADVPL - Classe e Função
content_hash: d736daac27fd6120b0b721d9a42d5b479c189068e5153271dc91fb36d6401eb3
fetched_at: '2026-06-28T22:40:19.352384+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função Fwmsgrun
  não atualiza as mensagens em tempo de execução
type: support-article
updated_at: '2024-01-31T10:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021631511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Fwmsgrun-n%C3%A3o-atualiza-as-mensagens-em-tempo-de-execu%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Na documentação da função FwMsgRun() consta a seguinte afirmativa: "permite atualizar o texto em tempo de execução", todavia ao utilizar as propriedades cTitle, cCaption ou o método SetText(), a caixa de diálogo não está sendo atualizada.  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**A não atualização ocorre pelo congelamento do SmartClient durante a execução de um processo longo.  
  
**Solução**Utilizar a função ProcessMessages().  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PRINCIPAL  
User function T151FWMSG()  
    Local oSay := NIL // CAIXA DE DIÁLOGO GERADA  
  
    // GERA A TELA DE PROCESSAMENTO  
    FwMsgRun(NIL, {|oSay| RunMessage(oSay)}, "Processing", "Starting process...")  
Return (NIL)  
  
// FUNÇÃO PARA ALTERAÇÃO DA MENSAGEM  
Static Function RunMessage(oSay)  
    Local nX := 0 // CONTROLE CONTADOR DO LAÇO  
  
    // SIMULA A PREPARAÇÃO PARA EXECUÇÃO  
    Sleep(2000)  
  
    // LAÇO COM PAUSA DE UM SEGUNDO PARA SIMULAÇÃO  
    For nX := 1 To 10  
        oSay:SetText("Working at: " + StrZero(nX, 6)) // ALTERA O TEXTO CORRETO  
        ProcessMessages() // FORÇA O DESCONGELAMENTO DO SMARTCLIENT  
  
        Sleep(1000) // SIMULA O PROCESSAMENTO DA FUNÇÃO  
    Next nX  
Return (NIL)
```

**Saiba mais**[FWMsgRun](http://tdn.totvs.com/display/PROT/FWMsgRun)  
[ProcessMessage](https://tdn.totvs.com/display/tec/ProcessMessages)
