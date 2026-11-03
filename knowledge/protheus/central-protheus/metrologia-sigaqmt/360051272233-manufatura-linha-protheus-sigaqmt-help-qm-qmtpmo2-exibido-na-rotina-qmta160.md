---
article_id: 360051272233
category: Metrologia (SIGAQMT)
content_hash: 71d2b05120eae1b4789ccb825889504713c38182dc8856b3e2546b577371a1ec
fetched_at: '2026-06-28T22:42:24.783897+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Help QM_QMTPMO2 exibido na rotina QMTA160
type: support-article
updated_at: '2021-08-10T16:46:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051272233-Manufatura-Linha-Protheus-SIGAQMT-Help-QM-QMTPMO2-exibido-na-rotina-QMTA160
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao acessar a rotina **QMTA160 -** **Movimentações** é apresentado o *help* **QM\_QMTPMO2**, impedindo a utilização desta rotina.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Esse *help* ocorre quando o parâmetro **MV\_QMTPMOV - Define o tipo de movimentação a ser realizada no QMT** está com conteúdo igual à **2**.  
Este parâmetro aceita as opções:

1. Movimento entre **Departamentos** de uma **Filial**
2. Movimento entre outras **Filiais**

**Solução**Somente é possível utilizar a rotina **QTMA160** quando o parâmetro **MV\_QMTPMOV** estiver com conteúdo igual à **1**, indicando que a transferência do instrumento será **Departamentos** da mesma **Filial**.  
Para realizar a transferência do instrumento entre **Filiais**, ou seja, com o parâmetro **MV\_QMTPMOV** com conteúdo igual à **2** é necessário utilizar a rotina **QMTA230 - Movimento de Instrumentos Entre Filiais**.
