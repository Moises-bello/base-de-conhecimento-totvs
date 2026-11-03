---
article_id: 21986852116375
category: ADVPL - Classe e Função
content_hash: bf64be054c7302edb70d0fd1c4d5bc3d79fe9b8b51997f3868eb595be798f662
fetched_at: '2026-06-28T22:40:18.257231+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL-  Função para obter
  o help de determinado campo?
type: support-article
updated_at: '2024-03-11T19:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21986852116375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-obter-o-help-de-determinado-campo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21986852085911) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Existe função pata obter o help de determinado campo?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**

Para tal, existe a função GetHlpSoluc no qual é possível resgatar informação de help de determinado campo.

```
#include "protheus.ch"  
User Function GetHelpSol()  
Local aHelp := GetHlpSoluc("A1_NOME")  
Local cTexto := ""  
  
cTexto := "Help de Problema: " + aHelp[1] + CHR(13)+CHR(10)+"Help de Solução: "+ aHelp[2]  
  
ApMsgInfo(cTexto)  
  
Return
```

**Saiba Mais**

[GetHlpSoluc](https://tdn.totvs.com/pages/releaseview.action?pageId=6814930)
