---
content_hash: c8668db404851bdacc3d463ee9e3cf5c20ae7ad3f8f699dc20b82e6b920e6c5a
fetched_at: '2026-06-29T00:09:20.290917+00:00'
page_id: '422545684'
product: rm
source: tdn-rm
title: Dados dos Itens do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545684
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("I") | Tipo da linha | X | Letra I |
| 2 | 2 | 6 | 5 | Inteiro |  | DITEM | CODCOLIGADA | Coligada | X |  |
| 3 | 7 | 36 | 30 | Caracter |  | DITEM | IDPRD | Código do Produto | X |  |
| 4 | 37 | 46 | 10 | Inteiro |  | DITEM | NUMITEM | Número do Item | X |  |
| 5 | 47 | 61 | 15 | Valor | 4 | DITEM | ALIQIPI | Alíquota de IPI |  |  |
| 6 | 62 | 76 | 15 | Valor | 4 | DITEM | BASEIPI | Base IPI |  |  |
| 7 | 77 | 91 | 15 | Valor | 4 | DITEM | VALORIPI | Valor IPI |  |  |
| 8 | 92 | 106 | 15 | Valor | 4 | DITEM | ISENTOIPI | Valor Isento IPI |  |  |
| 9 | 107 | 121 | 15 | Valor | 4 | DITEM | OUTROSIPI | Valor Outros IPI |  |  |
| 10 | 122 | 136 | 15 | Valor | 4 | DITEM | QTDEPRD | Quantidade |  |  |
| 11 | 137 | 157 | 21 | Valor | 10 | DITEM | PRECOPRD | Preço |  | Para versões abaixo da versão 11.82 o tamanho é 15 e Decimais é igual a 4 |
| 12 | 158 | 172 | 15 | Valor | 2 | DITEM | BASEICMSPRD | Valor Base ICMS |  |  |
| 13 | 173 | 187 | 15 | Valor | 2 | DITEM | BASEICMSSTPRD | Valor Base ICMS Subst. Tributária |  |  |
| 14 | 188 | 192 | 5 | Caracter |  | DITEM | CODUND | Código da Unidade |  |  |
| 15 | 193 | 207 | 15 | Valor | 4 | DITEM | VLRDIFALIQUOTA | Valor Diferencial Alíquota |  |  |
| 16 | 208 | 222 | 15 | Valor | 4 | DITEM | VLRICMSPRD | Valor ICMS Produto |  |  |
| 17 | 223 | 247 | 25 | Caracter |  | DITEM | CODBEM | Código do Bem |  | preencher com brancos |
| 18 | 248 | 262 | 15 | Valor | 4 | DITEM | VLRICMSSTPRD | Valor ICMS ST Produto |  |  |
| 19 | 263 | 277 | 15 | Valor | 4 | DITEM | ALIQDAPI | Alíquota DAPI |  |  |
| 20 | 278 | 292 | 15 | Valor | 4 | DITEM | DESCONTOITEM | Valor Desconto do Item |  |  |
| 21 | 293 | 317 | 25 | Caracter |  | DITEM | CODCCUSTO | Centro Custo Contábil |  |  |
| 22 | 318 | 332 | 15 | Valor | 4 | DITEM | VLRFRETE | Valor Frete do Item |  |  |
| 23 | 333 | 347 | 15 | Valor | 4 | DITEM | VALORIPISEMCREDITO | Valor IPI Sem Credito |  |  |
| 24 | 348 | 362 | 15 | Valor | 4 | DITEM | VALORICMSFRETE | Valor ICMS Frete |  |  |
| 25 | 363 | 377 | 15 | Valor | 4 | DITEM | VALORSEGURO | Valor Seguro |  |  |
| 26 | 378 | 392 | 15 | Valor | 4 | DITEM | VALORDESPESA | Valor despesa |  |  |
| 27 | 393 | 402 | 10 | Caracter |  | DITEM | CUPOMFISCAL | Cupom Fiscal |  |  |
| 28 | 403 | 405 | 3 | Caracter |  | DITEM | CST | CST |  |  |
| 29 | 406 | 420 | 15 | Valor | 4 | DITEM | OUTROSICMS | Valor Outros ICMS |  |  |
| 30 | 421 | 435 | 15 | Valor | 4 | DITEM | ISENTOICMS | Valor Isento ICMS |  |  |
| 31 | 436 | 447 | 12 | Caracter |  | DITEM | NUMERORE | Numero RE |  |  |
| 32 | 448 | 457 | 10 | Data |  | DITEM | DATARE | Data RE |  |  |
| 33 | 458 | 472 | 15 | Valor | 4 | DITEM | PERCDIFERIMENTOPARCIALICMS | Valor Diferimento Parcial |  |  |
| 34 | 473 | 502 | 30 | Caracter |  | DITEM | IDCLASSIFITEMENERGIA | Classificação Item de Comunicação / Energia |  | Preencher com Branco quando não existir |
| 35 | 503 | 517 | 15 | Valor | 4 | DITEM | BASESUBSTCOMPL | Valor Base ST Complementar |  |  |
| 36 | 518 | 532 | 15 | Valor | 4 | DITEM | VALORSUBSTCOMPL | Valor ST Complementar |  |  |
| 37 | 533 | 547 | 15 | Valor | 4 | DITEM | ALIQUOTASUBSTCOMPL | Aliquota ST Complementar |  |  |
| 38 | 548 | 647 | 100 | Caracter |  |  |  | Observação |  |  |
| 39 | 648 | 697 | 50 | Caracter |  | DITEM | NUMMEMOEXP | Número do Memorando de Exportação |  |  |
| 40 | 698 | 718 | 21 | Caracter |  | DITEM | CODIGOCODIF | Código CODIF |  |  |
| 41 | 719 | 738 | 20 | Caracter |  | DITEM | CODMUNICIPIOSERV | Código do Município do Serviço |  |  |
| 42 | 739 | 740 | 2 | Caracter |  | DITEM | UFMUNICIPIOSERV | UF do Município do Serviço |  |  |
| 43 | 741 | 755 | 15 | Caracter |  | DITEM | CODIGOSERVICO | Código do Serviço |  |  |
| 44 | 756 | 770 | 15 | Valor | 4 | DITEM | VALORMERC | Valor da Mercadoria |  |  |
| 45 | 771 | 785 | 15 | Valor | 4 | DITEM | QTDECONTRATADA | Quantidade Contratada |  |  |
| 46 | 786 | 787 | 2 | Caracter |  | DITEM | CODETDHABILITACAOTEL | UF de Habilitação do Telefone |  |  |
| 47 | 788 | 801 | 14 | Inteiro |  | DITEM | CNPJADQUIRENTE | CNPJ/CPF do Adquirente da mercadoria |  |  |
| 48 | 802 | 802 | 1 | Inteiro |  | DITEM | TIPORECEITA | Tipo de Receita |  |  |
| 49 | 803 | 805 | 3 | Inteiro |  | DITEM | CODFILIALTERCEIRO | Filial Terceira |  |  |
| 50 | 806 | 830 | 25 | Caracter |  | DITEM | CODCFOTERCEIRO | Cód. Clif/For Terceiro |  |  |
| 51 | 831 | 832 | 2 | Caracter |  | DITEM | CODCOLFCFOTERCEIRO | Cód. Coligada de Cód. Clif/For Terceiro |  |  |
| 52 | 833 | 842 | 10 | Caracter |  | DITEM | PLACA | Placa |  |  |
| 53 | 843 | 844 | 2 | Caracter |  | DITEM | CODETDPLACA | UF Placa |  |  |
| 54 | 845 | 846 | 2 | Caracter |  | DITEM | CODETDCOLETA | UF Coleta |  |  |
| 55 | 847 | 866 | 20 | Caracter |  | DITEM | CODMUNICIPIOCOLETA | Código do Município de Coleta |  |  |
| 56 | 867 | 868 | 2 | Caracter |  | DITEM | CODETDENTREGA | UF Entrega |  |  |
| 57 | 869 | 888 | 20 | Caracter |  | DITEM | CODMUNICIPIOENTREGA | Código do Município de Entrega |  |  |
| 58 | 889 | 890 | 2 | Caracter |  | DITEM | TPMOVCIAP | Tipo Movimentação CIAP |  |  |
| 59 | 891 | 905 | 15 | Valor | 4 | DITEM | VLRICMSDESONERADO | Valor do ICMS Desonerado |  |  |
| 60 | 906 | 908 | 3 | Caracter |  | DITEM | NATREC | Natureza da receita |  |  |
| 61 | 909 | 910 | 2 | Caracter |  | DITEM | NATBCCRED | Código da Base de Calculo de Credito |  |  |
| 62 | 911 | 915 | 5 | Caracter |  | DITEM | TIPOCREDITO | Tipo de Crédito |  |  |
| 63 | 916 | 916 | 1 | Caracter |  | DITEM | INDNATFRETE | Indicação da natureza do Frete |  |  |
| 64 | 917 | 931 | 15 | Valor | 4 | DITEM | VALORIBPTFEDERAL | Valor Total dos Tributos Federais |  | Versão 11.82 com código defensivo ou Superior |
| 65 | 932 | 946 | 15 | Valor | 4 | DITEM | VALORIBPTESTADUAL | Valor Total dos Tributos Estaduais |  | Versão 11.82 com código defensivo ou Superior |
| 66 | 947 | 961 | 15 | Valor | 4 | DITEM | VALORIBPTMUNICIPAL | Valor Total dos Tributos Municipais |  | Versão 11.82 com código defensivo ou Superior |
| 67 | 962 | 981 | 20 | Caracter |  | DITEM | CHAVEIBPT | Chave IBPT |  | Versão 11.82 com código defensivo ou Superior |
| 68 | 982 | 996 | 15 | Valor | 4 | DITEM | VLRTOTTRIB | Valor Total dos Tributos |  | Versão 11.82 com código defensivo ou Superior |
| 69 | 997 | 1011 | 15 | Valor | 4 | DITEM | VLRICMSESTDESTINO | Valor do ICMS de partilha para a UF do destinatário |  | Versão 11.82 com código defensivo ou Superior |
| 70 | 1012 | 1026 | 15 | Valor | 4 | DITEM | VLRICMSESTREMETENTE | Valor do ICMS de partilha para a UF do remetente |  | Versão 11.82 com código defensivo ou Superior |
| 71 | 1027 | 1041 | 15 | Valor | 4 | DITEM | VLRICMSITEMFCPESTDEST | Valor do ICMS relativo ao FECP para a UF do Destinatário |  | Versão 11.82 com código defensivo ou Superior |
| 72 | 1042 | 1056 | 15 | Valor | 4 | DITEM | PERFECPITEM | Percentual FECP |  | Versão 11.82 com código defensivo ou Superior |
