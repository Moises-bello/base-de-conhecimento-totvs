---
content_hash: 1e8f9f8d3c0a34c08a7986ab43dc34ada56e60b9f271b12257068812729d401d
fetched_at: '2026-06-29T00:09:20.165071+00:00'
page_id: '422545674'
product: rm
source: tdn-rm
title: DMS - Jaboatão dos Guararapes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545674
version: 8
---

A geração da DMS de Jaboatão dos Guararapes-PE é executada a partir do menu Obrigações Acessórias | agrupador Rotinas Fiscais | Municipais. Na tela de geração da rotina, informe os seguintes dados:

* O código da Filial, que deverá estar devidamente configurada para o município de Jaboatão dos Guararapes;
* O Tipo de Lançamento, sendo as opções entrada, saída ou ambos;
* Diretório local onde será gravado o arquivo XML referente aos dados gerados da rotina;
* Data de Emissão Inicial e Data de Emissão Final;
* Número Inicial e Número Final;
* Tipo do Serviço;
* Caso o usuário deseje gerar os dados somente dos lançamentos que não foram gerados, basta selecionar a opção "Exportar somente movimentos não exportados anteriormente."

***Observação***: O arquivo será gerado em formato XML para depois serem importados no site da Prefeitura.

**Seleção de Lançamentos**

Serão selecionadas as notas fiscais de entrada e saída respeitando as parametrizações do processo e que contenham o tributo do ISS no lançamento ou nos itens que pertencem o lançamento selecionado. Se não houver lançamentos fiscais carregados não haverá geração do arquivo DMS XML.  
Caso o Tipo do Serviço selecionado na rotina seja igual "Empresas que apenas tem obrigação de Substituição Tributária", não serão carregadas as Notas Fiscais de Saída afetando diretamente da não geração do Tipo de Registro Documentos Emitidos. A seleção dos demais tipos de serviço não afetam a geração da rotina.

**Preenchimento dos Campos**

Segue relação dos tipos de registros gerados na rotina:  
  
**Layout para o Tipo de Registro****Header**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Formato** | **Obrigatório** | **Tamanho** | **Tabela Campo** | **Observação** |
| heInsc | Inscrição Mercantil do Contribuinte | Numérico | S | 7 | GFILIAL.INSCMUN |  |
| heComp | Competência | Numérico | S | 6 | Rotina.DataEmissaoInicial |  |
| heGeDt | Data da Geração do Arquivo | N | S | 8 |  | Data Atual |
| heGeHo | Hora da Geração do Arquivo | N | S | 6 |  | Hora Atual |
| heVers | Versão da DMS | N | S | 4 |  | Campo Fixo '2000' |
| hePref | Código de Identificação do Município | N | S | 4 |  | Campo Fixo 'JABO' |

**Layout para o Tipo de Registro** **Tomador/Prestador**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Formato** | **Obrigatório** | **Tamanho** | **Tabela Campo** | **Observação** |
| tpCod | Código do Tomador/Prestador | N | S | Auto Numerado |  | Campo sequencial conforme inclusão de Cliente/Fornecedor |
| tpNome | Nome ou Razão Social | A | S | 105 | FCFO.NOME |  |
| tpDocu | CPF/CNPJ | N | S | 14 | FCFO.CGCCFO | Este campo não será preenchido quando o Cliente fornecedor seja do exterior. |
| tpInMu | Inscrição Municipal | N | N | 7 | FCFO.INSCRMUNICIPAL |  |
| tpPass | Número do Passaporte | A | N | 20 | FCFO.CGCCFO | Caso o cliente fornecedor seja do exterior o numero do passaporte deverá ser preenchido no campo FCFO.CGCCFO do cadastro de cliente Fornecedor. Este campo será preenchido somente para Cliente fornecedor do exterior. |
| tpRgNu | Número do RG | N | N | 15 |  | Não Preenchido |
| tpRgOr | Órgão Expedidor | A | N | 6 |  | Não Preenchido |
| tpRgEs | Estado de Expedição | A | N | 2 |  | Não Preenchido |
| tpCep | CEP | A | S | 9 | FCFO.CEP |  |
| tpLogr | Nome do Logradouro | A | S | 105 | FCFO.RUA |  |
| tpNume | Número | A | S | 6 | FCFO.NUMERO |  |
| tpComp | Complemento | A | N | 45 | FCFO.COMPLEMENTO |  |
| tpBair | Bairro | A | S | 45 | FCFO.BAIRRO |  |
| tpMuni | Município | A | S | 45 | DVIEWMUNICIPIOS.NOMEMUNICIPIO |  |
| tpEsta | Estado | A | S | 2 | FCFO.CODETD |  |
| tpPais | Código do País | N | N | 3 | DPAIS.CODPAIS | Não será preenchido para cliente fornecedor do exterior |
| tpMail | E-mail | A | N | 60 | FCFO.EMAIL |  |
| tpTReD | Telefone Residencial - DDD | N | N | 2 | FCFO.TELEFONE | Será preenchido caso pessoa física |
| tpTReN | Telefone Residencial - Número | N | N | 8 | FCFO.TELEFONE | Será preenchido caso pessoa física |
| tpTCeD | Telefone Celular - DDD | N | N | 2 |  | Não Preenchido |
| tpTCeN | Telefone Celular - Número | N | N | 8 |  | Não Preenchido |
| tpTCoD | Telefone Comercial - DDD | N | N | 2 | FCFO.TELEFONE | Será preenchido caso pessoa jurídica |
| tpTCoN | Telefone Comercial - Número | N | N | 8 | FCFO.TELEFONE | Será preenchido caso pessoa jurídica |
| tpTFaD | Fax - DDD | N | N | 2 | FCFO.FAX |  |
| tpTFaN | Fax - Número | N | N | 8 | FCFO.FAX |  |
| tpNFan | Nome Fantasia | A | N | 105 |  | Não Preenchido |
| tpInEs | Inscrição Estadual | N | N | 20 | FCFO.INSCRESTADUAL |  |
| tpInEs | Natureza Jurídica | N | N | 2 |  | Não Preenchido |

**Layout para o Tipo de Registro** **Base Legal** 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Formato** | **Obrigatório** | **Tamanho** | **Tabela Campo** | **Observação** |
| blCod | Código da Base Legal | N | S | Sequencial |  |  |
| blTip | Tipo de Base Legal | A | S | 1 |  | Deve ser um dos abaixo:  C - Lei Complementar  CON - Convênio  CTM - C.T.M.  D - Decreto  I - Instrução Normativa  INF - Informativo  L - Liminar  O - Lei Ordinária  P - Portaria  R - Resolução |
| blNum | Número | N | S | 6 |  |  |
| blAno | Ano | N | S | 4 |  |  |
| blArt | Artigo | N | N | 4 |  |  |
| blInc | Inciso | A | N | 5 |  |  |
| blPar | Parágrafo | N | N | 5 |  |  |
| blAli | Alínea | A | N | 1 |  |  |
| blDes | Descrição | A | N | 105 |  |  |

O produto TOTVS Gestão Fiscal não possui aderência para o registro Base Legal.  
Para inclusão do registro Base Legal será utilizado às informações do histórico do lançamento fiscal, o histórico deve ser preenchido da seguinte forma para que o registro seja gerado corretamente:  
Tipo de Base Legal (Obrigatório) - Número (Obrigatório) - Ano (Obrigatório) - Descrição (Opcional), exemplo: C - 000001 - 2013 – Lei XPTO do município de Jaboatão dos Guararapes  
 ***Observação***: Está forma de gerar a base legal segue o mesmo padrão da DMS de Jaboatão dos Guararapes TXT, é necessário que o tipo de recolhimento do lançamento seja retido.  
   
**Layout para o Tipo de Registro** **Documentos Emitidos** 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Formato** | **Obrigatório** | **Tamanho** | **Tabela Campo** | **Observação** |
| deCod | Código do Documento Emitido | N | S |  |  | DLAF.IDLAF |
| deToma | Tomador do Serviço | N | S | 5 |  | Cliente/Fornecedor vinculado ao lançamento fiscal |
| deTpDo | Tipo de Documento | A | S | 1 |  | DMODELOISS.MODELOISS |
| deSub | Sub-Série | A | N | 3 |  | DLAF.SUBSERIE |
| deNume | Número | N | S | 10 |  | DLAF.DOCINI |
| deSitu | Situação | N | S | 1 |  | E - Emitido, C - Cancelado |
| deData | Data | N | S | 8 | DLAF.DATAEMISSAO ou DLAF.DATACANCELAMENTO |  |
| deMoCa | Motivo do Cancelamento | A | N | 1 | DLAF.MOTIVOCANCELAMENTO | Deve ser um dos abaixo:     D - Desistência Cliente  E - Erro preenchimento  L - Lacuna  O - Outros  R - Rasura  V - Validade Vencida  Será considerado o primeiro caractere da descrição do motivo de cancelamento. |
| deCSer | Serviço Prestado | N | S | 5 | DLAF.CODIGOSERVICO |  |
| deVSer | Valor do Serviço | N | S | 11 | DLAF.VALORCONT |  |
| deReti | Indicação de Retenção | A | S | 1 |  | 'S' para Retido ou 'N' para Não Retido.  Se Tributo ISS e Tipo de Recolhimento seja Retido na Fonte ou Retido na fonte deduzido  Retorna 'S'  Senão  Retorna 'N' |
| deBasC | Base de Cálculo | N | S | 11 |  | Totaliza a Base de Calculo do Tributo ISS |
| deAliq | Alíquota | N | S | 4 |  | Recupera a alíquota utilizada |
| deVIss | Valor do ISS | N | S | 11 |  | Totaliza o Valor do ISS do Tributo ISS |
| deBaLe | Base Legal | N | N | 5 | Código sequencial da Base Legal gerada | Para inclusão da base legal será utilizado às regras abaixo:  O campo deReti dever estar preenchido com 'S'.   O campo deVSer deve ter o valor maior que o campo deBasC  O Histórico do Lançamento fiscal deve estar preenchido conforme informado no registro Base Legal |

***Observação***: Quando a situação for 'Cancelado', o campo 'deMoCa' é obrigatório  os campos 'deToma', 'deCSer', 'deVSer', 'deReti', 'deBasC', 'deAliq', 'deVIss' e 'deBaLe' não são preenchidos.  
   
**Layout para o Tipo de Registro** **Documentos Recebidos**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Formato** | **Obrigatório** | **Tamanho** | **Tabela Campo** | **Observação** |
| drCod | Código do Documento Recebido | N | S | Sequencial |  | DLAF.IDLAF |
| drPres | Prestador do Serviço | N | S | 5 |  | Cliente/Fornecedor vinculado ao lançamento fiscal |
| drTpDo | Tipo de Documento | A | S | 1 | DMODELOISS.MODELOISS |  |
| drSeri | Série | A | N | 2 | DLAF.SERIEDOC |  |
| drSub | Sub-Série | A | N | 3 | DLAF.SUBSERIE |  |
| drNume | Número | N | S | 14 | DLAF.DOCINI |  |
| drData | Data | N | S | 8 | DLAF.DATAEMISSAO |  |
| drCSer | Serviço Tomado | N | S | 5 | DLAF.CODIGOSERVICO |  |
| drVSer | Valor do Serviço | N | S | 11 | DLAF.VALORCONT |  |
| drReti | Indicação de Retenção | A | S | 1 |  | 'S' para Retido ou 'N' para Não Retido.  Se Tributo ISS e Tipo de Recolhimento seja Retido na Fonte ou Retido na fonte deduzido  Retorna 'S'  Senão  Retorna 'N' |
| drBasC | Base de Cálculo | N | S | 11 |  | Totaliza a Base de Calculo do Tributo ISS |
| drAliq | Alíquota | N | S | 4 |  | Recupera a alíquota utilizada no tributo ISS |
| drVIss | Valor do ISS | N | S | 11 |  | Totaliza o Valor do ISS do Tributo ISS |
| drBaLe | Base Legal | N | N | 5 | Código sequencial da Base Legal gerada | Para inclusão da base legal será utilizado às regras abaixo:  O campo deReti dever estar preenchido com 'S'.   O campo deVSer deve ter o valor maior que o campo deBasC  O Histórico do Lançamento fiscal deve estar preenchido conforme informado no registro Base Legal |
| drLoEs | Código do estado | N | S | 2 | DLAF.UFMUNICIPIOSERV | Código do estado de acordo com o [cadastro do IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php). |

**Layout para o Tipo de Registro** **Trailler**  
O registro tipo Trailler tem a finalidade de totalizar todos os registros informados que estão presentes no arquivo DMS-XML de Jaboatão dos Guararapes.
