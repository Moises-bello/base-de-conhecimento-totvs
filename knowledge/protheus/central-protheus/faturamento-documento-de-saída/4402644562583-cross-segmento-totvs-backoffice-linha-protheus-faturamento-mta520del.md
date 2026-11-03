---
article_id: 4402644562583
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 36f095ef519f8ddc7a094ab84a0dbcd9d79d389a69d1b0152873f3a082c0de45
fetched_at: '2026-06-28T22:38:43.816477+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - MTA520DEL
type: support-article
updated_at: '2021-06-14T11:49:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402644562583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-MTA520DEL
---

**Dúvida**Do que se trata o Help MTA520DEL?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento- Todas as versões  
  
**Solução**

O help ocorre para pedidos (**Mata410**) que tiveram integração com o SIGAEEC, onde está verificando os embarques do modulo de exportação - SIGAEEC para poder excluir a nota.

A validação consiste em verificar se o módulo é diferente do módulo 29, se a função do EEC , **EECFat2NFEst** não foi encontrada e se o campo **D2\_PREEMB** não está vazio ou se função  EECFat2NFEst foi encontrada e se a Nota pode ser excluída, quando o Pedido relacionado estiver na  **fase de embarque**, verificando se a nota foi comparada ou não com o embarque informado .

Lembrando que somente os pedidos de origem do SIGAECC trazem a informação de embarque diretamente para preenchimento do campo D2\_PREEMB no momento do faturamento, para pedidos de exportação com origem direto do SIGAFAT, é necessário efetuar o complemento de exportação em Livros Fiscais.
