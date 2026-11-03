---
article_id: 22836290927511
category: Materiais - Compras (SIGACOM)
content_hash: 493611c7894f42fb29b93713f527ac334fde2948abd83dfa508fefe960ed0120
fetched_at: '2026-06-28T22:41:11.492358+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Ponto de Entrada A140ICOND
type: support-article
updated_at: '2024-04-19T17:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22836290927511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Ponto-de-Entrada-A140ICOND
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22836278642583) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Como utilizar o ponto de Entrada A140ICOND?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS- Todas as versões  
  
**Solução**

Ao gerar a Pré-Nota/doc de Entrada no Importador (monitor),  o sistema valida se a condição de pagamento está vinculada ao pedido de compras ou ao cadastro de Fornecedor. Essa validação é realizada considerando se uma TES foi informada na linha do produto, com a configuração para gerar duplicatas (F4\_DUPLIC = SIM).

**OBSERVAÇÃO:** Se não for digitada uma TES ou se a TES estiver configurada para não gerar duplicatas, a condição de pagamento não será acionada durante este processo.

Se desejar utilizar uma condição de pagamento diferente das disponíveis nos cadastros mencionados, é possível utilizar o ponto de entrada A140ICOND. No entanto, este ponto de entrada também depende da configuração da TES para gerar duplicata.

![TOTVS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22836790819991)

Saiba mais em :

[TC02016 - A140ICOND - Ponto que permite alterar e validar a condição de pagamento no monitor do Totvs Colaboração.](https://tdn.totvs.com/pages/releaseview.action?pageId=505755731)

[Ponto de entrada - Totvs Colaboração](https://tdn.totvs.com/pages/releaseview.action?pageId=284475658)
