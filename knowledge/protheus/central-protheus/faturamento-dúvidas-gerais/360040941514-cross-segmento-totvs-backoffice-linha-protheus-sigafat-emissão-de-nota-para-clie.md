---
article_id: 360040941514
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 876f0f34e1b00a7740e4ed9953fd6ee25e18975c6db232b8ee5cfb4a34812ac0
fetched_at: '2026-06-28T22:38:32.713334+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Emissão de
  Nota para cliente com entrega em outro endereço
type: support-article
updated_at: '2023-09-05T17:23:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040941514-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Emiss%C3%A3o-de-Nota-para-cliente-com-entrega-em-outro-endere%C3%A7o
---

**Ocorrência**

Em algumas transações comerciais, é necessário realizar a venda para o CNPJ que realizará o pagamento e a entrega das mercadorias precisa ser realizada em outro CNPJ ou em outro endereço do mesmo CNPJ.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

1. Caso **necessite emitir duas notas**, uma para o Comprador e outra para o local de entrega, é possível realizar o processo de venda por **Contrato de Parceria (FATA400)**.

Neste processo o sistema permite a inclusão de uma nota de venda, que gera financeiro, mas não movimento estoque, e uma ou várias notas de remessa, que movimentam estoque, porém não geram financeiro.

Para detalhes sobre a inclusão do contrato de parceria, consulte a **opção 3** da documentação: <https://tdn.totvs.com/x/sUNtDQ>

2. Caso necessite emitir apenas a nota para entrega, utilize os campos **“Cli. Entrega” (C5\_CLIENT)** e **“Loja Entrega” (C5\_LOJAENT)** no pedido de vendas, dessa forma os títulos e movimentos internos do sistema (financeiro, estoque, contábil, etc.) serão gerados para o cliente principal do pedido, porém o **DANFE** será impresso em nome do cliente entrega.
