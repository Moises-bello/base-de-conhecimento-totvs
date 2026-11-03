---
article_id: 360016310251
category: Financeiro - Integrações (SIGAFIN)
content_hash: b23f292b944a7b403fceec50c8a45eae32dad0ead257e9b04749a97316054d7d
fetched_at: '2026-06-28T22:38:18.560795+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: 'MP - SIGAFIN - Por que alguns registros estão marcados como contabilizados,
  mas não existem os lançamentos '
type: support-article
updated_at: '2021-07-28T17:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016310251-MP-SIGAFIN-Por-que-alguns-registros-est%C3%A3o-marcados-como-contabilizados-mas-n%C3%A3o-existem-os-lan%C3%A7amentos
---

**Dúvida**Por que alguns registros estão marcados como contabilizados, mas não existem os lançamentos ?  
   
 **Ambiente**Microsiga Protheus – Financeiro - A partir da versão 11.80  
   
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

No sistema existem alguns processos onde os campos de *Flag* de **contabilização** já nascem com "S", mesmo sem existir o **lançamento contábil**.  
Este tratamento ocorre para não haver a duplicidade na contabilidade.

**Exemplo 1:** Inclusão de adiantamento para clientes**.**

O campo **E5\_LA** referente ao adiantamento já é gravado com S, uma vez que o campo **E1\_LA** deste registro vai ficar em branco, se a contabilização não foi feita em modo ***on-line***.

**Exemplo 2:** Na criação automática de um registro de **contas a pagar, contas** **a receber** através da **entrada** e **saída de uma nota fiscal**.

Os campos **E2\_LA / E1\_LA** já serão gravados com "S", pois a contabilização da operação é feita pelo módulo de origem (**compras** / **faturamento**), evitando assim a duplicidade do **lançamento** quando houver a **contabilização** no modulo de origem.
