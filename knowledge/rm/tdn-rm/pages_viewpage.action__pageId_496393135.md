---
content_hash: dfb36c37f230f9e34d9d20ba9d96db6483cc65cb4cb7b992fd607f90b6a5f6f3
fetched_at: '2026-06-29T00:10:22.070318+00:00'
page_id: '496393135'
product: rm
source: tdn-rm
title: Fornecedor de Benefícios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496393135
version: 5
---

Neste cadastro é armazenado os dados dos fornecedores de benefícios. Em que é realizada uma associação com os cadastros de:

**[Cliente/Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=421388786)**, nativo do módulo de Gestão Financeira e cadastro de **[Operadora de Saúde](http://tdn.totvs.com/pages/viewpage.action?pageId=452718733)**, nativo do módulo de Folha de Pagamento.

**Campos do Cadastro:**

* **Código do Fornecedor:** Código do fornecedor de benefícios adotado no módulo de Gestão de Pessoas, a ser atribuído pelo usuário.
* **Código do Tipo de Segmento:** Será associado de acordo com a tabela dinâmica **VBENEFTPOFORN**, cujos itens são de uso interno do sistema. Tem por objetivo classificar o tipo de segmento do fornecedor. Exemplo: 1 - Assistência Médica, 2 - Assistência Odontológica.
* **Código do Cliente Fornecedor:** Associado ao cadastro de cliente/fornecedor. Caso não exista poderá ser incluído pelo atalho disponibilizado na consulta dos dados disponíveis para preenchimento.
* **CNPJ:** Preenchido automaticamente com base no cadastro do cliente/fornecedor.
* **Código da Operadora de Saúde:** Associado ao cadastro de Operadora de Saúde. Caso não exista poderá ser incluído pelo atalho disponibilizado na consulta dos dados disponíveis para preenchimento.
* **Registro ANS:** Preenchido automaticamente com base no cadastro de Operadora de Saúde.
