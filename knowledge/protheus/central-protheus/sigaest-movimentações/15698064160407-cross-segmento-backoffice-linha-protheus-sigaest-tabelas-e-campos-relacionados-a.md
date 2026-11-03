---
article_id: 15698064160407
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b298286588b96e1e619d90408f7e9e8523e9020684b9add0c81602ec0fd47b4c
fetched_at: '2026-06-28T22:38:57.429709+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tabelas e Campos relacionados
  a Rastreabilidade por Lote/Sublote
type: support-article
updated_at: '2023-06-30T19:36:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15698064160407-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tabelas-e-Campos-relacionados-a-Rastreabilidade-por-Lote-Sublote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15698076517527) Tempo aproximado para leitura: **00:04:12 min** **Dúvida**Quais são os campos e tabelas que tem relação com o controle de Lote e  Sublote no *Protheus*?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Segue abaixo a lista completa de Tabelas e Campos de Saldos e Movimentações que tem relação direta com controle de rastreabilidade.

**Tabelas e campos:**

Observação: Os campos já estão contidos no dicionário nativo do Protheus, não é necessária a execução do UPDDISTR.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **X3\_ARQUIVO** | **X3\_ORDEM** | **X3\_CAMPO** | **X3\_TIPO** | **X3\_TAMANHO** | **X3\_DECIMAL** | **X3\_TITULO** | **X3\_TITSPA** | **X3\_TITENG** | **X3\_DESCRIC** |
| SB1 | 57 | B1\_RASTRO | C | 1 |  | Rastro | Seguimiento | Tracking | Rastreabilidade Produto |
| SB1 | 75 | B1\_FORMLOT | C | 3 |  | Cod Form Lot | Cod For.Subl | Lot Formula | Cod. Formula preen. Lote |
| SB7 | 10 | B7\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SB7 | 11 | B7\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SB7 | 12 | B7\_DTVALID | D | 8 |  | Data Validad | Fch Validez | Validity Dt. | Data de Validade do Lote |
| SB8 | 01 | B8\_FILIAL | C | 8 |  | Filial | Sucursal | Branch | Filial do Sistema |
| SB8 | 02 | B8\_QTDORI | N | 14 | 2 | Qtd.Original | Ctd.Original | Original Qty | Quantidade Original |
| SB8 | 03 | B8\_PRODUTO | C | 15 |  | Produto | Producto | Product | Codigo do Produto |
| SB8 | 04 | B8\_LOCAL | C | 2 |  | Armazem | Deposito | Warehouse | Armazem |
| SB8 | 05 | B8\_DATA | D | 8 |  | Data | Fecha | Date | Data da CriaþÒo do Lote |
| SB8 | 06 | B8\_DTVALID | D | 8 |  | Data Validad | Fch Validez | Validity Dt. | Data de Validade do Lote |
| SB8 | 07 | B8\_SALDO | N | 14 | 2 | Saldo Lote | Sldo Lote | Lot Balance | Saldo do Lote |
| SB8 | 08 | B8\_EMPENHO | N | 14 | 2 | Emp. do Lote | Res. Lote | Lot Alloc. | Empenho do Lote |
| SB8 | 09 | B8\_ORIGLAN | C | 2 |  | Origem Lcto. | Origen Reg. | Origin Entry | Origem do Lancamento |
| SB8 | 10 | B8\_LOTEFOR | C | 18 |  | Lote Fornec. | Lote Prov | Supplier Lot | NÀm. Lote no Fornecedor |
| SB8 | 11 | B8\_CHAVE | C | 36 |  | Chave Acesso | Clave Acceso | Access Code | Chave de Acesso SD1/SD3 |
| SB8 | 12 | B8\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SB8 | 13 | B8\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SB8 | 14 | B8\_QEMPPRE | N | 14 | 4 | Empen. Previ | Res. Previs. | Alloc.Expect | Quantidade Empenhada Prev |
| SB8 | 15 | B8\_QACLASS | N | 14 | 2 | Qtd. Distrib | Cantidad | Quantity | Quantidade a Distribuir |
| SB8 | 16 | B8\_SALDO2 | N | 14 | 2 | Sdo.Lote 2UM | Sdo Lote2 | 2UM Lot Bal. | Saldo do Lote 2a UM |
| SB8 | 17 | B8\_QTDORI2 | N | 14 | 2 | Qtd.Orig.2UM | Ctd.Orig.2UM | Oirg.Qty 2 | Quantidade Original 2a UM |
| SB8 | 18 | B8\_EMPENH2 | N | 14 | 2 | Emp.Lote 2UM | Res. Lote2 | 2UM Lot Allo | Empenho do Lote 2a UM |
| SB8 | 19 | B8\_QEPRE2 | N | 14 | 4 | Emp.Prev.2UM | +Res.Prev.2? | Fore.Alloc.2 | Qtde Emp. Prevista 2a UM |
| SB8 | 20 | B8\_QACLAS2 | N | 14 | 2 | Qtd.Dist.2UM | Cantidad 2 | Quantity 2 | Qtde a Distribuir 2a UM |
| SB8 | 21 | B8\_DOC | C | 9 |  | Documento | Documento | Document | Numero do Documento |
| SB8 | 22 | B8\_SERIE | C | 3 |  | Serie | Serie | Series | Serie do Documento |
| SB8 | 23 | B8\_CLIFOR | C | 6 |  | Clie/Forn | Clien/Provee | Cust./Sup. | Cod. Cliente/Fornecedor |
| SB8 | 24 | B8\_LOJA | C | 2 |  | Loja | Tienda | Unit | Loja Cliente/Fornecedor |
| SB8 | 25 | B8\_CODGRP | C | 4 |  | Grupo | Grupo | Group | Grupo Veiculos/Oficina |
| SB8 | 26 | B8\_CODITE | C | 27 |  | Cod. Produto | Cod.Producto | Product Code | Produto Veiculos/Oficina |
| SB8 | 27 | B8\_POTENCI | N | 6 | 2 | Potencia Lot | Potencia Lot | Lot pot. | Potencia do Lote |
| SB8 | 28 | B8\_PRCLOT | N | 12 | 2 | Preco Lote | Precio Lote | Lot Price | Preco do Lote |
| SB8 | 29 | B8\_ITEM | C | 4 |  | Item NF | Item Fac. | Invoice item | Item da Nota Fiscal |
| SB8 | 30 | B8\_NUMDESP | C | 16 |  | Nro Despacho | Nro Envio | Despatch Nbr | Numero do Despacho |
| SB8 | 31 | B8\_ORIGEM | C | 3 |  | Origem Imp. | Origen Imp. | Imp.Origin | Origem da Importacõo |
| SB8 | 32 | B8\_DFABRIC | D | 8 |  | Data Fabric | Fecha Fabric | Manuf Date | Data de FabricaþÒo Lote |
| SB8 | 33 | B8\_SDOC | C | 3 |  | SÚrie Doc. | Serie Doc. | Inv. Series | SÚrie do Documento Fiscal |
| SBJ | 01 | BJ\_FILIAL | C | 8 |  | Filial | Sucursal | Branch | Filial do Sistema |
| SBJ | 02 | BJ\_COD | C | 15 |  | Produto | Producto | Product | Codigo do produto |
| SBJ | 03 | BJ\_LOCAL | C | 2 |  | Armazem | Deposito | Warehouse | Armazem do Produto |
| SBJ | 04 | BJ\_DATA | D | 8 |  | Data Saldo | Fecha Saldo | Balance Date | Data Saldo inicial |
| SBJ | 05 | BJ\_QINI | N | 14 | 2 | Qtd.Inic.Mes | Ctd.Inic.Mes | Mth.Int.Qty. | Qtde inicial no mes |
| SBJ | 06 | BJ\_QISEGUM | N | 14 | 2 | Qt.Ini.2a UM | Ct.Ini.2a UM | In.Qt.Mt.2UM | Qtde inicial no mes 2a.UM |
| SBJ | 07 | BJ\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SBJ | 08 | BJ\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SBJ | 09 | BJ\_DTVALID | D | 8 |  | Dt. Validade | Fc. Validez | Validity Dt. | Data de Validade |
| SC6 | 51 | C6\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SC6 | 52 | C6\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SC6 | 53 | C6\_DTVALID | D | 8 |  | Valid. Lote | Vald.Lote | Lot Validity | Validade do Lote Inform. |
| SC9 | 21 | C9\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SC9 | 22 | C9\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SC9 | 26 | C9\_DTVALID | D | 8 |  | Dt. Validade | Fch Validez | Validity Dt. | Data de Validade do Lote |
| SD1 | 56 | D1\_LOTEFOR | C | 18 |  | Lote Fornec. | Lote Proveed | Supplier Lot | NÀ[m.do](http://m.do/) Lote no Fornecedor |
| SD1 | 60 | D1\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SD1 | 61 | D1\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SD1 | 62 | D1\_DTVALID | D | 8 |  | Valid. Lote | Validez Lote | Lot Validity | Validade do Lote inform. |
| SD2 | 60 | D2\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SD2 | 61 | D2\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SD2 | 62 | D2\_DTVALID | D | 8 |  | Valid. Lote | Validez Lote | Lot Validity | Validade do Lote Inform. |
| SD3 | 36 | D3\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SD3 | 37 | D3\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SD3 | 38 | D3\_DTVALID | D | 8 |  | Valid. Lote | Vald.Lote | Lot Validity | Validade do Lote inform. |
| SD4 | 11 | D4\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SD4 | 12 | D4\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SD4 | 13 | D4\_DTVALID | D | 8 |  | Data Validad | Fch Validez | Validity Dt. | Data de Validade do Lote |
| SD5 | 01 | D5\_FILIAL | C | 8 |  | Filial | Sucursal | Branch | Filial do Sistema |
| SD5 | 02 | D5\_LOTEFOR | C | 18 |  | Lote Fornec. | Lote Prov | Supplier Lot | NÀm. Lote no Fornecedor |
| SD5 | 03 | D5\_PRODUTO | C | 15 |  | Produto | Producto | Product | Codigo do Produto |
| SD5 | 04 | D5\_LOCAL | C | 2 |  | Armazem | Deposito | Warehouse | Armazem |
| SD5 | 05 | D5\_DOC | C | 9 |  | Documento | Documento | Document | Documento |
| SD5 | 06 | D5\_SERIE | C | 3 |  | Serie | Serie | Series | SÚrie |
| SD5 | 07 | D5\_OP | C | 14 |  | O.P. | O.P. | P.O. | Ordem de ProduþÒo |
| SD5 | 08 | D5\_DATA | D | 8 |  | Data Movim. | Fch  Movim. | Movement Dt. | Data da MovimentaþÒo |
| SD5 | 09 | D5\_ORIGLAN | C | 3 |  | Origem Lcto. | Origen Reg. | Entry Origin | Origem do Lanþamento |
| SD5 | 10 | D5\_NUMSEQ | C | 6 |  | Sequencial | Secuencial | Sequential | Numero Sequencial |
| SD5 | 11 | D5\_CLIFOR | C | 6 |  | Cliente/Forn | Clien/Provee | Cust./Supp. | Cliente/Fornecedor |
| SD5 | 12 | D5\_LOJA | C | 2 |  | Loja Cli/For | Tda.Cli/Prov | Unit | Loja Cliente/Fornecedor |
| SD5 | 13 | D5\_QUANT | N | 12 | 2 | Quantidade | Cantidad | Quantity | Quantidade |
| SD5 | 14 | D5\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SD5 | 15 | D5\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |
| SD5 | 16 | D5\_DTVALID | D | 8 |  | Valid. Lote | Vald.Lote | Lot Validity | Validade do Lote inform. |
| SD5 | 17 | D5\_QTSEGUM | N | 12 | 2 | Qtd. 2a UM | Ctd. 2a. UM | 2nd.Unit Mea | Quantidade 2a UM |
| SD5 | 18 | D5\_ESTORNO | C | 1 |  | Estornado | Devolucion | Reversed | Indica se Mov. Estornado |
| SD5 | 19 | D5\_CODGRP | C | 4 |  | Grupo | Grupo | Group | Grupo Veiculos/Oficina |
| SD5 | 20 | D5\_CODITE | C | 27 |  | Cod. Produto | Cod.Producto | Product Code | Produto Veiculos/Oficina |
| SD5 | 21 | D5\_POTENCI | N | 6 | 2 | Potencia Lot | Potencia Lot | Lot potency | Potencia do Lote |
| SD5 | 22 | D5\_SLDINI | C | 2 |  | Lote inicial | Lote inicial | Initial Lot | Lote inicial |
| SD5 | 23 | D5\_SLOTEPR | C | 6 |  | SubLote Prod | Sublote Prod | Prod.Sublot | Sub Lote produzido |
| SD5 | 24 | D5\_LOTEPRD | C | 10 |  | Lote produzi | Lote prod. | Produced Lot | Lote produzido |
| SD5 | 25 | D5\_PRMAIOR | C | 1 |  | Prod Maior | Prod Mayor | Greater Prod | Prod Maior |
| SD5 | 26 | D5\_SDOC | C | 3 |  | SÚrie Doc. | Serie Doc. | Inv. Series | SÚrie do Documento Fiscal |
| SD7 | 18 | D7\_LOTECTL | C | 10 |  | Lote | Lote | Lot | Lote |
| SD7 | 19 | D7\_NUMLOTE | C | 6 |  | Sub-Lote | Sublote | Sublot | Sub-Lote |

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Habilitando o Controle de Rastreabilidade no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020604251-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Habilitando-o-Controle-de-Rastreabilidade-no-Protheus)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
