---
content_hash: c5cc487626f9a3378c215c55ab7a43195081bac98ed1c0a1ef3a43598facec39
fetched_at: '2026-06-29T00:09:19.979996+00:00'
page_id: '422545626'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco D 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545626
version: 69
---

#f5f5f5#363636LayoutEste bloco é composto pelos registros:BLOCODleftD100D100falseTipo de Documento

**Código 07** - Aquisição de Serviço de Transporte – Nota Fiscal de Transporte;

**Código 08** - Conhecimentos de Transporte Rodoviário de carga;

**Código 88** - Conhecimento de Transporte de Cagas Avulso;

**Código 10** - Aquaviário de cargas (código 09), Aéreo;

**Código 26** - Ferroviário de cargas (Código 11), Multimodal de cargas;

**Código 27** - Nota Fiscal de Transporte Ferroviário de carga;

**Código 57** - Nota Fiscal de Transporte Eletrônico – CT-e;

**Código 67** - Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS;

**Código 63** - Bilhetes de Passagem Eletrônico – BP-e;

Informações Adicionais

Para a geração deste registro serão selecionados os lançamentos de Entrada/Saída que estejam associados a CFOP do tipo fiscal e aos CODMODDOC 07, 08, 08B, 09, 10, 11, 26, 27, 57 e 67 e 63. Não deve ser gerado o CT-e denegado e Numeração inutilizada a partir de 2023.

| N° | Campo | Descrição | Origem da Informação | Observações |
| --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "C113" | Não se aplica |  |
| 02 | IND\_OPER | Indicador do tipo de operação: 0- Aquisição; 1- Prestação | DLAF.TIPOLF | Tipo de lançamento Entrada ou Saída |
| 03 | IND\_EMIT | Indicador do emitente do título: 0- Emissão própria; 1- Terceiros | DLAF.FLAGCFO | Lançamento de Saída => Emissão Própria; Lançamento de Entrada onde Emitente = Filial e é Regime Especial => Emissão Terceiros; Lançamento de Entrada onde Emitente = Filial => Emissão Própria; Lançamento de Entrada onde Emitente <> Filial => Emissão Terceiros |
| 04 | COD\_PART | Código do participante emitente (campo 02 do Registro 0150) do documento referenciado. | DLAF.EMITENTECFO | Código do Cliente/Fornecedor do lançamento. |
| 05 | COD\_MOD | Código do documento fiscal, conforme a Tabela 4.1.1 | FTDO.CODMODDOC | Código do modelo de documento vinculado ao lançamento. |
| 06 | COD\_SIT | Código da situação do documento fiscal, conforme a Tabela 4.1.2 | DLAF.STATUSLF |  |
| 07 | SER | Série do documento fiscal | DLAF.SERIEDOC | O campo série será completado com zeros a esquerda quando necessário.  Exemplo:  Série: 3  Arquivo Gerado: SER → 003 |
| 08 | SUB | Subsérie do documento fiscal | DLAF.SUBSERIE |  |
| 09 | NUM\_DOC | Número do documento fiscal | DLAF.DOCINI |  |
| 10 | CHV\_CTE | Chave do Conhecimento de Transporte Eletrônico ou do Bilhete de Passagem Eletrônico | DLAF.CHAVEACESSONFE ou TNFEESTADUAL.CHAVEACESSO |  |
| 11 | DT\_DOC | Data da emissão do documento fiscal | DLAF.DATAEMISSAO |  |
| 12 | DT\_A\_P | Data da aquisição ou da prestação do serviço | DLAF.DATAES |  |
| 13 | TP\_CT-e | Tipo de Conhecimento de Transporte Eletrônico conforme definido no Manual de Integração do CT-e ou do Bilhete de Passagem Eletrônico conforme definido no Manual de Integração do BP-e | DLAFAGRUP.TIPOCTE | O campo 13 do Registro D100 será gerado com a informação do campo "Tipo CT-e / BP-e / CT-e OS" para os códigos modelo documento 57, 63 e 67. O campo fica localizado na Pasta Transporte > Remetente/Destinatário: Imagem   O campo é gerado com as seguintes opções:   * "0" - Normal; * "1" - Complemento Valores; * "2"-  Anulação Valores; * "3" - Substituto  Maiores Informações [Documentação Técnica.](http://tdn.totvs.com/pages/viewpage.action?pageId=451252097) |
| 14 | CHV\_CTE\_REF | Chave do Bilhete de Passagem Eletrônico substituído | DLAFREFERENCIA.CHAVEACESSO ou DLAF.CHAVEACESSONFE ou TNFEESTADUAL.CHAVEACESSO |  |
| 15 | VL\_DOC | Valor total do documento fiscal | DLAFAGRUP.VALORCONT |  |
| 16 | VL\_DESC | Valor total do desconto | DLAF.DESCONTOS |  |
| 17 | IND\_FRT | Indicador do tipo do frete: 0 - Por conta de terceiros; 1 - Por conta do emitente; 2 - Por conta do destinatário; 9 - Sem cobrança de frete.   ---  Obs.: A partir de 01/07/2012 passará a ser: Indicador do tipo do frete: 0 - Por conta do emitente; 1 - Por conta do destinatário/remetente; 2 - Por conta de terceiros; 9 - Sem cobrança de frete. | DLAF.TIPOFRETE | Gerado conforme o preenchimento do Tipo frete, no Lançamento fiscal - Transporte | Identificação Imagem |
| 18 | VL\_SERV | Valor total da prestação de serviço | ValorMerc - Desconto+ValorDespesa+ValorSeguro+VlrFrete |  |
| 19 | VL\_BC\_ICMS | Valor da base de cálculo do ICMS | DLAF.BASEICMS |  |
| 20 | VL\_ICMS | Valor do ICMS | DLAF.VALORICMS |  |
| 21 | VL\_NT | Valor não-tributado | 0 |  |
| 22 | COD\_INF | Código da informação complementar do documento fiscal (campo 02 do Registro 0450) | Campo 02 do Registro 0450 |  |
| 23 | COD\_CTA | Código da conta analítica contábil debitada/creditada | TPRDFISCAL.CODCONTA | Código da conta contábil informada no cadastro do produto. |
| 24 | COD\_MUN\_ORIG | Código do município de origem do serviço, conforme a tabela IBGE (Preencher com 9999999, se Exterior) | DLAFTRANSP.CODMUNICIPIOCOLETA |  |
| 25 | COD\_MUN\_DEST | Código do município de destino, conforme a tabela IBGE (Preencher com 9999999, se Exterior) | DLAFTRANSP.CODMUNICIPIOENTREGA |  |

CamposleftNota Campo\_14

## **1CHV\_CTE\_REF**

Conforme manual da rotina (página 168 [http://sped.rfb.gov.br/estatico/30/5EC21565F41BC9D392045D71E5706429186705/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.6.pdf](http://sped.rfb.gov.br/estatico/30/5EC21565F41BC9D392045D71E5706429186705/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.6.pdf "Follow link"))

Campo 14 (CHV\_CTE\_REF) - Preenchimento:

Quando o campo TP\_CT-e ou BP-e se referir a “BP-e Substituição”, informar a chave do BP-e substituído. Nas demais situações o Campo não deve ser preenchido.

Será gerado com o campo "Chave de Acesso" da aba de referência do lançamento fiscal, conforme imagem abaixo, caso este campo não esteja preenchido será gerado com a chave do lançamento de origem. 

Imagem

Para que seja gerado a chave de acesso do campo "Chave de Acesso" da aba de referência do lançamento fiscal ou do lançamento de origem é necessário preencher o motivo de referência nos parâmetros do tipo de movimento na etapa Fis - Escrituração 1/2 que irá substituir.

Imagem

É necessário marcar na CFOP do movimento de substituição na etapa Outros Dados "Possui Documentos Relacionados":

Imagem

É necessário também selecionar o tipo BP-e "BP-e Substituição"

ImagemMaiores Informações

[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=619146888)

D500D500#f5f5f5#363636SPED Fiscal

**REGISTRO D500**: NOTA FISCAL DE SERVIÇO DE COMUNICAÇÃO (CÓDIGO 21) E NOTA FISCAL DE SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 22)

Este registro tem por objetivo apresentar as notas fiscais de serviços de comunicações. Na aquisição de serviço, será utilizado por todos os contribuintes; nas prestações de serviço, pelos contribuintes não enquadrados no Convênio ICMS 115/03. Empresas sujeitas ao disposto no Convênio ICMS 115/03 deverão utilizar este registro para informar os documentos emitidos nos modelos 21 e 22, nos casos não previstos no referido convênio.

Observar a Regra para gerar os campos:  

Registro é gerado quando: lançamento de entrada

                                            Ou

                                            lançamento de saída, Perfil A e o campo "Cód. Autenticação Digital Doc. Fiscal" (DLAF.CODAUTENTDIGITALDOC) vazio.

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "D500” | Fixo D500 |
| 02 | IND\_OPER | Indicador do tipo de operação:  0 - Aquisição;  1 - Prestação | DLAF.TIPOLF |
| 03 | IND\_EMIT | Indicador de emitente do documento fiscal:  0 - Emissão própria;  1- Terceiros | SE DLAF.TIPOLF = 'S' ENTÃO: '0'  SENÃO  SE CNPJ DA FILIAL = CNPJ DO EMITENTE ENTÃO: 0  SENÃO: 1 |
| 04 | COD\_PART | Código do participante (campo 02 do Registro 0150):    - do prestador do serviço, no caso de aquisição;  - do tomador do serviço, no caso de prestação. | FCFO.CODCFO  ou  GFILIAL.CODFILIAL |
| 05 | COD\_MOD | Código do modelo do documento fiscal. | FTDO.CODMODDOC |
| 06 | COD\_SIT | Código da situação do documento fiscal. | DLAF.STATUSLF |
| 07 | SER | Série do documento fiscal. | DLAF.STATUSLF |
| 08 | SUB | Subsérie do documento fiscal | DLAF.SERIEDOC |
| 09 | NUM\_DOC | Número do documento fiscal. | DLAF.DOCINI |
| 10 | DT\_DOC | Data da emissão do documento fiscal. | DLAF.DATAEMISSAO |
| 11 | DT\_A\_P | Data da Entrada (aquisição) ou da saída (prestação do serviço). | DLAF.DATAES |
| 12 | VL\_DOC | Valor total do documento fiscal. |  |
| 13 | VL\_DESC | Valor total do desconto. | DLAF.DESCONTOS + DLAF.OUTROSDESC |
| 14 | VL\_SERV | Valor da prestação de serviços | SE DNATUREZA.TIPONATICMS <> "Sem ICMS" Então:     Σ((DITEM.QTDEPRD \* DITEM.PRECOPRD) -        (DITEM.DESCONTOITEM                               +         DITEM.VALORDESPESA                                +        DITEM.VALORSEGURO                                  +        DITEM.FRETE)) Senão: 0 |
| 15 | VL\_SERV\_NT | Valor total dos serviços não-tributados pelo ICMS | SE TPRD.TIPO = 'S' e DNATUREZA.TIPONATICMS = "Sem ICMS" e DITEM.TIPORECEITA = "Algum dos tipos de receita própria"  então:       Σ ((DITEM.QTDEPRD \* DITEM.PRECOPRD) -            DITEM.DESCONTOITEM +             DITEM.VALORDESPESA) senão: 0 |
| 16 | VL\_TERC | Valores cobrados em nome de terceiros. | SE DITEM.TIPORECEITA = "Algum dos tipos de receita de terceiro" então Σ ((VALORMERC) - DITEM.DESCONTOITEM +  DITEM.VALORDESPESA) senão 0 |
| 17 | VL\_DA | Valor de outras despesas indicadas no documento fiscal. | DLAF.ACRESCIMO + DLAF. OUTROSACREC |
| 18 | VL\_BC\_ICMS | Valor a base de cálculo do ICMS. | DLAF. BASEREDICMS |
| 19 | VL\_ICMS | Valor do ICMS. | DLAF. VALORICMS |
| 20 | COD\_INF | Código da informação complementar. |  |
| 21 | VL\_PIS | Valor do PIS. | DTRBLAF.VALORTRB (TIPOTRIBFISC = ‘10’) |
| 22 | VL\_COFINS | Valor da COFINS. | DTRBLAF.VALORTRB (TIPOTRIBFISC = ‘11’) |
| 23 | COD\_CTA | Código da conta analítica contábil debitada/creditada. |  |
| 24 | TP\_ASSINANTE | Código do Tipo de Assinante:  1 - Comercial/Industrial  2 - Poder Público  3 - Residencial/Pessoa física  4 - Público  5 - Semi-Público  6 - Outros | DLAF.TIPOASSINANTE |

D695D695#f5f5f5#363636SPED Fiscal

**REGISTRO D695**: CONSOLIDAÇÃO DA PRESTAÇÃO DE SERVIÇOS – NOTAS DE SERVIÇO DE COMUNICAÇÃO (CÓDIGO 21) E DE SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 22) (EMPRESAS OBRIGADAS À ENTREGA DOS ARQUIVOS PREVISTOS NO CONVÊNIO ICMS 115/03). Registro é gerado através da tela de cadastro "".

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "D695” | Fixo D695 |
| 02 | COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1. | DREGISRO.CODMODDOC |
| 03 | SER | Série do documento fiscal | DREGISRO.SERIE |
| 04 | NRO\_ORD\_INI | Número de ordem inicial | DREGISRO.NUMDOCINICIAL |
| 05 | NRO\_ORD\_FIN | Número de ordem final | DREGISRO.NUMDOCFINAL |
| 06 | DT\_DOC\_INI | Data de emissão inicial dos documentos / Data inicial de vencimento da fatura | DREGISRO.DATAEMISSAOINICIAL |
| 07 | DT\_DOC\_FIN | Data de emissão final dos documentos / Data final do vencimento da fatura | DREGISRO.DATAEMISSAOFINAL |
| 08 | NOM\_MEST | Nome do arquivo Mestre de Documento Fiscal | DREGISRO.NOMEARQDOCFISCAL |
| 09 | CHV\_COD\_DIG | Chave de codificação digital do arquivo Mestre de Documento Fiscal | DREGISRO.CHAVEDIGITALDOCFISCAL |

D696D696#f5f5f5#363636Lançamentos Fiscais

É necessário identificar os Lançamentos Fiscais de Saída que serão gerados nos Registros. Conforme o manual do Sped Fiscal, para as Empresas obrigadas aos arquivos previstos no Convênio 115/03, temos duas opções de registros diferentes.

true01Lançamentos Fiscais

* Documentos **previstos** no Convênio 115/03 (via única). Deve gerar os Registros**D696** – Lançamentos de Saídas.
* Demais documentos **não abrangidos** pelo Convênio 115/03. Deve-se gerar os Registros **D500, D510, D530 e D590**.

Observação

**Lançamento de Saída**: Pelos contribuintes **não** enquadrados no Convênio ICMS 115/03, Lançamentos **não previstos** no referido convênio, se houver.

**Lançamento de Entrada**: Na aquisição de serviço, será utilizado por **todos os contribuintes**.

O campo **“Código de Autenticação Digital Documento Fiscal”** informado no - Lançamento Fiscal – Sub Pasta Dados de Energia\Comunicação identifica em qual registro o **Lançamento Fiscal de Saída deve ser gerado, no D500 ou no D695.**

Conforme demonstrado no documento do convênio: [Tipo M - MESTRE DE DOCUMENTO FISCAL](https://tdn.totvs.com/display/public/LRM/Tipo+M+-+MESTRE+DE+DOCUMENTO+FISCAL)

Link do campo: [Autenticação de Documento Fiscal](https://tdn.totvs.com/pages/releaseview.action?pageId=342307314)

#f5f5f5#363636SPED Fiscal

**REGISTRO D696**: REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 21 E 22). Neste Registro deve ser considerado somente Lançamentos de **Saída**, com CFOP iniciados em 5 e 6, e que o campo **Código de Autenticação Digital documento fiscal** esteja preenchido. Totalizado por CST, CFOP, ALÍQUOTA. 

Observar a Regra para gerar os campos:  

**Campo 02 (CST\_ICMS)**

**a)** se os dois últimos dígitos deste campo forem 30, 40, 41, 50, ou 60, então os valores dos campos **VL\_BC\_ICMS**, **ALIQ\_ICMS** e **VL\_ICMS** deverão ser iguais a “0” (zero);

**b)** se os dois últimos dígitos deste campo forem diferentes de 30, 40, 41, 50, e 60, então os valores dos campos **VL\_BC\_ICMS**, **ALIQ\_ICMS** e **VL\_ICMS** deverão ser maiores que “0” (zero); 

**c)** se os dois últimos dígitos deste campo forem iguais a 51 ou 90, então os valores dos campos **VL\_BC\_ICMS**, **ALIQ\_ICMS** e **VL\_ICMS** deverão ser maiores ou iguais a “0” (zero).

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "D696” | Fixo D696 |
| 02 | CST\_ICMS | Código da Situação Tributária, conforme a tabela indicada no item 4.3.1 | CST associado ao Item do Lançamento Fiscal. DITEM.CST |
| 03 | CFOP | Código Fiscal de Operação e Prestação, conforme a tabela indicada no item 4.2.2 | CFOP associado ao Lançamento Fiscal Subpasta Situação Tributária – Características  DNATUREZA.CFOP |
| 04 | ALIQ\_ICMS | Alíquota do ICMS | Alíquota do ICMS informado no Lançamento Fiscal – Subpasta Situação Tributária – ICMS e IPI  DLAF.ALIQICMS |
| 05 | VL\_OPR | Valor da operação correspondente à combinação de CST\_ICMS, CFOP, e alíquota do ICMS, incluídas as despesas acessórias e acréscimos | (VALORMERC) -  DITEM.DESCONTOITEM +   DITEM.VALORDESPESA |
| 06 | VL\_BC\_ICMS | Parcela correspondente ao "Valor da base de cálculo do ICMS" referente à combinação CST\_ICMS, CFOP, e alíquota do ICMS | É a soma do campo Base do ICMS informado no Item do Lançamento Fiscal – Subpasta Valores ICMS agrupado por CST, Alíquota e CFOP DITEM.BASEICMSPRD |
| 07 | VL\_ICMS | Parcela correspondente ao "Valor do ICMS" referente à combinação CST\_ICMS, CFOP, e alíquota do ICMS | É a soma do campo Valor do ICMS informado no Item – Subpasta Valores ICMS, agrupado por CST, Alíquota e CFOP DITEM.VLRICMSPRD |
| 08 | VL\_BC\_ICMS\_ | Parcela correspondente ao valor da base de cálculo do ICMS de outras UFs, referente à combinação de CST\_ICMS, CFOP e alíquota do ICMS | É a soma do campo Base do ICMS informado no Item do Lançamento Fiscal – Subpasta Valores ICMS agrupado por CST, Alíquota, CFOP e UF  DITEM.BASEICMSPRD  DLAF.CODETD  **Campo Gerado sob Demanda** |
| 09 | VL\_ICMS\_UF | Parcela correspondente ao valor do ICMS de outras UFs, referente à combinação de CST\_ICMS, CFOP, e alíquota do ICMS | É a soma do campo Valor do ICMS informado no Item – Subpasta Valores ICMS, agrupado por CST, Alíquota, CFOP e UF  DITEM.VLRICMSPRD  DLAF.CODETD  **Campo Gerado sob Demanda** |
| 10 | VL\_RED\_BC | Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST\_ICMS, CFOP e alíquota do ICMS | É a soma dos campos Outro, ou Isento quando a Base de cálculo for Reduzida informado no Item do Lançamento Fiscal – Subpasta Valores Isento ou Outros agrupado por CST, Alíquota, CFOP e UF  DITEM.ISENTOICMS  DITEM.OUTROSICMS |
| 11 | COD\_OBS | Código da observação do lançamento fiscal (campo 02 do Registro 0460) | Código gerado no Registro 0460  Obs.: Verificar a geração do Registro 0460 e incluir o Registro D696. |

D700D700#f5f5f5#363636SPED Fiscal

### Registro D700 - Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom (Código 62)

Este registro tem por objetivo escriturar notas de comunicação individualizadas, de entradas e saídas.

Observar a Regra para gerar os campos:  

Registro é gerado quando: lançamento de entrada ou lançamento de saída que possua modelo de documento 62 que não esteja cancelado e que tenham sido gerados a partir de 2023.

Nas entradas, a informação dos campos VL\_DOC, VL\_DESC, VL\_SERV, VL\_SERV\_NT, VL\_TERC e VL\_DA não  
deve levar em conta os serviços com cClass 110, 120 e 130.

Grupo de informações do documento referenciado será gerado quando na Natureza de operação - Outros dados - estiver marcado o flag: Possui Documentos Relacionados.

DCFOP.OPERACAOREFOUTRANF

**IMPORTANTE**: Caso possua mais de um documento referenciado, os campos serão preenchidos com os dados do primeiro.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 01 | REG | Texto fixo contendo "D700” |  |
| 02 | IND\_OPER | Indicador do tipo de prestação:  0: Entrada  1: Saída | Gerado com o Tipo do Lançamento Fiscal DLAF.TIPOLF |
| 03 | IND\_EMIT | Indicador do emitente do documento fiscal:  0: Emissão própria;  1: Terceiros. | Gerado conforme o Tipo do Lançamento Fiscal  Lançamento de Saída e o CNOJ da Filial igual do Emitente então “O – Emissão Própria”. Se Lançamento de Entrada “1 – Terceiro” SE DLAF.TIPOLF = ‘S’ ENTÃO: ‘0’ SENÃO     SE CNPJ DA FILIAL = CNPJ DO EMITENTE ENTÃO: 0     SENÃO: 1 |
| 04 | COD\_PART | Código do participante (Campo 02 do Registro 0150) do prestador, no caso de entradas | Participante do Lançamento Fiscal (Cliente/Fornecedor ou Filial no caso de de Transferência) FCFO.CODCFO ou GFILIAL.CODFILIAL  Gerado somente nas entradas. |
| 05 | COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1. | Gerado com o Código de Modelo do Documento associado ao lançamento fiscal. FTDO.CODMODDOC |
| 06 | COD\_SIT | Código da situação do documento fiscal, conforme a Tabela 4.1.2. | Gerado com o Campo situação do Lançamento Fiscal. DLAF.STATUSLF |
| 07 | SER | Série do documento fiscal. | Gerado com o Campo serie do lançamento Fiscal  DLAF.SERIEDOC |
| 08 | NUM\_DOC | Número do documento fiscal. | Gerado com o Campo Doc iniciado do lançamento fiscal DLAF.DOCINI |
| 09 | DT\_DOC | Data da emissão do documento fiscal. | Gerado com a Data de Emissão do Lançamento Fiscal  DLAF.DATAEMISSAO |
| 10 | DT\_E\_S | Data da entrada | Gerado com a data de Entrada do Lançamento Fiscal DLAF.DATAES |
| 11 | VL\_DOC | Valor do documento fiscal. | Gerado com o somatório do campo Valor Total da Situação Tributária.  DLAF.VALORCONT |
| 12 | VL\_DESC | Valor do desconto. | Gerado com o Campo Desconto ou Outro Desconto da Sub Pasta Valor da Mercadoria do Lançamento Fiscal DLAF.DESCONTOS + DLAF.OUTROSDESC |
| 13 | VL\_SERV | Valor dos serviços tributados pelo ICMS. | se DNATUREZA.TIPONATICMS <> "Sem ICMS" Então:     Σ((DITEM.VALORMERC) -        (DITEM.DESCONTOITEM                               +         DITEM.VALORDESPESA                                +        DITEM.VALORSEGURO                                  +        DITEM.FRETE)) Senão: 0 |
| 14 | VL\_SERV\_NT | Valores cobrados em nome do prestador sem destaque de ICMS. | se TPRD.TIPO = 'S' e DNATUREZA.TIPONATICMS = "Sem ICMS" e  DITEM.TIPORECEITA = "Receita Própria - xxx" então:       Σ ((DITEM.VALORMERC) -            DITEM.DESCONTOITEM +             DITEM.VALORDESPESA) senão: 0 |
| 15 | VL\_TERC | Valores cobrados em nome de terceiros | Gerado conforme o campo Tipo de Receita informado no item do Lançamento Fiscal Se DITEM.TIPORECEITA = "Algum dos tipos de receita de terceiro" então Σ ((VALORMERC) - DITEM.DESCONTOITEM +  DITEM.VALORDESPESA) senão 0 |
| 16 | VL\_DA | Valor de despesas acessórias indicadas no documento fiscal. | Gerado com o Campo Acréscimo ou Outro Acréscimo da SubPasta Valor da Mercadoria do Lançamento Fiscal DLAF.ACRESCIMO + DLAF. OUTROSACREC |
| 17 | VL\_BC\_ICMS | Valor da Base de Cálculo (BC) do ICMS. | Gerar com o somatório do valor do Campo Base de Cálculo Tributada ICMS da SubPasta ICMS\IPI  DLAF. BASEREDICMS |
| 18 | VL\_ICMS | Valor do ICMS | Se ICMS gera Credito/Debito  Então  Gerar com o somatório do valor do Campo Valor ICMS da SubPasta ICMS\IPI do Lançamento Fiscal DLAF. VALORICMS  Senão: 0 |
| 19 | COD\_INF | Código da informação complementar do documento fiscal (campo 02 do Registro 0450). | Gerado a partir de campo complementar |
| 20 | VL\_PIS | Valor do PIS/Pasep. | Gerado com o somatório do Valor do Tributo PIS informado na SubPasta Outros Tributos do Lançamento Fiscal DTRBLAF.VALORTRB (TIPOTRIBFISC = ‘10’)  Se valor menor ou igual a zero o campo não é preenchido. || |
| 21 | VL\_COFINS | Valor do Cofins. | Gerado com o somatório do Valor do Tributo Cofins informado na SubPasta Outros Tributos do Lançamento Fiscal DTRBLAF.VALORTRB (TIPOTRIBFISC = ‘11’)  Se valor menor ou igual a zero o campo não é preenchido. || |
| 22 | CHV\_DOCe | Chave da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica. | Gerado com o campo Chave Acesso (NF-e/NFS-e, NFC-e/CT-e/NF3-e/NFCom). em Outros na Sub Pasta Informações Adicionais do Lançamento Fiscal.   DLAF.CHAVEACESSONFE |
| 23 | FIN\_DOCe | Finalidade da emissão do documento eletrônico:  0 - NFCom Normal;  3 - NFCom de Substituição;  4 - NFCom de Ajuste; | Se Tipo de Operação da CFOP = Natureza de Ajuste  DCFOP.TIPOOPERACAO  Então 4 - Ajuste  Senão  Se Operação Com Documentos Relacionados = Possui Documentos Relacionados  DCFOP.OPERACAOREFOUTRANF  Então 3  Senão  0 |
| 24 | TIP\_FAT | TIP\_FAT Tipo de faturamento do documento eletrônico:  0 - Faturamento Normal;  1 - Faturamento Centralizado;  2 - Cofaturamento | Fixo 0 |
| 25 | COD\_MOD\_DOC\_ REF | Código do modelo do documento fiscal referenciado, conforme a Tabela 4.1.1. | Gerado com o campo Tipo de Documento do lançamento que foi referenciado em: Referencias - Lançamentos Fiscais.  DLAF.CODTDO |
| 26 | CHV\_DOCe\_REF | Chave da nota referenciada | Gerado quando o modelo do documento referenciado for 62.  Campo Chave de Acesso informada em:  Referencias - Lançamentos Fiscais.  DLAFREFERENCIA.CHAVEACESSO |
| 27 | HASH\_DOC\_REF | Código de autenticação digital do registro, campo 36 do registro do Arquivo tipo mestre de documento fiscal, conforme definido no Convênio 115/2003. | Gerado quando o modelo do documento referenciado for 21 ou 22.  Gerado com o campo Cód. Autenticação Digital Doc. Fiscal da aba: Informações Adicionais, sub Aba: Energia /Comunicação do lançamento que foi referenciado.  DLAF.CODAUTENTDIGITALDOC |
| 28 | SER\_DOC\_REF | Série do documento fiscal referenciado. | Gerado quando o modelo do documento referenciado for 21 ou 22 e o campo  Cód. Autenticação Digital Doc. Fiscal não estiver preenchido.  Gerado com o campo Série da aba: Identificação, sub Aba: Cabeçalho do lançamento que foi referenciado.  DLAF.SERIEDOC |
| 29 | NUM\_DOC\_REF | Número do documento fiscal referenciado. | Gerado quando o modelo do documento referenciado for 21 ou 22 e o campo  Cód. Autenticação Digital Doc. Fiscal não estiver preenchido.  Gerado com o campo Doc.Inicial da aba: Identificação, sub Aba: Cabeçalho do lançamento que foi referenciado.  DLAF.DOCINI |
| 30 | MES\_DOC\_REF | MES\_DOC\_REF Mês e ano da emissão do documento fiscal referenciado | Gerado quando o modelo do documento referenciado for 21 ou 22 e o campo  Cód. Autenticação Digital Doc. Fiscal não estiver preenchido.  Gerado com o campo Data Emissão da aba: Identificação, sub Aba: Cabeçalho do lançamento que foi referenciado.  DLAF.DATAEMISSAO |
| 31 | COD\_MUN\_DEST | Código do município do destinatário conforme a tabela do IBGE. | Município do Cliente/Fornecedor |
| 32 | DED | Deduções | Não implementado |

D730D730#f5f5f5#363636SPED Fiscal

### Registro D730 - Registro analítico Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom (Código 62)

Este registro tem por objetivo representar a escrituração dos documentos fiscais informados no registro D700 totalizados pela combinação de CST, CFOP e Alíquota de ICMS.

Observar a Regra para gerar os campos:  

Registro é gerado quando: lançamento de entrada ou lançamento de saída que possua modelo de documento 62 que não esteja cancelado.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 01 | REG | Texto fixo contendo "D730” | Registro gerado por Situação Tributária |
| 02 | CST\_ICMS | Código da Situação Tributária, conforme a tabela indicada no item 4.3.1 | Valor Calculado  Se Campo CST do item estiver preenchido (DITEM.CST)  então  DITEM.CST  Senão  Gerado com o CST informado na Regra do ICMS associado a CFOP do Lançamento Fiscal DREGRAICMS.SITTRIBUTARIA |
| 03 | CFOP | Código Fiscal de Operação e Prestação, conforme a tabela indicada no item 4.2.2 | Gerar com a CFOP associada ao Lançamento Fiscal – SubPasta – Situações Tributarias DNATUREZA.CODNAT |
| 04 | ALIQ\_ICMS | Alíquota do ICMS | Gera com o Campo Alíquota do ICMS da Pasta Situações Tributarias\SubPasta ICMS\IPI.  DLAF.ALIQICMS |
| 05 | VL\_OPR | Valor da prestação correspondente à combinação de CST\_ICMS, CFOP, e alíquota do ICMS, incluídas as despesas acessórias e acréscimos | Valor Calculado Se parcela possui item  Então  Somatório do campo Valor Mercadorias dos itens da parcela DITEM.VALORMERC   Senão  DLAF.VALORMERC |
| 06 | VL\_BC\_ICMS | Parcela correspondente ao "Valor da base de cálculo do ICMS" referente à combinação CST\_ICMS, CFOP, e alíquota do ICMS | Valor Calculado  Se parcela possui item e possui tributo do tipo ICMS.  Então  Somatório da base de calculo dos itens da parcela DITEM.BASEICMSPRD  Senão  Gerar com o Campo Base de Cálculo do ICMS Tributada da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF. BASEREDICMS |
| 07 | VL\_ICMS | Parcela correspondente ao "Valor do ICMS" referente à combinação CST\_ICMS, CFOP, e alíquota do ICMS, incluindo o FCP, quando aplicável, referente à combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Valor Calculado  Se parcela possui item e possui tributo do tipo ICMS e ICMS gera Credito/Debito  Então  Somatório da valor ICMS dos itens da parcela DITEM.VALORICMSPRD  Gerar com o Campo Valor do ICMS da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF. VALORICMS  Senão  0 |
| 08 | VL\_RED\_BC. | Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Campo gerado conforme a definição da CFOP associado ao Lançamento Fiscal.  Se DNATUREZA.COLOCARREDUCAOEM = "Isentos"  Então       Se possui item       Então       DITEM.ISENTOICMS       Senão       DLAF.ISENTOICMS Senão:     Se DNATUREZA.COLOCARREDUCAOEM = "Outros"       Se possui item       Então       DITEM.OUTROSICMS       Senão       DLAF.OUTROSICMS |
| 09 | COD\_OBS | Código da observação (campo 02 do Registro D735) |  |

D731D731#f5f5f5#363636SPED Fiscal

### Registro D731 - Informações do fundo de combate à pobreza – FCP – (Código 62)

Estas informações equivalem ao valor de FECP próprio do item.

Observar a Regra para gerar os campos:  

Registro é gerado quando: lançamento de entrada ou lançamento de saída que possua modelo de documento 62 e valor FECP Próprio e que não esteja cancelado.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 01 | REG | Texto fixo contendo "D731” |  |
| 02 | VL\_FCP\_OP | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST\_ICMS, CFOP e alíquota do ICMS | Gerar com o Campo Valor FCP ICMS Próprio da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF. VLRFCPROPRIO |

D735D735#f5f5f5#363636SPED Fiscal

### Registro D735 - Observações do lançamento fiscal (Código 62)

Estas informações equivalem às observações que são lançadas na coluna “Observações” dos Livros Fiscais previstos no Convênio SN/70 – SINIEF, art. 63, I a IV.

Observar a Regra para gerar os campos:  

Registro é gerado quando: lançamento de entrada ou lançamento de saída que possua modelo de documento 62 que não esteja cancelado.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 01 | REG | Texto fixo contendo "D735” |  |
| 02 | COD\_OBS | Código da Observação do lançamento fiscal (campo 09 do Registro D730) | Contador do Registro D735 |
| 03 | TXT\_COMPL | Código Fiscal de Operação e Prestação, conforme a tabela indicada no item 4.2.2 | Observação da Situação Tributária do Lançamento Fiscal |

D737D737#f5f5f5#363636SPED Fiscal

### Registro D737 - Outras obrigações tributárias, ajustes e informações de valores proveniente de documento fiscal

Observar a Regra para gerar os campos:  

Registro é gerado quando: lançamento de entrada ou lançamento de saída que possua Modelo de Documento 62 que não esteja cancelado.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 01 | REG | Texto fixo contendo "D737” |  |
| 02 | COD\_AJ | Código do ajustes/benefício/incentivo, conforme tabela indicada no item 5.3 | Gerado com o Código de Ajuste associado ao Lançamento Fiscal ou ao Item. |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste do documento fiscal. | Gerado com Descrição informado no Ajuste do Lançamento ou do Item, Pasta Situações Tributarias\Subpasta Ajuste Sped – ou Ajuste Sped  do Item |
| 04 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Código do Item do Lançamento Fiscal que tem o Código de Ajuste associado |
| 05 | VL\_BC\_ICMS | Base de cálculo do ICMS | Gerado com o Valor da Base de Cálculo informado no Ajuste do Lançamento ou do Item, Pasta Situações Tributarias\Subpasta Ajuste Sped – ou Ajuste Sped  do Item |
| 06 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com a alíquota informado no Ajuste do Lançamento ou do Item, Pasta Situações Tributarias\Subpasta Ajuste Sped – ou Ajuste Sped  do Item |
| 07 | VL\_ICMS | Valor do ICMS | Gerado com o Valor ddo ICMS informado no Ajuste do Lançamento ou do Item, Pasta Situações Tributarias\Subpasta Ajuste Sped – ou Ajuste Sped  do Item |
| 08 | VL\_OUTROS | Outros valores | Gerado com o Valor de Outros informado no Ajuste do Lançamento ou do Item, Pasta Situações Tributarias\Subpasta Ajuste Sped – ou Ajuste Sped  do Item |

D750D750

**Registro esta sendo implementado  
REGISTRO D750 - ESCRITURAÇÃO CONSOLIDADA DA NOTA FISCAL FATURA ELETRÔNICA DE SERVIÇOS DE COMUNICAÇÃO - NFCom (CÓDIGO 62)**

| N | Campo | Descrição | Tipo | Tam | Dec | Origem do Dados |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Rec | Texto fixo contendo "D750" | C | 004 |  | Texto FIxo |
| 02 | COD\_MOD | Código do modelo do documento fiscal, conforme a  Tabela 4.1.1 | C | 002 |  |  |
| 03 | SER | Série do documento fiscal | N | 003 |  | Gerado com o Campo Serie do Lançamento Fiscal |
| 04 | DT\_DOC | Data da emissão dos documentos | N | 008 |  | Gerado com a Data LF |
| 05 | QTD\_CONS | Quantidade de documentos consolidados neste registro | N |  |  |  |
| 06 | IND\_PREPAGO | Forma de pagamento:  0 – pré pago  1 – pós pago | N | 001 |  | Gerado conforme o Campo novo criado no Cadastro do Produto |
| 07 | VL\_DOC | Valor total dos documentos | N |  | 002 | Gerado com o somatório do campo Valor Total da Situação Tributária de todos os lançamentos selecionados.  DLAF.VALORCONT |
| 08 | VL\_SERV | Valor dos serviços tributados pelo ICMS | N |  | 002 | se DNATUREZA.TIPONATICMS <> "Sem ICMS" Então:     Σ((DITEM.VALORMERC) -        (DITEM.DESCONTOITEM                               +         DITEM.VALORDESPESA                                +        DITEM.VALORSEGURO                                  +        DITEM.FRETE)) Senão: 0 |
| 09 | VL\_SERV\_NT | Valores cobrados em nome do prestador sem destaque de  ICMS | N |  | 002 | se TPRD.TIPO = 'S' e DNATUREZA.TIPONATICMS = "Sem ICMS" e  DITEM.TIPORECEITA = "Receita Própria - xxx" então:       Σ ((DITEM.VALORMERC) -            DITEM.DESCONTOITEM +             DITEM.VALORDESPESA) senão: 0 |
| 10 | VL\_TERC | Valor total cobrado em nome de terceiros | N |  | 002 | Gerado conforme o campo Tipo de Receita informado no item do Lançamento Fiscal Se DITEM.TIPORECEITA = "Algum dos tipos de receita de terceiro" então Σ ((VALORMERC) - DITEM.DESCONTOITEM +  DITEM.VALORDESPESA) senão 0 |
| 11 | VL\_DESC | Valor total dos descontos | N |  | 002 | Gerado com o Campo Desconto ou Outro Desconto da Sub Pasta Valor da Mercadoria do Lançamento Fiscal DLAF.DESCONTOS + DLAF.OUTROSDESC |
| 12 | VL\_DA | Valor total das despesas acessórias | N |  | 002 | Gerado com o Campo Acréscimo ou Outro Acréscimo da SubPasta Valor da Mercadoria do Lançamento Fiscal DLAF.ACRESCIMO + DLAF. OUTROSACREC |
| 13 | VL\_BC\_ICMS | Valor total da base de cálculo do ICMS | N |  | 002 | Gerar com o somatório do valor do Campo Base de Cálculo Tributada ICMS da SubPasta ICMS\IPI  DLAF. BASEREDICMS |
| 14 | VL\_ICMS | Valor total do ICMS | N |  | 002 | Se ICMS gera Credito/Debito Então Gerar com o somatório do valor do Campo Valor ICMS da SubPasta ICMS\IPI do Lançamento Fiscal DLAF. VALORICMS Senão: 0 |
| 15 | VL\_PIS | Valor total do PIS | N |  | 002 | Gerado com o somatório do Valor do Tributo PIS informado na SubPasta Outros Tributos do Lançamento Fiscal DTRBLAF.VALORTRB (TIPOTRIBFISC = ‘10’) Se valor menor ou igual a zero o campo não é preenchido. |
| 16 | VL\_COFINS | Valor total da COFINS | N |  | 002 | Gerado com o somatório do Valor do Tributo Cofins informado na SubPasta Outros Tributos do Lançamento Fiscal DTRBLAF.VALORTRB (TIPOTRIBFISC = ‘11’) Se valor menor ou igual a zero o campo não é preenchido. |
| 17 | DED | Deduções | N |  | 002 | Não implementado |

D760D760

**Registro esta sendo implementado**

**Registro D760** - **REGISTRO ANALÍTICO DA ESCRITURAÇÃO CONSOLIDADA DA NOTA FISCAL FATURA ELETRÔNICA DE SERVIÇOS DE COMUNICAÇÃO - NFCom (CÓDIGO 62)** 

Este registro tem por objetivo representar a escrituração dos documentos fiscais informados no registro D750 totalizados pela combinação de CST, CFOP e Alíquota de ICMS.

**Validação do Registro:** não podem ser informados dois ou mais registros com a combinação de mesmos valores dos   
campos CST\_ICMS, CFOP e ALIQ\_ICMS para o mesmo documento.

Filtro

Registro filho do D750, gerado com a soma de todos os lançamentos selecionado no Registro D750.

| N | Campo | Descrição | Tipo | Tam | Dec | Origem do Dados |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Rec | Texto fixo contendo "D760" | C | 004 |  | Texto FIxo |
| 02 | CST\_ICMS | Código da Situação Tributária, conforme a tabela indicada  no item 4.3.1 | C | 003 |  | Valor Calculado Se Campo CST do item estiver preenchido (DITEM.CST) então  DITEM.CST Senão  Gerado com o CST informado na Regra do ICMS associado a CFOP do Lançamento Fiscal DREGRAICMS.SITTRIBUTARIA |
| 03 | CFOP | Código Fiscal de Operação e Prestação, conforme a tabela  indicada no item 4.2.2 | N | 004 |  | Gerar com a CFOP associada ao Lançamento Fiscal – SubPasta – Situações Tributarias DNATUREZA.CODNAT |
| 04 | ALIQ\_ICMS | Alíquota do ICMS | N | 006 | 02 | Gera com o Campo Alíquota do ICMS da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF.ALIQICMS |
| 05 | VL\_OPR | Valor total dos itens relacionados aos serviços próprios,  com destaque de ICMS, correspondente à combinação de  CST\_ICMS, CFOP, e alíquota do ICMS. | N |  | 02 | Valor Calculado Se parcela possui item  Então Somatório do campo Valor Mercadorias dos itens da parcela DITEM.VALORMERC  Senão DLAF.VALORMERC |
| 06 | VL\_BC\_ICMS | Parcela correspondente ao "Valor da base de cálculo do  ICMS" referente à combinação CST\_ICMS, CFOP, e  alíquota do ICMS | N |  | 02 | Valor Calculado Se parcela possui item e possui tributo do tipo ICMS. Então  Somatório da base de calculo dos itens da parcela DITEM.BASEICMSPRD Senão Gerar com o Campo Base de Cálculo do ICMS Tributada da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF. BASEREDICMS |
| 07 | VL\_ICMS | Parcela correspondente ao "Valor do ICMS", incluindo o  FCP, quando aplicável, referente à combinação de  CST\_ICMS, CFOP e alíquota do ICMS. | N |  | 02 | Valor Calculado Se parcela possui item e possui tributo do tipo ICMS e ICMS gera Credito/Debito Então  Somatório da valor ICMS dos itens da parcela DITEM.VALORICMSPRD Gerar com o Campo Valor do ICMS da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF. VALORICMS Senão 0 |
| 08 | VL\_RED\_BC | Valor não tributado em função da redução da base de  cálculo do ICMS, referente à combinação de CST\_ICMS,  CFOP e alíquota do ICMS. | N |  | 02 | Campo gerado conforme a definição da CFOP associado ao Lançamento Fiscal. Se DNATUREZA.COLOCARREDUCAOEM = "Isentos" Então      Se possui item      Então       DITEM.ISENTOICMS      Senão      DLAF.ISENTOICMS Senão:     Se DNATUREZA.COLOCARREDUCAOEM = "Outros"      Se possui item      Então       DITEM.OUTROSICMS      Senão      DLAF.OUTROSICMS |
| 09 | COD\_OBS | Código da observação (campo 02 do Registro 0460) | C | 006 |  |  |

D761D761

**Registro esta sendo implementado**

**REGISTRO D761: INFORMAÇÕES DO FUNDO DE COMBATE À POBREZA – FCP – (CÓDIGO 62)**

Este registro tem por objetivo prestar informações do Fundo de Combate à Pobreza (FCP), constante na NFCom.

| N | Campo | Descrição | Tipo | Tam | Dec | Origem do Dados |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Rec | Texto fixo contendo "D761" | C | 004 |  | Texto FIxo |
| 02 | VL\_FCP\_OP | Valor do Fundo de Combate à Pobreza (FCP) vinculado à  operação própria, na combinação de CST\_ICMS, CFOP e  alíquota do ICMS | N |  | 02 | Gerar com o Campo Valor FCP ICMS Próprio da Pasta Situações Tributarias\SubPasta ICMS\IPI. DLAF. VLRFCPROPRIO |

#f5f5f5#363636Vídeos

**How to - EFD ICMS IPI D695/D696:  
648432**
