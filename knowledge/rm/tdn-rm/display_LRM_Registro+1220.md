---
content_hash: 6d383e806e5d0058d6c48e1475bd0124ff73b89cc5d1316482ab7841601e9b81
fetched_at: '2026-06-29T00:10:46.017228+00:00'
page_id: '553906006'
product: rm
source: tdn-rm
title: Registro 1220
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1220
version: 8
---

**Registro das notas fiscais de devolução das saídas internas para consumidor final**

Neste registro devem ser demonstradas as notas fiscais de devolução de vendas ocorridas no mesmo mês da venda.

Devem ser selecionados os lançamentos fiscais que atendam à seguintes regras:

* Lançamentos Fiscais de Entrada
* CFOP de Devolução
* O Item referenciado (item devolvido) deve ter saído no registro 1210.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| G01d | REG | Registro 1220 | Texto fixo contendo 1220 |
| G02d | DT\_DOC | Data de Emissão do documento fiscal NO Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| G03d | CST\_CSOSN | Código da Situação Tributária | Se a Filial for Optante pelo Simples, será gerado com o CSOSN da Regra de ICMS associada ao CFOP.  Caso contrário, será gerado com o CST informado no Item do Lançamento Fiscal (DITEM.CST). |
| G04d | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| G05d | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| G06d | CNPJ\_EMIT | CNPJ Emitente | No caso de consumidor final, via de regra, a própria Filial emite a nota fiscal da entrada. Logo, devem ser gerados os dados do Cli/For associado ou da Filial, caso esta seja informada como emitente.  FCFO.CGCCFO  FCFO.CODETD  GFILIAL.CGC  GFILIAL.ESTADO |
| G07d | UF\_EMIT | UF Emitente |
| G08d | CNPJ\_CPF\_DEST | CNPJ ou CPF do destinatário | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| G09d | UF\_DEST | UF do Destinatário |
| G10d | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 1101. |
| G11d | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| G12d | UNID\_ITEM | Unidade de medida do item utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| G13d | QTD\_DEVOLVIDA | Quantidade do item devolvida convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| G14d | VL\_UNIT\_ITEM | Valor unitário líquido do item | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO) / DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| G15d | VL\_ICMS\_EFETIVO | Valor do ICMS efetivo na saída  É o resultado da multiplicação da alíquota vigente para as operações internas sobre o valor da operação de venda a consumidor final | É o mesmo valor informado no campo G15 do Registro 1210, porém, considerando apenas a quantidade que está sendo devolvida.  ((Campo G13d \* Campo G14d) \* Alíquota interna do Produto na UF) |
| G16d | CHAVE\_REF | Chave de acesso do documento fiscal referenciado | Chave de acesso do Lançamento Fiscal de saída referenciado  DLAF.CHAVEACESSONFE |
| G17d | N\_ITEM\_REF | Número do item no documento fiscal referenciado | Ordem sequencial do item no documento fiscal de saída referenciado  DITEM.NUMITEM |
