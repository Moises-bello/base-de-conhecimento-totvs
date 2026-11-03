---
content_hash: 1db2ef43a79a3dc0e3431951bb64996ca0efac5ed10f213c4ac63fb6a2c55069
fetched_at: '2026-06-29T00:10:50.594514+00:00'
page_id: '561869149'
product: rm
source: tdn-rm
title: Validação de conta sem débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561869149
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parametrização**

## **01. VISÃO GERAL**

* Não é permitido que o valor total do resumo seja 0 se houver gastos particulares. O parâmetro “Mostrar relatório com mensagens não impeditivas” determina se será emitido um alerta ou erro.
* Se o valor total do resumo for 0, verificar:     
  + se não houver registros nas tabelas SZATENDHONORARIO E SZATENDSADT e valor do pacote do resumo for 0, retorna erro.
  + se houver registros, retorna erro ou alerta, dependendo do parâmetro “Mostrar relatório com mensagens não impeditivas"

## **02. PARAMETRIZAÇÃO**

]]>
