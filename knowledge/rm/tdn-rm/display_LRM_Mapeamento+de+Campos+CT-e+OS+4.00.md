---
content_hash: 883e55933a8fc540ef0023d899b15f64a502457434a5d2d9f6b5119005f5a3e2
fetched_at: '2026-06-29T00:05:45.189437+00:00'
page_id: '1003484179'
product: rm
source: tdn-rm
title: Mapeamento de Campos CT-e OS 4.00
type: documentation
url: https://tdn.totvs.com/display/LRM/Mapeamento+de+Campos+CT-e+OS+4.00
version: 2
---

Campos\_CteOS

Campos\_CteOS

## **Mapeamento de Campos CT-e OS 4.00**

Estão listados abaixo os principais campos do CT-e OS de acordo com o Manual de Orientação do Contribuinte 4.00.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| TAG | | | | Campo ERP | Observações ERP |
| # | Campo | Descrição | Observação |
| 1 | versao | Versão do Leiaute |  |  |  |
| A. Dadosdo CT-e | | |  | | |
| 2 | infCte | Informações do CTe Outros Serviços |  |  |  |
| 3 | versao | Versão do leiaute | Versão do leiaute (v4.0) | TPARFILIAL.VERSAOCTE |  |
| 4 | Id | Identificador da TAG a ser assinada | Informar a chave de acesso do CTe OS e precedida do literal "CTe" |  |  |
| B. Identificação do CTe Outros Serviços | | |  | | |
| 6 | ide | Identificação do CT-e |  |  |  |
| 7 | cUF | Código da UF do emitente do CTe. | Utilizar a Tabela do IBGE. | GFILIAL.ESTADO |  |
| 8 | cCT | Código Numérico que compõe a Chave de Acesso | Número aleatório gerado pelo emitente para cada CTe, com o objetivo de evitar acessos indevidos ao documento. | Concatena TMOV.CODCOLIGADA + TMOV.IDMOV resultando em um numero aleatorio (num)  Se num > 8  {   pos = tamanho do num - 8;   num = num.Remove(pos, pos);  }  cnf = 100000000-num |  |
| 9 | CFOP | Código Fiscal de Operações e Prestações |  | DNATUREZA.CODNAT |  |
| 10 | natOp | Natureza da Operação |  | DNATUREZA.NOME |  |
| 11 | mod | Modelo do documento fiscal | Utilizar o código 67 para identificação do CTe Outros Serviços, emitido em substituição a Nota Fiscal Modelo 7 para transporte de pessoas, valores e excesso de bagagem. |  |  |
| 12 | serie | Série do CTe OS | Preencher com "0" no caso de série única | TMOV.SERIE |  |
| 13 | nCT | Número do CTe OS |  | TMOV.NUMEROMOV |  |
| 14 | dhEmi | Data e hora de emissão do CTe OS | Formato AAAA-MM-DDTHH:MM:DD TZD | TMOV.HORARIOEMISSAO |  |
| 15 | tpImp | Formato de impressão do DACTE OS | Preencher com: 1 - Retrato; 2 - Paisagem. | TTMVEXT.FORMATODACTE |  |
| 16 | tpEmis | Forma de emissão do CT-e | Preencher com: 1 - Normal; 5 - Contingência FSDA; 7 - Autorização pela SVC-RS; 8 - Autorização pela SVC-SP | TPARFILIAL.MODALIDADECTEOS |  |
| 17 | cDV | Digito Verificador da chave de acesso do CT-e | Informar o dígito de controle da chave de acesso do CTe, que deve ser calculado com a aplicação do algoritmo módulo 11 (base 2,9) da chave de acesso. |  |  |
| 18 | tpAmb | Tipo do Ambiente | Preencher com:1 - Produção; 2 - Homologação | TPARFILIAL.AMBIENTECTE |  |
| 19 | tpCTe | Tipo do CT-e OS | Preencher com: 0 - CTe Normal; 1 - CTe Complementar; 3 - CTe de Substituição. | TMOVTRANSP.TIPOCTE |  |
| 20 | procEmi | Identificador do processo de emissão do CT-e OS | Preencher com: 0 - emissão de CTe com aplicativo do contribuinte; 3- emissão CTe pelo contribuinte com aplicativo fornecido pelo Fisco. |  | 0 - Valor fixo |
| 21 | verProc | Versão do processo de emissão | Informar a versão do aplicativo emissor de CTe. |  | Busca a versão do TSS ou parceiro utilizado no totvscolaboração |
| 23 | cMunEnv | Código do Município de envio do CT-e (de onde o documento foi transmitido) | Utilizar a tabela do IBGE. Informar 9999999 para as operações com o exterior. | DVIEWMUNICIPIOS.CODIFICACAO (baseado no campo GFILIAL.CODMUNICIPIO) |  |
| 22 | XMunEnv | Nome do Município de envio do CT-e (de onde o documento foi transmitido) | Informar PAIS/Município para as operações com o exterior. | DVIEWMUNICIPIOS.NOMEMUNICIPIO (baseado no campo GFILIAL.CODMUNICIPIO) |  |
| 23 | UFEnv | Sigla da UF de envio do CT-e (de onde o documento foi transmitido) | Informar 'EX' para operações com o exterior. | GFILIAL.ESTADO |  |
| 24 | modal | Modal do CTe OS | Preencher com: 01-Rodoviário; 02- Aéreo; 03 - Aquaviário; 04 - Ferroviário. | TTMVEXT.MODAL |  |
| 25 | tpServ | Tipo do Serviço | Preencher com: 6 - Transporte de Pessoas; 7 - Transporte de Valores; 8 - Excesso de Bagagem. | TMOVTRANSP.TIPOSERVICOCTE |  |
| 26 | IndIEToma | Indicador da IE do tomador: 1 – Contribuinte ICMS; 2 – Contribuinte isento de inscrição; 9 – Não Contribuinte | Aplica-se ao tomador que for indicado no toma3 ou toma4 | FCFO.CONTRIBUINTE |  |
| 27 | cMunIni | Código do Município de início da prestação | Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior. | TMOVTRANSP.CODMUNICIPIOCOLETA |  |
| 28 | xMunIni | Nome do Município do início da prestação | Informar 'EXTERIOR' para operações com o exterior. | DVIEWMUNICIPIOS.NOMEMUNICIPIO |  |
| 29 | UFIni | UF do início da prestação | Informar 'EX' para operações com o exterior. | TMOVTRANSP.CODETDCOLETA |  |
| 30 | cMunFim | Código do Município de término da  prestação | Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior. | TMOVTRANSP.CODMUNICIPIOENTREGA |  |
| 31 | xMunFim | Nome do Município do término da  prestação | Informar 'EXTERIOR' para operações com o exterior. | DVIEWMUNICIPIOS.NOMEMUNICIPIO |  |
| 32 | UFFim | UF do término da prestação | Informar 'EX' para operações com o exterior. | TMOVTRANSP.CODETDENTREGA |  |
| 33 | infPercurso | Informações do Percurso do CTe Outros Serviços |  |  |  |
| 34 | UFPer | Sigla das Unidades da Federação do percurso do veículo. | Não é necessário repetir as UF de Início e Fim | TINFPERCURSO.CODETD |  |
| # | xx | Sequência XML |  |  |  |
| 36 | dhCont | Data e Hora da entrada em contingência | Informar a data e hora no formato AAAAMM- DDTHH:MM:SS |  |  |
| 37 | xJust | Justificativa da entrada em contingência |  |  |  |
| C. Dados Complementares do CT-e | | |  | | |
| 38 | compl | Dados complementares do CT-e para  fins operacionais ou comerciais |  |  |  |
| 39 | xCaracAd | Característica adicional do transporte | Texto livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc | Não obrigatório |  |
| 40 | xCaracSer | Característica adicional do serviço | Texto livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA; CONVENCIONAL; EMERGENCIAL; etc | Não obrigatório |  |
| 41 | xEmi | Funcionário emissor do CTe |  | Não obrigatório |  |
| 42 | xObs | Observações Gerais |  | TMOVHISTORICO.HISTORICOLONGO |  |
| 43 | ObsCont | Campo de uso livre do contribuinte | Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto |  |  |
| 44 | xCampo | Identificação do campo |  | Não obrigatório |  |
| 45 | xTexto | Conteúdo do campo |  | Não obrigatório |  |
| 46 | ObsFisco | Campo de uso livre do contribuinte | Informar o nome do campo no atributo xCampo e o conteúdo do campo no Xtexto |  |  |
| 47 | xCampo | Identificação do campo |  | Não obrigatório |  |
| 48 | xTexto | Conteúdo do campo |  | Não obrigatório |  |
| D. Identificação do Emitente | | |  |  |  |
| 49 | emit | Identificação do Emitente do CT-e OS |  |  |  |
| 50 | CNPJ | CNPJ do emitente | Informar os zeros não significativos. | GFILIAL.CGC |  |
| 51 | IE | Inscrição Estadual do Emitente |  | GFILIAL.INSCRICAOESTADUAL |  |
| 52 | IEST | Inscrição Estadual do Substituto Tributário |  | Não obrigatório |  |
| 53 | xNome | Razão social ou Nome do emitente |  | GFILIAL.NOME |  |
| 54 | xFant | Nome Fantasia |  | GFILIAL.NOMEFANTASIA |  |
| 55 | enderEmit | Endereço do emitente |  |  |  |
| 56 | xLgr | Logradouro |  | GFILIAL.RUA |  |
| 57 | nro | Número |  | GFILIAL.NUMERO |  |
| 58 | xCpl | Complemento |  | GFILIAL.COMPLEMENTO |  |
| 59 | xBairro | Bairro |  | GFILIAL.BAIRRO |  |
| 60 | cMun | Código do município (utilizar a tabela do  IBGE) |  | DVIEWMUNICIPIOS.CODIFICACAO (baseado no campo GFILIAL.CODMUNICIPIO) |  |
| 61 | xMun | Nome do Município |  | DVIEWMUNICIPIOS.NOMEMUNICIPIO (baseado no campo GFILIAL.CODMUNICIPIO) |  |
| 62 | CEP | CEP | Informar zeros não significativos | GFILIAL.CEP |  |
| 63 | UF | Sigla da UF |  | GFILIAL.ESTADO |  |
| 64 | fone | Telefone |  | GFILIAL.TELEFONE |  |
| 65 | CRT | Código do Regime Tributário | Informar: 1=Simples Nacional; 2=Simples Nacional, excesso sublimite de receita bruta; 3=Regime Normal; 4=Simples Nacional - Microempreendedor Individual – MEI. | DFILIAL.CLASSIFTRIBUTARIA                                 DFILIAL.OPTANTESIMPLES                            DFILIAL.SUBLIMITEEXCEDIDO | SE (DFILIAL.CLASSIFTRIBUTARIA == MEI)        CRT = 4;        SE ((DFILIAL.OPTANTESIMPLES) && (DFILIAL.SUBLIMITEEXCEDIDO))        CRT = 2;        SE (DFILIAL.OPTANTESIMPLES)         CRT = 1;        SENAO CRT = 3; |
| E - Informações do Tomador | | |  |  |  |
| 66 | toma | Informações do Tomador/Usuário do Serviço | Opcional para Excesso de Bagagem |  |  |
| 67 | CNPJ | CNPJ do Remetente | Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos. | FCFO.CGCCFO ou GFILIAL.CGC |  |
| 68 | CPF | CPF do Remetente | Informar os zeros não significativos | FCFO.CGCCFO ou GFILIAL.CGC |  |
| 69 | IE | Inscrição Estadual | Informar a IE do tomador ou ISENTO se tomador é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o tomador não seja contribuinte do ICMS não informar o conteúdo. | FCFO.INSCRESTADUAL ou GFILIAL.INSCRICAOESTADUAL |  |
| 70 | xNome | Razão Social ou Nome |  | FCFO.NOME ou GFILIAL.NOME |  |
| 71 | xFant | Nome Fantasia |  | FCFO.NOMEFANTASIA ou GFILIAL.NOMEFANTASIA |  |
| 72 | fone | Telefone |  | FCFO.TELEFONE ou GFILIAL..TELEFONE |  |
| 73 | enderToma | Dados do endereço |  |  |  |
| 74 | xLgr | Logradouro |  | FCFO.RUA ou GFILIAL.RUA |  |
| 75 | nro | Número |  | FCFO.NUMERO ou GFILIAL.NUMERO |  |
| 76 | xCpl | Complemento |  | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO |  |
| 77 | xBairro | Bairro |  | FCFO.BAIRRO ou GFILIAL.BAIRRO |  |
| 78 | cMun | Código do município (utilizar a tabela do  IBGE) | Informar 9999999 para operações com o exterior. | DVIEWMUNICIPIOS.CODIFICACAO (baseado no campo FCFO.CIDADEou GFILIAL.CODMUNICIPIO ) |  |
| 79 | xMun | Nome do Município | nformar EXTERIOR para operações com o exterior. | DVIEWMUNICIPIOS.NOMEMUNICIPIO (baseado no campo FCFO.CIDADEou GFILIAL.CODMUNICIPIO ) |  |
| 80 | CEP | CEP | Informar os zeros não significativos | FCFO.CEP ou GFILIAL.CEP |  |
| 81 | UF | Sigla da UF | Informar EX para operações com o exterior. | FCFO.CODETD ou GFILIAL.ESTADO |  |
| 82 | cPais | Código do país | Utilizar a tabela do BACEN | DPAIS.CODPAIS |  |
| 83 | xPais | Nome do país |  | GPAIS.DESCRICAO |  |
| 84 | email | Endereço de email |  | Não obrigatório |  |
| F - Valores da Prestação de Serviço | | |  | | |
| 85 | vPrest | Valores da Prestação de Serviço |  |  |  |
| 86 | vTPrest | Valor Total da Prestação do Serviço | 15 posições, sendo 13 inteiras e 2 casas decimais. Pode conter zeros quando o CTe for de complemento de ICMS | TMOV.VALORLIQUIDO |  |
| 87 | vRec | Valor a Receber | 15 posições, sendo 13 inteiras e 2 casas decimais. |  | Retorna o valor da fórmula contida no campo TTMV.CODFRMRATEIOLAN. Caso não exista nenhuma fórmula nesse campo,  TMOV.VALORLIQUIDO |
| 88 | Comp | Componentes do Valor da Prestação |  |  |  |
| 89 | xNome | Nome do componente | Exemplos: FRETE PESO, FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc |  |  |
| 90 | vComp | Valor do componente | 15 posições, sendo 13 inteiras e 2 casas decimais. | TMOV.VLRDESPACHO, TMOV.VLRSECCAT, TMOV.VLRPEDAGIO e TMOV.VLRFRETEOUTROS |  |
| G - Impostos | | |  | | |
| 91 | imp | Informações relativas aos Impostos |  |  |  |
| 92 | ICMS | Informações relativas ao ICMS |  |  |  |
| 93 | ICMS00 | Prestação sujeito à tributação normal do  ICMS |  |  |  |
| 94 | CST | Classificação Tributária do Serviço | 00 - Tributação normal ICMS | DNATUREZA.SITTRIBUTARIA | 00 -Valor fixo |
| 95 | vBC | Valor da BC do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.BASEDECALCULO |  |
| 96 | pICMS | Alíquota do ICMS | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.ALIQUOTA |  |
| 97 | vICMS | Valor do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.VALOR |  |
| 98 | ICMS20 | Prestação sujeito à tributação com redução de BC do ICMS |  |  |  |
| 99 | CST | Classificação Tributária do Serviço | 20 - Tributação com BC reduzida do ICMS | DNATUREZA.SITTRIBUTARIA | 20 - valor fixo |
| 100 | pRedBC | Percentual de redução da BC | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.FATORREDUCAO |  |
| 101 | vBC | Valor da BC do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.BASEDECALCULO |  |
| 102 | pICMS | Alíquota do ICMS | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.ALIQUOTA |  |
| 103 | vICMS | Valor do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.VALOR |  |
| 104 | ICMS45 | ICMS Isento, não Tributado ou diferido |  |  |  |
| 105 | CST | Classificação Tributária do Serviço | Preencher com: 40 - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido | DNATUREZA.SITTRIBUTARIA |  |
| 106 | ICMS90 | ICMS Outros |  |  |  |
| 107 | CST | Classificação Tributária do Serviço | 90 - ICMS outros | DNATUREZA.SITTRIBUTARIA | 90 - valor fixo |
| 108 | pRedBC | Percentual de redução da BC | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.FATORREDUCAO |  |
| 109 | vBC | Valor da BC do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.BASEDECALCULO |  |
| 110 | pICMS | Alíquota do ICMS | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.ALIQUOTA |  |
| 111 | vICMS | Valor do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.VALOR |  |
| 112 | vCred | Valor do Crédito outorgado/Presumido | 15 posições, sendo 13 inteiras e 2 casas decimais. |  |  |
| 113 | ICMSOutraUF | ICMS devido à UF de origem da prestação, quando diferente da UF do emitente | Será gerado somente quando o CST informado na regra de ICMS for igual 90 ou em branco |  | Se utiliza Crédito Outorgado (DFILIAL.UTILIZACREDITOOUTORGADO) então essa tag terá valor = TTRBMOV.VALOR \* (DFILIAL.PERCCREDITOOUTORGADO / 100). Se não, será igual a TTRBMOV.VALOR. |
| 114 | CST | Classificação Tributária do Serviço | 90 - ICMS Outra UF |  |  |
| 115 | pRedBCOutraUF | Percentual de redução da BC | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.FATORREDUCAO |  |
| 116 | vBCOutraUF | Valor da BC do ICMS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.BASEDECALCULO |  |
| 117 | pICMSOutraUF | Alíquota do ICMS | 5 posições, sendo 3 inteiras e 2 casas decimais. | TTRBMOV.ALIQUOTA |  |
| 118 | vICMSOutraUF | Valor do ICMS devido outra UF | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.VALOR |  |
| 119 | ICMSSN | Simples Nacional |  |  |  |
| 120 | CST | Classificação Tributária do Serviço | 90 - ICMS Simples Nacional |  |  |
| 121 | indSN | Indica se o contribuinte é Simples  Nacional 1=Sim |  | DFILIAL.OPTANTESIMPLES |  |
| 122 | vTotTrib | Valor Total dos Tributos | 15 posições, sendo 13 inteiras e 2 casas decimais. | A soma de todos os TITMMOVFISCAL.VLRTOTTRIB do Movimento |  |
| 123 | infAdFisco | Informações adicionais de interesse do Fisco | Norma referenciada, informações complementares etc. | Não obrigatório |  |
| 124 | ICMSUFFim | Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual | Grupo a ser informado nas prestações interestaduais para consumidor final, não contribuinte do ICMS |  |  |
| 125 | vBCUFFim | Valor da BC do ICMS na UF de término da prestação do serviço de transporte | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.BASEDECALCULO |  |
| 126 | pFCPUFFim | Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de término da prestação do serviço de transporte | 5 posições, sendo 3 inteiras e 2 casas decimais. Alíquota adotada nas operações internas na UF do destinatário | DREGRAICMS.PERICMSFCP |  |
| 127 | pICMSUFFim | Alíquota interna da UF de término da prestação do serviço de transporte | 5 posições, sendo 3 inteiras e 2 casas decimais. Alíquota adotada nas operações internas na UF do destinatário | DREGRAICMS.ALIQSUBST |  |
| 128 | pICMSInter | Alíquota interestadual das UF envolvidas | 5 posições, sendo 3 inteiras e 2 casas decimais. Alíquota interestadual das UF envolvidas | DREGRAICMS.ALIQICMS |  |
| 129 | vFCPUFFim | Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de término da prestação | 15 posições, sendo 13 inteiras e 2 casas decimais. | vBCUFFim \* pFCPUFFim % |  |
| 130 | vICMSUFFim | Valor do ICMS de partilha para a UF de término da prestação do serviço de transporte | 15 posições, sendo 13 inteiras e 2 casas decimais. | Se DREGRAICMS.PERICMSESTDESTINO> 0   ( (vBCUFFim \* pICMSUFFim %) - (vBCUFFim \* pICMSInter %)) \* PERICMSESTDESTINO % |  |
| 131 | vICMSUFIni | Valor do ICMS de partilha para a UF de início da prestação do serviço de transporte | 15 posições, sendo 13 inteiras e 2 casas decimais. | SE vICMSUFFim > 0   ( (vBCUFFim \* pICMSUFFim %) - (vBCUFFim \* pICMSInter %)) - vICMSUFFim |  |
| 132 | infTribFed | Informações dos tributos federais | Grupo a ser informado nas prestações interestaduais para consumidor final, não contribuinte do ICMS |  |  |
| 133 | vPIS | Valor do PIS | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 134 | vCOFINS | Valor COFINS | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 135 | vIR | Valor de Imposto de Renda | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 136 | vINSS | Valor do INSS | 15 posições, sendo 13 inteiras e 2 casas decimais. | TTRBMOV.VALOR |  |
| 137 | vCSLL | Valor do CSLL | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| K - Grupo de informações do CT-e Normal | | |  | | |
| 138 | infCTeNorm | Grupo de informações do CTe OS Normal |  |  |  |
| 139 | infServico | Informações da Prestação do Serviço |  |  |  |
| 140 | xDescServ | Descrição do Serviço prestado |  |  |  |
| 141 | infQ | Informações de quantidades da Carga do Cte | Para Transporte de Pessoas indicar número de passageiros, para excesso de bagagem e transporte de valores indicar número de Volumes/Malotes |  |  |
| 142 | qCarga | Quantidade | 15 posições, sendo 11 inteiras e 4 casas decimais. | TMOV.QUANTIDADE |  |
| 143 | infDocRef | Informações dos documentos referenciados |  |  |  |
| 144 | nDoc | Número |  | TCTRC.NUMERODOC, |  |
| 145 | serie | Série |  | TCTRC.SERIEDOC |  |
| 146 | subserie | Subsérie |  | Não obrigatório |  |
| 147 | dEmi | Data de Emissão | Formato AAAA-MM-DD | TCTRC.DATAEMISSAO |  |
| 148 | vDoc | Valor Transportado | 15 posições, sendo 13 inteiras e 2 casas decimais. | TCTRC.VALORTOTAL |  |
| 149 | chBPe | Chave de acesso do BP-e que possui eventos excesso de bagagem |  | TCTRC.CHAVEACESSONFE |  |
| 150 | seg | Informações de Seguro da Carga |  |  |  |
| 151 | respSeg | Responsável pelo seguro | Preencher com: 4 - Emitente do CTe; 5 - Tomador de Serviço. | TCTESEGURO.RESPONSAVEL |  |
| 152 | xSeg | Nome da Seguradora |  | TCTESEGURO.SEGURADORA |  |
| 153 | nApol | Número da Apólice | Obrigatório pela lei 11.442/07 (RCTRC) | TCTESEGURO.APOLICE |  |
| KE - Informações do modal | | |  |  |  |
| 154 | infModal | Informações do modal Obrigatório para Pessoas e Bagagem |  |  |  |
| 155 | versaoModal | Versão do leiaute específico para o  Modal |  | TPARFILIAL.VERSAOCTE |  |
| 156 | xs:any | XML do modal Insira neste local o XML específico do modal | O elemento do tipo -any- permite estender o documento XML com elementos não especificados pelo schema. Insira neste local - any- o XML específico do modal (rodoviário). A especificação do schema XML para cada modal pode ser encontrada nos arquivos que acompanham este pacote de liberação: Rodoviário - ver arquivo CTeModalRodoviarioOS\_v9.99 Onde v9.99 é a a designação genérica para a versão do arquivo. Por exemplo, o arquivo para o schema do modal Rodoviário na versão 4.00 será denominado "CTeModalRodoviarioOS\_v4.00". |  |  |
| KG - CT-e Substituto | | |  |  |  |
| 157 | infCteSub | Informações do CT-e de substituição |  |  |  |
| 158 | chCte | Chave de acesso do CT-e a ser substituído (original) |  | TCTEOS.CHAVEACESSO | Busca-se a chave de acersso do CT-e OS original através da TMOVRELAC |
| 159 | refCTeCanc | Chave de acesso do CTe Cancelado Somente para Transporte de Valores |  | Não obrigatório |  |
| L - Dados de Cobrança do Cte | | |  |  |  |
| 160 | cobr | Dados da cobrança do Cte |  |  |  |
| 161 | fat | Dados da fatura |  |  |  |
| 162 | nFat | Número da fatura |  | Não obrigatório |  |
| 163 | vOrig | Valor original da fatura | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 164 | vDesc | Valor do desconto da fatura | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 165 | vLiq | Valor líquido da fatura | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 166 | dup | Dados das duplicatas |  |  |  |
| 167 | nDup | Número da duplicata |  | Não obrigatório |  |
| 168 | dVenc | Data de vencimento da duplicata (AAAAMM- DD) |  | Não obrigatório |  |
| 169 | vDup | Valor da duplicata | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 170 | infGTVe | Informações das GTVe relacionadas ao CTe OS |  | Não obrigatório |  |
| 171 | chCTe | Chave de acesso da GTVe |  | Não obrigatório |  |
| 172 | Comp | Componentes do Valor da GTVe |  | Não obrigatório |  |
| 173 | tpComp | Tipo do Componente | 1-Custodia 2-Embarque 3-Tempo de espera 4-Malote 5-Ad Valorem 6-Outros | Não obrigatório |  |
| 174 | vComp | Valor do componente | 15 posições, sendo 13 inteiras e 2 casas decimais. | Não obrigatório |  |
| 175 | xComp | Nome do componente (informar apenas para outros) | Exemplos: FRETE PESO, FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc | Não obrigatório |  |
| LA - Detalhamento do Cte Complementado | | |  |  |  |
| 176 | infCteComp | Detalhamento do CTe complementado |  |  |  |
| 177 | chCTe | Chave do CTe complementado |  | TCTEOS.CHAVEACESSO | Busca-se a chave de acersso do CT-e OS original através da TMOVRELAC |
| LB - Autorizados para download do XML | | |  |  |  |
| 178 | autXML |  |  |  |  |
| 179 | CNPJ | CNPJ do autorizado | Informar zeros não significativos |  |  |
| 180 | CPF | CPF do autorizado | Informar zeros não significativos |  |  |
| LC - Informações do Responsável Técnico | | |  |  |  |
| 181 | infRespTec | Informações do Responsável Técnico pela emissão do DF-e |  |  |  |
| 182 | CNPJ | CNPJ da pessoa jurídica responsável técnica pelo sistema utilizado na emissão do documento fiscal eletrônico | Informar o CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico. | DRESPONSAVELTECNICONFE.CNPJ |  |
| 183 | xContato | Nome da pessoa a ser contatada | Informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico. No caso de pessoa física, informar o respectivo nome. | DRESPONSAVELTECNICONFE.NOME |  |
| 184 | email | Email da pessoa jurídica a ser contatada |  | DRESPONSAVELTECNICONFE.EMAIL |  |
| 185 | fone | Telefone da pessoa jurídica a ser contatada | Preencher com o Código DDD + número do telefone. | DRESPONSAVELTECNICONFE.TELEFONE |  |
| 186 | xx | Sequência XML |  |  |  |
| 187 | idCSRT | Identificador do código de segurança do responsável técnico | Identificador do CSRT utilizado para geração do hash |  |  |
| 188 | hashCSRT | Hash do token do código de segurança do responsável técnico | O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT) Observação: 28 caracteres são representados no schema como 20 bytes do tipo base64Binary |  |  |
| 189 | infCTeSupl | Informações suplementares do Cte |  |  |  |
| 190 | qrCodCTe | Texto com o QR-Code impresso no DACTE |  | TPARFILIAL.URLSEFAZCTEOS |  |
| 191 |  | ds:Signature |  |  |  |
| **M - Modal Rodoviário OS** | | |  | | |
| 1 | rodoOS | Informações do modal Rodoviário |  |  |  |
| 2 | TAF | Termo de Autorização de Fretamento - TAF | Registro obrigatório do emitente do CTe OS junto à ANTT, de acordo com a Resolução ANTT nº 4.777/2015 | TVEICULOS.TERMOAUTFRETAMENTO |  |
| 3 | NroRegEstadual | Número do Registro Estadual | Registro obrigatório do emitente do CTe OS junto à Agência Reguladora Estadual. | TVEICULOS.NUMEROREGISTROESTADUAL |  |
| 4 | veic | Dados dos Veículos |  |  |  |
| 5 | placa | Placa do veículo |  | TVEICULOS.PLACA |  |
| 6 | RENAVAM | RENAVAM do veículo |  | TVEICULOS.RENAVAM |  |
| 7 | prop | Proprietário ou possuidor do Veículo. Só preenchido quando o veículo não pertencer à empresa emitente do CTe OS |  |  |  |
| 8 | CPF | Número do CPF |  | FCFO.CGCCFO |  |
| 9 | CNPJ | Número do CNPJ | Informar os zeros não significativos. | FCFO.CGCCFO |  |
| 10 | TAF | Termo de Autorização de Fretamento – TAF | De acordo com a Resolução ANTT nº 4.777/2015 | TVEICULOS.TERMOAUTFRETAMENTO |  |
| 11 | NroRegEstadual | Número do Registro Estadual | Registro obrigatório do emitente do CTe OS junto à Agência Reguladora Estadual | TVEICULOS.NUMEROREGISTROESTADUAL |  |
| 12 | xNome | Razão Social ou Nome do proprietário |  | FCFO.NOME |  |
| 13 | xx | Sequência XML |  |  |  |
| 14 | IE | Inscrição Estadual |  | FCFO.INSCRESTADUAL |  |
| 15 | UF | UF |  | FCFO.CODETD |  |
| 16 | tpProp | Tipo Proprietário ou possuidor | Preencher com: 0-TAC – Agregado; 1-TAC Independente; ou 2 – Outros. | TVEICULOS.TIPOPROPTERCEIROS |  |
| 17 | UF | UF em que veículo está licenciado | Sigla da UF de licenciamento do veículo. | FCFO.CODETD |  |
| 18 | infFretamento | Dados do fretamento (apenas para Transporte de Pessoas) |  |  |  |
| 19 | tpFretamento | Tipo Fretamento | Preencher com: 1 - Eventual 2 - Continuo | TMOVTRANSP.TIPOFRETAMENTOPESSOAS |  |
| 20 | dhViagem | Data e hora da viagem (Apenas para fretamento eventual) | Formato AAAA-MM-DDTHH:MM:DD TZD | TMOVTRANSP.DATAHORAVIAGEM |  |

---
