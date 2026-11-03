---
content_hash: 77d77cdce901dfe430037c40547ebf507d357d34a792ce8dd520310573431c9b
fetched_at: '2026-06-29T00:10:46.028772+00:00'
page_id: '553906013'
product: rm
source: tdn-rm
title: Registro 1310
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1310
version: 10
---

**Registro das notas fiscais de saída para outros estados**

Este registro deve conter todas as notas fiscais de saída emitidas para **outros estados**, do produto declarado no registro 1000.

Devem ser selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamento Fiscal de Saída
* Operação Fora do Estado
* Cuja DATALF esteja dentro do período da rotina
* Tenham movimentado produtos marcados como "**Tributado pelo ICMS-ST**" para o Estado da Filial e Data de Início da Tributação ST maior ou igual início do período da rotina (Anexo Dados Fiscais por UF)

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| I01 | REG | Registro 1310 | Texto fixo contendo 1310 |
| I02 | DT\_DOC | Data de Emissão do documento fiscal no Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| I03 | CST\_CSOSN | Código da Situação Tributária | CST informado no Item do Lançamento Fiscal  DITEM.CST  No caso do CSOSN, buscar da Regra de ICMS associada ao CFOP. |
| I04 | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| I05 | N\_NF | Número do documento Fiscal | DLAF.DOCINI |
| I06 | CNPJ\_EMIT | CNPJ Emitente | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| I07 | UF\_EMIT | UF Emitente |
| I08 | CNPJ\_CPF\_DEST | CNPJ ou CPF do destinatário | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| I09 | UF\_DEST | UF do Destinatário |
| I10 | CFOP | Código fiscal de operação e prestação | Gerar com o CFOP associado ao Lançamento Fiscal.  (OBS. Não há orientações no Manual sobre esse campo. Por isso deve ser gerado com o CFOP até o segundo nível, ou seja, desconsiderando nível analítico) |
| I11 | N\_ITEM | Número do item no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| I12 | UNID\_ITEM | Unidade de medida do item utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| I13 | QTD\_SAIDA | Quantidade do produto na saída na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, converter para esta. |
| I14 | VL\_UNIT\_ITEM | Valor unitário líquido do item (considerando descontos) | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, preencher o valor unitário considerando esta. |
| I15 | VL\_ICMS\_EFET | Valor do ICMS efetivo na saída  É o valor do imposto da própria operação interestadual destacado na nota fiscal | Deve ser preenchido com o valor do ICMS informado para o item  DITEM.VLRICMSPRD  Quando no campo não houver valor ou fora zerado o mesmo será gerado em branco. |
