---
content_hash: d82c6b944d752df1a6e94a134a9dd87d3b41095cdbcdae98c6d724046f912431
fetched_at: '2026-06-29T00:09:20.585565+00:00'
page_id: '422545715'
product: rm
source: tdn-rm
title: Auto Declaração de Vendas (Mapeamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545715
version: 9
---

Mapeamento os Campos do layout do arquivo XML referente a Auto declaração de vendas.

|  |  |  |  |
| --- | --- | --- | --- |
| **TAG** | **Descrição** | **Origem dos dados** | **Observação** |
| **< <?xml version="1.0"?>** | Cabeçalho do arquivo XML não devendo ser alterado | Gerado Internamente |  |
| **tns:AutoDeclaracao**   **xmlns:tns=**[{\*}{+}](http://www.tarea.com.br/InovarAuto/AutoDeclaracao)[http://www.tarea.com.br/InovarAuto/AutoDeclaracao+\*](http://www.tarea.com.br/InovarAuto/AutoDeclaracao+*)   **xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">** | Utilizada apenas para agrupar os dados da Auto declaração |  | Preencha com "TRUE" quando se tratar de uma declaração retificadora ou "false" quando não for. Campo de preenchimento obrigatório |
| **<tns:retificadora>** | Indica se esta declaração é retificadora ou não. | Gerando conforme informação da Tela |  |
| **<tns:declarante>** | Utilizada apenas para agrupar os dados do declarante |  |  |
| **<tns:tipo\_declarante>** | Indica o tipo de pessoa jurídica que está gerando o arquivo, neste caso um fornecedor. |  | Preencha com "F" por se tratar de fornecedor direto de montadora. Se uma montadora atuar como fornecedora direta de outra montadora, também deve preencher com "F". Campo de preenchimento obrigatório |
| **<tns:razao\_social>** | Razão social da empresa que está gerando o arquivo, no caso, o fornecedor direto da montadora | Gerado conforme o cadastro da Filial |  |
| **<tns:cnpj>** | Número do CNPJ da empresa que está gerando o arquivo | Gerado conforme o cadastro da Filial | Apenas com os caracteres numéricos, ignorando "." e "/". |
| **<tns:matriz>** | Indica se o CNPJ do fornecedor é da matriz ou não | Gerado conforme o cadastro da Filial |  |
| **<tns:operacao>** | Utilizada apenas para agrupar os dados da operação realizada pelo fornecedor |  |  |
| **<tns:natureza\_operacao>** | Indica a natureza da operação, ou seja, que o registro desta operação está tratando de uma venda |  | Preencha com "V" por se tratar de vendas diretas para montadoras. Campo de preenchimento obrigatório |
| **<tns:empresa>** | Utilizada apenas para agrupar os dados da empresa que está vendendo para a montadora que gera o arquivo |  |  |
| **<tns:razao\_social>** | Razão social da montadora para quem se realizou a venda | Gerado Conforme o Cadastro do Cliente/Fornecedor – Que o Campo Habilitado para Inovar Auto esteja habilitado |  |
| **<tns:cnpj>** | Número do CNPJ da montadora que adquiriu a venda realizada pelo fornecedor direto, gerador deste arquivo | Gerado Conforme o Cadastro do Cliente/Fornecedor – Que o Campo Habilitado para Inovar Auto esteja habilitado |  |
| **<tns:mes\_ref>** | Mês de referência dos dados |  |  |
| **<tns:ano\_ref>** | Ano de referência dos dados |  |  |
| **<tns:vl\_total\_notas>** | Valor total de notas fiscais do fornecedor direto da montadora |  |  |
| **<tns:vl\_parc\_dedutivel>** | Valor total da parcela dedutível para fins de apuração de crédito de IPI |  |  |
