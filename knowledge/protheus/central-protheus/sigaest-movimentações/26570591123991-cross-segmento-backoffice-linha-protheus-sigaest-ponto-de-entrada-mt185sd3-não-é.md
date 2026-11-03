---
article_id: 26570591123991
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 89dde7f1b24ab52c82b99cf9ba6973e27bcc0c90dd02377f37899289f579e895
fetched_at: '2026-06-28T22:38:57.242083+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ponto de Entrada MT185SD3
  não é chamado na rotina MATA185.
type: support-article
updated_at: '2024-09-23T19:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26570591123991-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ponto-de-Entrada-MT185SD3-n%C3%A3o-%C3%A9-chamado-na-rotina-MATA185
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26570606936983) Tempo aproximado para leitura: **00:00:45 min****Dúvida**Ao utilizar o ponto de entrada MT185SD3 ele não está sendo chamado na rotina MATA185.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Conforme pode ser verificado no TDN disponibilizado sobre o Ponto de Entrada [MT185SD3](https://tdn.totvs.com/x/gNWEMw)

A chamada deste ponto se encontra na função A185AtuSD3 que está localizada na "Baixa Por Item", dessa maneira, para que o PE seja acionado, deve realizar a alteração do F12 da rotina, conforme o print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26570606940183)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
