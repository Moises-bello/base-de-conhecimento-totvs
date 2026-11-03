---
article_id: 360020639631
category: Folha Mensal
content_hash: 52228b175cab4d7e553daae009a4688566746912587424ddcb53bf8239cdd1c6
fetched_at: '2026-06-28T22:46:59.558960+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: Conferência do FGTS com a GFIP emitida pelo
  SEFIP'
type: support-article
updated_at: '2025-03-07T14:53:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020639631-RH-RM-FOP-Folha-Anal%C3%ADtica-Confer%C3%AAncia-do-FGTS-com-a-GFIP-emitida-pelo-SEFIP
---

**Dúvida**Como gerar a Folha Analítica de forma que os valores de FGTS possam ser comparados com os valores da GFIP emitida pelo SEFIP?  
  
**Ambiente**RM - Folha de Pagamento - A partir da versão 12.1  
  
**Solução**Para que os valores de FGTS da folha analítica possam ser comparados aos valores da GFIP emitida pelo SEFIP, o usuário poderá criar fórmulas de cálculo e inserir nos campos de **Fórmula** da folha analítica.   
  
As fórmulas abaixo zeram a base FGTS dos funcionários demitidos no mês com Tipo 2 e Tipo T e que tiveram o recolhimento através da GRFC. Estas são fórmulas de **exemplo** sobre como realizar esta comparação.  
  
**01.** Crie a fórmula de**Base FGTS (GFIP)**:

```
SE( (SFUNC = 'D') E ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) )  
  
  
OU  
  
( (SFUNC = 'A') E( (TABFUNC('RESCISAOCALCULADA' , 'V') = 1) ) E  
  
( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) E  
  
( (TABFUNC(' FGTSMESANTRECOLGRFP' , 'V') = 1) ) )  
  
ENTAO 0  
  
SENAO BASEFGTS  
  
FIMSE
```

**02.** Crie a fórmula **Base FGTS 13º (GFIP)**:

```
SE( (SFUNC = 'D') E ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) )  
  
OU  
  
( (SFUNC = 'A') E( (TABFUNC('RESCISAOCALCULADA' , 'V') = 1) ) E  
  
( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) E  
  
( (TABFUNC(' FGTSMESANTRECOLGRFP' , 'V') = 1) ) )  
  
ENTAO 0  
  
SENAO BSFGTS13  
  
FIMSE
```

**03.** Em seguida, acesse **Folha Mensal | Folha Analítica** avance até chegar na tela **Informações do Funcionário**, marque a Fórmula 1 e Fórmula 2 e no campo **Resumo Funcionário - Fórmulas** insira as fórmulas que criou anteriormente.   
  
Veja como ficará na imagem abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016624891/mceclip1.png)  
  
**04.** Finalize a geração da folha analítica e verifique no relatório gerado que o sistema irá levar as fórmulas como campos do relatório:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016541452/mceclip1.png)
