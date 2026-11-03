---
content_hash: 47e77a4d0e5f79d6722e9a8856ed578d236e1d9e650fbe4f7ad2d574a5af6f49
fetched_at: '2026-06-29T00:10:39.207278+00:00'
page_id: '546245237'
product: rm
source: tdn-rm
title: LGPD no TOTVS Backoffice (Linha RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546245237
version: 19
---

Esta documentação tem como objetivo informar o conteúdo disponibilizado pelo TOTVS Backoffice (Linha RM). Trata-se do mapeamento mínimo e sugestivo de campos pessoais e sensíveis relativos ao Backoffice. O cliente deverá revisar a configuração, acrescentando ou alterando dados, inclusive  as classificações que foram liberadas pela TOTVS, conforme orientação de sua área jurídica.

Mais informações de como fazer: <https://tdn.totvs.com/pages/releaseview.action?pageId=527375989>

**Campos mapeados**

Os campos mapeados acima são utilizados em diversas rotinas do TOTVS Backoffice (Linha RM) as quais listamos abaixo.

Gestão ContábilDados do Auditor vinculado à escrituração da ECD - Escrituração Contábil Digital (SPED Contábil)

<https://tdn.totvs.com/display/LRM/Auditores+Independentes>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CAUDITOR | NOME | Não |
| CAUDITOR | CPFCNPJ | Não |
| CAUDITOR | CODCVMAUDITOR | Não |

Dados dos Signatários vinculados à escrituração da ECD - Escrituração Contábil Digital (SPED Contábil)

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938723>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CSIGNATARIO | NOME | Não |
| CSIGNATARIO | CPF | Não |
| CSIGNATARIO | INSCCRC | Não |
| CSIGNATARIO | EMAIL | Não |
| CSIGNATARIO | FONE | Não |
| CSIGNATARIO | ANOCRC | Não |
| CSIGNATARIO | UFCRC | Não |
| CSIGNATARIO | NUMSEQCRC | Não |
| CSIGNATARIO | DTCRC | Não |

Dados das contas contábeis

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938354>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CCONTA | DESCRICAO | Não |

Dados das contas gerenciais

<https://tdn.totvs.com/display/LRM/Plano+Contas+Gerencial>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CGERENCIA | DESCRICAO | Não |

Contas contábeis do plano anterior do SPED

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938671>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CCTAANTERIORSPED | DESCRICAOCONTAANT | Não |

Informações das partidas contábeis (lançamento contábil)

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938436>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CPARTIDA | Complemento | Não |

Informações de Histórico de contas contábeis

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938477>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CCONTAHISTORICO | DESCRICAO | Não |

Informações de Histórico de contas gerenciais

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938479>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CGERENCIAHIST | Descrição | Não |

Gestão Estoque/Compras/FaturamentoDados do Emissor de Docs Anteriores Cte

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938183>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TCTEEMISSOR | CNPJCPF | Não |
| TCTEEMISSOR | CODETD | Não |
| TCTEEMISSOR | INSCRESTADUAL | Não |
| TCTEEMISSOR | NOME | Não |

Dados de Motorista do Cte

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938183>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TCTEMOTORISTA | CPF | Não |
| TCTEMOTORISTA | NOME | Não |

Cupom Fiscal

<https://tdn.totvs.com/display/LRM/Cupom+Fiscal>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TCUPOMFISCAL | NOMEADQUIRENTE | Não |

Pagamentos do Cupom Fiscal

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TCUPOMFISCALFIN | NOMEEMITENTE | Não |
| TCUPOMFISCALFIN | TELEMITENTE | Não |

Fabricantes

<https://tdn.totvs.com/display/LRM/Fabricantes>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TFAB | BAIRRO | Não |
| TFAB | CEP | Não |
| TFAB | CGC | Não |
| TFAB | CIDADE | Não |
| TFAB | CODETD | Não |
| TFAB | COMPLEMENTO | Não |
| TFAB | CONTATO | Não |
| TFAB | FAX | Não |
| TFAB | INSCRESTADUAL | Não |
| TFAB | NOME | Não |
| TFAB | NUMERO | Não |
| TFAB | PAIS | Não |
| TFAB | RUA | Não |
| TFAB | TELEFONE | Não |
| TFAB | TELEX | Não |

Dados do Cheque

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TFCHEQUE | CNPJCPF | Não |
| TFCHEQUE | NOMEEMITENTE | Não |
| TFCHEQUE | TELEMITENTE | Não |

Log de Caixa

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TFLOGCAIXA | CNPJCPF | Não |
| TFLOGCAIXA | NOMEEMITENTE | Não |
| TFLOGCAIXA | TELEMITENTE | Não |

Movimentos

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938113>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TMOV | CNPJCPFADQUIRENTE | Não |
| TMOV | NOMEADQUIRENTE | Não |

Histórico de Cliente/Fornecedor x Movimento

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938113>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TMOVCFO | BAIRRO | Não |
| TMOVCFO | CEP | Não |
| TMOVCFO | CIDADE | Não |
| TMOVCFO | CNPJCPF | Não |
| TMOVCFO | CODETD | Não |
| TMOVCFO | CODMUNICIPIO | Não |
| TMOVCFO | COMPLEMENTO | Não |
| TMOVCFO | CONTATO | Não |
| TMOVCFO | EMAIL | Não |
| TMOVCFO | ENDERECO | Não |
| TMOVCFO | FAX | Não |
| TMOVCFO | INSCRICAOESTADUAL | Não |
| TMOVCFO | INSCRICAOMUNICIPAL | Não |
| TMOVCFO | NOME | Não |
| TMOVCFO | NOMEFANTASIA | Não |
| TMOVCFO | NUMERO | Não |
| TMOVCFO | PAIS | Não |
| TMOVCFO | TELEFONE | Não |

Dados de Transporte

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938113>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TMOVTRANSP | BAIRROCOLETA | Não |
| TMOVTRANSP | BAIRROENTREGA | Não |
| TMOVTRANSP | CEPCOLETA | Não |
| TMOVTRANSP | CEPENTREGA | Não |
| TMOVTRANSP | CNPJCPFCOLETA | Não |
| TMOVTRANSP | CNPJCPFENTREGA | Não |
| TMOVTRANSP | CODETDCOLETA | Não |
| TMOVTRANSP | CODETDENTREGA | Não |
| TMOVTRANSP | CODMUNICIPIOCOLETA | Não |
| TMOVTRANSP | CODMUNICIPIOENTREGA | Não |
| TMOVTRANSP | CODPAISCOLETA | Não |
| TMOVTRANSP | CODPAISENTREGA | Não |
| TMOVTRANSP | COMPLCOLETA | Não |
| TMOVTRANSP | COMPLENTREGA | Não |
| TMOVTRANSP | EMAILCOLETA | Não |
| TMOVTRANSP | EMAILENTREGA | Não |
| TMOVTRANSP | MUNICIPIOCOLETA | Não |
| TMOVTRANSP | MUNICIPIOENTREGA | Não |
| TMOVTRANSP | NOMECOLETA | Não |
| TMOVTRANSP | NOMEENTREGA | Não |
| TMOVTRANSP | RUACOLETA | Não |
| TMOVTRANSP | RUAENTREGA | Não |
| TMOVTRANSP | TELEFONECOLETA | Não |
| TMOVTRANSP | TELEFONEENTREGA | Não |

Lançamentos do Movimento

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TPAGTO | CNPJCPF | Não |
| TPAGTO | NOMEEMITENTE | Não |
| TPAGTO | TELEMITENTE | Não |

Relatório de comissões

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TRELCOM | NOMECLIENTE | Não |

Representantes

<https://tdn.totvs.com/display/LRM/Representantes>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TRPR | BAIRRO | Não |
| TRPR | BAIRROPGTO | Não |
| TRPR | CELULAR | Não |
| TRPR | CEP | Não |
| TRPR | CEPPGTO | Não |
| TRPR | CGC | Não |
| TRPR | CIDADE | Não |
| TRPR | CIDADEPGTO | Não |
| TRPR | CODETD | Não |
| TRPR | CODETDPGTO | Não |
| TRPR | COMPLEMENTO | Não |
| TRPR | COMPLEMENTOPGTO | Não |
| TRPR | CONTATO | Não |
| TRPR | EMAIL | Não |
| TRPR | FAX | Não |
| TRPR | HOMEPAGE | Não |
| TRPR | NOME | Não |
| TRPR | NOMEFANTASIA | Não |
| TRPR | NUMERO | Não |
| TRPR | PAIS | Não |
| TRPR | RUA | Não |
| TRPR | RUAPGTO | Não |
| TRPR | TELEFONE | Não |

Vendedores

<https://tdn.totvs.com/pages/viewpage.action?pageId=423938162>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| TVEN | NOME | Não |

Gestão FinanceiraCliente/Fornecedor

<https://tdn.totvs.com/pages/viewpage.action?pageId=421388786>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FCFO | NOME | Não |
| FCFO | NOMEFANTASIA | Não |
| FCFO | CGCCFO | Não |
| FCFO | INSCRESTADUAL | Não |
| FCFO | RUA | Não |
| FCFO | NUMERO | Não |
| FCFO | COMPLEMENTO | Não |
| FCFO | TELEFONE | Não |
| FCFO | RUAPGTO | Não |
| FCFO | NUMEROPGTO | Não |
| FCFO | COMPLEMENTOPGTO | Não |
| FCFO | TELEFONEPGTO | Não |
| FCFO | RUAENTREGA | Não |
| FCFO | NUMEROENTREGA | Não |
| FCFO | COMPLEMENTREGA | Não |
| FCFO | TELEFONEENTREGA | Não |
| FCFO | EMAIL | Não |
| FCFO | INSCRMUNICIPAL | Não |
| FCFO | EMAILENTREGA | Não |
| FCFO | EMAILPGTO | Não |
| FCFO | SUFRAMA | Não |
| FCFO | TELEFONECOMERCIAL | Não |
| FCFO | INSCRESTADUALST | Não |
| FCFO | EMAILFISCAL | Não |
| FCFO | DOCUMENTOESTRANGEIRO | Não |

Contatos do Cliente/Fornecedor

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FCFOCONTATO | NOME | Não |
| FCFOCONTATO | EMAIL | Não |
| FCFOCONTATO | TELEFONE | Não |
| FCFOCONTATO | RUA | Não |
| FCFOCONTATO | NUMERO | Não |
| FCFOCONTATO | COMPLEMENTO | Não |

Dados bancários

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FDADOSPGTO | FAVORECIDO | Não |
| FDADOSPGTO | CGCFAVORECIDO | Não |

Dados Originais do Cliente/Fornecedor

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FCFOHISTORICO | NOME | Não |
| FCFOHISTORICO | NOMEFANTASIA | Não |
| FCFOHISTORICO | CGCCFO | Não |
| FCFOHISTORICO | INSCRMUNICIPAL | Não |
| FCFOHISTORICO | INSCRESTADUAL | Não |
| FCFOHISTORICO | SUFRAMA | Não |
| FCFOHISTORICO | NUMDEPENDENTES | Não |
| FCFOHISTORICO | RUA | Não |
| FCFOHISTORICO | NUMERO | Não |
| FCFOHISTORICO | COMPLEMENTO | Não |
| FCFOHISTORICO | TELEFONE | Não |
| FCFOHISTORICO | EMAIL | Não |

Conta bancária

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FCONTA | CGCCEDENTE | Não |

Convênio

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FCONVENIO | CGCCEDENTE | Não |

Extrato de Caixa

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FXCX | CGCCEDENTE | Não |

Retenção acumulada em lançamentos financeiros

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FRETENCAOACUMULADA | CGCCFO | Não |
| FRETENCAOACUMULADAHST | CGCCFO | Não |

Gestão FiscalFilial

<https://tdn.totvs.com/pages/viewpage.action?pageId=422545738>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensíel** |
| GFILIAL | CONTATO | Não |
| GFILIAL | EMAIL | Não |
| GFILIAL | DDD | Não |
| GFILIAL | TELEFONE | Não |
| GFILIAL | DDDFAX | Não |
| GFILIAL | FAX | Não |
| DFILIAL | NOMECONTADOR | Não |
| DFILIAL | CPFCONTADOR | Não |
| DFILIAL | LOGRADCONTADOR | Não |
| DFILIAL | NROLOGRADCONTADOR | Não |
| DFILIAL | COMPLOGRADCONTADOR | Não |
| DFILIAL | BAIRROCONTADOR | Não |
| DFILIAL | CEPCONTADOR | Não |
| DFILIAL | CXPOSTALCONTADOR | Não |
| DFILIAL | CEPCXPOSTALCONTADOR | Não |
| DFILIAL | UFCONTADOR | Não |
| DFILIAL | CODMUNICCONTADOR | Não |
| DFILIAL | DDDCONTADOR | Não |
| DFILIAL | TELCONTADOR | Não |
| DFILIAL | DDDFAXCONTADOR | Não |
| DFILIAL | FAXCONTADOR | Não |
| DFILIAL | EMAILCONTADOR | Não |
| DFILIAL | DDDCELCONTADOR | Não |
| DFILIAL | CELULARCONTADOR | Não |
| DFILIAL | TIPOINSCRCONTADOR | Não |
| DFILIAL | UFCRCCONTADOR | Não |
| DFILIAL | CRCCONTADOR | Não |
| DFILIAL | DIGITOCRCCONTADOR | Não |
| DFILIAL | NOMEREPRES | Não |
| DFILIAL | CPFREPRES | Não |
| DFILIAL | LOGRADREPRES | Não |
| DFILIAL | NROLOGRADREPRES | Não |
| DFILIAL | COMPLOGRADREPRES | Não |
| DFILIAL | BAIRROREPRES | Não |
| DFILIAL | UFREPRES | Não |
| DFILIAL | CODMUNICREPRES | Não |
| DFILIAL | CEPREPRES | Não |
| DFILIAL | CEPCXPOSTALREPRES | Não |
| DFILIAL | CXPOSTALREPRES | Não |
| DFILIAL | DDDREPRESENTANTE | Não |
| DFILIAL | TELREPRES | Não |
| DFILIAL | DDDFAXREPRESENTANTE | Não |
| DFILIAL | FAXREPRES | Não |
| DFILIAL | DDDCELREPRES | Não |
| DFILIAL | CELULARREPRES | Não |
| DFILIAL | EMAILREPRES | Não |
| DFILIAL | CARGOREPRES | Não |
| DFILIAL | CODQUALIFICACAO | Não |

Parâmetros da ECF

<https://tdn.totvs.com/pages/viewpage.action?pageId=422545950>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| DSOCIOECF | CPFCNPJ | Não |
| DSOCIOECF | CPFREPRESENTANTE | Não |
| DSOCIOECF | IDPAIS | Não |
| DSOCIOECF | NOME | Não |
| DSOCIOECF | QUALIF | Não |
| DSOCIOECF | QUALIFREPRELEGAL | Não |

Responsável técnico NF-e

<https://tdn.totvs.com/pages/viewpage.action?pageId=422546178>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| DRESPONSAVELTECNICONFE | CNPJ | Não |
| DRESPONSAVELTECNICONFE | EMAIL | Não |
| DRESPONSAVELTECNICONFE | NOME | Não |
| DRESPONSAVELTECNICONFE | TELEFONE | Não |
| DRESPONSAVELTECNICONFE | UF | Não |

Lançamento Fiscal

<https://tdn.totvs.com/pages/viewpage.action?pageId=427041477>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| DCTEMOTORISTA | CPF | Não |
| DCTEMOTORISTA | NOME | Não |
| DFILIALLOG | VALORANTERIOR | Não |
| DITEM | CNPJADQUIRENTE | Não |
| DITEMHISTORICO | CNPJADQUIRENTE | Não |
| DLAF | CNPJCPFADQUIRENTE | Não |
| DLAF | DOCESTRANGEIROADQUIRENTE | Não |
| DLAF | NOMEADQUIRENTE | Não |
| DLAFTRANSP | BAIRROCOLETA | Não |
| DLAFTRANSP | BAIRROENTREGA | Não |
| DLAFTRANSP | CNPJCPFCOLETA | Não |
| DLAFTRANSP | CNPJCPFENTREGA | Não |
| DLAFTRANSP | CODETDCOLETA | Não |
| DLAFTRANSP | CODETDENTREGA | Não |
| DLAFTRANSP | CODMUNICIPIOCOLETA | Não |
| DLAFTRANSP | CODMUNICIPIOENTREGA | Não |
| DLAFTRANSP | COMPLCOLETA | Não |
| DLAFTRANSP | COMPLENTREGA | Não |
| DLAFTRANSP | NOMECOLETA | Não |
| DLAFTRANSP | NOMEENTREGA | Não |
| DLAFTRANSP | NUMEROCOLETA | Não |
| DLAFTRANSP | NUMEROENTREGA | Não |
| DLAFTRANSP | RUACOLETA | Não |
| DLAFTRANSP | RUAENTREGA | Não |
| DLDCNF | CNPJCPFCEI | Não |
| DNFTERCEIROS | CNPJCPFCEI | Não |

Período Fiscal

<https://tdn.totvs.com/pages/viewpage.action?pageId=422545772>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| DCTEMOTORISTAHISTORICO | CPF | Não |
| DCTEMOTORISTAHISTORICO | NOME | Não |
| DITEMHISTORICO | CNPJADQUIRENTE | Não |
| DLAFHISTORICO | CNPJCPFADQUIRENTE | Não |
| DLAFHISTORICO | DOCESTRANGEIROADQUIRENTE | Não |
| DLAFHISTORICO | NOMEADQUIRENTE | Não |
| DLAFTRANSPHISTORICO | BAIRROCOLETA | Não |
| DLAFTRANSPHISTORICO | BAIRROENTREGA | Não |
| DLAFTRANSPHISTORICO | CNPJCPFCOLETA | Não |
| DLAFTRANSPHISTORICO | CNPJCPFENTREGA | Não |
| DLAFTRANSPHISTORICO | CODETDCOLETA | Não |
| DLAFTRANSPHISTORICO | CODETDENTREGA | Não |
| DLAFTRANSPHISTORICO | CODMUNICIPIOCOLETA | Não |
| DLAFTRANSPHISTORICO | CODMUNICIPIOENTREGA | Não |
| DLAFTRANSPHISTORICO | COMPLCOLETA | Não |
| DLAFTRANSPHISTORICO | COMPLENTREGA | Não |
| DLAFTRANSPHISTORICO | NOMECOLETA | Não |
| DLAFTRANSPHISTORICO | NOMEENTREGA | Não |
| DLAFTRANSPHISTORICO | NUMEROCOLETA | Não |
| DLAFTRANSPHISTORICO | NUMEROENTREGA | Não |
| DLAFTRANSPHISTORICO | RUACOLETA | Não |
| DLAFTRANSPHISTORICO | RUAENTREGA | Não |
| DNFTERCEIROSHISTORICO | CNPJCPFCEI | Não |

Gestão Patrimonial

Atualmente utilizamos os tabelas/campos abaixo, porém não somos os donos das tabelas e a anonimização ocorrerá nos módulos donos destas tabelas, mas precisamos informar ao usuário o que ocorrerá do nosso lado (quais as regras serão verificadas) quando os módulos responsáveis chamarem a anonimização.

Funcionários responsáveis pelos patrimônios

OBS: quando os responsáveis são utilizados da tabela do módulo Folha de Pagamento.

<https://tdn.totvs.com/pages/viewpage.action?pageId=444616202>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| PFUNC | CHAPA | Não |
| PFUNC | NOME | Não |

Fornecedores informados nos patrimônios

<https://tdn.totvs.com/pages/viewpage.action?pageId=421388786>

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| FCFO | Nome | Não |
| FCFO | Nome Fantasia | Não |

Conta contábil informada nos grupos de patrimônios

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| CCONTA | Descrição | Não |

Planejamento e Controle de ProduçãoLog Atividade

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Coluna** | **Sensível** |
| KLOGATIVIDADE | NOMEMO | Não |

**Processos**

Os campos mapeados acima são utilizados em diversas rotinas do TOTVS Backoffice (Linha RM) as quais listamos abaixo.

Gestão Contábil

* Controle de atividade
* Apontamento
* Correção de Apontamento
* Razão de parada onde a razão é mão de obra
Gestão Estoque/Compras/Faturamento

* Comunicar Fornecedores (Cotação)
* Enviar Email do Quadro Comparativo
* Relatório do Quadro Comparativo
* Imprimir Quadro Comparativo
* Imprimir DACT-e (CT-e)
* Imprimir DACT-e OS (CT-e OS)
* Imprimir DAMDFE (MDF-e)
* Imprimir Documentos (Movimento)
Gestão Financeira

* Envio de e-mail de boleto
* Exportação de XML de Cliente/Fornecedor
* Extrato de Cliente/Fornecedor
* Inclusão de boletos
* Remessa bancária
* Registro online de boletos
* Vínculo entre Cli/For e Pessoa
Gestão Fiscal

* NF-e

+ Cancelar NF-e
+ Consultar Inutilização
+ Enviar XML por E-mail
+ Enviar
+ Consultar Autorização
+ Salvar XML
+ Imprimir DANFE .NET (RM Reports)
+ Consultar Autorização Automática (Job)
+ Gerar DANFE.NET em Contingência
+ Atualizar Responsável Técnico

* Eventos da NF-e

+ Envio de Eventos
+ Consulta de Eventos
+ Salvar XML

* NFS-e

+ Enviar NFS-e
+ Salvar XML
+ Consultar Autorização pelo número RPS
+ Consultar Autorização/Cancelamento
+ Consultar Autorização/Cancelamento Automático (Job)
+ Substituir NFS-e

* SPED Fiscal

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link (****).**
