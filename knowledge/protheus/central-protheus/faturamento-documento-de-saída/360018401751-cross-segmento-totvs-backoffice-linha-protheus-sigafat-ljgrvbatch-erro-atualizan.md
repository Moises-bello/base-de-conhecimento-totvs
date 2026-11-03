---
article_id: 360018401751
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a5e7d55bb0edc36f9c7234380a27495370c1b95bb26bed3a6ef632c4c1f3272e
fetched_at: '2026-06-28T22:38:43.882475+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - LjGrvBatch Erro
  atualizando Pedido de Venda -SC5
type: support-article
updated_at: '2023-08-15T14:49:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018401751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-LjGrvBatch-Erro-atualizando-Pedido-de-Venda-SC5
---

**Ocorrência**

LjGrvBatch: Erro atualizando Pedido de Venda (SC5).

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

O problema ocorre por falta da variável correta STR para o botão Visualiza Documento.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote do **acumulado de faturamento**, conforme a release: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859) ;**  
2. Via TDS ou Vs\_code , aplique o pacote em seu repositório de objetos;  
3. Reinicie o Smartclient e refaça o processo.

Obs: Para a aplicação de pacotes no ambiente é necessário o conhecimento em estrutura de Protheus, caso necessite apoio, acione a equipe de Framework.
