---
content_hash: 8e8d9e83a7eb133d3deaad373a99f1ce71aaaf35b7c11ac8ad85d6d69e3fdf5c
fetched_at: '2026-06-29T00:08:26.812791+00:00'
page_id: '271385841'
product: rm
source: tdn-rm
title: Limitações Design
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271385841
version: 4
---

# Índice:

---

.\*ndice:

# Introdução:

---

       Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

Identificamos uma inconsistência na edição do design de relatórios com a seguinte situação: **Consultas SQL** utilizadas como **fontes de dados** e que **possuem colunas** com **alias que se iniciam com números**. Nestes casos o gerador permite que a **consulta SQL seja adicionada ao relatório**, entretanto, não é possível **"arrastar"** tais campos para o corpo do relatório. No exemplo abaixo a **consulta SQL** possui três campos, os campos **CHAPA** e **NOME** podem ser **"arrastados"** para o relatório sem problemas, entretanto, o campo **11CODCOLIGADA** não pode ser **"arrastado"** devido a limitação dos componentes de terceiros utilizados.

Complementando, os bancos de dados compatíveis com o **RM (SQL Server e Oracle)** não permitem a **criação de tabelas** contendo **colunas com nomes que se iniciam com números**. Esta situação só é permitida com a atribuição de alias para as colunas, todavia, **a utilização deste recurso** gera **incompatibilidade com o design do RM Reports**.

OBSERVACAO

Existem situações semelhantes documentadas pela **Devexpress**, são elas:

**Utilização de "." (ponto) em alias de coluna de tabelas**

* <https://www.devexpress.com/Support/Center/Question/Details/B142625>
* <https://www.devexpress.com/Support/Center/Question/Details/B142623>
* <https://www.devexpress.com/Support/Center/Question/Details/B132174>

**Utilização de "@" (arroba) em alias de coluna de tabelas**

* <https://www.devexpress.com/Support/Center/Question/Details/T295645>
falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Limitações Design

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
