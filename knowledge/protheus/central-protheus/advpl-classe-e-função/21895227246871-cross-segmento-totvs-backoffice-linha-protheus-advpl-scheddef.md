---
article_id: 21895227246871
category: ADVPL - Classe e Função
content_hash: 1188ec00ee83fd90fefb20c9f4d68eb1cdd16941da7aa26d210713d42a873563
fetched_at: '2026-06-28T22:40:17.993578+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - SchedDef
type: support-article
updated_at: '2024-03-08T18:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21895227246871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-SchedDef
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21895227236119) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Qual a diferença do SchedDef em Schedule?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Soluções**

Através do *SchedDef*, ele irá abrir o ambiente automaticamente conforme informado no cadastro do schedule e também permitirá a chamada de perguntas (SX1) ao cadastrar a tarefa no Schedule, desta forma caso a função possua parâmetros, deve enviar os parâmetros da rotina/função pela pergunta.  
  
**Exemplos**

```
#include "totvs.ch"  
  
User Function TestSched()  
  
    Conout("Acesso: " + CACESSO)  
    Conout("Empresa logada: " + cEmpAnt )  
    Conout("Filial logada: "+ cFilAnt)  
  
    cSepar := ":"  
    cHora := SubStr(Time(), 1, 5)  
    cHora := StrTran(cHora, ':', cSepar)  
    Conout("Schedule executado! ",+ dtoc(date())+ "Hora: "+ cHora)  
  
Return  
  
Static Function SchedDef()  
    Local aOrd :={}  
    Local aParam:={}  
  
    aParam := { "R",;   //Tipo R para relatorio P para processo  
    "ParamDef",  ;      // Nome do pergunte do relatorio, caso nao use passar ParamDef  
    "",         ;       // Alias  
    aOrd,       ;       //Array de ordens  
    }  
Return aParam
```

**Observação**

Para o SchedDef ser chamado o nome do fonte terá que ser o mesmo nome que o da função, neste caso seria TestSched.prw

**Saiba Mais**

[SchedDef](https://tdn.totvs.com/pages/releaseview.action?pageId=36800166)
