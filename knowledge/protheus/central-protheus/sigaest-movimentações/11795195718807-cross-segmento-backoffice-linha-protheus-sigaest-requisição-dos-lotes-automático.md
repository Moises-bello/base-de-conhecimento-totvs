---
article_id: 11795195718807
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d2652e5ea9272690083674b01aaf0ceb51d4624ede50a40d1bf6c57062e841ba
fetched_at: '2026-06-28T22:38:58.457946+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -Requisição dos Lotes
  automáticos é possível alterar a sequência?
type: support-article
updated_at: '2026-04-06T21:37:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11795195718807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Requisi%C3%A7%C3%A3o-dos-Lotes-autom%C3%A1ticos-%C3%A9-poss%C3%ADvel-alterar-a-sequ%C3%AAncia
---

No TOTVS Protheus, a sequência automática de requisição dos lotes segue o critério FEFO (primeiro que vence, primeiro a sair). Para alterar essa ordem, é necessário utilizar o Ponto de Entrada MTSLDORD, conforme documentação oficial da TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38536848743703) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível alterar a sequência automática de requisição dos Lotes?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Custos - Todas as versões.  
  
**Solução**  
No Protheus padrão a sequência de requisição automática respeita o Lote que vence primeiro (FEFO), ou seja, consumindo a data de validade mais perto de vencer. Caso a data de valide dos lotes sejam a mesma, ele irá considerar em ordem alfanumérica.

**Caso precisar alterar esse comportamento, somente é possível através do Ponto de Entrada MTSLDORD**. Veja abaixo documentação do Ponto de Entrada.

**MTSLDORD - Alteração da sequência de requisição de lote**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6087842>

***Saiba Mais:***

[*SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
