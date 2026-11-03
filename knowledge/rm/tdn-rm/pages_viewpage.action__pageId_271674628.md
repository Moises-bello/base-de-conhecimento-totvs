---
content_hash: 254c663b6f92a4b9ec3bfe101c1a260ef25ba835ead6b3f7c39f878451419e5e
fetched_at: '2026-06-29T00:08:28.317727+00:00'
page_id: '271674628'
product: rm
source: tdn-rm
title: ER_ICMS_115/03
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271674628
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Fiscal |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | Convênio ICMS 115/03 | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.17 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Especificar as regras de negócio e o comportamento do Sistema ao gerar a Rotina ICMS 115/03.

## Premissas

Tem como funcionalidade gerar os arquivos magnéticos conforme disponível no Convênio ICMS 115/03, que dispõe sobre a prestação das informações dos documentos fiscais emitidos por Contribuintes Prestadores de Serviços de Comunicação e Fornecedores de Energia Elétrica, com os seguintes tipos de Documentos:

a) Nota Fiscal/Conta de Energia Elétrica, modelo 6;

b) Nota Fiscal de Serviço de Comunicação, modelo 21;

c) Nota Fiscal de Serviço de Telecomunicações, modelo 22;

d) qualquer outro documento fiscal de prestação de serviços de comunicação ou telecomunicações ou fornecimento de Energia Elétrica ou Gás canalizado

Serão selecionados somente Lançamentos de Saídas (CFOPs iniciados por 5, 6 ou 7).

O Registro de IDENTIFICAÇÃO E CONTROLE (Tipo C) com a identificação do contribuinte e resumo da quantidade de registros  e somatória de valores dos arquivos acima referidos não será gerado pelo Aplicativo Gestão Fiscal. O  programa  e-Nota  Fiscal,  após  a  validação  sem  erros  do arquivo importado, permite a geração do registro de controle.

Os arquivos deverão ser gerados mensalmente,contendo apenas as informações referentes aos documentos fiscais escriturados na apuração do ICMS do mês.

OBS: os arquivos serão gerados conforme texto da Rotina que passou a valer a partir de 01/01/2017.

## Definição da Regra de Negócio

Quanto à Geração dos Arquivos

Foi disponibilizado o menu “Obrigações Acessórias -> Rotinas Fiscais -> Estaduais -> Convênio ICMS 115/2003”:

                                                                                                                                                           

Através do menu dispobilizado, o usuário acessará a tela de Geração da Rotina:

O arquivo da Rotina ICMS 115/03, será gerado no diretório parametrizado pra os Arquivos Temporários:

### 

Os arquivos serão gerados com o seguinte padrão de nomenclatura:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UF | CNPJ | Modelo | Série | Ano | Mês | Status | Tipo |  | Extensão |
| UU | CCCCCCCCCCCCCC | MM | SSS | AA | MM | Snn | T | . | VVV |

Onde:

UF (UF) - sigla da unidade federada do emitente dos documentos fiscais;

CNPJ (CCCCCCCCCCCCCC) - CNPJ do emitente dos documentos fiscais;

Modelo (MM) - modelo dos documentos fiscais;

Série (SSS) - série dos documentos fiscais;

Ano (AA) - ano do período de apuração dos documentos fiscais;

Mês (MM) - mês do período de apuração dos documentos fiscais;

Status (Snn) - indica se o arquivo é normal (N) ou substituto (S). Em caso de arquivo substituto, deverá ser indicado o número sequencial com dois dígitos (“nn”) do arquivo substituto, iniciando em “01”. Caso se trate de arquivo normal, preencher com “01”. Essa informação é fornecida pelo usuário na tela de geração da rotina.

Tipo (T) - inicial do tipo do arquivo, podendo assumir um dos seguintes valores:

a) ‘M’- MESTRE DE DOCUMENTO FISCAL;

b) ‘I’ - ITEM DE DOCUMENTO FISCAL;

c) ‘D’ - DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL;

d) ‘C’ - CONTROLE E IDENTIFICAÇÃO (conforme observado nas premissas, não será gerado pelo Gestão Fiscal);

Volume (VVV) - número sequencial do volume, a quantidade de registros do arquivo MESTRE DE DOCUMENTO FISCAL é limitado a 100 (cem) mil ou 1 (um) milhão de documentos fiscais. Sempre que alcançado o limite, deverão ser criados arquivos de continuação, cuja numeração será sequencial e consecutiva, iniciada em 001.

Os arquivos devem ser divididos quando ultrapassarem 100 (cem) mil documentos para contribuintes com volume mensal de emissão até 1 (hum) milhão de documentos ou

1 (hum) milhão de documentos para os contribuintes com volume mensal de emissão superior a 1 (hum) milhão de documentos.

Quanto aos parâmetros de Geração da Rotina:

Nesse passo serão informados os seguintes campos:

* + Filial: será informada a Filial para geração da Rotina. O preenchimento desse campo é obrigatório para geração da rotina.
  + Data Inicial: será informada a Data inicial para filtro dos Lançamentos que serão gerados. O preenchimento desse campo é obrigatório para geração da rotina.
  + Data Final: será informada a Data final para filtro dos Lançamentos que serão gerados. O preenchimento desse campo é obrigatório para geração da rotina.
  + Situação: será informado o valor "Normal" ou "Substituto". Esse valor será gerado no nome do arquivo, conforme será descrito com mais detalhes abaixo.
  + Rotina: será informada a Rotina a ser gerada. O preenchimento desse campo é obrigatório para geração da rotina.
  + Calcula Código de Autenticação Digital do Documento Fiscal: caso o campo seja marcado, o sistema irá calcular o Código de Autenticação dos documentos na geração dos arquivos.

Quanto à Seleção dos Lançamentos

Serão selecionados os Lançamentos que sejam da Filial selecionada.

Serão selecionados os Lançamentos cuja Data do Documento esteja dentro do período informado na tela de geração da Rotina.

Serão selecionados somente os Lançamentos Emitidos (Saída).

Serão selecionados somente os Lançamentos cujo Modelo do Tipo de Documento seja "06" (Energia Elétrica), "21" (Comunicação) e "22" (Telecomunicação).

Quanto à geração dos Registros de acordo com o Layout

Sobre o formato dos campos:

Numérico (N), sem sinal, não compactado, alinhado à direita, suprimidos quaisquer caracteres não numéricos, com as posições não significativas preenchidas com zeros. Os valores negativos serão representados com o sinal negativo na primeira posição do campo. Na ausência de informação, o campo deverá ser preenchido com zero.

Alfanumérico (X), alinhado à esquerda, com as posições não significativas em branco. Na ausência de informação, o campo deverá ser preenchido com brancos.

As datas devem ser preenchidas no formato ano, mês e dia (AAAAMMDD);

* Arquivo “Mestre de Documento Fiscal”: arquivo que contém as informações das notas em ordem crescente do número do documento.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ordem | Campo | Tamanho | Pos. Inicial | Pos. Final | Formato | Campo Origem | Tabela Origem | Observações |
| 1 | CNPJ ou CPF | 14 | 1 | 14 | N | CGCCFO | FCFO |  |
| 2 | IE | 14 | 15 | 28 | X | INSCRESTADUAL | FCFO |  |
| 3 | Razão Social | 35 | 29 | 63 | X | NOME | FCFO |  |
| 4 | UF | 2 | 64 | 65 | X | CODETD | FCFO | Caso o Cli/For seja do Exterior, será gerado o valor fixo "EX". |
| 5 | Classe de Consumo | 1 | 66 | 66 | N | IDCLASSECONSUMO | DLAF | Será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "1 - Classe Consumo". |
| 6 | Fase ou Tipo de Utilização | 1 | 67 | 67 | N | IDTIPOUTILIZACAO | DLAF | Será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "5 - Tipo de Utilização". |
| 7 | Grupo de Tensão | 2 | 68 | 69 | N | IDGRUPOTENSAO | DLAF | Será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "3 - Grupo Tensão". |
| 8 | Código de Identificação do consumidor ou assinante | 12 | 70 | 81 | X | TIPOASSINANTE | DLAF |  |
| 9 | Data de emissão | 8 | 82 | 89 | N | DATAEMISSAO | DLAF |  |
| 10 | Modelo | 2 | 90 | 91 | N | CODMODDOC | FTDO | Nota Fiscal de Serviço de Comunicação, modelo 21; Nota Fiscal de Serviço de Telecomunicações, modelo 22 ;  Nota Fiscal/Conta de Energia Elétrica, modelo 6; |
| 11 | Série | 3 | 92 | 94 | X | SERIEDOC | DLAF |  |
| 12 | Número | 9 | 95 | 103 | N | DOCINI | DLAF |  |
| 13 | Código de Autenticação Digital do documento fiscal | 32 | 104 | 135 | X | \* | \* | Será informado o código de autenticação digital obtido por meio da aplicação do  algoritmo MD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de caracteres  formada pelos campos 01, 12, 14, 15, 16, 09 e 27, nessa ordem, respeitando o tamanho previsto do campo, assim como os brancos e zeros de preenchimento. |
| 14 | Valor Total (com 2 decimais) | 12 | 136 | 147 | N | VALORCONT | DLAF |  |
| 15 | BC ICMS (com 2 decimais) | 12 | 148 | 159 | N | BASEICMS | DLAF |  |
| 16 | ICMS destacado (com 2 decimais) | 12 | 160 | 171 | N | VALORICMS | DLAF |  |
| 17 | Operações isentas ou não tributadas (com 2 decimais) | 12 | 172 | 183 | N | ISENTOICMS | DLAF |  |
| 18 | Outros valores (com 2 decimais) | 12 | 184 | 195 | N | OUTROSICMS | DLAF |  |
| 19 | Situação do documento | 1 | 196 | 196 | X | STATUSLF  DATAEMISSAO | DLAF | “S”, em se tratando de documento fiscal cancelado dentro do mesmo período de apuração;  “R”, em se tratando de documento fiscal emitido em substituição a um documento fiscal cancelado dentro do mesmo período de apuração;  “C”, em se tratando de documento fiscal complementar;  “N”, nos demais casos.  Nas hipóteses de situação “R” ou “C”, deve ser preenchido o campo 34 - “Informações Adicionais” (item 5.2.5.13). |
| 20 | Ano e Mês de referência de apuração | 4 | 197 | 200 | N | DATAEMISSAO | DLAF | Formato “AAMM” |
| 21 | Referência ao item da NF | 9 | 201 | 209 | N | \* | \* | Número da linha do arquivo onde se encontra o primeiro item do Documento Fiscal. |
| 22 | Número do terminal telefônico ou da unidade  consumidora | 12 | 210 | 221 | X | CONTACONSUMO | DLAF |  |
| 23 | Indicação do tipo de informação contida no campo 1 | 1 | 222 | 222 | N | CGCCFO | FCFO | Para Pessoa Física: 2 - Caso tenha sido informado o CPF ou 4 - Caso não tenha sido informado o CPF.  Para Pessoa Jurídica: 1 - Caso tenha sido informado o CNPJ ou 3 - Caso não tenha sido informado o CNPJ. |
| 24 | Tipo de cliente | 2 | 223 | 224 | N | TIPOCLIENTE | FCFO | Para Modelo "06":  13 - Consumidor Cativo;  21 - Consumidor Livre;  22 - Consumidor Especial;  23 - Consumidor Parcialmente Livre;  Para Modelo "21" ou "22":  01 - Comercial;  02 - Industrial;  03 - Residencial/Pessoa Física;  04 - Produtor Rural;  05 - Órgão da administração pública estadual direta e suas fundações e autarquias, quando mantidas pelo poder público estadual e regidas por normas de direito público, nos termos do Convênio ICMS 107/95;  06 - Prestador de serviço de telecomunicação responsável pelo recolhimento do imposto incidente sobre a cessão dos meios de rede do prestador do serviço ao usuário final, nos termos do Convênio ICMS 17/13;  07 - Missões Diplomáticas, Repartições Consulares e Organismos Internacionais, nos termos do Convênio ICMS 158/94;  08 - Igrejas e Templos de qualquer natureza;  99 - Outros não especificados anteriormente; |
| 25 | Subclasse de consumo | 2 | 225 | 226 | N | IDSUBCLASSE | DLAF | Será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "7 - Subclasses no Fornecimento de Energia Elétrica". |
| 26 | Número do terminal telefônico principal | 12 | 227 | 238 | X | CONTACONSUMOPRI | DLAF |  |
| 27 | CNPJ do emitente | 14 | 239 | 252 | N | CGC | GFILIAL |  |
| 28 | Número ou código da fatura comercial | 20 | 253 | 272 | X | NUMFATCOMERCIAL | DLAF |  |
| 29 | Valor total da fatura comercial | 12 | 273 | 284 | N | VALORFATCOMERCIAL | DLAF |  |
| 30 | Data de leitura anterior | 8 | 285 | 292 | N | DATALEITURAANT | DLAF |  |
| 31 | Data de leitura atual | 8 | 293 | 300 | N | DATALEITURA | DLAF |  |
| 32 | Brancos - reservado para uso futuro | 50 | 301 | 350 | X | \* | \* |  |
| 33 | Brancos - reservado para uso futuro | 8 | 351 | 358 | N | \* | \* |  |
| 34 | Informações adicionais | 30 | 359 | 388 | X | \* | \* | Informar os dados dos documentos fiscais substituídos ou complementados nos casos de:  a) documento fiscal emitido em substituição a outro que tenha sido objeto de estorno de débito (apenas para as unidades federadas que admitem esta hipótese).  b) o campo 19 tersido preenchido com “R” (documento fiscal emitido em substituição a um documento fiscal cancelado) ou  com “C” (documento fiscal complementar).  Devem ser informados:  referência de apuração (4 algarismos),  modelo (2 caracteres)  série (3 caracteres)  número (9 algarismos)  data de emissão (8 algarismos)  Totalizando 30 caracteres, no seguinte formato: “AAMM\_MO\_SSS\_NNNNNNNNN\_AAAAMMDD”.  Exemplo: “0901\_22\_A \_000001234\_20090131“, para o documento fiscal da referência “0901”, modelo “22”, série “A“, número “000001234”, emitido em 31/01/2009. Nos demais casos, preencher com brancos. |
| 35 | Brancos - reservado para uso futuro | 5 | 389 | 393 | X | \* | \* |  |
| 36 | Código de Autenticação Digital do Registro | 32 | 394 | 425 | X | \* | \* | Informar o código de autenticação digital obtido por meio da aplicação do algoritmo MD5 (Message Digest 5) de 128 bits na cadeia de caracteres formada pelos campos 01 a 35. |

 

* Arquivo “Item de Documento Fiscal”: arquivo que contém as informações dos itens das notas em ordem crescente do número do documento e o número do item:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ordem | Campo | Tamanho | Pos. Inicial | Pos. Final | Formato | Campo Origem | Tabela Origem | Observações |
| 1 | CNPJ ou CPF | 14 | 1 | 14 | N | CGCCFO | FCFO |  |
| 2 | UF | 2 | 15 | 16 | X | CODETD | FCFO |  |
| 3 | Classe do Consumo | 1 | 17 | 17 | N | IDCLASSECONSUMO | DLAF | Para nota fiscal Modelo "06", será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "1 - Classe Consumo".  Para outros Modelos será gerado zero. |
| 4 | Fase ou Tipo de Utilização | 1 | 18 | 18 | N | IDTIPOLIGACAO  IDTIPOUTILIZACAO | DLAF | Para nota fiscal Modelo "06", será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "2 - Tipo Ligação".  Para os outros Modelos, será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "5 - Tipo de Utilização". |
| 5 | Grupo de Tensão | 2 | 19 | 20 | N | IDGRUPOTENSAO | DLAF | Para nota fiscal Modelo "06", será informado um dos valores da tabela DVALORROTINAS, que tenham tipo "3 - Grupo Tensão".  Para outros Modelos será gerado zero. |
| 6 | Data de Emissão | 8 | 21 | 28 | N | DATAEMISSAO | DLAF |  |
| 7 | Modelo | 2 | 29 | 30 | N | CODMODDOC | FTDO | Nota Fiscal de Serviço de Comunicação, modelo 21; Nota Fiscal de Serviço de Telecomunicações, modelo 22 ;  Nota Fiscal/Conta de Energia Elétrica, modelo 6; |
| 8 | Série | 3 | 31 | 33 | X | SERIEDOC | DLAF |  |
| 9 | Número | 9 | 34 | 42 | N | DOCINI | DLAF |  |
| 10 | CFOP | 4 | 43 | 46 | N | CODNAT | DCFOP |  |
| 11 | Nº de ordem do Item | 3 | 47 | 49 | N | NUMITEM | DITEM | Informar o número de ordem do item do documento fiscal. A quantidade máxima de itens por documento fiscal é limitada em 990 (novecentos e noventa), devendo ser iniciada em 001 (um). |
| 12 | Código do item | 10 | 50 | 59 | X | CODIGOPRD | TPRODUTO |  |
| 13 | Descrição do item | 40 | 60 | 99 | X | DESCRICAO | TPRODUTO |  |
| 14 | Código de classificação do item | 4 | 100 | 103 | N | CODFISCAL | TPRDCODFISCAL |  |
| 15 | Unidade | 6 | 104 | 109 | X | CODUND | DITEM |  |
| 16 | Quantidade contratada (com 3 decimais) | 12 | 110 | 121 | N | QTDECONTRATADA | DITEM |  |
| 17 | Quantidade medida (com 3 decimais) | 12 | 122 | 133 | N | QTDEPRD | DITEM |  |
| 18 | Total (com 2 decimais) | 11 | 134 | 144 | N | VALORCONT | DLAF |  |
| 19 | Desconto / Redutores (com 2 decimais) | 11 | 145 | 155 | N | DESCONTOITEM | DITEM |  |
| 20 | Acréscimos e Despesas Acessórias (com 2 decimais) | 11 | 156 | 166 | N | VALORDESPESA | DITEM |  |
| 21 | BC ICMS (com 2 decimais) | 11 | 167 | 177 | N | BASEICMSPRD | DITEM |  |
| 22 | ICMS (com 2 decimais) | 11 | 178 | 188 | N | VLRICMSPRD | DITEM |  |
| 23 | Operações Isentas ou não tributadas (com 2 decimais) | 11 | 189 | 199 | N | ISENTOICMS | DITEM |  |
| 24 | Outros valores (com 2 decimais) | 11 | 200 | 210 | N | OUTROSICMS | DITEM |  |
| 25 | Alíquota do ICMS (com 2 decimais) | 4 | 211 | 214 | N | ALIQICMS | DLAF |  |
| 26 | Situação | 1 | 215 | 215 | X | STATUSLF  DATAEMISSAO | DLAF | “S”, em se tratando de documento fiscal cancelado dentro do mesmo período de apuração;  “R”, em se tratando de documento fiscal emitido em substituição a um documento fiscal cancelado dentro do mesmo período de apuração;  “C”, em se tratando de documento fiscal complementar;  “N”, nos demais casos.  Nas hipóteses de situação “R” ou “C”, deve ser preenchido o campo 34 - “Informações Adicionais” (item 5.2.5.13). |
| 27 | Ano e Mês de referência de apuração | 4 | 216 | 219 | X | DATAEMISSAO | DLAF | Formato “AAMM” |
| 28 | Número do Contrato | 15 | 220 | 234 | X | NUMCONTRATO | DITEM |  |
| 29 | Quantidade faturada (com 3 decimais) | 12 | 235 | 246 | N | QTDEFATURADA | DITEM |  |
| 30 | Tarifa Aplicada / Preço Médio Efetivo (com 6 decimais) | 11 | 247 | 257 | N | VALPRECOTARIFA | DITEM |  |
| 31 | Alíquota PIS/PASEP (com 4 decimais) | 6 | 258 | 263 | N | ALIQTRB | DTRBITEM |  |
| 32 | PIS/PASEP (com 2 decimais) | 11 | 264 | 274 | N | VALORTRB | DTRBITEM |  |
| 33 | Alíquota COFINS (com 4 decimais) | 6 | 275 | 280 | N | ALIQTRB | DTRBITEM |  |
| 34 | COFINS (com 2 decimais) | 11 | 281 | 291 | N | VALORTRB | DTRBITEM |  |
| 35 | Indicador de Desconto Judicial | 1 | 292 | 292 | X | \* | \* | Será gerado em branco. |
| 36 | Tipo de Isenção/Redução de Base de Cálculo | 2 | 293 | 294 | N | TIPOISENREDBASE | DITEM | Em se tratando de Nota Fiscal de Serviço de Comunicação, modelo 21, ou Nota Fiscal de Serviço de Telecomunicação, modelo 22, será preenchido conforme tabela 11.10:  01 - Programa Governo Eletrônico - Serviço de Atendimento ao Cidadão - GESAC (Convênio ICMS 141/07);  02 - Programa Internet Popular (Convênio ICMS 38/09);  03 - Programa Internet destinado à escolas públicas federais, estaduais, distritais e municipais (Convênio ICMS 47/08);  04 - Programa Acesso Individual Classe Especial - AICE (Convênio ICMS 16/12);  05 - Prestação de Serviço de Televisão por Assinatura (Convênio ICMS 57/99);  06 - Prestação de serviço de monitoramento e rastreamento de veículo e carga (Convênio ICMS 139/06);  07 - Prestação de serviço de provimento de acesso à internet (Convênio 78/01);  99 - Outras;  Se não houver isenção ou redução de base de cálculo, será preenchido com zeros. Em se tratando de nota fiscal modelo 6,  preencher com zeros; |
| 37 | Brancos - reservado para uso futuro | 5 | 295 | 299 | X | \* | \* |  |
| 38 | Código de Autenticação Digital do registro | 32 | 300 | 331 | X | \* | \* | Informar o código de autenticação digital obtido por meio da aplicação do algoritmo MD5 (Message Digest 5) de 128 bits na cadeia de caracteres formada pelos campos 01 a 37. |

* Arquivo “Dados Cadastrais do Destinatário do Documento Fiscal”: O arquivo deverá ser composto por registros que contenham as seguintes informações, devendo ser apresentado um registro para cada documento fiscal contido no Arquivo MESTRE DE DOCUMENTO FISCAL, classificados pelo número do documento fiscal, em ordem crescente:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ordem | Campo | Tamanho | Pos. Inicial | Pos. Final | Formato | Campo Origem | Tabela Origem | Observações |
| 1 | CNPJ ou CPF | 14 | 1 | 14 | N | CGCCFO | FCFO |  |
| 2 | IE | 14 | 15 | 28 | X | INSCRESTADUAL | FCFO |  |
| 3 | Razão Social | 35 | 29 | 63 | X | NOME | FCFO |  |
| 4 | Logradouro | 45 | 64 | 108 | X | RUA | FCFO |  |
| 5 | Número | 5 | 109 | 113 | N | NUMERO | FCFO |  |
| 6 | Complemento | 15 | 114 | 128 | X | COMPLEMENTO | FCFO |  |
| 7 | CEP | 8 | 129 | 136 | N | CEP | FCFO |  |
| 8 | Bairro | 15 | 137 | 151 | X | BAIRRO | FCFO |  |
| 9 | Município | 30 | 152 | 181 | X | CIDADE | FCFO | Caso o Fornecedor seja do Exterior, será gerado "Exterior". |
| 10 | UF | 2 | 182 | 183 | X | CODETD | FCFO | Caso o Fornecedor seja do Exterior, será gerado "EX". |
| 11 | Telefone de contato | 12 | 184 | 195 | X | TELEFONE | FCFO |  |
| 12 | Código de identificação do consumidor ou assinante | 12 | 196 | 207 | X | CODCFO | DLAF |  |
| 13 | Número do terminal telefônico ou da unidade consumidora | 12 | 208 | 219 | X | CONTACONSUMO | DLAF |  |
| 14 | UF de habilitação do terminal telefônico | 2 | 220 | 221 | X | CODETD | FCFO | Caso o Fornecedor seja do Exterior, será gerado "EX". |
| 15 | Data de emissão | 8 | 222 | 229 | N | DATAEMISSAO | DLAF |  |
| 16 | Modelo | 2 | 230 | 231 | N | CODMODDOC | DLAF | Nota Fiscal de Serviço de Comunicação, modelo 21; Nota Fiscal de Serviço de Telecomunicações, modelo 22 ;  Nota Fiscal/Conta de Energia Elétrica, modelo 6; |
| 17 | Série | 3 | 232 | 234 | X | SERIEDOC | DLAF |  |
| 18 | Número | 9 | 235 | 243 | N | DOCINI | DLAF |  |
| 19 | Código do Município | 7 | 244 | 250 | N | CODIGO | DCODIFICACAOMUNICIPIO | Código do município da tabela do IBGE. |
| 20 | Brancos - reservado para uso futuro | 5 | 251 | 255 | X | \* | \* |  |
| 21 | Código de Autenticação Digital do registro | 32 | 256 | 287 | X | \* | \* | Informar o código de autenticação digital obtido por meio da aplicação do algoritmo MD5 (Message Digest 5) de 128 bits na cadeia de caracteres formada pelos campos 01 a 20. |

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
