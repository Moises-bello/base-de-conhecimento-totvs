---
article_id: 24856642901911
category: Financeiro - Compensação Contas a Pagar
content_hash: 7679366d2d6bc4735ec5e2e6deec1d34c5eddf33a0f755071e9f0a1059b7da3c
fetched_at: '2026-06-28T22:37:33.642663+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como vincular um título
  a uma nota fiscal lançada após sua criação
type: support-article
updated_at: '2025-11-13T20:17:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24856642901911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-vincular-um-t%C3%ADtulo-a-uma-nota-fiscal-lan%C3%A7ada-ap%C3%B3s-sua-cria%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24856642871959) Tempo aproximado para leitura: **05:00 min** **Dúvida**Depois de incluir um título direto no financeiro, é possível vincular um pedido ou nota fiscal vindo do módulo compras/faturamento neste título?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

No momento, o sistema não possui uma funcionalidade que permita vincular diretamente um pedido ou nota fiscal, originados dos módulos de Compras ou Faturamento, a um título já existente no Financeiro.

Essa limitação pode gerar duplicidade de lançamentos, pois ao incluir a nota fiscal caso esteja com a configuração de geração de duplicata, o sistema cria automaticamente um novo título.

Como alternativa, você pode incluir um título do tipo **PA – Pagamento Antecipado** com movimentação bancária. Assim, quando a nota fiscal for lançada, será possível realizar a **compensação entre os títulos** (NF x PA), mantendo o controle correto dos valores.

**Saiba Mais**

[Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Quais os modos de inclusão de PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA)
