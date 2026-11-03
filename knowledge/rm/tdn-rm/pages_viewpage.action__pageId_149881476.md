---
content_hash: c903663a82db73bd2bb711d7a805ef14156c4099888009b7c4e54ecc30ad0d78
fetched_at: '2026-06-29T00:05:56.315325+00:00'
page_id: '149881476'
product: rm
source: tdn-rm
title: Utilizando a atividade "Gerar Auto-Incremento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881476
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     Este documento tem por objetivo especificar a atividade “Gerar Auto-Incremento” disponível na Fórmula Visual.

# Especificação:

---

     A atividade “Gerar Auto-Incremento” realiza o auto incremento de um campo presente na tabela GAUTOINC (Tabela responsável por controlar os códigos de auto incremento das tabelas do sistema).

     Sua parametrização deve possuir os seguintes valores obrigatoriamente:

* CodigoAutoInc – é referente aos registros presente no campo CODAUTOINC da tabela GAUTOINC

* CodigoSistema – referente aos registros presentes no campo CODSISTEMA da tabela GAUTOINC. Este código deve ser o mesmo do CodigoAutoInc inserido na Fórmula Visual.

* NovoValor – Informa se os parâmetros passados são novos ou se já existem na tabela

Observação

     Devido a novas implementações presentes no sistema, esta atividade se encontra obsoleta, entretanto, é possível que em algumas rotinas de produtos da linha RM sua utilização seja conveniente.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Atividade "Gerar Auto-Incremento" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
