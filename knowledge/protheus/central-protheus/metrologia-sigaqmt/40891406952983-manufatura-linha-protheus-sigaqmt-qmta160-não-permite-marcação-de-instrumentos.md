---
article_id: 40891406952983
category: Metrologia (SIGAQMT)
content_hash: 557d99147c918d0d1e597eea8ddf4b82b7b0851d5d8439edeb6b2b100619d6ac
fetched_at: '2026-06-28T22:42:24.873402+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA160 - Não permite marcação de instrumentos
type: support-article
updated_at: '2026-06-01T20:00:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40891406952983-Manufatura-Linha-Protheus-SIGAQMT-QMTA160-N%C3%A3o-permite-marca%C3%A7%C3%A3o-de-instrumentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40891406921111) Tempo aproximado para leitura: **00:00:45 min**  
  
**Ocorrência**  
Na rotina **QMTA160 - Movimentação**, ao realizar o filtro e trazer o instrumento, o **Sistema não permite marcar** o instrumento. Como proceder?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**  
A situação ocorre quando a na rotina **QMTA030 - Cadastro de Famílias de Instrumentos** o campo **Controla Movimentação** está marcado como **Não**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **QMTA030** e selecione o cadastro relacionado ao instrumento;  
2. Altere o campo **Controla Movimentação? - Cont. Movim. de N-Não para S - Sim;**  
3. Preencha os campos **Control. Val, Depto. Distr. e Resp.Distr;**  
4. Salve a alteração realizada;  
5. Acesse a rotina **QMTA160** para liberar o instrumento.
