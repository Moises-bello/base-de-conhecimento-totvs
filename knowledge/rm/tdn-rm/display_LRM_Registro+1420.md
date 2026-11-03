---
content_hash: 12aebf50b22bf2373b362ebf739c154ada0955ad40d96a1f211e40602a60dbc9
fetched_at: '2026-06-29T00:10:46.054010+00:00'
page_id: '553906029'
product: rm
source: tdn-rm
title: Registro 1420
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1420
version: 4
---

**Registro das notas fiscais de devolução das saídas internas que trata o art. 119 do RICMS/17**

Este registro deve conter as notas fiscais de devoluções de vendas ocorridas no mesmo mês em que foi computada a saída.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| K01d | REG | Registro 1420 | Texto fixo contendo 1420 |
| K02d | DT\_DOC | Data de Emissão do documento fiscal no Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| K03d | CST\_CSOSN | Código da Situação Tributária | CST informado no Item do Lançamento Fiscal  DITEM.CST  No caso do CSOSN, buscar da Regra de ICMS associada ao CFOP. |
| K04d | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| K05d | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| K06d | CNPJ\_EMIT | CNPJ Emitente | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| K07d | UF\_EMIT | UF Emitente |
| K08d | CNPJ\_DEST | CNPJ do destinatário | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| K09d | UF\_DEST | UF do Destinatário |
| K10d | CFOP | Código fiscal de operação e prestação | Gerar com o CFOP associado ao Lançamento Fiscal.  (OBS. Não há orientações no Manual sobre esse campo. Por isso deve ser gerado com o CFOP até o segundo nível, ou seja, desconsiderando nível analítico) |
| K11d | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NSEQITMMOV |
| K12d | UNID\_ITEM | Unidade de medida do item utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| K13d | QTD\_DEVOLVIDA | Quantidade do item devolvida convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, converter para esta. |
| K14d | VL\_UNIT\_ITEM | Valor unitário líquido do item | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, preencher o valor unitário considerando esta. |
| K15d | VL\_ICMS\_EFETIVO | Valor do ICMS efetivo na saída  É o resultado da multiplicação da alíquota vigente para as operações internas sobre o valor da operação de saída, ou na hipótese de operação beneficiada com redução da base de cálculo, sobre a base de cálculo reduzida, caso a operação fosse tributada. | É o mesmo valor informado no campo G15 do Registro 1210, porém, considerando apenas a quantidade que está sendo devolvida.  ((Campo I13d \* Campo I14d) \* Alíquota interna do Produto na UF) |
| K16d | CHAVE\_REF | Chave de acesso do documento fiscal referenciado | Chave de acesso do Lançamento Fiscal de saída referenciado  DLAF.CHAVEACESSONFE |
| K17d | N\_ITEM\_REF | Número do item no documento fiscal referenciado | Ordem sequencial do item no documento fiscal de saída referenciado  DITEM.NSEQITMMOV |
