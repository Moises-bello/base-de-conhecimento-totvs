---
article_id: 360024784414
category: Metrologia (SIGAQMT)
content_hash: e63ad69f3fa95d5f9cc614c6f469292c5752b844f758fe040574a06235bfe6ef
fetched_at: '2026-06-28T22:42:24.799197+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Help RECNO - Não existem registros
  no arquivo em pauta
type: support-article
updated_at: '2021-08-10T16:49:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024784414-Manufatura-Linha-Protheus-SIGAQMT-Help-RECNO-N%C3%A3o-existem-registros-no-arquivo-em-pauta
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min**  
**Ocorrência**No módulo **SIGAMQT - Metrologia**, ao tentar realizar a retirada na rotina **QMTA160 - Mov. de Instrumentos** ocorre a mensagem **Help: RECNO Problema: Não existem registros no arquivo em pauta**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Esta mensagem ocorre quando a quantidade de dias informada no campo **Dias p/****Devolução** nos parâmetros da opção **Retirada** é inferior ao somatório da data base mais a data de validade de calibração.  
  
**Solução**Para que seja possível realizar a retirada do instrumento é necessário que a data do campo **Val. Calibr.** da rotina **QMTA010 - Instrumentos** seja maior ou igual que a data base somada aos dias informados no campo **Dias p/ Devolução.**
