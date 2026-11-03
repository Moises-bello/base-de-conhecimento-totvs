---
article_id: 8187853425815
category: ADVPL - Classe e Função
content_hash: db2315bab135102edfc72be5e5ceedc0cd1d1bcd0055670ca302bb3cf2f7aa69
fetched_at: '2026-06-28T22:40:20.747187+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Funções de tela
  de carregamento
type: support-article
updated_at: '2022-08-15T17:34:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8187853425815-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%B5es-de-tela-de-carregamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais classes que apresentam uma tela de carregamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Segue abaixo uma lista contendo nome da classe/função que geram uma tela de carregamento.  
  
**FWMsgRun()**Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8186741777943/mceclip0.png)  
  
**TMeter()**Exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8186874364823/mceclip2.png)  
  
**Processa()**Exemplo:

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8187498380439/mceclip6.png)  
  
Customizada**Caso deseje montar manualmente uma tela para carregamento segue abaixo um exemplo:

```
#include 'totvs.ch'   
#include 'sigawin.ch'   
User Function MeuAguarde()    
Local oDlg    
Local lEnd := .f.    
DEFAULT lAbort := .f.    
DEFAULT cMsg := OemToAnsi("Processando..."), cTitle := OemToAnsi("Aguarde") //"Processando..." ### "Aguarde"    
DEFINE MSDIALOG oDlg FROM 12,35 TO 19.5, 75 TITLE OemToAnsi(cTitle)       
@ 10, 20 SAY oText VAR OemToAnsi(cMsg) SIZE 130, 10 PIXEL OF oDlg FONT oDlg:oFont    
ACTIVATE DIALOG oDlg VALID lEnd CENTERED   
Return nil
```

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8187219270551/mceclip3.png)

**Saiba Mais**[**FWMsgRun()**](https://tdn.totvs.com/display/public/framework/FWMsgRun)  
[**TMeter()**](https://tdn.totvs.com/display/tec/TMeter)  
[**Processa()**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888204707863)
