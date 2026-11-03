---
article_id: 28680105336343
category: ADVPL - Classe e Função
content_hash: 7617b4e067e5b75867d42dd3aaa016c59d197ec1ac7fcba6e3d4348877e180b6
fetched_at: '2026-06-28T22:40:21.600287+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível criar
  uma tabela que seja compartilhada entre Threads?
type: support-article
updated_at: '2024-12-20T14:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28680105336343-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-criar-uma-tabela-que-seja-compartilhada-entre-Threads
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28680134784791)Tempo aproximado para leitura: **00:01:00 min****Dúvida**É possível criar uma tabela que seja compartilhada entre Threads?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – a partir da versão 12.1.2210  
  
**Solução**Para essa necessidade existe a classe **totvs.framework.database.temporary.SharedTable** no qual permite criar uma tabela temporária compartilhada entre as threads.

Essa classe assemelha-se com a **FWTemporaryTable**, mas com o diferencial de permitir que outras threads possam ver e trabalhar na tabela criada.

**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE "FWLIBVERSION.CH"  
#INCLUDE "TOPCONN.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function ExFWTemporaryTable()  
Local aFields := {}  
Local oTempTable1  
Local cAlias := "ATESTE"  
  
oTempTable1 := totvs.framework.database.temporary.SharedTable():New( cAlias )  
  
aadd(aFields,{"DESCR","C",30,0})  
aadd(aFields,{"CONTR","N",3,1})  
aadd(aFields,{"ALIAS","C",3,0})  
  
oTemptable1:SetFields( aFields )  
  
oTempTable1:Create()  
conout(oTempTable1:GetRealName())  
  
Return
```

**Saiba mais**  
[totvs.framework.database.temporary.SharedTable](https://tdn.totvs.com.br/display/public/framework/totvs.framework.database.temporary.SharedTable)

[FWTemporaryTable](https://tdn.totvs.com.br/display/public/framework/FWTemporaryTable)
