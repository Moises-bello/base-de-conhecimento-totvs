---
article_id: 360050562754
category: ADVPL - Relatório
content_hash: 83ba76327832f2992c53a4e18c5cf08a7e50c806182ac3e1882447a3176a0858
fetched_at: '2026-06-28T22:40:22.946075+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Treport gerar arquivo
  .REL
type: support-article
updated_at: '2021-12-30T19:17:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050562754-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Treport-gerar-arquivo-REL
---

**Dúvida**Como gerar um arquivo **.REL** com a Classe **Treport**  
  
**Ambiente**Protheus – ADVPL – A partir da versão P12.1.17  
  
**Solução**

A classe **TReport**não tem uma parametrização em especifico para gerar o arquivo **.Rel**.

Exemplo relatório **TReport** gerando arquivo **.REL**

```
#include "protheus.ch"  
#include "rptdef.ch"  
#define EMPRESA "99"  
#define FILIAL "01"  
  
//-------------------------------------------------------------------  
  
/*{Protheus.doc} u_CallReport  
Chama a impressão de relatório em outra thread, ficando assim um  
job sem interface  
  
*/  
  
//-------------------------------------------------------------------  
  
function u_CallReport()  
StartJob("u_mySED_Report", getEnvServer(), .T.)  
  
return nil  
  
//-------------------------------------------------------------------  
  
/*{Protheus.doc} u_mySED_Report  
Função para testes da classe TReport, exportando PDF e .REL  
  
*/  
  
//-------------------------------------------------------------------  
  
user function mySED_Report()  
  
local oReport as object  
local oSection as object  
local cAlias as char  
local cTitle as char  
local cFile as char  
rpcSetEnv(EMPRESA, FILIAL)  
cAlias := "SED"  
cTitle := "Naturezas"  
cFile := "SED_Nat"  
oReport := TReport():New(cFile, cTitle, /*uParam*/, {|oReport| oSection:print()} )  
oSection := TRSection():New(oReport, cTitle, cAlias, /*aOrder*/, .T.)  
oReport:lPreview:= .F.  
oReport:setFile(cFile)  
oReport:nDevice := IMP_PDF  
oReport:nEnvironment:= 1 // 1 -Server / 2- Cliente  
oReport:nRemoteType:= NO_REMOTE  
//oReport:printDialog(, cAlias)  
oReport:print()  
FreeObj(oReport)  
FreeObj(oSection)  
rpcClearEnv()  
  
return nil
```

Saiba mais:

[TReport](https://tdn.totvs.com/display/public/PROT/TReport)
