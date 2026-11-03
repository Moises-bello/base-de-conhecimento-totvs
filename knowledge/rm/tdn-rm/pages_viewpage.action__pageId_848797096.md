---
content_hash: 16b129f3a3415b6d5321b2b342a489bb7dbc9c22b3ab65318de5726436d02582
fetched_at: '2026-06-29T00:11:51.471894+00:00'
page_id: '848797096'
product: rm
source: tdn-rm
title: Regra de Formatação em Banda de Subdetalhe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848797096
version: 3
---

## Índice:

---

2

# Código de Referência

---

false

**formatting-rule-in-child-detail**

# Contexto

---

Regras de Formatação em bandas de Subdetalhe não são suportadas pelo **Smart View**. Dessa forma, não é possível acelerá-las do **RM Reports**

# Solução

---

false

**Antes de aceitar aceleração:**

Ao fazer a conversão de um relatório que possua regras de formatação ligadas ao subdetalhe, é importante fazer uma alteração e passar a usar essas regras nas bandas de detalhe para o correto funcionamento.

false

**Após aceitar aceleração:**

Após fazer a conversão de um relatório que possua regras de formatação ligadas ao subdetalhe, no Smart View, podemos adicionar as regras no lugar correto.

Na banda de subdetalhe, vamos copiar a expressão presente em Nome do estilo.

E colar nos detalhes que quisermos aplicar as regras:

Após isso o relatório passará a funcionar corretamente.

# Relatórios Não Conformes

---

INLINE

### Exemplo de Não Conformidade

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
