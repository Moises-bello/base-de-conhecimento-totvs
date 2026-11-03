---
content_hash: 1c8db2f74ba07fd1890d183506c40b38655d39105c3cb9575ab47d573d5112d0
fetched_at: '2026-07-02T19:24:25.932813+00:00'
page_id: '514746948'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave UseLargeRecno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514746948
version: 4
---

Esta chave permite habilitar ou desabilitar a criação de campo Recno do tipo "BigInt", aumentando o limite de registros para **9.223.372.036.854.775.807**.

O limite padrão é de **2.147.483.647** registros.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita a utilização de Large Recno. |
| 1 (**Padrão**) | Habilita a utilização de Large Recno. |

---

## Observações

* Habilitar ou desabilitar este recurso, fará com que novas tabelas criadas passem a utilizar (ou não) este tipo de campo.
* Alterar o valor desta chave não afeta as tabelas já criadas no ambiente.
* Esta chave pode ser configurada por Environment, especificando assim, quais ambientes utilizarão esta configuração.

---

## Exemplos

textTodos os ambientes passarão a utilizar esta configuração

.

Apenas este ambiente passará a utilizar esta configuração
