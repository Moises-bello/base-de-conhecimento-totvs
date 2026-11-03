---
content_hash: 7a8293294b1cfe6490f16e196f080dbf217e5e916b47f74b52cc839c23927fbd
fetched_at: '2026-06-29T00:11:39.069086+00:00'
page_id: '787858319'
product: rm
source: tdn-rm
title: Dependentes do Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=787858319
version: 2
---

Através do anexo Dependentes é possível visualizar o cadastro das pessoas dependentes e vinculadas ao cliente/fornecedor. Este cadastro deve ser usado para informações de Dependentes IR Autônomos da rotina  e-Social - Leiaute S-1.2.

Para opções do campo Tipo deve ser criada uma tabela dinâmica, no módulo Serviços Globais, para o Sistema Gestão Financeira, com nome FTIPODEPEN e visível para todas as coligadas. Cadastre os itens de tabela dinâmica de acordo com sua regra de negócio.

Para um mesmo CPF é possível cadastrar mais de um registro de dependente desde que não haja conflito do período de vigência:

* Somente um registro com data de início informada e data de fim em branco pode existir.
* Não podem existir dois registros onde ambos possuem as datas de vigência em branco.
* Os períodos de vigência não podem se sobrepor.
