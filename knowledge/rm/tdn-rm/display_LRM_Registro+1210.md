---
content_hash: 955f36c575c0cbbc6085000702fee66bfcd2773d9115cb73ae030cb3b411728b
fetched_at: '2026-06-29T00:10:46.010109+00:00'
page_id: '553906003'
product: rm
source: tdn-rm
title: Registro 1210
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1210
version: 8
---

**Registro das notas fiscais de saída interna para consumidor final**

Este registro deve conter todas as notas fiscais de saída emitidas em **operação interna** de venda a consumidor final do produto declarado no registro 1000 sujeito a substituição tributária, ainda que não exista valor a recuperar, a ressarcir ou a complementar.

Devem ser selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamento Fiscal de Saída
* Operação Dentro do Estado
* Operação com consumidor final
* Cuja DATALF esteja dentro do período da rotina
* Tenham movimentado produtos marcados como "**Tributado pelo ICMS-ST**" para o Estado da Filial e Data de Início da Tributação ST maior ou igual início do período da rotina (Anexo Dados Fiscais por UF)

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| G01 | REG | Registro 1210 | Texto fixo contendo 1210 |
| G02 | DT\_DOC | Data de Emissão do documento fiscal no Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| G03 | CST\_CSOSN | Código da Situação Tributária | Se a Filial for Optante pelo Simples, será gerado com o CSOSN da Regra de ICMS associada ao CFOP.  Caso contrário, será gerado com o CST informado no Item do Lançamento Fiscal (DITEM.CST) |
| G04 | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| G05 | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| G06 | CNPJ\_EMIT | CNPJ Emitente | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| G07 | UF\_EMIT | UF Emitente |
| G08 | CNPJ\_CPF\_DEST | CNPJ ou CPF do destinatário | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| G09 | UF\_DEST | UF do Destinatário |
| G10 | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 5101. |
| G11 | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| G12 | UNID\_ITEM | Unidade de medida do item utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| G13 | QTD\_SAIDA | Quantidade do produto na saída na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| G14 | VL\_UNIT\_ITEM | Valor unitário líquido do item (considerando descontos) | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO) / DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| G15 | VL\_ICMS\_EFET | Valor do ICMS efetivo na saída  É o resultado da multiplicação da alíquota interna da mercadoria sobre o valor da operação de venda a consumidor final, ou na hipótese de operação beneficiada com redução da base de cálculo, sobre a base de cálculo reduzida | Esse campo deve ser calculado sobre o valor da operação, considerando redução de BC se houver, aplicando-se a alíquota interna do produto.  ((Campo G13 \* Campo G14) \* Alíquota interna do Produto na UF) |
