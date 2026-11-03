---
content_hash: 9684ebe25759273075534d76e6d7ff151e5d2282d572286d977575deea8811f6
fetched_at: '2026-06-29T00:09:50.614428+00:00'
page_id: '435105486'
product: rm
source: tdn-rm
title: Relatório - Registros Diários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105486
version: 2
---

**Relatório - Registros Diários**

---

Este relatório é responsável por recuperar os dados  referentes aos contratos de venda criados no período informado e de acordo com o filtro selecionado. Neste registro são recuperados contratos de venda Efetuados, Emitidos, Quitados e Cancelados  
 **Pré-Condições:**  
 1 - Ter Efetuado, Emitidos, Quitado e/ou Cancelado um contrato de venda dentro do período informado ao executar o relatório.  
 **Dados Recuperados**  
 **Dados dos Empreendimentos:** Retornará Código  e Nome do Empreendimento , além de todos os campos referentes a medições: Áreas: Construída , reservada , do terreno , total  e de venda , custo por metro quadrado  e dados do endereço do empreendimento  
 **Dados das Vendas:** Tais informações serão lidas da tabela venda com relacionamentos específicos para cada área de informação:  
 **Vendas Efetuadas:** Fará o relacionamento com as tabelas de Cliente Fornecedor , Situação da Venda  e Itens de Venda  para retornar os seguintes campos:

* Cliente
* Venda
* Data da Venda
* Contrato
* Unidade
* Subunidade
* Situação da venda

**Contratos Emitidos:** Fará o relacionamento com as tabelas de Cliente Fornecedor (FCFO), Situação do Contrato  e Itens de Venda  e contrato  para retornar os seguintes campos:

* Cliente
* Venda
* Data da Venda
* Contrato
* Unidade
* Subunidade
* Emissão do Contrato

**Vendas Finalizadas:** Fará o relacionamento com as tabelas de Cliente Fornecedor, Situação da Venda  e Itens de Venda  para retornar os seguintes campos:

* Cliente
* Venda
* Data da Venda
* Contrato
* Unidade
* Subunidade
* Data de Quitação
* Situação da venda

**Vendas Canceladas:** Fará o relacionamento com as tabelas de Cliente Fornecedor, Situação da Venda e Itens de Venda  para retornar os seguintes campos:

* Cliente
* Venda
* Data da Venda
* Contrato
* Unidade
* Subunidade
* Data do Cancelamento
* Motivo

Voltar
