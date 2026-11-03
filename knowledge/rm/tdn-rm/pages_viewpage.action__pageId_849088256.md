---
content_hash: e5b97d9d17fb1e475ec30118ea07e73b03a8bdf6f1cb64a2e96ac5d053609721
fetched_at: '2026-06-29T00:11:51.554054+00:00'
page_id: '849088256'
product: rm
source: tdn-rm
title: Totalizador sem Zerar na Quebra com Quebra em cabeçalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849088256
version: 2
---

## Índice:

---

2

# Código de Referência

---

false

**totalizer-without-reset-on-break-with-header-break**

# Contexto

---

**Totalizadores** sem o campo ***Zerar na Quebra***marcado não serão convertidos corretamente caso exista **Ordenação/Quebra** no **Cabeçalho do Detalhe**

# Solução

---

## Antes da Aceleração, no RM Reports

Remover a ordenação/quebra antes de realizar a aceleração.

---

# Relatórios Não Conformes / Conformes

---

INLINE

### Exemplo de Não Conformidade

50%

**Geração (Relatório não Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório não Conforme) - Smart View**

Note que enquanto no RM Reports, o **Totalizador** se comporta somando os valores do salário dos Subdetalhes entre si, no Smart View,  a primeira seção é totalizada, porém as próximas não são capazes de serem calculadas.

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
