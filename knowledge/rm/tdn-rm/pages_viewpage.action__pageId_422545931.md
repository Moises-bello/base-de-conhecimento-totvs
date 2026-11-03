---
content_hash: 40c0d276d96fea787c25578a38ddd258ec8a92cef7a322d816ec80aeb3d4dd03
fetched_at: '2026-06-29T00:09:21.954196+00:00'
page_id: '422545931'
product: rm
source: tdn-rm
title: Bloco D (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545931
version: 30
---

## Documentos Fiscais — II — Serviços (ICMS)

1leftd001Registro D001**Registro D001 — Abertura do Bloco D**  
Este registro informa se houve movimentação no bloco D.d100Registro D010**Registro D010 — Identificação do Estabelecimento**  
Gerado para cada filial que possui movimentação no período da escrituração.d100Registro D100

**Registro D100 — Aquisição de Serviço de Transporte**

Para a geração deste registro serão selecionados os lançamentos de entrada que estejam associados a CFOP do tipo fiscal e aos Código Modelo de Documento:

* Nota Fiscal de Transporte (Código 07);
* Conhecimentos de Transporte Rodoviário de carga (Código 08);
* Conhecimento de Transporte de Cagas Avulso (Código 88);
* Aquaviário de cargas (código 09);
* Aéreo (Código 10);
* Ferroviário de cargas (Código 11);
* Multimodal de cargas (Código 26);
* Nota Fiscal de Transporte Ferroviário de carga (Código 27);
* Nota Fiscal de Transporte Eletrônico — CT-e (Código 57);
* Bilhete de Passagem Eletrônico BP-e (Código 63);
* Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (Código 67).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nº | Campo | Descrição | Campo da Base | Observações |
| 01 | REG | Texto fixo contendo "D100" |  | Gerado pela rotina |
| 02 | IND\_OPER | Indicador do tipo de operação: 0 - Aquisição; 1 - Prestação | Valor fixo "0 - Aquisição" | Gerado pela rotina |
| 03 | IND\_EMIT | Indicador do emitente do documento fiscal: 0 - Emissão própria; 1 - Terceiros |  | SE Lancamento de Entrada onde Emitente é origem destino = Filial => Emissão Própria  SE  Lancamento de Entrada onde Emitente = Filial e é Regime Especial => Emissão Terceiros  SE Lancamento de Entrada onde Emitente = Filial => Emissão Própria  SE Lancamento de Entrada onde Emitente <> Filial => Emissão Terceiros |
| 04 | COD\_PART | Código do participante (campo 02 do Registro 0150): - do prestador de serviço, no caso de aquisição de serviço; - do tomador do serviço, no caso de prestação de serviços |  |  |
| 05 | COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1 | FTDO.CODMODDOC |  |
| 06 | COD\_SIT | Código da situação do documento fiscal, conforme a Tabela 4.1.2 | DLAF.STATUSLF |  |
| 07 | SER | Série do documento fiscal | DLAF.SERIEDOC |  |
| 08 | SUB | Subsérie do documento fiscal | DLAF.SUBSERIE |  |
| 09 | NUM\_DOC | Número do documento fiscal | DLAF.DOCINI |  |
| 10 | CHV\_CTE | Chave do Conhecimento de Transporte Eletrônico ou do Bilhete de Passagem Eletrônico | DLAF.CHAVEACESSONFE |  |
| 11 | DT\_DOC | Data da emissão do documento fiscal | DLAF.DATAEMISSAO |  |
| 12 | DT\_A\_P | Data da aquisição ou da prestação do serviço | DLAF.DATAES |  |
| 13 | TP\_CT-e | Tipo de Conhecimento de Transporte Eletrônico conforme definido no Manual de Integração do CT-e ou do Bilhete de Passagem Eletrônico conforme definido no Manual de Integração do BP-e | DLAFAGRUP.TIPOCTE |  |
| 14 | CHV\_CTE\_REF | Chave do Documento Eletrônico Substituído |  | *Não será gerado* |
| 15 | VL\_DOC | Valor total do documento fiscal | DLAFAGRUP.VALORCONT |  |
| 16 | VL\_DESC | Valor total do desconto | DLAF.DESCONTOS + DLAF.OUTROSDESC |  |
| 17 | IND\_FRT | Indicador do tipo do frete: 0 - Por conta do emitente; 1 - Por conta do destinatário/remetente; 2 - Por conta de terceiros; 9 - Sem cobrança de frete | DLAF.TIPOFRETE |  |
| 18 | VL\_SERV | Valor total da prestação de serviço |  |  |
| 19 | VL\_BC\_ICMS | Valor da base de cálculo do ICMS |  |  |
| 20 | VL\_ICMS | Valor do ICMS |  |  |
| 21 | VL\_NT | Valor não-tributado |  |  |
| 22 | COD\_INF | Código da informação complementar do documento fiscal (campo 02 do Registro 0450) |  |  |
| 23 | COD\_CTA | Código da conta analítica contábil debitada/creditada |  |  |

d101Registro D101**Registro D101 — Complemento do Documento de Transporte — PIS/PASEP**d105Registro D105**Registro D105 — Complemento do Documento de Transporte — COFINS**  
Para cada documento declarado no registro D100 serão geradas uma ou mais linhas com base nos itens do Lançamento Fiscal agrupado por CST e Natureza da Base do Cálculo do crédito para os tributos incidentes.d111Registro D111**Registro D111 — Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro D100 possuir processo judicial associado.d200Registro D200

**Registro D200 — Resumo da Escrituração Diária**

Na geração deste registro serão selecionados Lançamentos Fiscais de Saída que estejam associados a CFOP do tipo fiscal e com os códigos modelo de documento:

* Nota Fiscal de Serviço de Transporte (Código 07);
* Conhecimentos de Transporte Rodoviário de carga (Código 08);
* Conhecimento de Transporte de Cagas Avulso (Código 88);
* Aquaviário de cargas (código 09);
* Aéreo (Código 10);
* Ferroviário de cargas (Código 11);
* Multimodal de cargas (Código 26);
* Nota Fiscal de Transporte Ferroviário de carga (Código 27);
* Nota Fiscal de Transporte Eletrônico — CT-e (Código 57);
* Bilhete de Passagem Eletrônico BP-e (Código 63);
* Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (Código 67).

Este registro é totalizado por Código Modelo de Documento, CFOP e data do resumo.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nº | Campo | Descrição | Campo da Base | Observações |
| 01 | REG | Texto fixo contendo "D200" |  | Gerado pela rotina |
| 02 | COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1 | FTDO.CODMODDOC |  |
| 03 | COD\_SIT | Código da situação do documento fiscal, conforme a Tabela 4.1.2 | DLAF.STATUSLF |  |
| 04 | SER | Série do documento fiscal | DLAF.SERIEDOC |  |
| 05 | SUB | Subsérie do documento fiscal | DLAF.SUBSERIE |  |
| 06 | NUM\_DOC\_INI | Número do documento fiscal inicial (mesmo modelo, série e subsérie). | DLAF.DOCINI |  |
| 07 | NUM\_DOC\_FIN | Número do documento fiscal final (mesmo modelo, série e subsérie). | DLAF.DOCFIM |  |
| 08 | CFOP | Código Fiscal de Operação e Prestação conforme tabela indicada no item 4.2.2 | DNATUREZA.CODNAT |  |
| 09 | DT\_REF | Data do dia de referência do resumo diário | DLAF.DATAEMISSAO |  |
| 10 | VL\_DOC | Valor total dos documentos fiscais |  | Calculado de acordo com os itens, se houverem.  SE a Natureza for tributada pelo ICMS, ENTÃO:                 Base de ICMS + Isentos + Outros + Despesa Condicional + ST SENAO:                 Valor de Mercadorias – Despesas + Descontos |
| 11 | VL\_DESC | Valor total dos descontos | DLAF.DESCONTOS + DLAF.OUTROSDESC |  |

**Observação:**

No caso específico da prestação de serviços de transporte, os documentos emitidos por meio do CT-e (modelo 57) devem ser informados na EFD Contribuições mesmo quando não houver incidência de PIS e Cofins, conforme orienta o Guia Prático da EFD Contribuições (versão 1.35).

Os CT-es sem destaque de PIS e Cofins são gerados na EFD Contribuições de forma automática com o CST 08 – Operação sem Incidência da Contribuição, nos seguintes registros:

D200 – Cabeçalho do CT-e

D201 – Itens do serviço de transporte

D205 – Complemento por UF da prestação

d201Registro D201

**Registro D201 — Totalização do Resumo Diário — PIS/PASEP**

Registro gerado com a totalização dos lançamentos selecionados no Registro D200, agrupando por CST do PIS/PASEP. (TIPOTRIBFISC = ‘10’)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nº | Campo | Descrição | Campo da Base | Observações |
| 01 | REG | Texto fixo contendo "D201" |  | Gerado pela rotina |
| 02 | CST\_PIS | Código da Situação Tributária referente ao PIS/PASEP | DTRBITEM.SITTRIBUTARIA |  |
| 03 | VL\_ITEM | Valor total dos itens | (DITEM.VALORMERC) - DITEM.DESCONTOITEM +  DITEM.VALORDESPESA | DITEM.VALORMERC =  Se DITEM.VALORMERC > 0  então    DITEM.VALORMERC  senão   DITEM.PRECOPRD \* DITEM.QTDEPRD |
| 04 | VL\_BC\_PIS | Valor da base de cálculo do PIS/PASEP | DTRBITEM.BASETRB |  |
| 05 | ALIQ\_PIS | Alíquota do PIS/PASEP (em percentual) | DTRBITEM.ALIQTRB |  |
| 06 | VL\_PIS | Valor do PIS/PASEP | DTRBITEM.VALORTRB |  |
| 07 | COD\_CTA | Código da conta analítica contábil debitada/creditada |  |  |

Observações: Caso a pessoa jurídica aproprie o valor da contribuição social em mais de uma conta analítica, em função da natureza da operação geradora da contribuição social, deverão ser informados vários registros D201, um para cada conta.

d205Registro D205**Registro D205 — Totalização do Resumo Diário — COFINS**  
Para cada linha gerada no registro D200 será gerada uma ou mais linhas totalizando os tributos PIS e COFINS com base nos itens dos lançamentos. Estes registros serão totalizados por CST.d209Registro D209**Registro D209 — Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro D200 possuir um processo judicial associado.d300Registro D300**Registro D300 — Resumo da Escrituração Diária — Bilhetes Consolidados de Passagem Rodoviário (Código 13), de Passagem Aquaviário (Código 14), de Passagem e Nota de Bagagem (Código 15) e de Passagem Ferroviário (Código 16), Resumo de Movimento Diário (Código 18).**  
Para a geração deste registro serão selecionados Lançamentos Fiscais de Saída que estejam associados as CFOP do tipo fiscal e que possuam os códigos modelo de documento 2E, 13, 14, 15 e 16. Este registro é totalizado por Código Modelo de Documento, CFOP, Data de emissão CST do PIS, Alíquota do PIS, CST da COFINS, Alíquota da COFINS. A tributação do PIS e da COFINS deverá estar nos itens do Lançamento Fiscal.d309Registro D309**Registro D309 — Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro D300 possuir um processo judicial associado.d350Registro D350**Registro D350 — Resumo diário de Cupom Fiscal emitido por ECF**  
Para a correta geração deste registro devem ser observadas as regras para parametrização de  Tipos de Documento emitidos por ECF.d390Registro D390**Registro D390 —  Processo Referenciado**  
Para que este registro seja gerado é necessário que existam Processos Judiciais associados aos Lançamentos de Cupom Fiscal.d500Registro D500

**Registro D500: Nota Fiscal de Serviço de Comunicação (Código 21), Nota Fiscal de Serviço de Telecomunicação (Código 22), Nota Fiscal Fatura de Serviços de Comunicação Eletrônica (Código 62)**

Para a geração deste registro serão selecionados os Lançamentos Fiscais de Entrada que estejam associados a CFOP do tipo fiscal, com os códigos modelo de documento 21, 22 ou 62 e os seguintes CSTs para o PIS e COFINS (50","51","52","53","54","55","56").

Neste registro deverá a pessoa jurídica informar as operações referentes à contratação de serviços de comunicação ou de telecomunicação que, em função da natureza do serviço e da atividade econômica desenvolvida pela pessoa jurídica, permita a apuração de créditos de PIS/Pasep e de Cofins, na forma da legislação tributária.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | Tipo | Tam | Dec | Obrig | **Observações** |
| 01 | REG | Texto fixo contendo "D500" | C | 004\* | - | S |  |
| 02 | IND\_OPER | Indicador do tipo de operação:  0- Aquisição | C | 001\* | - | S |  |
| 03 | IND\_EMIT | Indicador do emitente do documento fiscal:  0- Emissão própria;  1- Terceiros | C | 001\* | - | S |  |
| 04 | COD\_PART | Código do participante prestador do serviço (campo 02 do Registro 0150). | C | 060 | - | S | O valor informado deve existir no campo COD\_PART do registro 0150. |
| 05 | COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1. | C | 002\* | - | S | Valores válidos: [21, 22, 62] |
| 06 | COD\_SIT | Çódigo da situação do documento fiscal, conforme a Tabela 4.1.2. | N | 002\* | - | S | Valores válidos: [00, 01, 02, 03, 06, 07, 08] |
| 07 | SER | Série do documento fiscal | C | 004 | - | N | Informar neste campo a série do documento fiscal, se existir. |
| 08 | SUB | Subsérie do documento fiscal | N | 003 | - | N | Informar neste campo a subsérie do documento fiscal, se existir. |
| 09 | NUM\_DOC | Número do documento fiscal | N | 009 | - | S | Informar neste campo o número do documento fiscal de aquisição de serviço de comunicação ou de telecomunicação com direito a crédito. O valor informado no campo deve ser maior que “0” (zero). |
| 10 | DT\_DOC | Data da emissão do documento fiscal | N | 008\* | - | S | Informar a data de emissão do documento, no formato “ddmmaaaa”; excluindo-se quaisquer caracteres de separação, tais como: “.”, “/”, “-”. A data informada neste campo ou a data da aquisição do serviço (campo 11) deve estar compreendida no período da escrituração (campos 06 e 07 do registro 0000). Regra aplicável na validação/edição de registros da escrituração, a ser gerada com a versão 1.0.2 do Programa Validador e Assinador da EFD-Contribuições. |
| 11 | DT\_A\_P | Data da entrada (aquisição) | N | 008\* | - | S | Informar a data de aquisição do serviço no formato “ddmmaaaa”, excluindo-se quaisquer caracteres de separação, tais como: “.”, “/”, “-”. a data informada neste campo ou a data de emissão do documento fiscal (campo 10) deve estar compreendida no período da escrituração (campos 06 e 07 do registro 0000). Regra aplicável na validação/edição de registros da escrituração, a ser gerada com a versão 1.0.2 do Programa Validador e Assinador da EFD-Contribuições. |
| 12 | VL\_DOC | Valor total do documento fiscal | N | - | 02 | S | Informar neste campo o valor do documento fiscal com direito à apuração de crédito. O valor informado no campo deve ser maior que “0” (zero). |
| 13 | VL\_DESC | Valor total do desconto | N | - | 02 | N |  |
| 14 | VL\_SERV | Valor da prestação de serviços | N | - | 02 | S | Informar neste campo o valor da prestação de serviço constante no documento fiscal. |
| 15 | VL\_SERV\_NT | Valor total dos serviços não-tributados pelo ICMS | N | - | 02 | N |  |
| 16 | VL\_TERC | Valores cobrados em nome de terceiros | N | - | 02 | N |  |
| 17 | VL\_DA | Valor de outras despesas indicadas no documento fiscal | N | - | 02 | N | Informar neste campo o valor de outras despesas/valores constantes no documento fiscal, que não sejam as informadas no campo 14. |
| 18 | VL\_BC\_ICMS | Valor da base de cálculo do ICMS | N | - | 02 | N |  |
| 19 | VL\_ICMS | Valor do ICMS | N | - | 02 | N | Informar neste campo o valor do total do ICMS. |
| 20 | COD\_INF | Código da informação complementar (campo 02 do Registro 0450) | C | 006 | - | N |  |
| 21 | VL\_PIS | Valor do PIS/PASEP | N | - | 02 | N | Informar neste campo o valor do total do PIS/Pasep. |
| 22 | VL\_COFINS | Valor da COFINS | N | - | 02 | N | Informar neste campo o valor da Cofins. |
| **23** | **CHV\_DOC\_E** | **Chave do Documento Fiscal Eletrônico** | **N** | **044\*** | **-** | **N** | **Informar a chave do documento eletrônico. Campo existente apenas a partir do período de apuração 01/04/2025, sendo obrigatório quando COD\_MOD for igual a “62” ou “55”. Será conferido o dígito verificador (DV) da chave do documento eletrônico. Será verificada consistência da raiz de CNPJ e UF do participante com a raiz de CNPJ e UF contida na chave do documento eletrônico.  Será verificada a consistência da informação dos campos COD\_MOD, NUM\_DOC e SER com o número do documento e série contidos na chave do documento eletrônico** |

d501Registro D501

**Registro D501 — Complemento da Operação — PIS/PASEP**

Registro Fillho do D500 - Verifique a regra de geração do Registro D500 para geração deste registro.  
Para cada documento declarado no registro D500 serão geradas uma ou mais linhas com base nos itens dos lançamentos com as informações dos tributos PIS e COFINS incidentes. Estes registros são totalizados por CST do Tributo e Natureza da Base de Cálculo do Crédito. Para a correta geração destes registros os tributos deverão estar gravados nos itens do Lançamento Fiscal.

Gerado para os seguintes CSTs de PIS e COFINS (50","51","52","53","54","55","56").

**Registro D501 —   Complemento da Operação — PIS/PASEP - NFCOM (Código 62)**  
Registro Fillho do D500 - Verifique a regra de geração do Registro D500 para geração deste registro.  
Para cada documento declarado no registro D500 serão geradas uma ou mais linhas com base nos itens dos lançamentos com as informações dos tributos PIS e COFINS incidentes. Estes registros são totalizados por CST do Tributo e Natureza da Base de Cálculo do Crédito. Para a correta geração destes registros os tributos deverão estar gravados nos itens do Lançamento Fiscal.

Gerado para os seguintes CSTs de PIS e COFINS (50","51","52","53","54","55","56").

d505Registro D505

**Registro D505 — Complemento da Operação — COFINS**

Registro Fillho do D500 - Verifique a regra de geração do Registro D500 para geração deste registro.  
Para cada documento declarado no registro D500 serão geradas uma ou mais linhas com base nos itens dos lançamentos com as informações dos tributos PIS e COFINS incidentes. Estes registros são totalizados por CST do Tributo e Natureza da Base de Cálculo do Crédito. Para a correta geração destes registros os tributos deverão estar gravados nos itens do Lançamento Fiscal.

Gerado para os seguintes CSTs de PIS e COFINS (50","51","52","53","54","55","56").

**Registro D505 —   Complemento da Operação — COFINS - NFCOM (Código 62)**  

Registro Fillho do D500 - Verifique a regra de geração do Registro D500 para geração deste registro.  
Para cada documento declarado no registro D500 serão geradas uma ou mais linhas com base nos itens dos lançamentos com as informações dos tributos PIS e COFINS incidentes. Estes registros são totalizados por CST do Tributo e Natureza da Base de Cálculo do Crédito. Para a correta geração destes registros os tributos deverão estar gravados nos itens do Lançamento Fiscal.

Gerado para os seguintes CSTs de PIS e COFINS (50","51","52","53","54","55","56").

d509Registro D509

**Registro D509 — Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro D500 possuir um processo judicial associado.

**Registro D509 —  Processo Referenciado - NFCOM (Código 62)**  
Este registro só será gerado se o documento declarado no registro D500 possuir um processo judicial associado.d600Registro D600

**Registro D600 — Consolidação da Prestação de Serviços — Notas de Serviço de Comunicação (código 21) e de Serviço De Telecomunicação (Código 22)**  
Para a geração destes registros serão selecionados Lançamentos Fiscais de saída que estejam associados a CFOP do tipo fiscal e com os códigos modelo de documento 21 ou 22. Este registro é totalizado por Código Modelo de Documento , Código de município onde o serviço de comunicação foi prestado, Série e Sub-Série.

**Registro D600 —  NFCOM (Código 62)**  
Para a geração destes registros serão selecionados Lançamentos Fiscais de saída que estejam associados a CFOP do tipo fiscal e com os códigos modelo de documento 21 ou 22. Este registro é totalizado por Código Modelo de Documento , Código de município onde o serviço de comunicação foi prestado, Série e Subsérie.d601Registro D601

**Registro D601 — Complemento da Consolidação da Prestação de Serviços — PIS/PASEP**Estes registros são gerados com base nas informações do PIS e da COFINS dos itens dos documentos declarados no registro D600. Estes registros são totalizados pelo Código da Classe de Consumo.

**Registro D601 —  Complemento da Consolidação da Prestação de Serviços — PIS/PASEP — NFCOM (Código 62)**  
Estes registros são gerados com base nas informações do PIS e da COFINS dos itens dos documentos declarados no registro D600. Estes registros são totalizados pelo Código da Classe de Consumo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem dos Dados** |
| 01 | REG | Texto fixo contendo "D601” |  |
| 02 | COD\_CLASS | Código de classificação do item do serviço de comunicação ou de telecomunicação, conforme a Tabela 4.4.1 | DVALORCAMPOS.CODIGO |
| 03 | VL\_ITEM | Valor acumulado do item |  |
| 04 | VL\_DESC | Valor acumulado dos descontos/exclusões da base de cálculo |  |
| 05 | CST\_PIS | Código da Situação Tributária referente ao PIS/PASEP |  |
| 06 | VL\_BC\_PIS | Valor da base de cálculo do PIS/PASEP |  |
| 07 | ALIQ\_PIS | Alíquota do PIS/PASEP (em percentual) |  |
| 08 | VL\_PIS | Valor do PIS/PASEP |  |
| 09 | COD\_CTA | Código da conta contábil debitada/creditada |  |

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem dos Dados** |
| 01 | REG | Texto fixo contendo "D601” |  |
| 02 | COD\_CLASS | Código de classificação do item do serviço de comunicação ou de telecomunicação, conforme a Tabela 4.4.1 | DVALORCAMPOS.CODIGO |
| 03 | VL\_ITEM | Valor acumulado do item |  |
| 04 | VL\_DESC | Valor acumulado dos descontos/exclusões da base de cálculo |  |
| 05 | CST\_PIS | Código da Situação Tributária referente ao PIS/PASEP |  |
| 06 | VL\_BC\_PIS | Valor da base de cálculo do PIS/PASEP |  |
| 07 | ALIQ\_PIS | Alíquota do PIS/PASEP (em percentual) |  |
| 08 | VL\_PIS | Valor do PIS/PASEP |  |
| 09 | COD\_CTA | Código da conta contábil debitada/creditada |  |

d605Registro D605

**Registro D605 — Complemento da Consolidação da Prestação de Serviços — COFINS**  
Estes registros são gerados com base nas informações do PIS e da COFINS dos itens dos documentos declarados no registro D600. Estes registros são totalizados pelo Código da Classe de Consumo.

**Registro D605 —  Complemento da Consolidação da Prestação de Serviços — COFINS — NFCOM (Código 62)**  
Estes registros são gerados com base nas informações do PIS e da COFINS dos itens dos documentos declarados no registro D600. Estes registros são totalizados pelo Código da Classe de Consumo.d609Registro D609

**Registro D609 — Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro D600 possuir  um processo judicial associado.

**Registro D609 —  Processo Referenciado — NFCOM (Código 62)**  
Este registro só será gerado se o documento declarado no registro D600 possuir  um processo judicial associado.d990Registro D990**Registro D990 — Encerramento do Bloco D**  
Este registro é gerado automaticamente com a quantidade de linhas existentes no Bloco D.
