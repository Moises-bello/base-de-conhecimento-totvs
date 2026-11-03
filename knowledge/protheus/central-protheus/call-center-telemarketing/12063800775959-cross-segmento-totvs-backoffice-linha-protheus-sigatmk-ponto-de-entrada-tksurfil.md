---
article_id: 12063800775959
category: Call Center - Telemarketing
content_hash: b54606eb7946e84a490154a1da8b72038189a061f94e8e8719f2ed6ffea4b2c7
fetched_at: '2026-06-28T22:41:29.455287+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada
  TKSURFIL
type: support-article
updated_at: '2023-01-31T13:33:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12063800775959-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TKSURFIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **TKSURFIL - Customização das ações**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Permite a customização das **ações que serão exibidas** para o operador pela **Consulta Padrão de ações do atendimento call center**.

O Array aItems é um array com as seguintes caracteristicas:

aItems[N][1] := Contém o código da solução (UR\_CODSOL)

aItems[N][2] := Contém a descrição da solução (UR\_DESC)

aItems[N][3] := Contém o ID do tree (UR\_IDTREE)

aItems[N][4] := Contém o ID do código (UR\_IDCODE)

aItems[N][5] := Reservado para o nome do responsável

aItems[N][6] := Reservado para o e-mail do responsável

**Exemplo**

```
User Function TKSURFIL()  
  
    Local aRet := {}         
  
    Alert("Passou pelo PE TKSURFIL")  
  
    If Len(ParamIXB[1]) > 0  
        //Filtra a ação do campo UD_SOLUCAO e exibe somente a primeira ação  
        aRet := {ParamIXB[1][1]}  
    EndIf        
  
Return aRet
```

**Saiba Mais**

**[TKSURFIL - Customização das ações](https://tdn.totvs.com/x/6pJn)**
