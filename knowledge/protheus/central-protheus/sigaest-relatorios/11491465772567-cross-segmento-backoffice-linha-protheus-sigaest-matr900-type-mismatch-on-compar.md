---
article_id: 11491465772567
category: SIGAEST - RELATORIOS
content_hash: d1827d4f351eab51fbadd6ce126db49febf0051f108decf173497f5134167d43
fetched_at: '2026-06-28T22:39:06.199285+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - type mismatch
  on compare  on REPORTPRINT(MATR900.PRX)
type: support-article
updated_at: '2023-01-06T19:25:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11491465772567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-type-mismatch-on-compare-on-REPORTPRINT-MATR900-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar emitir o relatório KARDEX POR PERÍODO (MATR900) apresenta o error.log ***"type mismatch on compare on REPORTPRINT(MATR900.PRX) 20/09/2021 10:12:24 line : 349"*** como corrigi-lo?.

type mismatch on compare on REPORTPRINT(MATR900.PRX) 20/09/2021 10:12:24 line : 349

[TOTVS build: 7.00.210324P-20211006]  
Called from {|OREPORT| REPORTPRINT(OREPORT)}(MATR900.PRX) 20/09/2021 10:12:24 line : 99  
Called from {|| IIF(SELF:INIT(),(LACTION := EVAL(SELF:BACTION,SELF),SELF:FINISH()),LOK:= .F. ),LEND := .T. ,ODLG:END()}(REPORT01.PRW) 12/11/2021 14:43:23 line : 2184  
Called from ::MSDIALOG:ACTIVATE  
Called from TREPORT:PRINT(REPORT01.PRW) 12/11/2021 14:43:23 line : 2197  
Called from TREPORT:PRINTDIALOG(REPORT01.PRW) 12/11/2021 14:43:23 line : 3442  
Called from MATR900(MATR900.PRX) 20/09/2021 10:12:24 line : 20  
Called from \_\_EXECUTE(APLIB090.PRW) 12/11/2021 14:43:23 line : 721  
Called from FWPREEXECUTE(FWPREEXECUTE.PRW) 12/11/2021 14:43:29 line : 86  
Called from {|| FWPreExecute('Por Período', 'MATR900()', 1, '04', 'xxxxxxxxxx') }(FWUIMENUL.PRW) 12/11/2021 14:43:29 line : 197  
Called from ::TWINDOW:ACTIVATE  
Called from MSAPP:ACTIVATE(FWAPP.PRW) 12/11/2021 14:43:28 line : 755  
Called from SIGAADV(APLIB000.PRW) 12/11/2021 14:43:23 line : 71

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Esse incidente geralmente ocorre, devido ausência da pergunta 17 do parâmetro, veja abaixo com corrigir.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

***1.*** Verificando no fonte do MATR900 na linha 349 exibe a necessidade da pergunta para impressão do relatório;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11491818933911)

***2.*** Acessar o módulo Configurador em Base de Dados / Dicionário / Base de Dados e posicionar em Perguntas e pesquisar pelo grupo de perguntas MTR900;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11492001247383)

***3.*** Editar o grupo de Perguntas para inclusçao da Pergunta 17

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11492039194135)

***2.*** Incluir uma linha a mais com os conteúdos como do print abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11492135445527)

Após esse procedimento não exibirá amis o error.log

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
