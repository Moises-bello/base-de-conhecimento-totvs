---
content_hash: 6343a1f19017eae098d74f41970ddeebefb6046687aa75fa4f07640992ddcc59
fetched_at: '2026-06-29T00:11:21.156498+00:00'
page_id: '689055672'
product: rm
source: tdn-rm
title: Grupo de Produtos
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+de+Produtos
version: 31
---

Atenção

Recurso disponível na release 12.1.2209 ou superior.

## **01. VISÃO GERAL**

O Grupo de Produtos permite que sejam agrupados produtos de acordo com  as suas  características.

## **02. EXEMPLO DE UTILIZAÇÃO**

Está localizado no menu: **Cadastros → Grupo de Produtos.**

**Tela principal:**São exibidos todos os Grupos de Produtos existentes de acordo com o filtro utilizado.

**Tela de edição:**Ao editar um Grupo de Produto uma segunda tela é exibida, possibilitando atualizar a descrição do grupo de produto e ou inativá-lo, caso seja necessário.

O código do Grupo de Produto pode ser definido através de uma máscara conforme a documentação: [acesse aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=423938842) .

Não é possível inativar um Grupo de Produtos que possua produtos vinculados ao mesmo. Ao tentar inativar um Grupo de Produto que tenha produtos vinculados será apresentada a mensagem abaixo:

## **03. TABELAS UTILIZADAS**

* TGRUPOPRODUTO - Tabela responsável pelas informações do Grupo de Produto.
* TPRDGRUPOPRODUTO - Tabela responsável pelo vínculo entre Produto e Grupo de Produto.
* TGRUPOPRODUTOCFO - Tabela responsável pelo vínculo entre Cliente/Fornecedor e Grupo de Produto.

Processos Relacionados

* Processo para
* Anexo
* Anexo do Produto -
* Anexo do Cliente/Fornecedor -
* Conceito / Gerador de Saídas -
* API Grupo de Produto -  <https://api.totvs.com.br/apidetails/StockGroup_v1_000.json>
* API Produto - <https://api.totvs.com.br/apidetails/Products_v2_000.json>
