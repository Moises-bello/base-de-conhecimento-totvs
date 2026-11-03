---
content_hash: e547f1379aa7b1758b1f1a60fba6280a3005417d5d6e0d27c2b609633069ec91
fetched_at: '2026-06-29T00:09:37.880973+00:00'
page_id: '425459642'
product: rm
source: tdn-rm
title: Solicitar Compra de Exemplares
type: documentation
url: https://tdn.totvs.com/display/LRM/Solicitar+Compra+de+Exemplares
version: 2
---

Este processo estará disponível quando houver integração com o Totvs Gestão Bibliotecária estiver integrado com o Totvs Gestão de Estoque, Compras e Faturamento e tem o objetivo de gerar movimento de solicitação de compras de publicações/exemplares para a Biblioteca.

O processo pode ser executado através do Cadastro da Publicação ou Cadastro de Sugestão de Compras.

Quando a solicitação de compra ocorrer pelo **Cadastro da Publicação** é preciso informar a quantidade de exemplares e o produto, caso este não tenha sido informado na publicação na categoria controle interno.  
 Já no **Cadastro de Sugestão de Compras** será necessário informar o grupo de publicação, tipo de publicação, categoria e o produto, visto que a publicação solicitada ainda não está cadastrada. Assim após a execução do processo será incluído o cadastro da publicação e gerado o movimento de solicitação de compra de exemplares.

**Importante**

* No Cadastro de publicações deve ser cadastrado através do anexo "Fornecedores" o(s) fornecedor(es) referente(s) à compra do exemplar. Este é o mesmo fornecedor que será informado no faturamento do produto no estoque.
* No cadastro de  deve ser informado o Local de Estoque, para que no momento do faturamento no TOTVS Gestão de Estoque, Compras e Faturamento, o exemplar seja corretamente cadastrado na unidade bibliotecária e filial correspondente.
* Parâmetros de integração podem ser configurados em:  .
