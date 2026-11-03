---
content_hash: c41b079ad0c9b76172b570801f8a437dede69b1a9a52e5d97aaf961ebbdfcd65
fetched_at: '2026-06-29T00:09:23.247693+00:00'
page_id: '422546085'
product: rm
source: tdn-rm
title: Registro 0200
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+0200
version: 2
---

Serão totalizadas operações de saídas interestaduais. As regras de seleção dos Lançamentos Fiscais são semelhantes às regras para os registros 0120 e 0130, porém a totalização será por UF e não por CFOP.  
 Os campos "Valor Contábil Não Contribuinte", "Valor Contábil Contribuinte", "Base de Cálculo Não Contribuinte" e "Base de Cálculo Contribuinte" serão preenchidos com o Valor Contábil e a Base Tributada ICMS dos Lançamentos Fiscais. Neste caso, o sistema estará identificando se a NF foi emitida para contribuinte de ICMS ou não.

**Flag Cliente/Fornecedor**: o sistema estará verificando o campo Contribuinte ICMS localizado no cadastro de Clientes / Fornecedores, aba Integrações sub aba Tributos.

**Flag Estado**: o campo Contribuinte encontra-se na própria edição do Lançamento Fiscal.

**Flag Empresa**: o sistema sempre estará considerando emissão para Contribuinte.

**Valor Outras Operações**: este campo estará recebendo um somatório dos valores de Isentos e Outros ICMS.

**Valor Imposto Cobrado ST**: este campo não será gerado.
