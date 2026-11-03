---
content_hash: 539a3934858478755cc81e789af2de29384c169939bddbd2013f82eb90d9a11c
fetched_at: '2026-06-29T00:09:45.466722+00:00'
page_id: '433251844'
product: rm
source: tdn-rm
title: Geração de Créditos Fiscais de Tributos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433251844
version: 21
---

# Conteúdo

**Conteúdo**

# 1. Introdução

A execução do processo **Geração de Créditos Fiscais de Tributos,** serão recuperados os lançamentos fiscais conforme as regras abaixo.

# 2. Regras

* Deve ser informados os parâmetros para coligada (corrente), filial (corrente), tributo e período, estes serão usados para seleção dos valores do crédito a partir do tributo do item dos lançamentos fiscais que serão filtrados também pela Data do Lançamento.
* O valor do crédito será o somatório dos valores dos tributos encontrados agrupados pelo Tipo do Crédito (informação do item do lançamento).
* Para lançamentos com Status "Normal" o valor irá para o campo Crédito Apurado, e para "Extemporâneo" para o campo Crédito Apurado Extemporâneo.
* Serão permitidos somente tributos cujo Tipo seja "**PIS**" ou "**COFINS**".
* Caso o registro de crédito já existe será exibida mensagem de aviso.

# 3. Execução do Processo

Imagens
