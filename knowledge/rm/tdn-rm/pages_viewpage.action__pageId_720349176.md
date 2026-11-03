---
content_hash: 779591ddadca2fde524613d03ed4e3e6e7e0f3ffe79beff6950a77969453712e
fetched_at: '2026-06-29T00:11:26.812999+00:00'
page_id: '720349176'
product: rm
source: tdn-rm
title: TOTVS Gestão Construção de Imóveis - API Cadastro de Cliente / Propostas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=720349176
version: 7
---

Criada uma API para ser utilizada no Portal de Imóveis ( Clientes ).

**Buscando cliente pelo CPF ou Nome.**

Criando os dados na tabelas de FCFO, XCLIENTEPESSOAFISICA e XPESSOACONJUGE,  se for informado o CPF, Caso contrário fica somente na tabela XPVICLIENTE.

CADASTROS DAS APISAPI Genérica para Consultar as Novas Tabelas do PI no RM |

Para consultar os dados das novas Tabelas do Portal Imóveis que foram criadas diretamente no banco do RM, utilize como base a API abaixo, substituindo o termo ***{nomedatabela**}*** pelo nome da tabela desejada.

[http://localhost:8051/api/imb/v1/registrations/{nomedatabela}](http://localhost:8051/api/imb/v1/registrations/%7Bnomedatabela%7D "Follow link")

Esta API só pode ser utilizada com verbo do tipo ***get***.

Exemplos de uso desta API:

Consultando as informações da Tabela XPIMIDIA, na qual estão as informações sobre as Mídias utilizadas para gerar as Propostas no PI (Portal de Imóveis):

<http://localhost:8051/api/imb/v1/registrations/XPIMIDIA>

Outras Tabelas disponíveis até o momento de edição deste documento são:

* XPIESTADOCIVIL - Que controla o cadastro dos Estados Civis das Pessoas no PI; e
* XPIPROFISSAO - Que controla o cadastro das Profissões das Pessoas no PI.
POST - Cadastro de Cliente |

<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData>

Neste exempo , via Postman estou cadastrando um Novo Cliente com os seguintes dados:

**Nome :** CLIENTE NOVO ASTONI

**Razão Social :** CLIENTE NOVO ASTONI

**CPF :** 044.266.846-50

**Pai:** PAI ASTONI

**Mãe :** MAE ASTONI

**Conjuge :** ESPOSA ASTONI

Cadastro realizado e é retornado o Código ID do Cliente com seu ID ERP ( CODCFO )

Cadastros realizados na base de dados RM

Observação:

Caso tente adiconar um cliente na qual já exista um com CPF já cadastro no sistema , é feita a validação da API retornando a mensagem que já existe cadastro para o CPF na base de dados.

DEL - Deletando registro de Cliente |

[http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/](http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/33){Número do ID que deseja excluir}

Cliente foi gerado com ID = 35 e neste exemplo , informo o Código 35 do ID que desejo excluir.

GET - Consulta Cadastro de Cliente com ou Sem Filtro |

<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData?filter=> ["nome like :nome and CPFCNPJ = :cpf", "%ASTONI%", "044.266.846-50"]

Neste exemplo é feita a consulta com Filtro , e esse exemplo é para buscar clientes com CPF acima e nome.

Neste exemplo é informado o Cliente conforme Filtro desejado, somente o CPF informado e que tenha ASTONI em seu nome.

<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData>

Neste caso a pesquisa não utiliza filtro.

Neste que não possui Filtros , informa a quantidade de Registros = 2 ( 2 Clientes ) com seus dados.

PUT e PATCH - Alterando dados do Cliente |

<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/34>

<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/34>

Ambas APIS alteram dados de Cliente

Não se esquecendo de informar o número do ID que deseja alterar e os campso que serão feitas as alterações.

Alterando neste exemplo os campos:

* Nome
* Razão Social
* Pai
* Mãe
* Nome da Esposa ( Conjuge )

Dados alterados no RM

**ALTERANDO COM PATCH**

Novamente informar o ID do Cliente que deseja alterar o cadastro e seus dados.

Alterando neste exemplo os campos:

* Nome
* Pai
* Mãe
* Nome da Esposa ( Conjuge )

Campos PVI com RM |

# **RM**                                                             **PVI**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Column\_name | Type | Nullable | Length | Coluna | tipo | Nullable | Length | Tabela | Id\_erp |
| CODCOLIGADA | DCODCOLIGADA | no | 2 | id\_erp | varchar | yes | 255 |  |  |
| CODCFO | varchar | no | 25 | id\_erp | varchar | yes | 255 |  |  |
| NOMEFANTASIA | varchar | yes | 100 | razaosocial | varchar | yes | 100 |  |  |
| NOME | varchar | yes | 100 | nome | varchar | yes | 100 |  |  |
| CGCCFO | varchar | yes | 20 | cpfcnpj | varchar | yes | 14 |  |  |
| INSCRESTADUAL | varchar | yes | 20 | inscricaoestadual | varchar | yes | 15 |  |  |
| PAGREC | smallint | no | 2 |  |  |  |  |  |  |
| RUA | varchar | yes | 100 | logradouro | varchar | yes | 100 |  |  |
| NUMERO | varchar | yes | 8 | numero | varchar | yes | 10 |  |  |
| COMPLEMENTO | DCOMPLEMENTO | yes | 60 | complemento | varchar | yes | 50 |  |  |
| BAIRRO | DBAIRRO | yes | 80 | bairro | varchar | yes | 50 |  |  |
| CIDADE | DCIDADE | yes | 32 | cidade | varchar | yes | 50 |  |  |
| CODETD | varchar | yes | 2 | uf | varchar | yes | 2 |  |  |
| CEP | DCEP | yes | 9 | cep | varchar | yes | 8 |  |  |
| TELEFONE | varchar | yes | 15 | telefone | varchar | yes | 15 |  |  |
| RUAPGTO | varchar | yes | 100 | logradourocobranca | varchar | yes | 100 |  |  |
| NUMEROPGTO | varchar | yes | 8 | numerocobranca | varchar | yes | 10 |  |  |
| COMPLEMENTOPGTO | DCOMPLEMENTO | yes | 60 | complementocobranca | varchar | yes | 50 |  |  |
| BAIRROPGTO | DBAIRRO | yes | 80 | bairrocobranca | varchar | yes | 50 |  |  |
| CIDADEPGTO | DCIDADE | yes | 32 | cidadecobranca | varchar | yes | 50 |  |  |
| CODETDPGTO | varchar | yes | 2 | ufcobranca | varchar | yes | 2 |  |  |
| CEPPGTO | DCEP | yes | 9 | cepcobranca | varchar | yes | 8 |  |  |
| FAX | varchar | yes | 15 | fax | varchar | yes | 15 |  |  |
| TELEX | varchar | yes | 15 | celular | varchar | yes | 15 |  |  |
| EMAIL | varchar | yes | 60 | email | varchar | yes | 50 |  |  |
| INSCRMUNICIPAL | varchar | yes | 20 | inscricaomunicipal | varchar | yes | 15 |  |  |
| ESTADOCIVIL | varchar | yes | 1 | estadocivil\_id | int | yes | 4 | estadocivil | sim |
| DTNASCIMENTO | datetime | yes | 8 | datanascimento | datetime | yes | 8 |  |  |
| RECCREATEDBY | varchar | yes | 50 | usuariocriacao\_id | int | yes | 4 | usuario | não |
| RECCREATEDON | datetime | yes | 8 | datahoracadastro | datetime | yes | 8 |  | não |
| RECMODIFIEDON | datetime | yes | 8 | data\_ultima\_interacao | date | yes | 3 | 10 |  |
| COD\_SEXO | char | yes | 1 | sexo | smallint | yes | 2 |  |  |
| CODETDMUNICIPIO | varchar | yes | 2 | naturalidade | varchar | yes | 50 |  |  |
| NAT\_CFO | varchar | yes | 30 | nacionalidade | varchar | yes | 50 |  |  |
| NOM\_PAI | varchar | yes | 45 | pai | varchar | yes | 50 |  |  |
| NOM\_MAE | varchar | yes | 45 | mae | varchar | yes | 50 |  |  |
| EMPR\_RENDA | RMDVALOR4 | yes | 15,4 | renda | decimal | yes | 9 |  |  |
| EMPR\_NOME | varchar | yes | 100 | empresa\_nome | varchar | yes | 100 |  |  |
| EMPR\_ENDERECO | varchar | yes | 30 | empresa\_logradouro | varchar | yes | 100 |  |  |
| EMPR\_NUMERO | varchar | yes | 8 | empresa\_numero | varchar | yes | 10 |  |  |
| EMPR\_COMPL | varchar | yes | 20 | empresa\_complemento | varchar | yes | 30 |  |  |
| EMPR\_BAIRRO | varchar | yes | 30 | empresa\_bairro | varchar | yes | 50 |  |  |
| EMPR\_CIDADE | varchar | yes | 30 | empresa\_cidade | varchar | yes | 50 |  |  |
| EMPR\_UF | varchar | yes | 2 | empresa\_uf | varchar | yes | 2 |  |  |
| EMPR\_CEP | varchar | yes | 9 | empresa\_cep | varchar | yes | 8 |  |  |
| EMPR\_TEL\_COM | varchar | yes | 15 | empresa\_telefone | varchar | yes | 15 |  |  |
| EMPR\_RAMAL | varchar | yes | 8 | empresa\_ramal | varchar | yes | 10 |  |  |
| EMPR\_FAX | varchar | yes | 15 | empresa\_fax | varchar | yes | 15 |  |  |
| EMPR\_DATA\_ADM | datetime | yes | 8 | empresa\_dataadmissao | datetime | yes | 8 |  |  |
| EMPR\_CARGO | varchar | yes | 25 | empresa\_cargo | varchar | yes | 50 |  |  |
| CODPROF | varchar | no | 3 | conjuge\_profissao\_id | int | yes | 4 |  |  |
| NOME | varchar | yes | 250 | conjuge\_nome | varchar | yes | 100 |  |  |
|  |  |  |  | conjuge\_email | varchar | yes | 50 |  |  |
| DATNASC | datetime | yes | 8 | conjuge\_datanascimento | datetime | yes | 8 |  |  |
| CPF | varchar | yes | 20 | conjuge\_cpf | varchar | yes | 11 |  |  |
| CI | varchar | yes | 20 | conjuge\_rgnumero | varchar | yes | 50 |  |  |
| ORGEMISCI | varchar | yes | 8 | conjuge\_rgorgao | varchar | yes | 20 |  |  |
| ORGEMISCI | varchar | yes | 8 | conjuge\_rguf | varchar | yes | 2 |  |  |
|  |  |  |  | conjuge\_sexo | varchar | yes | 1 |  |  |
| NOMPAI | varchar | yes | 45 | conjuge\_pai | varchar | yes | 100 |  |  |
| NOMEMAE | varchar | yes | 45 | conjuge\_mae | varchar | yes | 100 |  |  |
| TELEFONE | varchar | yes | 15 | conjuge\_telefone | varchar | yes | 15 |  |  |
| CELULAR | varchar | yes | 15 | conjuge\_celular | varchar | yes | 15 |  |  |
|  |  |  |  | conjuge\_naturalidade | varchar | yes | 50 |  |  |
| NAT\_PESS | varchar | yes | 30 | conjuge\_nacionalidade | varchar | yes | 50 |  |  |
|  |  |  |  | conjuge\_cartoriofirma | varchar | yes | 50 |  |  |
|  |  |  |  | conjuge\_renda | decimal | yes | 9 |  |  |
| LOCALTRAB | varchar | yes | 40 | conjuge\_empresa\_nome | varchar | yes | 100 |  |  |
|  |  |  |  | conjuge\_empresa\_cargo | varchar | yes | 50 |  |  |
|  |  |  |  | conjuge\_empresa\_dataadmissao | datetime | yes | 8 |  |  |
| TELCOMER | varchar | yes | 15 | conjuge\_empresa\_telefone | varchar | yes | 15 |  |  |
| LOGRADOURO | varchar | yes | 45 | conjuge\_empresa\_logradouro | varchar | yes | 100 |  |  |
| NUMEROEND | varchar | yes | 6 | conjuge\_empresa\_numero | varchar | yes | 10 |  |  |
| COMPLEMENTOEND | varchar | yes | 15 | conjuge\_empresa\_complemento | varchar | yes | 50 |  |  |
| BAIRRO | varchar | yes | 25 | conjuge\_empresa\_bairro | varchar | yes | 50 |  |  |
| CIDADE | varchar | yes | 30 | conjuge\_empresa\_cidade | varchar | yes | 50 |  |  |
| UF | varchar | yes | 2 | conjuge\_empresa\_uf | varchar | yes | 2 |  |  |
| CEP | varchar | yes | 8 | conjuge\_empresa\_cep | varchar | yes | 8 |  |  |
| DATACASAMENTO | datetime | yes | 8 | datacasamento | datetime2 | yes | 8 |  |  |

Incluir Proposta |

**API para inclusão de Proposta :** <http://localhost:8051/api/imb/v1/sales/proposals>

Exemplo da API para inclusão de Proposta:

{  
    "codcoligada": 1,              
    "statuspvi": 1,  
    "codempreendimento": 100,         
    "codunidade": "01",      
    "codsubunidade": "000502",              
    "idcorretorpvi": 1,      
    "idclienteprincipalpvi": 17,  
    "idclientespvi": [  
                17,  
                18  
                 ]

}

Idclientepvi : ( 17 e 18 ) estão cadastrados.

IDclientePrincipal = 17 ( ADRIANO ASTONI FERREIRA 01 )

Proposta 61 incluída na Base de Dados RM.

Proposta com os Dois compradores inserida e a SubUnidade .

Consultar Propostas |

**API para consultar Propostas :** <http://localhost:8051/api/imb/v1/sales/proposals>

Alterando dados API Proposta |

**API Alterando Proposta PUT** : <http://localhost:8051/api/imb/v1/sales/proposals/1_61>    ( 1\_61  = Coligada e número da Proposta que deseja alterar os dados )

Neste exemplo estou alterando o Comprador principal 17 para 18.

Foi alterado para o Adriano Astoni Ferreira 02 o Comprador Principal.

**API Alterando Proposta PATCH :**<http://localhost:8051/api/imb/v1/sales/proposals/1_61>

Mesmo critério de PUT - Inserindo a coligada e numero da Proposta.

{  
    "codcoligada": 1,          
    "idpropostavenda": 61,      
    "statuspvi": 1,  
   "codempreendimento": 100,         
    "codunidade": "01",      
    "codsubunidade": "000502",              
    "idcorretorpvi": 1,      
    "idclienteprincipalpvi": 18,  
    "idclientespvi": [  
                18  
                  
                 ]

}

**Excluíndo o ID 17** da Proposta.

Comprador ID 17 Excluído.

API para Deletar Proposta |

**API para Deletar Proposta** : <http://localhost:8051/api/imb/v1/sales/proposals/1_61>

Inserir o número da Proposta que deseja excluir via API .

Proposta excluída da Base de Dados RM.
