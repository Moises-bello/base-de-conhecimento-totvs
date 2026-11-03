---
content_hash: f20abe6bde6cdb708c83fc52cbf76bbf7d82c4f00416a939bf9ea54bf5648fe2
fetched_at: '2026-06-29T00:10:31.253733+00:00'
page_id: '521134713'
product: rm
source: tdn-rm
title: FISCAL01-11508-DT REGISTRO 1391 - Alteração no Cadastro de Produção da Usina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521134713
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Produção Diária da usina |
| Ticket: | FISCAL01-11508 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11508 |

## **02. SITUAÇÃO/REQUISITO**

Criar no cadastro de Produção Diária da Usina os seguintes campos:

1. Código do Produto com Lookup para o Cadastro de Produtos
2. Tipo de resíduo com as opções:
   * 01 - Bagaço de cana
   * DDG
   * WGD
3. Quantidade de resíduo produzido (02 decimais)

## **03. SOLUÇÃO**

Visando atender a solicitação, foi criado os seguintes campos na aba de "Identificação":

* Produto
* Tipo de Resíduo

E o seguinte campo para a aba de "Valores"

* Quantidade de resíduo produzido
