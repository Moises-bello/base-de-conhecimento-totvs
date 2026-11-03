---
content_hash: 016439d5d781128569f590492ea9041252c0bb199c420b2e382a932f40ee589c
fetched_at: '2026-06-29T00:11:59.887652+00:00'
page_id: '876226391'
product: rm
source: tdn-rm
title: Listagem de campos do Movimento para importação via Conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=876226391
version: 44
---

As informações do layout relatado abaixo deverão ser disponibilizadas em um único arquivo, pois no momento da importação o sistema irá distinguir a informação através do identificador de Linha.

Observação

Este documento lista campos possíveis de serem utilizados na importação, a obrigatoriedade entre eles terá variação conforme a parametrização do movimento.

**Movimento :**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: M |
| 2 | TMOV.CODFILIAL | Código Filial | Número Inteiro | 5 |  |
| 3 | TMOV.CODDEPARTAMENTO | Código do Departamento | Texto | 30 |  |
| 4 | TMOV.CODLOC | Código do Local de Estoque | Texto | 15 |  |
| 5 | TMOV.CODLOCENTREGA | Código do Local de Entrega | Texto | 15 |  |
| 6 | TMOV.CODLOCDESTINO | Código do Local de Destino | Texto | 15 |  |
| 7 | TMOV.CODCFO | Código do Cliente / Fornecedor | Texto | 25 |  |
| 8 | TMOV.CODCFONATUREZA | Código Cliente / Fornecedor RM Finanças | Texto | 25 |  |
| 9 | TMOV.NUMEROMOV | Número do Movimento | Texto | 35 |  |
| 10 | TMOV.SERIE | Série | Texto | 8 |  |
| 11 | TMOV.CODTMV | Código do Tipo de Movimento | Texto | 10 |  |
| 12 | TMOV.TIPO | Tipo | Texto | 1 |  |
| 13 | TMOV.STATUS | Status | Texto | 1 | Verificar [Constantes do Movimento - Tabela TMOV](https://tdn.totvs.com/display/LRM/Constantes) preenchendo com apenas com o valor da constante |
| 14 | TMOV.MOVIMPRESSO | Identificador de Movimento Impresso | Número Inteiro | 1 |  |
| 15 | TMOV.DOCIMPRESSO | Documento Impresso | Número Inteiro | 1 |  |
| 16 | TMOV.FATIMPRESSA | Fatura Impressa | Número Inteiro | 1 |  |
| 17 | TMOV.DATAEMISSAO | Data da Emissão | Data | 10 |  |
| 18 | TMOV.DATASAIDA | Data da Saída | Data | 10 |  |
| 19 | TMOV.DATAEXTRA1 | Data Extra 1 | Data | 10 |  |
| 20 | TMOV.DATAEXTRA2 | Data Extra 2 | Data | 10 |  |
| 21 | TMOV.CODRPR | Código do Representante | Texto | 15 |  |
| 22 | TMOV.COMISSAOREPRES | Comissão do Representante | Número Decimal | 20 |  |
| 23 | TMOV.NORDEM | Número Ordem | Texto | 20 |  |
| 24 | TMOV.CODCPG | Código da Condição de Pagamento | Texto | 5 |  |
| 25 | TMOV.NUMEROTRIBUTOS | Número dos Tributos | Número Inteiro | 5 |  |
| 26 | TMOV.VALORBRUTO | Valor Bruto | Número Decimal | 20 |  |
| 27 | TMOV.VALORLIQUIDO | Valor do Documento | Número Decimal | 20 |  |
| 28 | TMOV.VALOROUTROS | Valor de Outros | Número Decimal | 20 |  |
| 29 | TMOV.OBSERVACAO | Observação | Texto | 60 |  |
| 30 | TMOV.PERCENTUALFRETE | Percentual do Frete | Número Decimal | 20 |  |
| 31 | TMOV.VALORFRETE | Valor do Frete | Número Decimal | 20 |  |
| 32 | TMOV.PERCENTUALSEGURO | Percentual do Seguro | Número Decimal | 20 |  |
| 33 | TMOV.VALORSEGURO | Valor do Seguro | Número Decimal | 20 |  |
| 34 | TMOV.PERCENTUALDESC | Percentual do Desconto | Número Decimal | 20 |  |
| 35 | TMOV.VALORDESC | Valor do Desconto | Número Decimal | 20 |  |
| 36 | TMOV.PERCENTUALDESP | Percentual da Despesa | Número Decimal | 20 |  |
| 37 | TMOV.VALORDESP | Valor da Despesa | Número Decimal | 20 |  |
| 38 | TMOV.PERCENTUALEXTRA1 | Percentual Extra1 | Número Decimal | 20 |  |
| 39 | TMOV.VALOREXTRA1 | Valor Extra1 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA2 | Percentual Extra2 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA2 | Valor Extra2 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA3 | Percentual Extra3 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA3 | Valor Extra3 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA4 | Percentual Extra4 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA4 | Valor Extra4 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA5 | Percentual Extra5 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA5 | Valor Extra5 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA6 | Percentual Extra6 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA6 | Valor Extra6 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA7 | Percentual Extra7 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA7 | Valor Extra7 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA8 | Percentual Extra8 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA8 | Valor Extra8 | Número Decimal | 20 |  |
| 40 | TMOV.PERCENTUALEXTRA9 | Percentual Extra9 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA9 | Valor Extra9 | Número Decimal | 20 |  |
|  | TMOV.PERCENTUALEXTRA10 | Percentual Extra10 | Número Decimal | 20 |  |
| 41 | TMOV.VALOREXTRA10 | Valor Extra10 | Número Decimal | 20 |  |
| 42 | TMOV.CODVEN1 | Código do Vendedor 1 | Texto | 16 |  |
| 43 | TMOV.PERCCOMISSAO | Percentual Comissão | Número Decimal | 20 |  |
| 44 | TMOV.CODMEN | Código da Mensagem | Texto | 5 |  |
| 45 | TMOV.CODMEN2 | Código da Mensagem2 | Texto | 5 |  |
| 46 | TMOV.VIADETRANSPORTE | Via de Transporte | Texto | 15 |  |
| 47 | TMOV.PLACA | Placa | Texto | 10 |  |
| 48 | TMOV.CODETDPLACA | Código do Estado na Placa | Texto | 2 |  |
| 49 | TMOV.PESOLIQUIDO | Peso Líquido | Número Decimal | 20 |  |
| 50 | TMOV.PESOBRUTO | Peso Bruto | Número Decimal | 20 |  |
| 51 | TMOV.MARCA | Marca | Texto | 10 |  |
| 52 | TMOV.NUMERO | Número | Número Inteiro | 10 |  |
| 53 | TMOV.QUANTIDADE | Quantidade | Número Inteiro | 10 |  |
| 54 | TMOV.ESPECIE | Espécie | Texto | 15 |  |
| 55 | TMOV.CODTB1FAT | Código Tabela Classificação1 Produto | Texto | 10 |  |
| 56 | TMOV.CODTB2FAT | Código Tabela Classificação2 Produto | Texto | 10 |  |
| 57 | TMOV.CODTB3FAT | Código Tabela Classificação3 Produto | Texto | 10 |  |
| 58 | TMOV.CODTB4FAT | Código Tabela Classificação4 Produto | Texto | 10 |  |
| 59 | TMOV.CODTB5FAT | Código Tabela Classificação5 Produto | Texto | 10 |  |
| 60 | TMOV.CODTB1FLX | Código Tabela Classificação1 Opcionais | Texto | 25 |  |
| 61 | TMOV.CODTB2FLX | Código Tabela Classificação2 Opcionais | Texto | 25 |  |
| 62 | TMOV.CODTB3FLX | Código Tabela Classificação3 Opcionais | Texto | 25 |  |
| 63 | TMOV.CODTB4FLX | Código Tabela Classificação4 Opcionais | Texto | 25 |  |
| 64 | TMOV.CODTB5FLX | Código Tabela Classificação5 Opcionais | Texto | 25 |  |
| 65 | TMOV.CAMPOLIVRE1 | Campo Livre1 | Texto | 100 |  |
| 66 | TMOV.CAMPOLIVRE2 | Campo Livre2 | Texto | 100 |  |
| 67 | TMOV.CAMPOLIVRE3 | Campo Livre3 | Texto | 100 |  |
| 68 | TMOV.CODMOEVALORLIQUIDO | Código da Moeda no Valor Líquido | Texto | 10 |  |
| 69 | TMOV.DATABASEMOV | Data Base do Movimento | Data | 10 |  |
| 70 | TMOV.DATAMOVIMENTO | Data do Movimento | Data | 10 |  |
| 71 | TMOV.NUMEROLCTGERADO | Número de Lançamento Gerado | Número Inteiro | 5 |  |
| 72 | TMOV.GEROUFATURA | Gerou Fatura | Número Inteiro | 5 |  |
| 73 | TMOV.NUMEROLCTABERTO | Número de Lançamento Aberto | Número Inteiro | 5 |  |
| 74 | TMOV.CODVEN2 | Código do Vendedor 2 | Texto | 16 |  |
| 75 | TMOV.CODUSUARIO | Código do Usuário | Texto | 20 |  |
| 76 | TMOV.FLAGEXPORTACAO | Flag Exportação | Número Inteiro | 5 |  |
| 77 | TMOV.EMITEBOLETA | Emite Boleta | Texto | 1 |  |
| 78 | TMOV.CODMENDESCONTO | Código da Mensagem de Desconto | Texto | 5 |  |
| 79 | TMOV.CODMENDESPESA | Código das Mensagem de Despesa | Texto | 5 |  |
| 80 | TMOV.CODMENFRETE | Código da Mensagem de Frete | Texto | 5 |  |
| 81 | TMOV.FRETECIFOUFOB | Frete CIF ou FOB | Número Inteiro | 5 |  |
| 82 | TMOV.USADESPFINANC | Usa Despesa Financeira | Número Inteiro | 5 |  |
| 83 | TMOV.IDNAT | Identificador da Natureza | Número Inteiro | 5 |  |
| 84 | TMOV.FLAGEXPORFISC | Flag Exportação Fiscal | Número Inteiro | 5 |  |
| 85 | TMOV.FLAGEXPORFAZENDA | Flag Exportação da Fazenda | Número Inteiro | 5 |  |
| 86 | TMOV.CODVEN3 | Código do Vendedor 3 | Texto | 16 |  |
| 87 | TMOV.CODVEN4 | Código do Vendedor 4 | Texto | 16 |  |
| 88 | TMOV.PERCCOMISSAOVEN2 | Percentual Comissão do Vendedor 2 | Número Decimal | 20 |  |
| 89 | TMOV.IDNAT2 | Identificador da Natureza 2 | Número Inteiro | 5 |  |
| 90 | TMOV.VALORADIANTAMENTO | Valor Adiantamento | Número Decimal | 20 |  |
| 91 | TMOV.CODTRA | Código da Transportadora | Texto | 5 |  |
| 92 | TMOV.CODTRA2 | Código da Transportadora2 | Texto | 5 |  |
| 93 | TMOV.STATUSLIBERACAO | Status de Liberação | Número Inteiro | 5 |  |
| 94 | TMOV.ITENSAGRUPADOS | Itens Agrupados | Número Inteiro | 5 |  |
| 95 | TMOV.FLAGIMPRESSAOFAT | Flag Impressão do Faturamento | Texto | 1 |  |
| 96 | TMOV.DATACANCELAMENTOMOV | Data Cancelamento do Movimento | Data | 10 |  |
| 97 | TMOV.SEGUNDONUMERO | Segundo Número | Texto | 20 |  |
| 98 | TMOV.CODCCUSTO | Centro de Custo | Texto | 25 |  |
| 99 | TMOV.CODCOLCXA | Coligada da Conta/Caixa | Número Inteiro | 5 |  |
| 100 | TMOV.CODCXA | Conta/Caixa | Texto | 10 |  |
| 101 | TMOV.CODFILIALDESTINO | Código da Filial de Destino | Número Inteiro | 5 |  |
| 102 | TMOV.CODCCUSTODESTINO | Centro de Custo Destino (Transferência) | Texto | 25 |  |
| 103 | TMOV.CODCOLCFO | Coligada do Cliente/Fornecedor | Número Inteiro | 5 |  |
| 104 | TMOV.CODCOLCFONATUREZA | Coligada do Cliente/Fornecedor Cpr | Número Inteiro | 5 |  |
| 105 | TMOV.IDMOVLCTFLUXUS | Identificador Movimento Lançamentos Pagar/Receber | Número Inteiro | 10 |  |
| 106 | TMOV.DATAENTREGA | Data de Entrega | Data | 10 |  |
| 107 | TMOV.NUMEROCAIXA | Número do Caixa | Número Inteiro | 10 |  |
| 108 | TMOV.NUMEROCUPOM | Número do Cupom | Número Inteiro | 10 |  |
| 109 | TMOV.HORARIOEMISSAO | Horário da Emissão do Movimento | Data | 20 |  |
| 110 | TMOV.CODFILIALENTREGA | Código da Filial de Entrega/Saída | Número Inteiro | 5 |  |
| 111 | DNATUREZA.CODNAT | Código Natureza 1 | Texto | 20 |  |
| 112 | DNATUREZA.CODNAT2 | Código Natureza 2 | Texto | 20 |  |
| 113 | FCFO.CGCCFO | CGC Cliente/Fornecedor | Texto | 20 |  |
| 114 | TMOV.DATACONTABILIZACAO | Data de contabilização do movimento | Data | 10 |  |
| 115 | TMOV.CODIGOSERVICO | Código do Serviço | Texto | 15 |  |
| 116 | TMOV.CODMUNSERVICO | Município da prestação de serviço | Texto | 20 |  |
| 117 | TMOV.CODETDMUNSERV | Código do Estado do Município | Texto | 2 |  |
| 118 | TMOV.PONTOVENDA | Código do Ponto de Venda | Texto | 10 |  |
| 119 | TMOV.CODEVENTO | Evento Contábil | Número Inteiro | 10 |  |
| 120 | TMOV.CODTDO | Código do tipo de documento | Texto | 10 |  |
| 121 | TMOV.CODIGOIRRF | Código de retenção do IRRF | Texto | 10 |  |
| 122 | TMOV.DEDUCAOIRRF | Percentual de dedução para IRRF | Número Decimal | 20 |  |
| 123 | TMOV.PERCBASEINSSEMPREGADO | Percentual da Base de INSS Empregado | Número Decimal | 20 |  |
| 124 | TMOV.PERCENTBASEINSS | Percentual da Base de INSS Empregador | Número Decimal | 20 |  |
| 125 | MPRJ.CODPRJ | Código do Projeto | Texto | 24 |  |
| 126 | TMOV.SUBSERIE | Sub Série | Texto | 8 |  |
| 127 | TMOV.IDCONTATOENTREGA | Contato p/ Entrega | Número Inteiro | 10 |  |
| 128 | TMOV.INSSEMOUTRAEMPRESA | Valor do INSS em Outra Empresa | Número Decimal | 20 |  |
| 129 | TMOV.APROPRIADO | Deve-se Apropriar Movimento Integrado ao TCOP | Número Inteiro | 5 |  |
| 130 | TMOV.DATALANCAMENTO | Data de lançamento | Data | 10 |  |
| 131 | TMOV.CRO | Contador de Reinício de Operação | Número Inteiro | 10 |  |
| 132 | COO | COO | Número Inteiro | 10 | Esta coluna deve estar vazia. |
| 133 | NUMEROREDUCAO | Número Redução | Número Inteiro | 10 |  |
| 134 | TMOV.HORASAIDA | Horário de entrada/saída do movimento | Data | 20 |  |
| 135 | TMOV.CODENTREGA | Tipo de Entrega | Texto | 15 |  |
| 136 | TMOV.RECIBONFESTATUS | Status do Recibo | Texto | 1 |  |
| 137 | TMOV.RECIBONFETIPO | Tipo do Recibo | Número Inteiro | 5 |  |
| 138 | TMOV.RECIBONFESITUACAO | Situação do Recibo | Número Inteiro | 5 |  |
| 139 | NROAIDF | NROAIDF | Texto | 30 |  |
| 140 | TMOV.CHAVEACESSONFE | Chave de Acesso da NF-e | Texto | 50 |  |
| 141 | TMOV.EXTENPORANEO | É movimento extemporâneo? | Número Inteiro | 5 |  |
| 142 | TMOV.VALORRECEBIDO | Valor Recebido | Número Decimal | 20 |  |
| 143 | TMOV.IDAIDF | Identificador das Autorizações | Número Inteiro | 5 |  |
| 144 | TMOV.PRODPREDOMINANTE | Produto Predominante | Texto | 60 |  |
| 145 | TMOV.NATUREZAVOLUMES | Natureza dos Volumes | Texto | 30 |  |
| 146 | TMOV.VALORMERCADORIAS | Valor das Mercadorias | Número Decimal | 20 |  |
| 147 | TMOV.CODVIATRANSPORTE | Código Via de Transporte | Texto | 1 |  |
| 148 | TMOV.VRBASEINSSOUTRAEMPRESA | Base Contribuição para INSS em outras empresas | Número Decimal | 20 |  |
| 149 | TMOV.VALORDESCCONDICIONAL | Valor do desconto condicional | Número Decimal | 20 |  |
| 150 | TMOV.VALORDESPCONDICIONAL | Valor do despesa condicional | Número Decimal | 20 |  |
| 151 | TMOV.CODMUNOPER | Código do Município de Operação | Texto | 20 |  |
| 152 | TMOV.CODUFOPER | UF do Município de Operação | Texto | 2 |  |
| 153 | TMOV.PERCENTUALEXTRA3 | Percentual Extra3 | Número Decimal | 20 |  |
| 154 | TMOV.VALOREXTRA3 | Valor Extra3 | Número Decimal | 20 |  |
| 155 | TMOV.PERCENTUALEXTRA4 | Percentual Extra4 | Número Decimal | 20 |  |
| 156 | TMOV.VALOREXTRA4 | Valor Extra4 | Número Decimal | 20 |  |
| 157 | TMOV.PERCENTUALEXTRA5 | Percentual Extra5 | Número Decimal | 20 |  |
| 158 | TMOV.VALOREXTRA5 | Valor Extra5 | Número Decimal | 20 |  |
| 159 | TMOV.PERCENTUALEXTRA6 | Percentual Extra6 | Número Decimal | 20 |  |
| 160 | TMOV.VALOREXTRA6 | Valor Extra6 | Número Decimal | 20 |  |
| 161 | TMOV.PERCENTUALEXTRA7 | Percentual Extra7 | Número Decimal | 20 |  |
| 162 | TMOV.VALOREXTRA7 | Valor Extra7 | Número Decimal | 20 |  |
| 163 | TMOV.PERCENTUALEXTRA8 | Percentual Extra8 | Número Decimal | 20 |  |
| 164 | TMOV.VALOREXTRA8 | Valor Extra8 | Número Decimal | 20 |  |
| 165 | TMOV.PERCENTUALEXTRA9 | Percentual Extra9 | Número Decimal | 20 |  |
| 166 | TMOV.VALOREXTRA9 | Valor Extra9 | Número Decimal | 20 |  |
| 167 | TMOV.PERCENTUALEXTRA10 | Percentual Extra10 | Número Decimal | 20 |  |
| 168 | TMOV.VALOREXTRA10 | Valor Extra10 | Número Decimal | 20 |  |

Observação: Valor Extra e Percentual Extra de 3 a 10 disponíveis a partir da versão 12.1.2606.

**Campos Complementares:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Valor Fixo | 1 | Valor Fixo: O |

**Relacionamento entre Movimentos:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: E |
| 2 | TMOVRELAC.CODCOLORIGEM | Código da Coligada | Número Inteiro | 5 |  |
| 3 | TMOV.SERIE | Série | Texto | 8 |  |
| 4 | TMOV.NUMEROMOV | Número do Movimento | Texto | 35 |  |
| 5 | TMOV.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 6 | TMOV.CODCFOAUX | Código Cliente/Fornecedor Auxiliar | Texto | 25 |  |
| 7 | TMOVRELAC.TIPORELAC | Tipo de Relacionamento entre Movimentos | Texto | 1 | Verificar [Constantes de Relacionamento - Tabela TMOVRELAC](https://tdn.totvs.com/display/LRM/Constantes) preenchendo com apenas com o valor da constante |
| 8 | TMOV.CODCFO | Código do Cliente/Fornecedor | Texto | 25 |  |
| 9 | TMOV.CODCOLCFOAUX | Código da Coligada do Cliente/Fornecedor Auxiliar | Número Inteiro | 5 |  |

**Itens de Movimentos :**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: I |
| 2 | TITMMOV.CODIGOPRD | Código do Produto | Texto | 30 |  |
| 3 | TITMMOV.NUMEROSEQUENCIAL | Número Sequencial | Número Inteiro | 5 |  |
| 4 | TITMMOV.CODTIP | Código Tipo de Produto para Faturamento | Texto | 10 |  |
| 5 | TITMMOV.QUANTIDADE | Quantidade | Número Decimal | 20 |  |
| 6 | TITMMOV.PRECOUNITARIO | Preço Unitário | Número Decimal | 20 |  |
| 7 | TITMMOV.PRECOTABELA | Preço Tabela | Número Decimal | 20 |  |
| 8 | TITMMOV.PERCENTUALDESC | Percentual Desconto | Número Decimal | 20 |  |
| 9 | TITMMOV.VALORDESC | Valor Desconto | Número Decimal | 20 |  |
| 10 | TITMMOV.PERCENTUALDESP | Percentual Despesa | Número Decimal | 20 |  |
| 11 | TITMMOV.VALORDESP | Valor Despesa | Número Decimal | 20 |  |
| 12 | TITMMOV.DATAEMISSAO | Data de Emissão | Data | 10 |  |
| 13 | TITMMOV.CODMEN | Código da Mensagem | Texto | 5 |  |
| 14 | TITMMOV.NUMEROTRIBUTOS | Número de Tributos | Número Inteiro | 5 |  |
| 15 | TITMMOV.CODTB1FAT | Código Tabela Classificação1 Produto | Texto | 10 |  |
| 16 | TITMMOV.CODTB2FAT | Código Tabela Classificação2 Produto | Texto | 10 |  |
| 17 | TITMMOV.CODTB3FAT | Código Tabela Classificação3 Produto | Texto | 10 |  |
| 18 | TITMMOV.CODTB4FAT | Código Tabela Classificação4 Produto | Texto | 10 |  |
| 19 | TITMMOV.CODTB5FAT | Código Tabela Classificação5 Produto | Texto | 10 |  |
| 20 | TITMMOV.CODTB1FLX | Código Tabela Classificação1 Opcionais | Texto | 25 |  |
| 21 | TITMMOV.CODTB2FLX | Código Tabela Classificação2 Opcionais | Texto | 25 |  |
| 22 | TITMMOV.CODTB3FLX | Código Tabela Classificação3 Opcionais | Texto | 25 |  |
| 23 | TITMMOV.CODTB4FLX | Código Tabela Classificação4 Opcionais | Texto | 25 |  |
| 24 | TITMMOV.CODTB5FLX | Código Tabela Classificação5 Opcionais | Texto | 25 |  |
| 25 | TITMMOV.CAMPOLIVRE | Campo Livre | Texto | 15 |  |
| 26 | TITMMOV.CODUND | Código da Unidade | Texto | 5 |  |
| 27 | TITMMOV.QUANTIDADEARECEBER | Quantidade a Receber | Número Decimal | 20 |  |
| 28 | TITMMOV.IDNAT | Identificador da Natureza | Número Inteiro | 5 |  |
| 29 | TITMMOV.CODCPG | Código da Condição de Pagamento | Texto | 5 |  |
| 30 | TITMMOV.DATAENTREGA | Data da Entrega | Data | 10 |  |
| 31 | TITMMOV.PRATELEIRA | Prateleira | Texto | 15 |  |
| 32 | TITMMOV.IDCNT | Identificador do Contrato | Número Inteiro | 10 |  |
| 33 | TITMMOV.NSEQITMCNT | Número Sequencial do Item de Contrato | Número Inteiro | 5 |  |
| 34 | TITMMOV.VALORTOTALITEM | Valor Total do Item | Número Decimal | 20 |  |
| 35 | TITMMOV.CODCCUSTO | Centro de Custo | Texto | 25 |  |
| 36 | TITMMOV.CODNAT | Código da Natureza | Texto | 20 |  |
| 37 | TITMMOV.CODRPR | Representante | Texto | 15 |  |
| 38 | TITMMOV.IDPRDCOMPOSTO | Identificador do Produto Kit | Texto | 30 |  |
| 39 | TITMMOV.CODDEPARTAMENTO | Código do Departamento | Texto | 25 |  |
| 40 | TITMMOV.TRIBUTACAOECF | Código da Tributação ECF | Texto | 10 |  |
| 41 | TITMMOV.VALORESCRITURACAO | Valor Escrituração Fiscal | Número Decimal | 20 |  |
| 42 | TITMMOV.VALORCODIGOPRD | Valor do Código do Produto | Texto | 60 |  |
| 43 | TITMMOV.TIPOCODIGOPRD | Tipo do Código do Produto | Número Inteiro | 5 |  |
| 44 | TITMMOV.CST | Código Situação Tributária | Texto | 3 |  |
| 45 | TITMMOV.CODTRF | Código da Tarefa | Texto | 60 |  |
| 46 | TITMMOV.CODTBORCAMENTO | Código Tabela Orçamento | Texto | 10 |  |
| 47 | TITMMOV.VALOROPFRM1 | Valor opcional 1 por fórmula | Número Decimal | 20 |  |
| 48 | TITMMOV.VALOROPFRM2 | Valor opcional 2 por fórmula | Número Decimal | 20 |  |
| 49 | TITMMOV.CANCELADO | Cancelado | Texto | 1 |  |
| 50 | TITMMOV.VALORUNTORCAMENTO | Valor Unitário do Orçamento | Número Decimal | 20 |  |
| 51 | TITMMOV.DATAORCAMENTO | Data do Orçamento | Data | 10 |  |
| 52 | TITMMOV.COMISSAOREPRES | Percentual de comissão do representante | Número Decimal | 20 |  |
| 53 | TITMMOV.QTDUNDPEDIDO | Quantidade na Unid. do Pedido | Número Decimal | 20 |  |
| 54 | TITMMOV.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 55 | TITMMOV.CODLOC | Código do Local de Estoque Movimentado | Texto | 15 |  |
| 56 | TITMMOV.VALORLIQUIDO | Valor Líquido do Item | Número Decimal | 20 |  |
| 57 | TITMMOV.CODVEN1 | Código do Vendedor | Texto | 16 |  |
| 58 | TITMMOV.PERCENTCOMISSAO | Comissão do funcionário por item | Número Decimal | 20 |  |
| 59 | TITMMOV.IDREGRATRIBUTARIA | Identificador da Regra Tributária | Número Inteiro | 4 |  |
| 60 | TITMMOV.DATARETORNOREMESSA | Data de Retorno de Remessa | Data | 10 |  |

**Grade de Itens de Movimentos** **(Descontinuado):**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: G |
| 2 | TPRD.CODIGOPRD | Código do Produto | Texto | 30 |  |
| 3 | TITMMOVGRD.NSEQITMMOV | Número Sequencial do Item de Movimento | Número Inteiro | 5 |  |
| 4 | TITMMOVGRD.CODGRD | Código da Grade | Texto | 20 |  |
| 5 | TITMMOVGRD.NSEQITMGRD | Número Sequencial do Item da Grade | Número Inteiro | 5 |  |
| 6 | TITMMOV.QUANTIDADE | Quantidade | Número Decimal | 20 |  |
| 7 | TITMMOV.QUANTIDADEARECEBER | Quantidade a Receber | Número Decimal | 20 |  |

**Lote de Itens de Movimentos:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: J |
| 2 | TLOTEPRD.NUMLOTE | Número do Lote | Texto | 50 |  |
| 3 | TPRD.CODIGOPRD | Código do Produto | Texto | 30 |  |
| 4 | TITMLOTEPRD.QUANTIDADE2 | Quantidade física 2 da mov. do lote | Número Decimal | 10 |  |

**Números de Série de Itens de Movimentos:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: S |
| 2 | TITMNUMSERIEPRD.NUMSERIE | Número de Série | Texto | 30 |  |
| 3 | TITMNUMSERIEPRD.CODIGOPRD | Código do Produto | Texto | 30 |  |

**Itens de Rateio por Centro de Custo:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: B |
| 2 | TITMMOVRATCCU.CODCCUSTO | Código do Centro de Custo | Texto | 25 |  |
| 3 | TITMMOVRATCCU.NSEQITMMOV | Número Seq. do Item do Movimento | Número Inteiro | 5 |  |
| 4 | TITMMOVRATCCU.PERCENTUAL | Percentual | Número Decimal | 20 |  |
| 5 | TITMMOVRATCCU.VALOR | Valor | Número Decimal | 20 |  |
| 6 | TITMMOVRATCCU.IDPRJ | Id. Projeto | Número Inteiro | 5 |  |
| 7 | TITMMOVRATCCU.IDTRF | Id. Tarefa | Número Inteiro | 5 |  |
| 8 | TITMMOVRATCCU.CODTBGRUPOORC | Código do Grupo Orçamentário | Texto | 40 |  |

**Itens de Rateio por Departamento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: V |
| 2 | TITMMOVRATDEP.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 3 | TITMMOVRATDEP.CODDEPARTAMENTO | Código do Departamento | Texto | 25 |  |
| 4 | TITMMOVRATDEP.NSEQITMMOV | Número Seq. do Item do Movimento | Número Inteiro | 5 |  |
| 5 | TITMMOVRATDEP.VALOR | Valor | Número Decimal | 20 |  |

**Histórico do Item de Movimento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: K |
| 2 | TITMMOVHISTORICO.HISTORICOCURTO/LONGO | Descrição Curta de Histórico | Texto | 255 |  |

**Fiscais do Item de Movimento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: [ |
| 2 | TITMMOVFISCAL.NROADICAO | Número da Adição de Importação | Número Inteiro | 5 |  |
| 3 | TITMMOVFISCAL.NROITEM | Número sequencial do Item na Adição | Número Inteiro | 5 |  |
| 4 | TITMMOVFISCAL.VALORDESC | Valor do Desconto do Item da DI | Número Decimal | 20 |  |
| 5 | TITMMOVFISCAL.VALORDESPADU | Valor das Despesas Aduaneiras | Número Decimal | 20 |  |
| 6 | TITMMOVFISCAL.NATREC | Natureza da Receita | Texto | 3 |  |
| 7 | TITMMOVFISCAL.NATBCCRED | Código da Base de Crédito | Texto | 2 |  |
| 8 | TITMMOVFISCAL.INDNATFRETE | Indicador da Natureza do Frete | Texto | 1 |  |
| 9 | TITMMOVFISCAL.VLRTOTTRIB | Valor aproximado total de tributos federais, estaduais e municipais | Número Decimal | 20 |  |

**Relacionamento do Item de Movimento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: X |
| 2 | TPRD.CODIGOPRD | Código do Produto | Texto | 30 |  |
| 3 | TITMMOVRELAC.CODCOLORIGEM | Código da Coligada | Número Inteiro | 5 |  |
| 4 | TMOV.NUMEROMOV | Número do Movimento | Texto | 35 |  |
| 5 | TMOV.SERIE | Série | Texto | 8 |  |
| 6 | TMOV.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 7 | TMOV.CODCFOAUX | Código Cliente/Fornecedor Auxiliar | Texto | 25 |  |
| 8 | TITMMOVRELAC.NSEQITMMOVORIGEM | Número Seq. do Item do Movimento | Número Inteiro | 5 |  |
| 9 | TMOV.CODCOLCFOAUX | Código da Coligada do Cliente/Fornecedor Auxiliar | Número Inteiro | 5 |  |

**Relacionamento de item de movimento Devolução:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: X |
| 2 | TPRODUTO.CODIGOPRD | Código do Produto | Texto | 30 |  |
| 3 | TITMMOVRELAC.CODCOLDESTINO | Código da Coligada de Destino | Número Inteiro | 5 |  |
| 4 | TMOV.NUMEROMOV | Número do Movimento | Texto | 35 |  |
| 5 | TMOV.SERIE | Série | Texto | 8 |  |
| 6 | TMOV.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 7 | TMOV.CODCFOAUX | Código Cliente/Fornecedor Auxiliar | Texto | 25 |  |
| 8 | TITMMOVRELAC.NSEQITMMOVDESTINO | Número Seq. do Item do Movimento de Destino | Número Inteiro | 5 |  |
| 9 | TMOV.CODCOLCFOAUX | Código da Coligada do Cliente/Fornecedor Auxiliar | Número Inteiro | 5 |  |
| 10 | TITMMOVRELAC.NSEQITMMOVORIGEM | Número Seq. do Item do Movimento Original | Número Inteiro | 5 |  |

**Tributos de Movimentos/Itens:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: T |
| 2 | TTRBMOV.NSEQITMMOV | Sequencial | Número Inteiro | 5 |  |
| 3 | TTRBMOV.CODTRB | Código do Tributo | Texto | 10 |  |
| 4 | TTRBMOV.BASEDECALCULO | Base de Cálculo | Número Decimal | 20 |  |
| 5 | TTRBMOV.ALIQUOTA | Alíquota | Número Decimal | 20 |  |
| 6 | TTRBMOV.VALOR | Valor | Número Decimal | 20 |  |
| 7 | TTRBMOV.FATORREDUCAO | Fator de Redução | Número Decimal | 20 |  |
| 8 | TTRBMOV.FATORSUBSTTRIB | Fator Substituição Tributária | Número Decimal | 20 |  |
| 9 | TTRBMOV.VLRISENTO | Isento Outros Tributos | Número Decimal | 20 |  |
| 10 | TTRBMOV.CODRETENCAO | Código de retenção do imposto | Texto | 5 |  |
| 11 | TTRBMOV.TIPORECOLHIMENTO | Tipo de Recolhimento do ISS | Texto | 5 |  |
| 12 | TTRBMOV.CODTRBBASE | Tributo Base para Escrituração | Texto | 10 |  |
| 13 | TTRBMOV.BASEDECALCULOCALCULADA | Base de Cálculo Obtida pela Fórmula | Número Decimal | 20 |  |
| 14 | TTRBMOV.EDITADO | Usuário editou os valores do tributo | Número Inteiro | 5 |  |
| 15 | TTRBMOV.MODALIDADEBC | Modalidade de Determinação da BC | Texto | 1 |  |
| 16 | TTRBMOV.SITTRIBUTARIA | Situação Tributária | Texto | 2 |  |
| 17 | TTRBMOV.VALORICMSDESONERADO | Valor do ICMS Desonerado | Número Decimal | 10 |  |
| 18 | TTRBMOV.VALORRETSUSPJUDIC | Valor do imposto não retido por decisão judicial | Número Decimal | 10 |  |
| 19 | TTRBMOV.ALIQUOTACHEIA | Alíquota Cheia | Número Decimal | 20 |  |
| 20 | TTRBMOV.PCTREDUCAOALIQUOTA | Percentual de Redução de Alíquota | Número Decimal | 20 |  |
| 21 | TTRBMOV.PCTDIFERIMENTO | Percentual de Diferimento | Número Decimal | 20 |  |
| 22 | TTRBMOV.TRIBUTODIFERIDO | Tributo Diferido | Número Decimal | 20 |  |
| 23 | TTRBMOV.CLASSTRIB | Classificação Tributária | Texto | 15 |  |
| 24 | TTRBMOV.CODCREDPRESUMIDO | Código do Crédito Presumido | Texto | 15 |  |
| 25 | TTRBMOV.PCCREDPRESUMIDO | Percentual do Crédito Presumido | Número Decimal | 20 |  |
| 26 | TTRBMOV.VALORCREDPRESUMIDO | Valor do Crédito Presumido | Número Decimal | 20 |  |

**Lançamento Financeiro :**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: L |
| 2 | FLAN.DATAVENCIMENTO | Data de Vencimento | Data | 10 |  |
| 3 | FLAN.DATAPREVBAIXA | Data Prevista de Baixa | Data | 10 |  |
| 4 | FLAN.HISTORICO | Histórico | Texto | 255 |  |
| 5 | FLAN.VALORORIGINAL | Valor Original | Número Decimal | 20 |  |
| 6 | FLAN.VALOROP1 | Valor OP1 | Número Decimal | 20 |  |
| 7 | FLAN.VALOROP2 | Valor OP2 | Número Decimal | 20 |  |
| 8 | FLAN.VALOROP3 | Valor OP3 | Número Decimal | 20 |  |
| 9 | FLAN.VALOROP4 | Valor OP4 | Número Decimal | 20 |  |
| 10 | FLAN.VALOROP5 | Valor OP5 | Número Decimal | 20 |  |
| 11 | FLAN.VALOROP6 | Valor OP6 | Número Decimal | 20 |  |
| 12 | FLAN.VALOROP7 | Valor OP7 | Número Decimal | 20 |  |
| 13 | FLAN.VALOROP8 | Valor OP8 | Número Decimal | 20 |  |
| 14 | FLAN.SEGUNDONUMERO | Segundo Número | Texto | 20 |  |
| 15 | FLAN.DATAOP1 | Data OP1 | Data | 10 |  |
| 16 | FLAN.DATAOP2 | Data OP2 | Data | 10 |  |
| 17 | FLAN.DATAOP3 | Data OP3 | Data | 10 |  |
| 18 | FLAN.CNABCARTEIRA | CNAB Carteira | Número Inteiro | 5 |  |
| 19 | FLAN.CNABCOMANDO | CNAB Comando | Número Inteiro | 5 |  |
| 20 | FLAN.CNABACEITE | CNAB Aceite | Número Inteiro | 5 |  |
| 21 | CNABINSTRUCAOCOD1 | CNAB Instrução Código 1 | Número Inteiro | 5 |  |
| 22 | CNABINSTRUCAOCOD2 | CNAB Instrução Código 2 | Número Inteiro | 5 |  |
| 23 | CNABNOSSONUMERO | CNAB Nosso Número | Texto | 20 |  |
| 24 | FLAN.CNABSTATUS | CNAB Status | Número Inteiro | 5 |  |
| 25 | FLAN.CNABBANCO | CNAB Banco | Texto | 3 |  |
| 26 | FLAN.CAMPOALFAOP1 | Campo Alfa OP1 | Texto | 100 |  |
| 27 | FLAN.CAMPOALFAOP2 | Campo Alfa OP2 | Texto | 20 |  |
| 28 | FLAN.CAMPOALFAOP3 | Campo Alfa OP3 | Texto | 20 |  |
| 29 | FLAN.IPTE | IPTE | Texto | 48 |  |
| 30 | FLAN.CODIGOBARRA | Código de Barras | Texto | 44 |  |
| 31 | FLAN.CONVENIO | Convênio | Texto | 20 |  |

**Pagamentos:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: P |
| 2 | TFORMAPAGTO.CODFORMAPAGTO | Código Forma de Pagamento | Texto | 10 |  |
| 3 | TPAGTO.BANCO | Código do Banco | Texto | 4 |  |
| 4 | TPAGTO.AGENCIA | Código da Agência | Texto | 20 |  |
| 5 | TPAGTO.DIGITOAGENCIA | Dígito da Agência | Texto | 2 |  |
| 6 | TPAGTO.CODPERIODO | Período | Texto | 20 |  |
| 7 | TPAGTO.CC | Código da C/C | Texto | 20 |  |
| 8 | TPAGTO.DIGITOCC | Dígito C/C | Texto | 2 |  |
| 9 | TPAGTO.DATAVENCIMENTO | Data de Vencimento | Data | 10 |  |
| 10 | TPAGTO.DEBITOCREDITO | Débito/Crédito | Texto | 1 |  |
| 11 | TPAGTO.CHEQUE | Número do Cheque | Texto | 20 |  |
| 12 | TPAGTO.DIGITOCHEQUE | Dígito do Cheque | Texto | 2 |  |
| 13 | TPAGTO.NSU | Número da Transação (NSU) | Texto | 12 |  |
| 14 | TPAGTO.TIPOPARCELAMENTO | Parcelado Administradora | Número Inteiro | 5 |  |
| 15 | TPAGTO.VALOR | Valor | Número Decimal | 20 |  |
| 16 | TPAGTO.DOLAR | Pagamento em Dólar | Número Inteiro | 5 |  |
| 17 | TPAGTO.TIPOPAGAMENTO | Tipo do Pagamento | Número Inteiro | 5 |  |
| 18 | TPAGTO.DATAEMISSAO | Data de Emissão | Data | 10 |  |
| 19 | TPAGTO.QTDEPARCELAS | Quantidade de Parcelas | Número Inteiro | 5 |  |
| 20 | TPAGTO.CNPJCPF | CNPJ ou CPF do Emitente do Cheque | Texto | 20 |  |
| 21 | TPAGTO.FISICAJURIDICA | Pessoa Física/Jurídica | Texto | 1 |  |
| 22 | TPAGTO.DATACOMPROVANTE | Data do Comprovante | Data | 10 |  |
| 23 | TPAGTO.CMC7 | Código CMC-7 | Texto | 60 |  |
| 24 | TPAGTO.NOMEREDE | Nome da Rede | Texto | 8 |  |
| 25 | TPAGTO.FINALIZACAO | Código Finalização | Texto | 30 |  |
| 26 | TPAGTO.ADMINISTRADORA | Nome da Administradora | Texto | 12 |  |
| 27 | TPAGTO.BAIXADO | Pagamento Baixado | Número Inteiro | 5 |  |
| 28 | TPAGTO.DESCRICAO | Descrição | Texto | 40 |  |
| 29 | TPAGTO.CODCOLCXA | Coligada da Conta Caixa | Número Inteiro | 5 |  |
| 30 | TPAGTO.CODCXA | Conta Caixa | Texto | 10 |  |
| 31 | TPAGTO.CAMPOLIVRE | Campo Livre | Texto | 100 |  |
| 32 | TPAGTO.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 33 | TPAGTO.CODCOLCFO | Coligada do Cliente/Fornecedor | Número Inteiro | 5 |  |
| 34 | TPAGTO.CODCFO | Código do Cliente/Fornecedor | Texto | 25 |  |
| 35 | FLAN.CODTDO | Código do Tipo de Documento | Texto | 10 |  |
| 36 | FLAN.NUMERODOCUMENTO | Número do Documento | Texto | 40 |  |
| 37 | FLAN.SERIEDOCUMENTO | Série do Documento | Texto | 8 |  |
| 38 | TPAGTO.TAXAADM | Taxa Administrativa | Número Decimal | 20 |  |
| 39 | TPAGTO.NOMEEMITENTE | Nome do Emitente | Texto | 30 |  |
| 40 | TPAGTO.TELEMITENTE | Telefone do Emitente | Texto | 20 |  |

**Contabilidade:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: C |
| 2 | TMOVCONT.TIPO | Tipo do Lançamento | Número Inteiro | 5 |  |
| 3 | TMOVCONT.CODCOLCONTA | Coligada da Conta Contábil | Número Inteiro | 5 |  |
| 4 | TMOVCONT.CODCONTA | Conta Contábil | Texto | 40 |  |
| 5 | TMOVCONT.VALOR | Valor do Lançamento | Número Decimal | 20 |  |
| 6 | TMOVCONT.CODFILIAL | Código da Filial | Número Inteiro | 5 |  |
| 7 | TMOVCONT.CODDEPARTAMENTO | Código do Departamento | Texto | 25 |  |
| 8 | TMOVCONT.CODCCUSTO | Código do Centro de Custo | Texto | 25 |  |
| 9 | TMOVCONT.CODHISTP | Código do Histórico | Texto | 10 |  |
| 10 | TMOVCONT.COMPLHISTORICO | Complemento do Histórico | Texto | 250 |  |
| 11 | TMOVCONT.ATIVO | Indica se está ativo | Número Inteiro | 5 |  |

**Rateio da Contabilidade:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: R |
| 2 | TMOVRAT.TIPO | Tipo do Lançamento | Número Inteiro | 5 |  |
| 3 | TMOVRAT.CODCOLCONTA | Coligada da Conta Contábil | Número Inteiro | 5 |  |
| 4 | TMOVRAT.CODCONTA | Código da Conta | Texto | 40 |  |
| 5 | TMOVRAT.VALOR | Valor do Lançamento | Número Decimal | 20 |  |
| 6 | TMOVRAT.CODCOLCONTAGER | Coligada da Conta Gerencial | Número Inteiro | 5 |  |
| 7 | TMOVRAT.CODCONTAGER | Conta Gerencial | Texto | 40 |  |

**Transporte:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: @ |
| 2 | TMOVTRANSP.CODETDENTREGA | UF Entrega da Mercadoria Transportada | Texto | 2 |  |
| 3 | TMOVTRANSP.CODMUNICIPIOENTREGA | Município Entrega da Mercadoria Transp. | Texto | 20 |  |
| 4 | TMOVTRANSP.CODETDCOLETA | UF Coleta da Mercadoria Transportada | Texto | 2 |  |
| 5 | TMOVTRANSP.CODMUNICIPIOCOLETA | Município de Coleta da Mercadoria Transportada | Texto | 20 |  |
| 6 | TMOVTRANSP.TIPOREMETENTE | Tipo Remetente da Mercadoria | Texto | 1 |  |
| 7 | TMOVTRANSP.REMETENTECODCOLCFO | Coligada do Remetente Cliente/Fornecedor | Número Inteiro | 5 |  |
| 8 | TMOVTRANSP.REMETENTECODCFO | Código Cliente do Remetente Cliente/Fornecedor | Texto | 25 |  |
| 9 | TMOVTRANSP.REMETENTEFILIAL | Código da Filial - Remetente Filial | Número Inteiro | 5 |  |
| 10 | TMOVTRANSP.TIPODESTINATARIO | Tipo Destinatário da Mercadoria | Texto | 1 |  |
| 11 | TMOVTRANSP.DESTINATARIOCODCOLCFO | Coligada do Destinatário Cliente/Fornecedor | Número Inteiro | 5 |  |
| 12 | TMOVTRANSP.DESTINATARIOCODCFO | Código do Cliente Destinatário Cliente/Fornecedor | Texto | 25 |  |
| 13 | TMOVTRANSP.DESTINATARIOFILIAL | Código da Filial - Destinatário Filial | Número Inteiro | 5 |  |
| 14 | TMOVTRANSP.CODTRAREDESPACHO | Cód. da Transp. responsável pelo REDESPACHO | Texto | 5 |  |
| 15 | TMOVTRANSP.CNPJCPFCOLETA | CNPJ/CPF do Contribuinte na Coleta | Texto | 20 |  |
| 16 | TMOVTRANSP.INSCRESTCOLETA | Inscr. Estadual do Contribuinte na Coleta | Texto | 20 |  |
| 17 | TMOVTRANSP.INSCRMUNCOLETA | Inscr. Municipal do Contribuinte na Coleta | Texto | 20 |  |
| 18 | TMOVTRANSP.CNPJCPFENTREGA | CNPJ/CPF do Contribuinte na Entrega | Texto | 20 |  |
| 19 | TMOVTRANSP.INSCRESTENTREGA | Inscr. Estadual do Contribuinte na Entrega | Texto | 20 |  |
| 20 | TMOVTRANSP.INSCRMUNENTREGA | Inscr. Municipal do Contribuinte na Entrega | Texto | 20 |  |
| 21 | TMOVTRANSP.TIPOFRETEREDESPACHO | Tipo Frete Redespacho | Texto | 1 |  |
| 22 | TMOVTRANSP.RUACOLETA | Rua da coleta | Texto | 100 |  |
| 23 | TMOVTRANSP.NUMEROCOLETA | Número da coleta | Texto | 8 |  |
| 24 | TMOVTRANSP.COMPLCOLETA | Complemento da coleta | Texto | 30 |  |
| 25 | TMOVTRANSP.BAIRROCOLETA | Bairro da coleta | Texto | 30 |  |
| 26 | TMOVTRANSP.RUAENTREGA | Rua da entrega | Texto | 100 |  |
| 27 | TMOVTRANSP.NUMEROENTREGA | Número da entrega | Texto | 8 |  |
| 28 | TMOVTRANSP.COMPLENTREGA | Complemento da entrega | Texto | 30 |  |
| 29 | TMOVTRANSP.BAIRROENTREGA | Bairro da entrega | Texto | 30 |  |

**Conhecimento de Transporte:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo:# |
| 2 | TCTRCMOV.QUANTIDADENOTAS | Quantidade de Notas Acobertadas pelo CTRC | Número Inteiro | 10 |  |
| 3 | TCTRCMOV.VALORNOTAS | Somatório do Valor das Notas Acobertadas | Número Decimal | 20 |  |

**Item de Conhecimento de Transporte:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Transporte | Texto | 1 | Valor Fixo:$ |
| 2 | TCTRC.NUMEROSEQNOTA | Numero sequencial Nota Fiscal | Número Inteiro | 10 |  |
| 3 | TMOV.SERIE | SERIE | Texto | 8 |  |
| 4 | TMOV.NUMEROMOV | NUMEROMOV | Texto | 35 |  |
| 5 | TMOV.CODFILIAL | CODFILIAL | Número Inteiro | 10 |  |
| 6 | TMOV.CODCFOAUX | CODCFOAUX | Texto | 25 |  |
| 7 | TMOV.CODTDOAUX | CODTDOAUX | Texto | 10 |  |
| 8 | TCTRC.CNPJ | CNPJ | Texto | 20 |  |
| 9 | TCTRC.INSCESTADUAL | Insc. Estadual do Remetente/Destinatário | Texto | 20 |  |
| 10 | TCTRC.UF | UF do Remetente/Destinatário | Texto | 2 |  |
| 11 | TCTRC.CODMUNICIPIO | Município do Remetente/Destinatário | Texto | 20 |  |
| 12 | TCTRC.NOME | Razão Social do Remetente/Destinatário | Texto | 60 |  |
| 13 | TCTRC.DATAEMISSAO | Data de Emissão da NF do conhecimento | Data | 10 |  |
| 14 | TCTRC.CODTDO | Espécie Doc. que acoberta Carga Transp. | Texto | 10 |  |
| 15 | TCTRC,SERIEDOC | Serie Doc. que acoberta Carga Transp. | Texto | 4 |  |
| 16 | TCTRC.SUBSERIEDOC | Subsérie Doc. que acoberta Carga Transp. | Texto | 3 |  |
| 17 | TCTRC.NUMERODOC | Numero Doc. que acoberta Carga Transp. | Texto | 12 |  |
| 18 | TCTRC.VALORTOTAL | Valor Total Nota acoberta Carga Transp. | Número Decimal | 20 |  |
| 19 | TMOV.CODCOLCFOAUX | CODCOLCFOAUX | Número Inteiro | 10 |  |
| 20 | TCTRC.QUANTIDADE | Quantidade | Número Decimal | 20 |  |
| 21 | TCTRC.VALORMERCADORIAS | Valor das Mercadorias | Número Decimal | 20 |  |
| 22 | NATUREZAVOLUMES | Natureza dos Volumes | Texto | 30 |  |
| 23 | TCTRC.VOLUMES | Volume Transportado | Texto | 30 |  |
| 24 | TCTRC.MARCA | Marca da Mercadoria Transportada | Texto | 30 |  |
| 25 | TCTRC.ESPECIE | Espécie da Mercadoria Transportada | Texto | 30 |  |
| 26 | TCTRC.NUMEROCARGA | Numeração da Mercadoria Transportada | Número Inteiro | 10 |  |
| 27 | TCTRC.PESOBRUTO | Peso Bruto | Número Decimal | 20 |  |
| 28 | TCTRC.PESOLIQUIDO | Peso Líquido | Número Decimal | 20 |  |
| 29 | TCTRC.CHAVEACESSONFE | Chave de Acesso da NF-e | Texto | 50 |  |

**Rateios por Departamento do Lançamento Financeiro:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: Y |

**Rateios por Centro de Custo:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: U |
| 2 | TMOVRATCCU.CODCCUSTO | Centro de Custo | Texto | 25 |  |
| 3 | TMOVRATCCU.VALOR | Valor | Número Decimal | 20 |  |
| 4 | TMOVRATCCU.HISTORICO | Histórico do rateio | Texto | 255 |  |
| 5 | TMOVRATCCU.PERCENTUAL | Percentual | Número Decimal | 20 |  |
| 6 | TMOVRATCCU.IDPRJ | Id. Projeto | Número Inteiro | 5 |  |
| 7 | TMOVRATCCU.IDTRF | Id. Tarefa | Número Inteiro | 5 |  |
| 8 | TMOVRATCCU.CODTBGRUPOORC | Cód. Grupo Orçamentário | Texto | 40 |  |

**Rateios por Departamento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: D |
| 2 | TMOVRATDEP.CODFILIAL | Filial | Número Inteiro | 5 |  |
| 3 | TMOVRATDEP.CODDEPARTAMENTO | Departamento | Texto | 25 |  |
| 4 | TMOVRATDEP.VALOR | Valor | Número Decimal | 20 |  |

**Histórico do Movimento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: H |
| 2 | TMOVHISTORICO.HISTORICOCURTO/HISTORICOLONGO | Descrição Curta de Histórico | Texto | 255 |  |

**Notas Fiscais de Terceiros:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: < |
| 2 | TNFTERCEIROS.IDNFTERCEIROS | Identificador da NF de Terceiros | Texto | 10 |  |
| 3 | TNFTERCEIROS.CODTDO | Espécie do Documento | Texto | 10 |  |
| 4 | TNFTERCEIROS.DOCINI | Número do Documento | Texto | 15 |  |
| 5 | TNFTERCEIROS.SERIEDOC | Série | Texto | 4 |  |
| 6 | TNFTERCEIROS.SUBSERIE | Subsérie | Texto | 3 |  |
| 7 | TNFTERCEIROS.CNPJCPFCEI | CNPJ/CPF/CEI do Emitente | Texto | 20 |  |
| 8 | TNFTERCEIROS.UF | UF do Emitente | Texto | 2 |  |
| 9 | TNFTERCEIROS.MOTIVOREF | Motivo de Referência | Texto | 2 |  |
| 10 | TNFTERCEIROS.OBSERVACAO | Observação da NF de Terceiros | Texto | 150 |  |
| 11 | TNFTERCEIROS.VALORTOTAL | Valor da NF de Terceiros | Número Decimal | 20 |  |
| 12 | TNFTERCEIROS.INSCRESTADUAL | Inscrição Estadual do Emitente | Texto | 20 |  |
| 13 | TNFTERCEIROS.DATAEMISSAO | Data Emissão da NF Terceiros | Data | 10 |  |

**Dados Fiscais do Movimento:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: = |
| 2 | TMOVFISCAL.DECLARACAOEXPORTACAO | Núm. Declaração de Exportação | Texto | 11 |  |
| 3 | TMOVFISCAL.DATADE | Data Declaração de Exportação | Data | 10 |  |
| 4 | TMOVFISCAL.NATUREZAEXPORTACAO | Natureza de Exportação | Número Inteiro | 5 |  |
| 5 | TMOVFISCAL.CONHECIMENTOEMBARQUE | Conhecimento de Embarque | Texto | 16 |  |
| 6 | TMOVFISCAL.DATACE | Data Conhecimento de Embarque | Data | 10 |  |
| 7 | TMOVFISCAL.TIPOCE | Tipo Conhecimento de Embarque | Número Inteiro | 5 |  |
| 8 | TMOVFISCAL.DATAAVERBACAO | Data de Averbação | Data | 10 |  |
| 9 | TMOVFISCAL.DECLARACAOIMPORTACAO | Núm. Declaração de Importação | Texto | 12 |  |
| 10 | TMOVFISCAL.DATADI | Data Declaração de Importação | Data | 10 |  |
| 11 | TMOVFISCAL.VALORDESPACHO | Valor do Despacho | Número Decimal | 20 |  |
| 12 | TMOVFISCAL.NUMDESPACHO | Número do Despacho | Texto | 11 |  |
| 13 | TMOVFISCAL.LOCALDESEMBARACO | Local de Desembaraço | Texto | 60 |  |
| 14 | TMOVFISCAL.UFDESEMBARACO | UF do Desembaraço | Texto | 2 |  |
| 15 | TMOVFISCAL.NATUREZAIMPORTACAO | Natureza de Importação | Texto | 5 |  |
| 16 | TMOVFISCAL.DATADESEMBARACO | Data do Desembaraço Aduaneiro | Data | 10 |  |
| 17 | TMOVFISCAL.NROCONTRATOASSINANTE | Número do Contrato do Assinante | Texto | 20 |  |
| 18 | TMOVFISCAL.DATACONTRATOINIASSINANTE | Data de Início do Contrato | Data | 10 |  |
| 19 | TMOVFISCAL.DATACONTRATOFIMASSINANTE | Data de Fim do Contrato | Data | 10 |  |
| 20 | TMOVFISCAL.NROTERMINALPRINCASSINANTE | Número do Terminal Principal do Serviço Contratado | Texto | 12 |  |
| 21 | TMOVFISCAL.CODETDTERMINALPRINCASSINANTE | Código da UF de Habilitação do Terminal Principal | Texto | 2 |  |
| 22 | TMOVFISCAL.CNPJCPFDESTSERV | CNPJ/CPF do Destinatário do Serviço | Texto | 20 |  |
| 23 | TMOVFISCAL.NIFDESTSERV | Número de Identificação Fiscal do Destinatário do Serviço | Texto | 40 |  |
| 24 | TMOVFISCAL.NAONIFDESTSERV | Motivo para não Informação do NIF do Destinatário do Serviço | Texto | 2 |  |
| 25 | TMOVFISCAL.NOMEDESTSERV | Nome do Destinatário do Serviço | Texto | 150 |  |
| 26 | TMOVFISCAL.CODMUNICIPIODESTSERV | Código do Município do Destinatário do Serviço | Texto | 20 |  |
| 27 | TMOVFISCAL.CEPDESTSERV | CEP do Destinatário do Serviço | Texto | 12 |  |
| 28 | TMOVFISCAL.CODPAISDESTSERV | Código do Pais do Destinatário do Serviço | Número Inteiro | 2 |  |
| 29 | TMOVFISCAL.CODETDDESTSERV | UF do Destinatário do Serviço | Texto | 2 |  |
| 30 | TMOVFISCAL.RUADESTSERV | Rua do Destinatário do Serviço | Texto | 100 |  |
| 31 | TMOVFISCAL.NUMERODESTSERV | Número do Destinatário do Serviço | Texto | 8 |  |
| 32 | TMOVFISCAL.COMPLDESTSERV | Complemento do Destinatário do Serviço | Texto | 60 |  |
| 33 | TMOVFISCAL.BAIRRODESTSERV | Bairro do Destinatário do Serviço | Texto | 80 |  |
| 34 | TMOVFISCAL.TELEFONEDESTSERV | Telefone do Destinatário do Serviço | Texto | 20 |  |
| 35 | TMOVFISCAL.EMAILDESTSERV | E-mail do Destinatário do Serviço | Texto | 80 |  |
| 36 | TMOVFISCAL.IDEVENTO | Identificador das  Informações relativas às atividades de eventos. | Número Inteiro | 4 |  |
| 37 | TMOVFISCAL.DTCOMPETENCIASERVICO | Data Competência Serviço | Data | 8 |  |
| 38 | TMOVFISCAL.TPOPER | Tipo de Operação com Entes Governamentais ou serviços sobre bens imóveis | Número Inteiro | 2 |  |

**Notas Fiscais do Município de São Paulo:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: ] |
| 2 | TNFE.VALORSERVICO | Valor do Serviço | Número Decimal | 20 |  |
| 3 | TNFE.ALIQUOTAISS | Alíquota de ISS | Número Decimal | 20 |  |
| 4 | TNFE.BASEDECALCULO | Base de Cálculo do Serviço NFe | Número Decimal | 20 |  |

**Dispositivos de Segurança:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo: + |
| 2 | TMOVDISPOSITIVO.NROSEGURANCA | Número do Doc. ou Dispositivo de Segurança | Texto | 12 |  |

**Relacionamento Movimento Devolução:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo:: E |
| 2 | TMOV.CODCOLIGADA | CODCOLIGADA | Número Inteiro | 5 |  |
| 3 | TMOV.SERIE | SERIE | Texto | 8 |  |
| 4 | TMOV.NUMEROMOV | NUMEROMOV | Texto | 35 |  |
| 5 | TMOV.CODFILIAL | CODFILIAL | Número Inteiro | 5 |  |
| 6 | TMOV.CODCFOAUX | CODCFOAUX | Texto | 25 |  |
| 7 | TMOVRELAC.TIPORELAC | Tipo de Relacionamento entre Movimentos | Texto | 1 |  |
| 8 | TMOV.CODCFO | CODCFO | Texto | 25 |  |
| 9 | TMOV.CODCOLCFOAUX | CODCOLCFOAUX | Número Inteiro | 5 |  |

**Dados Fiscais de Serviço:**

| # | Tabela/Campo | Descrição | Tipo | Tamanho | Observação |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Tipo de Registro | Texto | 1 | Valor Fixo:: > |
| 2 | TMOVFISCALSERV.INSCRICAOIMOBILIARIA | Código da Inscrição Imobiliária Fiscal | Texto | 30 |  |
| 3 | TMOVFISCALSERV.CIB | Código do Cadastro Imobiliário Brasileiro | Texto | 8 |  |
| 4 | TMOVFISCALSERV.CEPENDIMOVEL | CEP do Endereço do Imóvel | Texto | 8 |  |
| 5 | TMOVFISCALSERV.ENDIMOVELLOGRADOURO | Logradouro do Endereço do Imóvel | Texto | 255 |  |
| 6 | TMOVFISCALSERV.ENDIMOVELNUMERO | Número no Logradouro do Endereço do Imóvel | Texto | 60 |  |
| 7 | TMOVFISCALSERV.ENDIMOVELCOMPLEMENTO | Complemento do Endereço do Imóvel | Texto | 156 |  |
| 8 | TMOVFISCALSERV.ENDIMOVELBAIRRO | Bairro do Endereço do Imóvel | Texto | 60 |  |
| 9 | TMOVFISCALSERV.ENDIMOVELEXTCEP | Código Postal do Imóvel no Exterior | Texto | 11 |  |
| 10 | TMOVFISCALSERV.ENDIMOVELEXTCIDADE | Cidade do Imóvel no Exterior | Texto | 60 |  |
| 11 | TMOVFISCALSERV.ENDIMOVELEXTREGIAO | Estado, Província ou Região da Cidade do Imóvel no Exterior | Texto | 60 |  |
| 12 | TMOVFISCALSERV.ENDIMOVELCODETD | Código do Estado | Texto | 2 |  |
| 13 | TMOVFISCALSERV.ENDIMOVELCODMUNICIPIO | Código do Municipio | Texto | 20 |  |
