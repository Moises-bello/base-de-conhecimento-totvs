---
content_hash: 1fc082e927f26b7efa53a9ccb54c34fd6f07f949f4e4b8a3b64c2ea128f3966a
fetched_at: '2026-06-29T00:11:51.542766+00:00'
page_id: '849087968'
product: rm
source: tdn-rm
title: Totalizador com Campo Inicial em Detalhe
type: documentation
url: https://tdn.totvs.com/display/LRM/Totalizador+com+Campo+Inicial+em+Detalhe
version: 1
---

## Índice:

---

2

# Código de Referência

---

false

**totalizer-with-initial-field-pointed-to-control**

# Contexto

---

Como os campos que estão contidos dentro das bandas de detalhe (Como por exemplo um campo relacionado à uma tabela) são dinâmicos e se alteram a cada linha executada, a conversão de Totalizadores não é capaz de garantir estes valores como valores iniciais válidos (Pelo fato de serem dinâmicos). Dessa forma, não é possível garantir que a conversão de totalizadores que utilizam deste tipo de valor dinâmico será realizada corretamente:

# Solução

---

## Antes da Aceleração, no RM Reports

No RM Reports, deve-se utilizar o totalizador com um valor inicial que não se altera conforme a execução do relatório para que a aceleração seja realizada com sucesso.

---

# Relatórios Não Conformes / Conformes

---

INLINE

### Exemplo de Não Conformidade

50%

**Geração (Relatório não Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório não Conforme) - Smart View**

### Exemplo de Conformidade

50%

**Geração (Relatório Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório Conforme) - Smart View**

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
