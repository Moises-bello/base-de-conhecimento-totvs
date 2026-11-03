---
article_id: 13607255595159
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 80577df9266fd9b24d05aa68a7b2bfe8496cf0d85246aa5922fc523d22385136
fetched_at: '2026-06-28T22:38:57.126905+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 -
  É possível inserir Lote na Transferência para produtos que não controlam lote?
type: support-article
updated_at: '2023-04-04T12:53:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13607255595159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-%C3%89-poss%C3%ADvel-inserir-Lote-na-Transfer%C3%AAncia-para-produtos-que-n%C3%A3o-controlam-lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:34 min** **Dúvida**Ao efetuar uma Transferência entre Filiais, é possível inserir o campo de Lote para produtos que não controlam rastreabilidade por lote/sublote?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Nas rotinas de Transferência entre Filiais  (MATA310 e MATA311) o fonte das mesmas faz validação se o produto envolvido está com sua configuração de rastreabilidade (B1\_RASTRO) igual à N (não controla) ou L/S (Lote/Sublote).

**Sendo N, ele automaticamente inibe o campo de preenchimento para o usuário para que não dê margem do Sistema quebrar a integridade gerando registro indevido na tabela de Saldos por Lote (SB8) e Movimentos por Lote (SD5) na hora de transferir**. Este é o comportamento padrão e entendido como o correto, não dispondo de configurações padrões que habilitem ao usuário preencher lote quando o produto não controla lote, por mais que haja algum controle interno do usuário/empresa.  
 

Portanto, via MATA310 ou MATA311, nos padrões das rotinas, na MATA310 o campo não permite preenchimento, e na MATA311 ao teclar o F4 de um produto que não controla rastro ocorre help:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13607190526487)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
