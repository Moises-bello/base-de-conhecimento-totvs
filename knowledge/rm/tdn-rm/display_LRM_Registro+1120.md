---
content_hash: 35faaf5faff82769b99a66ead6e8c4e45cfdf1d93f9e5da27aa1911ca728d53f
fetched_at: '2026-06-29T00:10:45.996924+00:00'
page_id: '553905989'
product: rm
source: tdn-rm
title: Registro 1120
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1120
version: 8
---

**Registro das notas fiscais de devolução das entradas**

Este registro deve conter as notas fiscais de devoluções das compras ocorridas no mês de geração da rotina.

Devem ser selecionados os lançamentos que atendam às seguintes regras:

* Lançamentos Fiscais de Saída
* CFOP de Devolução
* Entrada referenciada tenha ocorrido dentro do próprio mês considerando a DATLF. Ou seja, a respectiva entrada deve estar no Registro 1110.  
  **Importante:**No caso da Saída de devolução deverá ser acessado o Lançamento de Saída e nele referenciar a entrada que já está sendo gerada no registro 1110.   
  (Não confundir referenciando a Saída no lançamento de entrada, nesse caso a referência é colocada no lançamento de Saída).

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| E01d | REG | Registro 1120 | Texto fixo contendo 1120 |
| E02d | DT\_DOC | Data de Emissão do documento fiscal no Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| E03d | CST\_CSOSN | Código da Situação Tributária | Se a Filial for Optante pelo Simples, será gerado com o CSOSN da Regra de ICMS associada ao CFOP.  Caso contrário, será gerado com o CST informado no Item do Lançamento Fiscal (DITEM.CST). |
| E04d | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| E05d | N\_NF | Número do documento fiscal | DLAF.DOCINI |
| E06d | CNPJ\_EMIT | CNPJ Emitente | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| E07d | UF\_EMIT | UF emitente |
| E08d | CNPJ\_DEST | CNPJ do destinatário | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| E09d | UF\_DEST | UF do Destinatário |
| E10d | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 1101. |
| E11d | N\_ITEM | Número do item do produto no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| E12d | UNID\_ITEM | Unidade de medida do item  utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| E13d | QTD\_DEVOLVIDA | Informar a quantidade do item devolvida, convertida na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do registro 1000. | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E14d | VL\_UNIT\_ITEM | Informar o valor unitário líquido de aquisição do item, convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do registro 1000. | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E15d | VL\_BC\_ICMS\_ST | Base de cálculo do ICMS ST | Base de Cálculo do ICMS ST informado no Item  DITEM.BASEICMSSTPRD  Se não houver Base de Cálculo do ICMS-ST informada, preencher com o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E16d | VL\_ICMS\_SUPORT\_ENTR | Corresponde ao valor total do imposto suportado pelo contribuinte substituído, abrangendo o imposto incidente na operação própria do substituto e o retido por ST, incluída a parcela do FECOP, se houver | Será a soma dos tributos ICMS e ICMSST informados no Item, pasta Valores ICMS.  (DITEM.VLRICMSPRD + DITEM.VLRICMSSTPRD)  Se não houver Base de Cálculo do ICMS-ST informada, preencher com o valor da operação:  (Campo E16 \* Alíquota interna do Produto na UF)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E17d | CHAVE\_REF | Chave de acesso do documento fiscal referenciado | Chave de acesso do Lançamento Fiscal de entrada referenciado  DLAF.CHAVEACESSONFE |
| E18d | N\_ITEM\_REF | Número do item no documento fiscal referenciado | Ordem sequencial do item no documento fiscal de entrada referenciado  DITEM.NUMITEM |
