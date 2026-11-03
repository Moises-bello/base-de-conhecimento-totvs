---
content_hash: 2d59f466c29f862521205f492bbc41901cec713f7d01a1644d65350773c091ae
fetched_at: '2026-06-29T00:09:20.436058+00:00'
page_id: '422545686'
product: rm
source: tdn-rm
title: Importação do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545686
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Carácter |  |  | FIXO("L") | Tipo da linha | X |  |
| 2 | 2 | 6 | 5 | Inteiro |  | DLAF | CODCOLIGADA | Coligada | X |  |
| 3 | 7 | 31 | 25 | Inteiro |  | DLAF | CODFILIAL | Código da Filial | X |  |
| 4 | 32 | 32 | 1 | Carácter |  | DLAF | TIPOLF | Tipo do Lançamento | X | Nota 1 |
| 5 | 33 | 37 | 5 | Inteiro |  | DLAF | CODCOLCFO | Coligada  Cliente/ Fornecedor | X |  |
| 6 | 38 | 62 | 25 | Carácter |  | DLAF | CODCFO | CNPJ / CPF / CEI do Cliente/Fornecedor/ Empresa | X |  |
| 7 | 63 | 82 | 20 | Carácter |  | DLAF | IDNAT | Código da Natureza de Operação | X |  |
| 8 | 83 | 92 | 10 | Data |  | DLAF | DATAES | Data de Entrada / Saída | X |  |
| 9 | 93 | 102 | 10 | Data |  | DLAF | DATAEMISSAO | Data de Emissão | X |  |
| 10 | 103 | 112 | 10 | Data |  | DLAF | DATALF | Data LF |  |  |
| 11 | 113 | 122 | 10 | Carácter |  | DLAF | CODTDO | Espécie | X |  |
| 12 | 123 | 126 | 4 | Carácter |  | DLAF | SERIEDOC | Série do Documento | X |  |
| 13 | 127 | 131 | 5 | Inteiro |  | DLAF | PARCELA | Parcela do Documento | X |  |
| 14 | 132 | 146 | 15 | Carácter |  | DLAF | DOCINI | Documento Inicial | X |  |
| 15 | 147 | 148 | 2 | Carácter |  | DLAF | CODETD | Sigla do Estado do Lançamento (UF), refere-se a UF da Operação Fiscal | X |  |
| 16 | 149 | 158 | 10 | Carácter |  | DLAF | CODTPRD | Código Tipo de Produto |  |  |
| 17 | 159 | 159 | 1 | Carácter |  | DLAF | FLAGCFO | FLAG identificador Cliente/ Fornecedor /  Empresa | X | Nota 2 |
| 18 | 160 | 160 | 1 | Carácter |  | DLAF | TIPOFRETE | Tipo de Frete |  | Nota 3 |
| 19 | 161 | 190 | 30 | Carácter |  | DLAF | IDPRD | Código do Produto |  |  |
| 20 | 191 | 191 | 1 | Carácter |  | DLAF | CONTRIBUINTE | Contribuinte |  | Nota 11 |
| 21 | 192 | 206 | 15 | Carácter |  | DLAF | DOCFIM | Documento Final |  |  |
| 22 | 207 | 221 | 15 | Valor | 4 | DLAF | VALORMERC | Valor da Mercadoria |  |  |
| 23 | 222 | 236 | 15 | Valor | 4 | DLAF | FRETE | Valor do Frete |  |  |
| 24 | 237 | 251 | 15 | Valor | 4 | DLAF | SEGURO | Valor do Seguro |  |  |
| 25 | 252 | 266 | 15 | Valor | 4 | DLAF | ACRESCIMO | Valor Acréscimo |  |  |
| 26 | 267 | 281 | 15 | Valor | 4 | DLAF | OUTROSACREC | Valor Outros Acréscimos |  |  |
| 27 | 282 | 296 | 15 | Valor | 4 | DLAF | DESCONTOS | Valor Descontos |  |  |
| 28 | 297 | 311 | 15 | Valor | 4 | DLAF | OUTROSDESC | Valor Outros Descontos |  |  |
| 29 | 312 | 326 | 15 | Valor | 4 | DLAF | VALORCONT | Valor Contábil |  |  |
| 30 | 327 | 341 | 15 | Valor | 4 | DLAF | BASEICMS | Valor Base de ICMS |  |  |
| 31 | 342 | 356 | 15 | Valor | 4 | DLAF | FATORICMS | Valor Fator de ICMS |  |  |
| 32 | 357 | 371 | 15 | Valor | 4 | DLAF | BASEREDICMS | Valor Base  Reduzida de ICMS |  |  |
| 33 | 372 | 386 | 15 | Valor | 4 | DLAF | ALIQICMS | Alíquota de ICMS |  |  |
| 34 | 387 | 401 | 15 | Valor | 4 | DLAF | VALORICMS | Valor de ICMS |  |  |
| 35 | 402 | 416 | 15 | Valor | 4 | DLAF | ISENTOICMS | Isento de ICMS |  |  |
| 36 | 417 | 431 | 15 | Valor | 4 | DLAF | OUTROSICMS | Outros de ICMS |  |  |
| 37 | 432 | 446 | 15 | Valor | 4 | DLAF | FATORSUBST | Fator Substituição Tributária |  |  |
| 38 | 447 | 461 | 15 | Valor | 4 | DLAF | BASESUBST | Valor da Base Substituição Tributária |  |  |
| 39 | 462 | 476 | 15 | Valor | 4 | DLAF | ALIQSUBST | Alíquota Substituição Tributária /. Alíquota Dif. Alíquota Interna |  |  |
| 40 | 477 | 491 | 15 | Valor | 4 | DLAF | VALORSUBST | Valor Substituição Tributária |  |  |
| 41 | 492 | 506 | 15 | Valor | 4 | DLAF | BASEIPI | Valor Base IPI |  |  |
| 42 | 507 | 521 | 15 | Valor | 4 | DLAF | VALORIPI | Valor IPI |  |  |
| 43 | 522 | 536 | 15 | Valor | 4 | DLAF | ISENTOIPI | Valor Isento IPI |  |  |
| 44 | 537 | 551 | 15 | Valor | 4 | DLAF | OUTROSIPI | Valor Outros IPI |  |  |
| 45 | 552 | 561 | 10 | Carácter |  | DLAF | SIMBOLO | Código da Moeda do Lançamento |  |  |
| 46 | 562 | 571 | 10 | Inteiro |  | DLAF | NUMLOTE | Número de Lote |  |  |
| 47 | 572 | 671 | 100 | Carácter |  |  |  | Observação |  |  |
| 48 | 672 | 681 | 10 | Data |  | DLAF | DATACONT | Data da Contabilização |  |  |
| 49 | 682 | 682 | 1 | Carácter |  | DLAF | INTEGFLUXUS | FLAG Identificador Integração com o TOTVS Gestão Financeira |  | Nota 4 |
| 50 | 683 | 697 | 15 | Valor | 4 | DLAF | DESCFINANC | Valor Descontos Financeiros |  |  |
| 51 | 698 | 707 | 10 | Data |  | DLAF | VENCIMENTO | Data de Vencimento do Documento |  |  |
| 52 | 708 | 732 | 25 | Carácter |  | DLAF | CODTB1FLX | Código da Tabela Opcional 1 TOTVS Gestão Financeira |  |  |
| 53 | 733 | 757 | 25 | Carácter |  | DLAF | CODTB2FLX | Código da Tabela Opcional 2 TOTVS Gestão Financeira |  |  |
| 54 | 758 | 782 | 25 | Carácter |  | DLAF | CODTB3FLX | Código da Tabela Opcional 3 TOTVS Gestão Financeira |  |  |
| 55 | 783 | 807 | 25 | Carácter |  | DLAF | CODTB4FLX | Código da Tabela Opcional 4 TOTVS Gestão Financeira |  |  |
| 56 | 808 | 832 | 25 | Carácter |  | DLAF | CODTB5FLX | Código da Tabela Opcional 5 TOTVS Gestão Financeira |  |  |
| 57 | 833 | 842 | 10 | Data |  | DLAF | DATABAIXA | Data de Baixa |  |  |
| 58 | 843 | 882 | 40 | Carácter |  | DLAF | CAMPOOPLF1 | Campo Opcional 1 do Lançamento |  |  |
| 59 | 883 | 922 | 40 | Carácter |  | DLAF | CAMPOOPLF2 | Campo Opcional 2 do Lançamento |  |  |
| 60 | 923 | 962 | 40 | Carácter |  | DLAF | CAMPOOPLF3 | Campo Opcional 3 do Lançamento |  |  |
| 61 | 963 | 1002 | 40 | Carácter |  | DLAF | CAMPOOPLF4 | Campo Opcional 4 do Lançamento |  |  |
| 62 | 1003 | 1017 | 15 | Valor | 2 | DLAF | VALOROPLF1 | Valor Opcional 1 do Lançamento |  |  |
| 63 | 1018 | 1032 | 15 | Valor | 2 | DLAF | VALOROPLF2 | Valor Opcional 2 do Lançamento |  |  |
| 64 | 1033 | 1047 | 15 | Valor | 2 | DLAF | VALOROPLF3 | Valor Opcional 3 do Lançamento |  |  |
| 65 | 1048 | 1062 | 15 | Valor | 2 | DLAF | VALOROPLF4 | Valor Opcional 4 do Lançamento |  |  |
| 66 | 1063 | 1072 | 10 | Data |  | DLAF | DATAOPLF1 | Data Opcional 1 do Lançamento |  |  |
| 67 | 1073 | 1082 | 10 | Data |  | DLAF | DATAOPLF2 | Data Opcional 2 do Lançamento |  |  |
| 68 | 1083 | 1092 | 10 | Data |  | DLAF | DATAOPLF3 | Data Opcional 3 do Lançamento |  |  |
| 69 | 1093 | 1102 | 10 | Data |  | DLAF | DATAOPLF4 | Data Opcional 4 do Lançamento |  |  |
| 70 | 1103 | 1103 | 1 | Carácter |  | DLAF | ORIGEMLF | Origem do Lançamento |  | Nota 5 |
| 71 | 1104 | 1104 | 1 | Carácter |  | DLAF | STATUSLF | Status do Lançamento |  | Nota 6 |
| 72 | 1105 | 1105 | 1 | Carácter |  | DLAF | STATUSEXPORTFLUXUS | Status Exportação TOTVS Gestão Financeira |  | Nota 4 |
| 73 | 1106 | 1106 | 1 | Carácter |  | DLAF | STATUSEXPORTLIBER | Status Exportação TOTVS Gestão Fiscal |  | Nota 11 |
| 74 | 1107 | 1107 | 1 | Carácter |  | DLAF | STATUSEXPORTFAZ | Status Exportação Secretaria da Fazenda |  | Nota 4 |
| 75 | 1108 | 1122 | 15 | Valor | 4 | DLAF | VALORDIFALIQ | Valor  Diferença de Alíquota |  |  |
| 76 | 1123 | 1137 | 15 | Valor | 4 | DLAF | BASEICMSDIFALIQ | Valor Base de Cálculo da Diferença de Alíquota |  |  |
| 77 | 1138 | 1152 | 15 | Valor | 4 | DLAF | ALIQICMSDIFALIQ | Valor Alíquota ICMS Diferença de Alíquota Interestadual |  |  |
| 78 | 1153 | 1153 | 1 | Carácter |  | DLAF | CONTABIL | FLAG Identificador Lançamento Contábil |  | Nota 7 |
| 79 | 1154 | 1158 | 5 | Inteiro |  | DLAF | FILIALRMSALDUS | Código Filial TOTVS Gestão Contábil |  |  |
| 80 | 1159 | 1159 | 1 | Carácter |  | DLAF | TIPOCONTFLUXUS | Tipo de Contabilização TOTVS Gestão Financeira |  | Nota 8 |
| 81 | 1160 | 1179 | 20 | Carácter |  | DLAF | SEGUNDONUMSEQ | Segundo Número Sequencial |  |  |
| 82 | 1180 | 1194 | 15 | Valor | 4 | DLAF | VALORIPIDIFALIQ | Valor IPI Diferença Alíquota |  |  |
| 83 | 1195 | 1195 | 1 | Carácter |  | DLAF | STATUSDIPI | Status Itens – Indica se Lançamento possui Itens |  | Nota 4 |
| 84 | 1196 | 1200 | 5 | Inteiro |  | DLAF | NUMPARCELA | Número Total de Parcelas |  |  |
| 85 | 1201 | 1215 | 15 | Valor | 4 | DLAF | VALORCONTTOTAL | Valor Contábil Total da Nota – Soma das Parcelas |  |  |
| 86 | 1216 | 1225 | 10 | Caracter |  | DLAF | CUPOMINICIAL | Número do Cupom Inicial |  |  |
| 87 | 1226 | 1235 | 10 | Carácter |  | DLAF | CUPOMFINAL | Número do Cupom Final |  |  |
| 88 | 1236 | 1238 | 3 | Carácter |  | DLAF | CODMAQ | Código da Máquina |  |  |
| 89 | 1239 | 1253 | 15 | Valor | 4 | DLAF | VALORFECHAICMS | Valor Fechamento ICMS |  |  |
| 90 | 1254 | 1268 | 15 | Valor | 4 | DLAF | VALORFECHAIPI | Valor Fechamento IPI |  |  |
| 91 | 1269 | 1283 | 15 | Valor | 4 | DLAF | VALORFECHAST | Valor Fechamento Subst. Tributária |  |  |
| 92 | 1284 | 1289 | 6 | Caracter |  |  |  | Branco |  | Informar branco - Campo Excluido da Tabela |
| 93 | 1290 | 1298 | 9 | Carácter |  | DLAF | NUMINIORDEM | Número Inicial da Ordem |  |  |
| 94 | 1299 | 1307 | 9 | Carácter |  | DLAF | NUMFINORDEM | Número Final da Ordem |  |  |
| 95 | 1308 | 1322 | 15 | Valor | 4 | DLAF | VALORIPIMERC | Valor IPI da Mercadoria |  |  |
| 96 | 1323 | 1327 | 5 | Inteiro |  | DLAF | CODCOLCFOORIGEMDESTINO | Código Coligada Cliente/Fornecedor Origem/Destino |  |  |
| 97 | 1328 | 1352 | 25 | Carácter |  | DLAF | CODCFOORIGEMDESTINO | Código / CNPJ Cliente/Fornecedor Origem/Destino |  |  |
| 98 | 1353 | 1367 | 15 | Valor | 4 | DLAF | ALIQDAPI | Valor Alíquota de Icms da DAPI |  |  |
| 99 | 1368 | 1372 | 5 | Inteiro |  | DLAF | CODEVENTO | Código Evento Contábil |  |  |
| 100 | 1373 | 1387 | 15 | Carácter |  | DLAF | NUMDOCSALDUS | Número Documento TOTVS Gestão Contábil |  |  |
| 101 | 1388 | 1388 | 1 | Inteiro |  | DLAF | CONTABILIZADOPORTOTAL | Flag identificador Contabilização por total |  | Nota 11 |
| 102 | 1389 | 1398 | 10 | Inteiro |  | DLAF | CODLOTESALDUS | Código Lote TOTVS Gestão Contábil |  |  |
| 103 | 1399 | 1399 | 1 | Inteiro |  | DLAF | STATUSEXPORTSALDUS | Status Exportação TOTVS Gestão Contábil |  | Nota 11 |
| 104 | 1400 | 1402 | 3 | Carácter |  | DLAF | SUBSERIE | Subsérie do lançamento |  |  |
| 105 | 1403 | 1414 | 12 | Carácter |  | DLAF | CONTADORREDUCAO | Contador de Reduções do Lançamento |  |  |
| 106 | 1415 | 1429 | 15 | Valor | 4 | DLAF | VALORINICIALDIA | Valor Inicial Dia Cupom |  |  |
| 107 | 1430 | 1444 | 15 | Valor | 4 | DLAF | VALORFINALDIA | Valor Final Dia Cupom |  |  |
| 108 | 1445 | 1459 | 15 | Valor | 4 | DLAF | VLRCANCELADOCUPOM | Valor Cancelamento Cupom |  |  |
| 109 | 1460 | 1474 | 15 | Valor | 4 | DLAF | VLRDESCONTOCUPOM | Valor Desconto Cupom |  |  |
| 110 | 1475 | 1499 | 25 | Carácter |  | DLAF | CODDEPARTAMENTO | Código do Departamento |  |  |
| 111 | 1500 | 1524 | 25 | Carácter |  | DLAF | CODCCUSTO | Código do Centro Custo |  |  |
| 112 | 1525 | 1529 | 5 | Inteiro |  | DLAF | CODCOLCXA | Código Coligada Conta Caixa |  |  |
| 113 | 1530 | 1539 | 10 | Carácter |  | DLAF | CODCXA | Código da Conta Caixa |  |  |
| 114 | 1540 | 1554 | 15 | Valor | 4 | DLAF | JUROSFINANC | Valor Juros Financeiro |  |  |
| 115 | 1555 | 1804 | 250 | Carácter |  | DLAF | HISTORICOFLUXUS | Histórico do TOTVS Gestão Financeira |  |  |
| 116 | 1805 | 1805 | 1 | Inteiro |  | DLAF | PAGAROURECEBER | Pagar / Receber |  | Nota 10 |
| 117 | 1806 | 1806 | 1 | Carácter |  | DLAF | TIPOFATURA | Tipo Fatura |  | Branco |
| 118 | 1807 | 1816 | 10 | Data |  | DLAF | DATAPREVBAIXA | Data Previsão Baixa |  |  |
| 119 | 1817 | 1817 | 1 | Inteiro |  | DLAF | STATUSREEXPORTFLUXUS | Status Reexport. TOTVS Gestão Financeira |  | Nota 11 |
| 120 | 1818 | 1832 | 15 | Valor | 4 | DLAF | VALORFINANCEIRO | Valor Financeiro |  |  |
| 121 | 1833 | 1857 | 25 | Carácter |  | DLAF | CODCCUSTOFIN | Cód. C. Custo Financeiro |  |  |
| 122 | 1858 | 1872 | 15 | Valor | 4 | DLAF | ABATIMENTOICMS | Vlr. Ref. Abatimento  ICMS (Desconto Condicional) |  |  |
| 123 | 1873 | 1887 | 15 | Valor | 4 | DLAF | FATORREDST | Valor do Fator de Redução ST |  |  |
| 124 | 1888 | 1911 | 24 | Inteiro |  | DLAF | IDPRJ | Cod. do Projeto-Const. Civil |  |  |
| 125 | 1912 | 1931 | 20 | Carácter |  | DLAF | CODMUNICIPIOSERV | Código do Município de Serviço |  |  |
| 126 | 1932 | 1933 | 2 | Carácter |  | DLAF | UFMUNICIPIOSERV | UF do Município de Serviço |  |  |
| 127 | 1934 | 1948 | 15 | Valor | 4 | DLAF | VALORFECHAIPIOUTROS | Fechamento IPI – Outros |  |  |
| 128 | 1949 | 1958 | 10 | Caracter |  | DLAF | NROSEGURANCA | Número de Segurança |  |  |
| 129 | 1959 | 1973 | 15 | Carácter |  | DLAF | CODIGOSERVICO | Código do Serviço |  |  |
| 130 | 1974 | 1983 | 10 | Data |  | DLAF | DATADEDUCAO | Data Dedução |  |  |
| 131 | 1984 | 1998 | 15 | Valor | 4 | DLAF | VLRCCIVIL01 | Valor Construção Civil 01 |  |  |
| 132 | 1999 | 2013 | 15 | Valor | 4 | DLAF | VLRCCIVIL02 | Valor Construção Civil 02 |  |  |
| 133 | 2014 | 2028 | 15 | Valor | 4 | DLAF | VLRCCIVIL03 | Valor Construção Civil 03 |  |  |
| 134 | 2029 | 2043 | 15 | Valor | 4 | DLAF | VLRCCIVIL04 | Valor Construção Civil 04 |  |  |
| 135 | 2044 | 2058 | 15 | Valor | 4 | DLAF | VLRCCIVIL05 | Valor Construção Civil 05 |  |  |
| 136 | 2059 | 2073 | 15 | Valor | 4 | DLAF | VALORIPISEMCREDITO | Valor IPI Sem Crédito |  |  |
| 137 | 2074 | 2088 | 15 | Valor | 4 | DLAF | VALORBASEIRRFFLX | Percentual Base IRRF |  |  |
| 138 | 2089 | 2103 | 15 | Caracter |  | DLAF | IDAIDF | Número AIDF |  | Branco quando não existir |
| 139 | 2104 | 2108 | 5 | Inteiro |  | DLAF | IDREDUCAOZ | Identificador da Redução Z |  | Branco quando não existir |
| 140 | 2109 | 2109 | 1 | Caracter |  | DLAF | TIPOSERVICO | Tipo Serviço |  |  |
| 141 | 2110 | 2110 | 1 | Inteiro |  | DLAF | INTEGRADOBONUM | Lançamento Fiscal Integrado com TOTVS Gestão Patrimonial |  |  |
| 142 | 2111 | 2125 | 15 | Valor | 4 | DLAF | ALIQICMSORIGINAL | Alíquota de ICMS Original |  |  |
| 143 | 2126 | 2126 | 1 | Inteiro |  | DLAF | ESCRITURADOMANUAL | Escriturado Manualmente |  |  |
| 144 | 2127 | 2127 | 1 | Inteiro |  | DLAF | CONTABILIZACAOONLINE | Contabilização On Line |  |  |
| 145 | 2128 | 2142 | 15 | Valor | 4 | DLAF | ALIQICMSFRETE | Alíquota de ICMS do Frete |  |  |
| 146 | 2143 | 2143 | 1 | Inteiro |  | DLAF | CONTRIBUINTECREDENCIADO | Contribuinte ICMS ST Credenciado |  |  |
| 147 | 2144 | 2158 | 15 | Valor | 4 | DLAF | DESPESACONDICIONAL | Despesa Condicional |  |  |
| 148 | 2159 | 2168 | 10 | Carácter |  | DLAF | CUPOMINICIALGERENCIAL | Cupom Inicial - Gerencial |  |  |
| 149 | 2169 | 2178 | 10 | Carácter |  | DLAF | CUPOMFINALGERENCIAL | Cupom Final - Gerencial |  |  |
| 150 | 2179 | 2193 | 15 | Valor | 4 | DLAF | INSSEMOUTRAEMPRESA | Valor INSS pago em outra Empresa |  |  |
| 151 | 2194 | 2203 | 10 | Carácter |  | DLAF | CODIGOIRRF | Código de retenção do IRRF |  |  |
| 152 | 2204 | 2218 | 15 | Valor | 4 | DLAF | PERCENTBASEINSS | Percentual da Base de INSS Empregador |  |  |
| 153 | 2219 | 2233 | 15 | Valor | 4 | DLAF | PERCBASEINSSEMPREGADO | Percentual da Base de INSS Empregado |  |  |
| 154 | 2234 | 2238 | 5 | Inteiro |  | DLAF | NUMLIVRO | Número do Livro |  |  |
| 155 | 2239 | 2243 | 5 | Inteiro |  | DLAF | NROMAPARESUMO | Número do Livro Mapa Resumo |  |  |
| 156 | 2244 | 2248 | 5 | Inteiro |  | DLAF | NUMFOLHA | Número da Folha no Registro Entrada/Saída |  |  |
| 157 | 2249 | 2258 | 10 | Data |  | DLAF | DATACANCELAMENTO | Data do Cancelamento |  |  |
| 158 | 2259 | 2259 | 1 | Carácter |  | DLAF | CODVIATRANSPORTE | Via de Transporte |  |  |
| 159 | 2260 | 2269 | 10 | Carácter |  | DLAF | PLACA | Placa |  |  |
| 160 | 2270 | 2271 | 2 | Carácter |  | DLAF | CODETDPLACA | UF Placa |  |  |
| 161 | 2272 | 2276 | 5 | Carácter |  | DLAF | CODTRA | Código Transportadora |  |  |
| 162 | 2277 | 2291 | 15 | Valor | 4 | DLAF | BASESTORIGINAL | Valor da Base Subst. Tributária Original |  |  |
| 163 | 2292 | 2296 | 5 | Inteiro |  | DLAF | DISTANCIA | Distância |  |  |
| 164 | 2297 | 2311 | 15 | Valor | 4 | DLAF | QUANTIDADE | Quantidade |  |  |
| 165 | 2312 | 2312 | 1 | Carácter |  | DLAF | UNCALCULO | Unidade de Cálculo |  |  |
| 166 | 2313 | 2313 | 1 | Carácter |  | DLAF | FORMACALCULO | Forma de Cálculo |  |  |
| 167 | 2314 | 2323 | 10 | Data |  | DLAF | DATAVISTO | Data Visto |  |  |
| 168 | 2324 | 2338 | 15 | Valor | 4 | DLAF | PESOBRUTO | Peso Bruto |  |  |
| 169 | 2339 | 2353 | 15 | Valor | 4 | DLAF | PESOLIQUIDO | Peso Líquido |  |  |
| 170 | 2354 | 2608 | 255 | Carácter |  | DLAF | MOTIVOCANCELAMENTO | Motivo Cancelamento |  |  |
| 171 | 2609 | 2613 | 5 | Inteiro |  | DLAF | OCAUTONOMO | Número Ocorrência Autônomo |  |  |
| 172 | 2614 | 2643 | 30 | Carácter |  | DLAF | MARCA | Marca |  |  |
| 173 | 2644 | 2673 | 30 | Carácter |  | DLAF | ESPECIE | Espécie |  |  |
| 174 | 2674 | 2683 | 10 | Inteiro |  | DLAF | NUMERO | Número |  |  |
| 175 | 2684 | 2693 | 10 | Inteiro |  | DLAF | QTDEDOCCANCELADOS | Quantidade Cancelado |  |  |
| 176 | 2694 | 2698 | 5 | Inteiro |  | DLAF | CRO | Contador de Reinicio de Operação (CRO) |  |  |
| 177 | 2699 | 2703 | 5 | Inteiro |  | DLAF | OPERACAOCONSUMIDORFINAL | Operação Consumidor Final |  |  |
| 178 | 2704 | 2733 | 30 | Inteiro |  | DLAF | IDCLASSECONSUMO | Classe Consumo |  |  |
| 179 | 2734 | 2763 | 30 | Inteiro |  | DLAF | IDTIPOLIGACAO | Tipo Ligação |  |  |
| 180 | 2764 | 2793 | 30 | Inteiro |  | DLAF | IDGRUPOTENSAO | Grupo Tensão |  |  |
| 181 | 2794 | 2823 | 30 | Inteiro |  | DLAF | IDTIPOUTILIZACAO | Tipo Utilização |  |  |
| 182 | 2824 | 2853 | 30 | Carácter |  | DLAF | DEMANDAPONTA | Demanda Ponta |  |  |
| 183 | 2854 | 2883 | 30 | Carácter |  | DLAF | DEMANDAFORAPONTA | Demanda Fora Ponta |  |  |
| 184 | 2884 | 2898 | 15 | Carácter |  | DLAF | CONTACONSUMO | Conta Consumo / Número Terminal |  |  |
| 185 | 2899 | 2900 | 2 | Carácter |  | DLAF | CODANTECIPACAOTRIBUTARIA | Código de Antecipação Tributária |  |  |
| 186 | 2901 | 2915 | 15 | Valor | 4 | DLAF | BASESUBSTCOMPL | Valor Base ST Complementar |  |  |
| 187 | 2916 | 2930 | 15 | Valor | 4 | DLAF | VALORSUBSTCOMPL | Valor ST Complementar |  |  |
| 188 | 2931 | 2945 | 15 | Valor | 4 | DLAF | ALIQUOTASUBSTCOMPL | Valor da Aliquota ST Complementar |  |  |
| 189 | 2946 | 2989 | 44 | Carácter |  | DLAF | CHAVEACESSONFE | Chave Acesso NF-e |  |  |
| 190 | 2990 | 3004 | 15 | Valor | 4 | DLAF | VLRSECCAT | Valores de coleta/custo adicional do transporte |  |  |
| 191 | 3005 | 3019 | 15 | Valor | 4 | DLAF | VLRDESPACHO | Valores de despacho |  |  |
| 192 | 3020 | 3034 | 15 | Valor | 4 | DLAF | VLRPEDAGIO | Valores de pedágio |  |  |
| 193 | 3035 | 3049 | 15 | Valor | 4 | DLAF | VLRFRETEOUTROS | Outros Valores de Frete |  |  |
| 194 | 3050 | 3064 | 15 | Valor | 4 | DLAF | VLRSERVICO | Valor do serviço |  |  |
| 195 | 3065 | 3074 | 10 | Data |  | DLAF | DATAINICIOCREDITO | Data Inicio do Crédito |  |  |
| 196 | 3075 | 3084 | 10 | Inteiro |  | DLAF | IDMOV | Identificador do Movimento |  | Informar Branco |
| 197 | 3085 | 3085 | 1 | Carácter |  | DLAF | TIPOASSINANTE | Tipo de Assinante |  |  |
| 198 | 3086 | 3095 | 10 | Data |  | DLAF | DATALEITURA | Data Leitura |  |  |
| 199 | 3096 | 3115 | 20 | Carácter |  | DLAF | DRAWBACK | DrawBack |  |  |
| 200 | 3116 | 3116 | 1 | Carácter |  | DLAF | MODOPRESTAÇÃO | Modo de Prestação da Operação |  | Versão 11.82 com código defensivo ou Superior - Valores Permitidos: 1 - Transfronteirico, 2 - ConsumosNoBrasil, 4 - MovimentoTempPessoaFisica |
| 201 | 3117 | 3126 | 10 | Data |  | DLAF | DATAINICIO | Data inicial da prestação da Operação |  | Versão 11.82 com código defensivo ou Superior |
| 202 | 3127 | 3136 | 10 | Data |  | DLAF | DATACONCLUSÃO | Data final da prestação da Operação |  | Versão 11.82 com código defensivo ou Superior |
| 203 | 3137 | 3186 | 50 | Carácter |  | DLAF | NRPROTSISCOSERV | Número Protocolo informado pelo SISCOSERV |  | Versão 11.82 com código defensivo ou Superior |
| 204 | 3187 | 3201 | 15 | Carácter |  | DLAF | NROSAT | Número de Série do Equipamento SAT |  | Versão 11.82 com código defensivo ou Superior |
| 205 | 3202 | 3216 | 15 | Valor | 4 | DLAF | PERICMSESTDESTINO | % ICMS UF Destinatário |  | Versão 11.82 com código defensivo ou Superior |
| 206 | 3217 | 3231 | 15 | Valor | 4 | DLAF | VLRICMSESTDESTINO | Valor do ICMS de partilha para a UF do destinatário |  | Versão 11.82 com código defensivo ou Superior |
| 207 | 3232 | 3246 | 15 | Valor | 4 | DLAF | VLRICMSESTREMETENTE | Valor do ICMS de partilha para a UF do remetente |  | Versão 11.82 com código defensivo ou Superior |
| 208 | 3247 | 3261 | 15 | Valor | 4 | DLAF | PERICMSFCP | % FCP (Fundo de Combate a Pobreza) |  | Versão 11.82 com código defensivo ou Superior |
| 209 | 3262 | 3276 | 15 | Valor | 4 | DLAF | VLRICMSFCPESTDEST | Valor do ICMS relativo ao FCP para a UF do Destinatário |  | Versão 11.82 com código defensivo ou Superior |
| 210 | 3277 | 3296 | 20 | Carácter |  | DLAF | CNPJCPFADQUIRENTE | CNPJ/CPF do Adquirente |  | Versão 11.82 com código defensivo ou Superior |
| 211 | 3297 | 3356 | 60 | Carácter |  | DLAF | NOMEADQUIRENTE | Nome do Adquirente |  | Versão 11.82 com código defensivo ou Superior |
| 212 | 3357 | 3376 | 20 | Carácter |  | DLAF | DOCESTRANGEIROADQUIRENTE | Doc. Estrangeiro do Adquirente |  | Versão 11.82 com código defensivo ou Superior |
| 213 | 3377 | 3377 | 1 | Carácter |  | DLAF | OPERACAOPRESENCIAL | Presença do comprador no estabelecimento comercial no ato da compra |  | Versão 11.82 com código defensivo ou Superior |
