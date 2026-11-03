---
article_id: 38213810807831
category: Inspeção de Processos (SIGAQIP)
content_hash: 1bde579db1c3f9797f12d7298f282222ed163ba9ecd4f149b475e385270a7e19
fetched_at: '2026-06-28T22:42:25.794072+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QTD-REJ-INV
type: support-article
updated_at: '2026-02-06T13:43:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38213810807831-Manufatura-Linha-Protheus-SIGAQIP-Help-QTD-REJ-INV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38213810796183) Tempo aproximado para leitura: **00:00:45 min**  
  
**Ocorrência**  
Na rotina **QIPA215 - Resultados**, na pasta **Baixas do CQ,** ao tentar incluir uma movimentação rejeitada ocorre o **help QTD-REJ-INV Problema: Rejeição acima da permitida.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**  
O **help** **QTD-REJ-INV** ocorre quando há **divergência no tamanho de campos** relacionados à quantidade, ou quando o **valor rejeitado não foi incluído na aba Laudo Geral**, no campo **Quantidade Rejeitada - QPL\_QTREJ**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se os **tamanhos de campos** estão equivalentes e seguindo a **regra ao final da documentação** [Baixas do CQ (QIPA215 - SIGAQIP)](https://tdn.totvs.com/pages/releaseview.action?pageId=742224954);  
2. Verifique se na aba **Laudo Geral** se no campo **Quantidade Rejeitada - QPL\_QTREJ** foi informado a quantidade a ser rejeitado. Conforme documentação [Integração com Estoque - Aba Baixas do CQ](https://tdn.totvs.com/pages/releaseview.action?pageId=742224643) **é pressuposto informar** neste campo a **quantidade rejeitada** para poder realizar a **movimentação de rejeição** na aba Baixas do CQ.
