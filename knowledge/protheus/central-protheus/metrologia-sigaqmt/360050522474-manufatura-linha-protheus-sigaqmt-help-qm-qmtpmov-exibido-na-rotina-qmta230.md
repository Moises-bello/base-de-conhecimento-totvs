---
article_id: 360050522474
category: Metrologia (SIGAQMT)
content_hash: 5b512bdf41e0b4e690d8f2e1034eb68a09fdff99a7638fa948c75d4e263f9e59
fetched_at: '2026-06-28T22:42:24.790093+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Help QM_QMTPMOV exibido na rotina QMTA230
type: support-article
updated_at: '2021-08-10T16:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050522474-Manufatura-Linha-Protheus-SIGAQMT-Help-QM-QMTPMOV-exibido-na-rotina-QMTA230
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao acessar a rotina **QMTA230 -** **Movimento de Instrumentos Entre Filiais** é apresentado o *help* **QM\_QMTPMOV**, impedindo a utilização desta rotina.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Esse *help* ocorre quando o parâmetro **MV\_QMTPMOV - Define o tipo de movimentação a ser realizada no QMT** está com conteúdo igual à **1**.  
Este parâmetro aceita as opções:

1. Movimento entre **Departamentos** de uma **Filial**
2. Movimento entre outras **Filiais**

**Solução**Somente é possível utilizar a rotina **QTMA230** quando o parâmetro **MV\_QMTPMOV** estiver com conteúdo igual à **2**, indicando que a transferência do instrumento será entre **Filiais**.  
Para realizar a transferência do instrumento entre **Departamentos** da mesma **Filial**, ou seja, com o parâmetro **MV\_QMTPMOV** com conteúdo igual à **1** é necessário utilizar a rotina **QMTA160 - Movimentações**.
