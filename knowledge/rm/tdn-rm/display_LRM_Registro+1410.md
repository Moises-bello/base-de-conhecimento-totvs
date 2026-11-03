---
content_hash: 4659de3f0d8b7c1b7adcdd3172c94bfee8ab154ba34648cccfb99fc839944bd0
fetched_at: '2026-06-29T00:10:46.047513+00:00'
page_id: '553906024'
product: rm
source: tdn-rm
title: Registro 1410
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1410
version: 7
---

**Registro das notas fiscais de saídas internas que trata o art. 119 do RICMS/17**

O artigo 119 do RICMS/PR diz respeito ao diferimento nas operações internas destinadas a contribuintes do ICMS.  Logo, devem ser selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamento Fiscal de Saída
* Operação Dentro do Estado
* Operação com Diferimento do ICMS (Regra ICMS, campo **Tipo Tributação** = Diferido)
* Cuja DATALF esteja dentro do período da rotina
* Tenham movimentado produtos marcados como "**Tributado pelo ICMS-ST**" para o Estado da Filial (Anexo Dados Fiscais por UF)

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| K01 | REG | Registro 1410 | Texto fixo contendo 1410 |
| K02 | DT\_DOC | Data de Emissão do documento fiscal | DLAF.DATAEMISSAO |
| K03 | CST\_CSOSN | Código da Situação Tributária | CST informado no Item do Lançamento Fiscal  DITEM.CST  No caso do CSOSN, buscar da Regra de ICMS associada ao CFOP. |
| K04 | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| K05 | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| K06 | CNPJ\_EMIT | CNPJ Emitente | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| K07 | UF\_EMIT | UF Emitente |
| K08 | CNPJ\_DEST | CNPJ do destinatário | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| K09 | UF\_DEST | UF do Destinatário |
| K10 | CFOP | Código fiscal de operação e prestação | Gerar com o CFOP associado ao Lançamento Fiscal.  (OBS. Não há orientações no Manual sobre esse campo. Por isso deve ser gerado com o CFOP até o segundo nível, ou seja, desconsiderando nível analítico) |
| K11 | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NSEQITMMOV |
| K12 | UNID\_ITEM | Unidade de medida do item | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| K13 | QTD\_SAIDA | Quantidade do produto na saída, convertida na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000. | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, converter para esta. |
| K14 | VL\_UNIT\_ITEM | Valor unitário líquido do item | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, preencher o valor unitário considerando esta. |
| K15 | VL\_ICMS\_EFET | Valor do ICMS efetivo na saída  É o resultado da multiplicação da alíquota interna da mercadoria sobre o valor da operação de saída, ou na hipótese de operação beneficiada com redução da base de cálculo, sobre a base de cálculo reduzida, caso a operação fosse tributada. | Esse campo deve ser calculado sobre o valor da operação, considerando redução de BC se houver, aplicando-se a alíquota interna do produto.  ((Campo K13 \* Campo K14) \* Alíquota interna do Produto na UF) |
