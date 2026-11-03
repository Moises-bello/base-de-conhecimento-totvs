---
content_hash: a2eeb29dffdd4cc1e9669e2b07dc9841b018f598e3b2d5ae9eccc193122e73ce
fetched_at: '2026-06-29T00:11:51.498692+00:00'
page_id: '848815820'
product: rm
source: tdn-rm
title: Filtro com Ligação de Dados ou Sumário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848815820
version: 1
---

## Índice:

---

2

# Código de Referência

---

false

**filter-with-data-binding**

# Contexto

---

Um componente de **Filtro** não deve ser utilizado apenas para retorno do filtro desejado, não devendo possuir Ligação de Dados, Sumário ou qualquer outra regra de negócio que não é pertinente aos Filtros. Para estes casos, utilize um controle de **Texto** normal.

# Solução

---

## Antes da Aceleração, no RM Reports

No RM Reports, é necessário passar as regras de negócio do controle de **Filtro** para um controle de **Texto**, a fim de que a conversão dos dois seja realizada corretamente.

# Relatórios Não Conformes / Conformes

---

50%

**Geração (Relatório não Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório não Conforme) - Smart View**

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
