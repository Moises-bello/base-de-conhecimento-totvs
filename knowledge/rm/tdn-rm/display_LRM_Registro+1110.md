---
content_hash: 8df421481cf1b3e0625b44c24a66941d5ae59538219cc9584849a3b2ae554e5f
fetched_at: '2026-06-29T00:10:45.988542+00:00'
page_id: '553905981'
product: rm
source: tdn-rm
title: Registro 1110
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1110
version: 10
---

**Registro das notas fiscais de entrada**

Este registro deve conter todas as notas fiscais de entrada da mercadoria declaradas no registro 1000, no período de referência. Se a quantidade declarada no mês de referência for insuficiente para acobertar o total das saídas declaradas nos registros 1200, 1300, 1400 e 1500, o contribuinte deverá retroagir aos meses anteriores até obter a quantidade suficiente para acobertar a quantidade das saídas da mesma mercadoria.

Serão gerados os Lançamentos Fiscais de Entrada de qualquer período que estejam associados aos Lançamentos Fiscais de saída relacionados nos registros 1210, 1310, 1410 e 1510, através do processo de [Associação Lançamentos de Saída](https://tdn.totvs.com/pages/viewpage.action?pageId=438273534).

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| E01 | REG | Registro 1110 | Texto fixo contendo 1110 |
| E02 | DT\_DOC | Data de Emissão do documento fiscal no Formato: DDMMAAAA | DLAF.DATAEMISSAO |
| E03 | COD\_RESP\_RET | Código que indica o responsável pela retenção do ICMS-ST:  1 – Remetente direto 2 – Remetente indireto 3 – Próprio declarante | Esse campo será gerado de acordo com o campo "**Situação da Retenção ICMS ST**" na pasta Dados ICMS ST da Regra do ICMS (DREGRAICMS.RETENCAOICMSST):   * Substituto Tributário = 1 * Não Se Aplica = 2 * Antecipação = 3 |
| E04 | CST\_CSOSN | Código da Situação Tributária | Se a Filial for Optante pelo Simples, será gerado com o CSOSN da Regra de ICMS associada ao CFOP. O CSOSN será gerado com um tamanho máximo de 3 posições.  Caso contrário, será gerado com o CST informado no Item do Lançamento Fiscal (DITEM.CST). O campo CST será gerado com 2 posições.  Ex.: CST com valor 010, será gerado com o valor 10. |
| E05 | CHAVE | Chave de acesso do documento fiscal eletrônico | DLAF.CHAVEACESSONFE |
| E06 | N\_NF | Número do documento fiscal | DLAF.DOCINI |
| E07 | CNPJ\_EMIT | CNPJ Emitente | Dados do Cliente/Fornecedor associado ao Lançamento Fiscal:  FCFO.CGCCFO  FCFO.CODETD |
| E08 | UF\_EMIT | UF emitente |
| E09 | CNPJ\_DEST | CNPJ do destinatário | Dados da própria Filial  GFILIAL.CGC  GFILIAL.ESTADO |
| E10 | UF\_DEST | UF do Destinatário |
| E11 | CFOP | Código fiscal de operação e prestação | Gerar com o código sintético do CFOP associado ao Lançamento Fiscal. Ex: 5101. |
| E12 | N\_ITEM | Número do item do produto no documento fiscal | Ordem sequencial do item no documento fiscal  DITEM.NUMITEM |
| E13 | UNID\_ITEM | Unidade de medida do item  utilizada para quantificação do estoque declarada no campo B09 do registro 1000 | Unidade de controle do estoque do item, a mesma declarada no Registro 1000, campo B09:  TPRODUTODEF.CODUNDCONTROLE |
| E14 | QTD\_ENTRADA | Informar a quantidade do item adquirido, convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Quantidade do item.  DITEM.QTDEPRD  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E15 | VL\_UNIT\_ITEM | Informar o valor unitário líquido de aquisição do item convertido na mesma unidade de medida declarada no campo B09 [UNID\_ITEM] do Registro 1000 | Valor unitário do item. Considerar demais valores que compõe o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E16 | VL\_BC\_ICMS\_ST | Base de cálculo do ICMS ST | Base de Cálculo do ICMS ST informado no Item  DITEM.BASEICMSSTPRD  Se não houver Base de Cálculo do ICMS-ST informada, preencher com o valor da operação:  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
| E17 | VL\_ICMS\_SUPORT\_ENTR | Corresponde ao valor total do imposto suportado pelo contribuinte substituído, abrangendo o imposto incidente na operação própria do substituto e o retido por ST, incluída a parcela do FECOP, se houver. | Será a soma dos tributos ICMS e ICMSST informados no Item, pasta Valores ICMS.  (DITEM.VLRICMSPRD + DITEM.VLRICMSSTPRD)  Se não houver Base de Cálculo do ICMS-ST informada, preencher com o valor da operação:  (Campo E16 \* Alíquota interna do Produto na UF)  Se a unidade informada no lançamento for diferente da unidade de controle do estoque, será aplicado o Fator de Conversão entre as unidades. |
