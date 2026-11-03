---
content_hash: cb49fd40947728bdf4d649d43336e7f5373bec5a202d226e130fdd00cc62fc62
fetched_at: '2026-06-29T00:11:51.547896+00:00'
page_id: '849088100'
product: rm
source: tdn-rm
title: Totalizador em Subdetalhe sem Zerar na Quebra
type: documentation
url: https://tdn.totvs.com/display/LRM/Totalizador+em+Subdetalhe+sem+Zerar+na+Quebra
version: 1
---

## Índice:

---

2

# Código de Referência

---

false

**totalizer-in-child-detail**

# Contexto

---

Totalizadores que estiverem contidos dentro do mesmo subdetalhe (Seja na mesma banda ou em um rodapé atrelado ao mesmo detalhe) não são capazes de converter de forma a realizar a soma total, zerando o totalizador a cada nova execução do Detalhe-pai.

# Solução

---

## Antes da Aceleração, no RM Reports

Para realizar a aceleração corretamente, deve-se mover o totalizador para o detalhe-pai (Preferivelmente no rodapé do detalhe-pai).

---

# Relatórios Não Conformes / Conformes

---

INLINE

### Exemplo de Não Conformidade

50%

**Geração (Relatório não Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório não Conforme) - Smart View**

Note que enquanto no RM Reports, o **Totalizador** se comporta somando os valores do salário dos Subdetalhes entre si, no Smart View, para cada nova informação de seção, este recomeça a soma.

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
