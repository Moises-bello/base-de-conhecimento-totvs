---
content_hash: 756ad8d4ad71471de3226c116eb21b36050bc51d0e0a435bde76a26a654a76a0
fetched_at: '2026-06-29T00:08:46.430701+00:00'
page_id: '317297872'
product: rm
source: tdn-rm
title: Pipelines
type: documentation
url: https://tdn.totvs.com/display/LRM/Pipelines
version: 16
---

# Ativador de Operações:

---

false.AbstractActionsOperation

**AbstractActionsOperation:**

Operação abstrata com ações

**Parâmetros:**

* **Action:** Lista de ações a serem executadas
* **Order:** Ordem que deve ser executado
* **Field:** Campo que será avaliado
ExtractOperation

**ExtractOperation:**

Extrair as informações de um campo, para outro determinado campo.

**Parâmetros:**

* **Destiny:** Campo que vai receber o resultado
* **Action:** Lista de ações a serem executadas
* **Order:** Ordem que deve ser executado
* **Field:** Campo que será avaliado

IHasActions

**IHasActions:**

Substituir o valor de um campo

**Parâmetros:**

* **Actions:** Lista de ações a serem executadas
* **Order:** Ordem que deve ser executado
ReplaceOperation

**ReplaceOperation:**

Substituir o valor de um campo

**Parâmetros:**

* **Actions:** Lista de ações a serem executadas
* **Order:** Ordem que deve ser executado
* **Field:** Campo que será avaliado

# Ativador de Ações:

---

false.FetchFirstFromListOrDefault

**FetchFirstFromListOrDefault:**

Pegar a primeira linha de uma lista ou retornar um valor padrão

**Parâmetros:**

* **Default:** Valor padrão caso não encontre uma linha
* **Order:** Ordem que deve ser executado
ForeachInListAction

**ForeachInListAction:**

Executar muitas ações em cada linha para obter uma lista

**Parâmetros:**

* **Stop**: Ponto de parada
* **InnerActions:** Ações que deveriam ser executadas
* **Order:** Ordem que deve ser executado
IfIsNullOrEmptySetDefaultAction

**IfIsNullOrEmptySetDefaultAction:**

Definir um valor padrão se a entrada for nula ou uma string vazia

**Parâmetros:**

* **Default:** Valor padrão caso não encontre uma linha
* **Order:** Ordem que deve ser executado
IHasInnerActions

**IfIsNullOrEmptySetDefaultAction:**

Quando uma ação tem ações internas

**Parâmetros:**

* **InnerActions:** Ações que deveriam ser executadas
* **Order:** Ordem que deve ser executado
JoinLinesAction

**JoinLinesAction:**

Juntar-se a uma lista de string de volta a uma única string

**Parâmetros:**

* **Separator:** Separador
* **Order:** Ordem que deve ser executado
RegexExtractAction

**RegexExtractAction:**

Executar uma operação regex para extrair informações de uma string

**Parâmetros:**

* **Pattern:** Padrão que deve ser avaliado
* **Order:** Ordem que deve ser executado
RegexReplaceAction

**RegexExtractAction:**

Execute um regex para substituir uma string

**Parâmetros:**

* **Pattern:** Padrão que deve ser avaliado
* **Replacement:** Valor de substituição
* **Order:** Ordem que deve ser executado
RemoveEmptyLinesAction

**RemoveEmptyLinesAction:**

Remover linhas vazias da lista de strings

**Parâmetros:**

* **Order:** Ordem que deve ser executado
ReverseListAction

**ReverseListAction:**

Inverter uma linha

**Parâmetros:**

* **Order:** Ordem que deve ser executado
SplitLinesAction

**SplitLinesAction:**

Dividir uma string em uma lista de strings

**Parâmetros:**

* **Order:** Ordem que deve ser executado
StringToLowerAction

**StringToLowerAction:**

Executar um ToLower em uma string

**Parâmetros:**

* **Order:** Ordem que deve ser executado
StringToUpperAction

**StringToUpperAction:**

Executar uma operação ToUpper em uma string

**Parâmetros:**

* **Order:** Ordem que deve ser executado
