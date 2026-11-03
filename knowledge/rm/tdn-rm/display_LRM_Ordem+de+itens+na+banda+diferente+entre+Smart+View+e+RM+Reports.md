---
content_hash: 3baa186e10a942ac2ff2f4aacc4aa1177a223f1d974c822c3317c04c8db294fe
fetched_at: '2026-06-29T00:11:51.464147+00:00'
page_id: '848795103'
product: rm
source: tdn-rm
title: Ordem de itens na banda diferente entre Smart View e RM Reports
type: documentation
url: https://tdn.totvs.com/display/LRM/Ordem+de+itens+na+banda+diferente+entre+Smart+View+e+RM+Reports
version: 5
---

## Índice:

---

2

# Contexto

---

Caso não exista nenhuma ordenação (Podendo ser de **Controle** ou por campos do **Detalhe**), o mecanismo de execução do Objeto de Negócio não é capaz de garantir que a ordem dos resultados esteja idêntica entre **Smart View** e **RM Reports:**

false

Todos os valores das bandas continuarão sendo retornados normalmente, mesmo que não seja determinada uma ordenação na banda. A única situação que realmente não pode ser garantida é a ordem destes valores.

# Possíveis Soluções

---

## Antes da Aceleração, no RM Reports

No RM Reports, é possível definir esta ordenação por meio tanto do campo **Ordenação** quanto do campo **Ordenação por controle**. Ao definir estes (Inclusive, no caso da **Ordenação**, com uma coluna da Fonte de Dados que não necessariamente está no relatório), estes, se ainda não existirem no Objeto de Negócio Acelerado, serão adicionado, fornecendo assim mais flexibilidade para o desenvolvedor do relatório.

---

## Após Aceleração, no Smart View

Também é possível definir a ordenação diretamente no **Smart View**, após a aceleração do relatório. Neste caso só será possível ordenar pelos campos existentes no Objeto de Negócio, o que oferece menos opções do que antes da aceleração:

# Exemplo de Não Conformidade

---

INLINE

### Exemplo de Não Conformidade - RM Reports / Smart View

50%

**Geração (Relatório não Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório não Conforme) - Smart View**

### Exemplo Conforme - RM Reports / Smart View

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
