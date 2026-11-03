---
content_hash: 18e335b31b816076472342008093bbe65466d4967e1ef1c3cfc303373dbad886
fetched_at: '2026-06-29T00:10:46.035533+00:00'
page_id: '553906017'
product: rm
source: tdn-rm
title: Registro 1320
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1320
version: 7
---

**Registro das notas fiscais de devolução das saídas para outros estados**

Neste registro deve conter as notas fiscais de devoluções de vendas ocorridas no mesmo mês da venda.

Devem ser selecionados os lançamentos fiscais que atendam à seguintes regras:

* Lançamentos Fiscais de Entrada
* CFOP de Devolução
* O Item referenciado (item devolvido) deve ter saído no registro 1310.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| I01d | REG | Registro 1320 | Texto fixo contendo 1320 |
| I02d | DT\_DOC | Data de Emissão do documento fiscal NO Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| I03d | CST\_CSOSN | Código da Situação Tributária | CST informado no Item do Lançamento Fiscal  DITEM.CST  No caso do CSOSN, buscar da Regra de ICMS associada ao CFOP. |
| I04d | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| I05d | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| I06d | CNPJ\_EMIT | CNPJ Emitente | Dados do Emitente do Lançamento Fiscal. Pode ser um Cli\For ou a própria Filial  FCFO.CGCCFO / GFILIAL.CGC  FCFO.CODETD / GFILIAL.ESTADO |
| I07d | UF\_EMIT | UF Emitente |
| I08d | CNPJ\_CPF\_DEST | CNPJ ou CPF do destinatário | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| I09d | UF\_DEST | UF do Destinatário |
| I10d | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 1101. |
| I11d | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| I12d | UNID\_ITEM | Unidade de medida do item utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| I13d | QTD\_DEVOLVIDA | Quantidade do item devolvida convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| I14d | VL\_UNIT\_ITEM | Valor unitário líquido do item | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| I15d | VL\_ICMS\_EFETIVO | Valor do ICMS efetivo na saída  É o valor do imposto da própria operação interestadual destacado na nota fiscal. | Deve ser preenchido com o valor do ICMS informado para o item  DITEM.VLRICMSPRD |
| I16d | CHAVE\_REF | Chave de acesso do documento fiscal referenciado | Chave de acesso do Lançamento Fiscal de saída referenciado  DLAF.CHAVEACESSONFE |
| I17d | N\_ITEM\_REF | Número do item no documento fiscal referenciado | Ordem sequencial do item no documento fiscal de saída referenciado  DITEM.NUMITEM |
