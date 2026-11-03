---
content_hash: 7570e43d8e630829866a71d927157732dc5fec96e2e83b7a70145bf5f17a18ee
fetched_at: '2026-06-29T00:10:46.065023+00:00'
page_id: '553906088'
product: rm
source: tdn-rm
title: Registro 1510
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1510
version: 5
---

**Registro das notas fiscais de saídas internas destinadas a contribuinte do Simples Nacional**

Este registro deve conter as notas fiscais de saída interna destinadas a contribuinte do Simples Nacional do produto declarado no registro 1000, no caso de aquisição de mercadorias a que se referem as Seções VI, VII, XVIII e XXII, do Anexo IX do RICMS/17, com imposto retido calculado com a aplicação do percentual integral da MVA.

* Lançamento Fiscal de Saída
* Operação Dentro do Estado
* Cliente/Fornecedor optante pelo Regime Simplificado (FCFO.OPTANTEPELOSIMPLES)
* Cuja DATALF esteja dentro do período da rotina
* Tenham movimentado produtos marcados como "**Tributado pelo ICMS-ST**" para o Estado da Filial e Data de Início da Tributação ST maior ou igual início do período da rotina (Anexo Dados Fiscais por UF)

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| M01 | REG | Registro 1510 | Texto fixo contendo 1510 |
| M02 | DT\_DOC | Data de Emissão do documento fiscal | DLAF.DATAEMISSAO |
| M03 | CST\_CSOSN | Código da Situação Tributária | Se a Filial for Optante pelo Simples, será gerado com o CSOSN da Regra de ICMS associada ao CFOP.  Caso contrário, será gerado com o CST informado no Item do Lançamento Fiscal (DITEM.CST) |
| M04 | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| M05 | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| M06 | CNPJ\_EMIT | CNPJ Emitente | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| M07 | UF\_EMIT | UF Emitente |
| M08 | CNPJ\_DEST | CNPJ do destinatário | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| M09 | UF\_DEST | UF do Destinatário |
| M10 | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 5101. |
| M11 | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| M12 | UNID\_ITEM | Unidade de medida do item | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| M13 | QTD\_SAIDA | Quantidade do produto na saída, convertida na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000. | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| M14 | VL\_UNIT\_ITEM | Valor unitário líquido do item | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
