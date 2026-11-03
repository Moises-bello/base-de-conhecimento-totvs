---
article_id: 360049503954
category: ADVPL - Relatório
content_hash: 7856fb8d196c95dba09595e6ae157fd5bda651813d0c2ea154ee9e19b06d9031
fetched_at: '2026-06-28T22:40:22.901238+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Salvar relatório
  Treport .PDF em diretório
type: support-article
updated_at: '2024-04-24T22:06:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049503954-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Salvar-relat%C3%B3rio-Treport-PDF-em-diret%C3%B3rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como podemos salvar relatório TReport em um diretório?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Solução**

Os relatórios somente são impressos respeitando o diretório presente no parâmetro **MV\_RELT**

Abaixo um exemplo que efetua a impressão via *Job* dentro da pasta *SPOOL*, pois meu parâmetro **MV\_RELT** está definido esse diretório.

```
#include "protheus.ch"  
#include "rptdef.ch"  
  
#define EMPRESA "99"  
#define FILIAL "01"  
  
//-------------------------------------------------------------------  
//Chama a impressão de relatório em outra thread, ficando assim um  
//job sem interface  
//-------------------------------------------------------------------  
function u_CallReport()  
  StartJob("u_mySED_Report", getEnvServer(), .T.)  
return nil  
  
//-------------------------------------------------------------------  
//Função para testes da classe TReport, exportando PDF*/  
//-------------------------------------------------------------------  
function u_mySED_Report()  
  local oReport  as object  
  local oSection as object  
  local cAlias   as char  
  local cTitle   as char  
  local cFile    as char  
  
  rpcSetEnv(EMPRESA, FILIAL)  
  
  cAlias := "SED"  
  cTitle := "Naturezas"  
  cFile := "SED_Nat"  
  oReport := TReport():New(cFile, cTitle, /uParam/, {|oReport| oSection:print()} )  
  oSection := TRSection():New(oReport, cTitle, cAlias, /aOrder/, .T.)  
  
  oReport:setFile(cFile)  
  oReport:nDevice := IMP_PDF  
  oReport:printDialog(, cAlias)  
  
  FreeObj(oReport)  
  FreeObj(oSection)  
  
  rpcClearEnv()  
return nil
```

**Saiba mais**  
[TReport](https://tdn.totvs.com/display/public/PROT/TReport)
