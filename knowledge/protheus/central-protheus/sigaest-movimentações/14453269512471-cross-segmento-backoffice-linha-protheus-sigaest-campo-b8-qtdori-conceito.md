---
article_id: 14453269512471
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f1485811744bb00bb630313e63beafb51248a6277b4213228c82faa68ddd8fa7
fetched_at: '2026-06-28T22:38:54.336993+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo B8_QTDORI conceito '
type: support-article
updated_at: '2023-05-09T11:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14453269512471-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-B8-QTDORI-conceito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual o conceito do campo ***B8\_QTDORI*** na ***tabela SB8***?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**O campo **B8\_QTDORI** armazena a quantidade que **originou o Lote** do produto. É atualizado apenas na **primeira movimentação** de entrada do Saldo do Lote. Diferente do campo **B8\_SALDO** que é atualizado com o "Saldo Atual" por Lote sempre que movimentado o mesmo.  
   
***Exemplo:*** Foi incluído um Documento de entrada com quantidade 100 unidades do produto e determinado Lote (Novo). O sistema atualizará os dois campos com quantidade 100. A medida que o saldo for consumido, o sistema baixa o saldo somente do campo **B8\_SALDO** e mantém a quantidade original **B8\_QTDORI**.  
  
Da mesma forma acontece se incluir mais quantidade para o mesmo Lote, o sistema atualizará somente o campo **B8\_SALDO**, mantendo o campo **B8\_QTDORI** com a quantidade original.

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)
