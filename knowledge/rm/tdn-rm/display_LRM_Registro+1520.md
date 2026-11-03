---
content_hash: e700c64fa0e1bb37e36bb77379bd44ef0f5316061d4ed51aeae214f24f72fa81
fetched_at: '2026-06-29T00:10:46.072221+00:00'
page_id: '553906093'
product: rm
source: tdn-rm
title: Registro 1520
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1520
version: 5
---

**Registro das notas fiscais de devolução das saídas internas destinadas a contribuinte do Simples****Nacional**

Este registro deve conter as notas fiscais de devolução de venda ocorridas no mesmo mês em que foi computada a saída. 

Devem ser selecionados os lançamentos fiscais que atendam à seguintes regras:

* Lançamentos Fiscais de Entrada
* CFOP de Devolução
* O Item referenciado (item devolvido) deve ter saído no registro 1510.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| M01d | REG | Registro 1520 | Texto fixo contendo 1520 |
| M02d | DT\_DOC | Data de Emissão do documento fiscal NO Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| M03d | CST\_CSOSN | Código da Situação Tributária | CST informado no Item do Lançamento Fiscal  DITEM.CST  No caso do CSOSN, buscar da Regra de ICMS associada ao CFOP. |
| M04d | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| M05d | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| M06d | CNPJ\_EMIT | CNPJ Emitente | No caso de consumidor final, via de regra, a própria Filial emite a nota fiscal da entrada. Logo, devem ser gerados os dados do Cli/For associado ou da Filial, caso esta seja informada como emitente.  FCFO.CGCCFO  FCFO.CODETD  GFILIAL.CGC  GFILIAL.ESTADO |
| M07d | UF\_EMIT | UF Emitente |
| M08d | CNPJ\_DEST | CNPJ do destinatário |
| M09d | UF\_DEST | UF do Destinatário |
| M10d | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 1101. |
| M11d | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| M12d | UNID\_ITEM | Unidade de medida do item utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| M13d | QTD\_DEVOLVIDA | Quantidade do item devolvida convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, converter para esta. |
| M14d | VL\_UNIT\_ITEM | Valor unitário líquido do item | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| M15d | CHAVE\_REF | Chave de acesso do documento fiscal referenciado | Chave de acesso do Lançamento Fiscal de saída referenciado  DLAF.CHAVEACESSONFE |
| M16d | N\_ITEM\_REF | Número do item no documento fiscal referenciado | Ordem sequencial do item no documento fiscal de saída referenciado  DITEM.NUMITEM |
