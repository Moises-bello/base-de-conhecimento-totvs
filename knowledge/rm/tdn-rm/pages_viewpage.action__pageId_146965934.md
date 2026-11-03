---
content_hash: a4ef3074593a8c6820e9f6a7b30ead18c290a4e4527d7cd8ae961abadc379155
fetched_at: '2026-06-29T00:05:55.867049+00:00'
page_id: '146965934'
product: rm
source: tdn-rm
title: Como faço pra gerar a Folha Analítica de forma que os valores de FGTS possam
  conferir com os valores da GFIP emitida pelo SEFIP?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146965934
version: 2
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Como faço pra gerar a Folha Analítica de forma que os valores de FGTS possam conferir com os valores da GFIP emitida pelo SEFIP?** |
| Solução | Para que os valores de FGTS da folha analítica possam conferir com os valores da GFIP emitida pelo SEFIP, o usuário poderá criar as fórmulas abaixo e inserir nos campos de bases de eventos campo 'Fórmula 1' e 'Fórmula 2' da folha analítica. As fórmulas abaixo zeram a base FGTS dos funcionários demitidos no mês, tipo 2 e tipo T e que tiveram o recolhimento através da GRFC.    Criar a fórmula : **Base FGTS (GFIP)**    SE( (SFUNC = 'D') E ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) )    OU    ( (SFUNC = 'A') E( (TABFUNC('RESCISAOCALCULADA' , 'V') = 1) ) E    ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) E    ( (TABFUNC(' FGTSMESANTRECOLGRFP' , 'V') = 1) ) )    ENTAO 0    SENAO BASEFGTS    FIMSE       Criar a fórmula : **Base FGTS 13º (GFIP)**    SE( (SFUNC = 'D') E ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) )    OU    ( (SFUNC = 'A') E( (TABFUNC('RESCISAOCALCULADA' , 'V') = 1) ) E    ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) E    ( (TABFUNC(' FGTSMESANTRECOLGRFP' , 'V') = 1) ) )    ENTAO 0    SENAO BSFGTS13    FIMSE |
