---
content_hash: dcc896f664841ae7fbe3b8d3afd38f5435335a8ecff481500cda06d46a06be90
fetched_at: '2026-06-29T00:08:47.370600+00:00'
page_id: '319788040'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-785 Evento GTV
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01-785+Evento+GTV
version: 101
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | RM |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-2059 |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-785 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

De acordo com o Manual de Orientações ao Contribuinte Versão 3.00 do Conhecimento de Transporte Eletrônico, após o envio do CT-e OS de Transporte de Valores, é necessário fazer o envio de pelo menos um evento de GTV (Guia de Transporte de Valores) referente ao CT-e OS enviado.

Abaixo, a descrição de como esse evento deverá ser implementado no sistema.

## Segurança

Para Incluir uma nova guia, Alterar, Excluir, Enviar Evento ou Consultar Evento, é necessário permitir acesso.

## Definição da Regra de Negócio

Visão de Conhecimento de Transportes Eletrônicos - Outros Serviços

1. Anexo Cadastro de GTV

Deverá ser criado um novo anexo da visão de Conhecimento de Transportes Eletrônicos - Outros Serviços chamado "Cadastro de GTV". Esse anexo deverá ser exibido somente quando o CT-e OS selecionado for um CT-e OS de Transporte de Valores.

Nesse anexo o usuário fará o cadastramento das GTVs associadas ao CT-e OS selecionado. O usuário deve ter a possibilidade de incluir, editar e excluir GTVs. Para cada GTV cadastrada deverá ser exibido um registro no anexo.

Esse anexo deverá apresentar duas abas, sendo a primeira aba chamada "Informações da GTV". A segunda aba, chamada "Espécies da GTV", deverá ser relacionada à primeira aba. Abaixo, o detalhamento dos dados de cada aba:

*Aba Informações da GTV*

Criar o GroupBox Identificação da GTV. Esse GroupBox conterá os seguintes campos:

* Número (campo tipo caracter, tamanho 20): campo de preenchimento obrigatório pelo usuário.
* Identificador (campo tipo caracter, tamanho 20): campo de preenchimento obrigatório pelo usuário. Este identificador serve para diferenciar GTV de mesmo número (Usar número do AIDF ou identificador interno da empresa).
* Série (campo tipo caracter, tamanho 3): campo de preenchimento opcional pelo usuário.
* Subsérie (campo tipo caracter, tamanho 3): campo de preenchimento opcional pelo usuário.
* Dígito Verificador (campo tipo numérico, tamanho 1): campo de preenchimento obrigatório pelo usuário.

Criar o GroupBox Rementente. Esse Groupbox deverá conter os seguintes campos:

* RadioButton Filial: se este RadioButton for marcado, o RadioButton Cliente/Fornecedor deve ser desmarcado.
* RadioButton Cliente/Fornecedor: se este RadioButton for marcado, o RadioButton Filial deve ser desmarcado.
* Remetente: se o RadioButton Filial estiver marcado, deverá ser exibido um lookup para listar as filiais ativas para que o usuário selecione a filial remetente. Se o RadioButton Cliente/Fornecedor estiver marcado, deverá ser exibido um lookup para listar os clientes/fornecedores ativos para que o usuário selecione o cliente/fornecedor remetente.

Criar o GroupBox Destinatário. Esse Groupbox deverá conter os seguintes campos:

* RadioButton Filial: se este RadioButton for marcado, o RadioButton Cliente/Fornecedor deve ser desmarcado.
* RadioButton Cliente/Fornecedor: se este RadioButton for marcado, o RadioButton Filial deve ser desmarcado.
* Remetente: se o RadioButton Filial estiver marcado, deverá ser exibido um lookup para listar as filiais ativas para que o usuário selecione a filial remetente. Se o RadioButton Cliente/Fornecedor estiver marcado, deverá ser exibido um lookup para listar os clientes/fornecedores ativos para que o usuário selecione o cliente/fornecedor remetente.

Criar o GroupBox Dados do Veículo. Esse Groupbox deverá conter os seguintes campos:

* Placa (campo tipo caracter, sem tamanho definido): campo de preenchimento opcional pelo usuário.
* UF (campo tipo caracter, tamanho 2): campo de preenchimento opcional pelo usuário.
* Deverá ser criado um lookup para que o usuário possa associar um veículo cadastrado. Quando for associado um veículo, os campos Placa e UF deverão ser preenchidos automaticamente com os dados do cadastro de veículo, TVEICULOS.PLACA e TVEICULOS.UF, respectivamente.

*Aba Espécies da GTV*

Nessa aba, o usuário deve ter a possibilidade de incluir, editar e excluir as espécies relacionadas ao GTV. Para cada espécie cadastrada deverá ser exibido um registro na aba. Abaixo o detalhamento de dados dessa aba:

Criar o GroupBox Dados da Carga. Esse Groupbox deverá conter os seguintes campos:

* Quantidade de Volumes/Malotes (campo tipo numérico, tamanho 11,4): campo de preenchimento obrigatório pelo usuário.
* Tipo da Espécie (campo tipo numérico, tamanho 1): campo de preenchimento obrigatório pelo usuário. Para esse campo deverá ser criado um ComboBox com os seguintes valores: 1 - Numerário; 2 - Cheque; 3 - Moeda; 4 - Outros.
* Valor Transportado (campo tipo numérico, tamanho 13,2): campo de preenchimento opcional pelo usuário.

2. Cadastros

Para que não ocorram erros no envio, deverão ser revisados alguns cadastros, de acordo com o seu papel no evento GTV. Segue detalhamento abaixo:

*Remetente*

O Remetente do GTV pode ser um cliente/fornecedor ou uma filial. Em ambos os casos, é necessário que o CPF/CNPJ, UF e Razão Social estejam devidamente informados:

Cadastro de Filial

|  |  |
| --- | --- |

Cadastro de Cliente/Fornecedor

*Emitente*

Caso sejam informados os dados do veículo de transporte do CT-e OS, é necessário que o Registro ANTT (RNTRC) da filial do transportador esteja devidamente informado:

3. Processos do Anexo do Cadastro de GTV

Deverá ser criados processos no Anexo do Cadastro de GTV, um para que o usuário faça o envio do GTV cadastrado e outro para que o usuário consulte o status do GTV enviado. O processo de envio deverá ser executado somente quando um ou mais GTVs estiverem selecionados e o processo de consulta poderá ser executado sem a seleção de GTVs.

4. Envio de GTV

Para o envio de GTVs deve-se utilizar o schema XML evGTV\_v9.99.xsd. Abaixo, o leiaute de envio e a descrição das informações que deverão ser enviadas:

| Campo | Agrupador | Pai | Tipo | Ocor | Tam | Dec. | Descrição/Observação | Campos RM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| evGTV | S | - | - | 1-1 | 1 |  | Schema XML de validação do evento de Informações da GTV | - |
| descEvento | N | evGTV | C | 1-1 | 18 |  | Descrição do Evento - “Informações da GTV” | - |
| infGTV | S | - | - | 1-n |  |  | Grupo de informações da GTV | - |
| nDoc | N | infGTV | C | 1-1 | 20 |  | Número da GTV | Campo Número do Anexo Cadastro de GTV |
| id | N | infGTV | C | 1-1 | 20 |  | Identificador para diferenciar GTV de mesmo número (Usar número do AIDF ou identificador interno da empresa) | Campo Identificador do Anexo Cadastro de GTV |
| serie | N | infGTV | C | 0-1 | 3 |  | Série da GTV (opcional) | Campo Série do Anexo Cadastro de GTV |
| subserie | N | infGTV | C | 0-1 | 3 |  | Subsérie da GTV (opcional) | Campo Subsérie do Anexo Cadastro de GTV |
| dEmi | N | infGTV | D | 1-1 |  |  | Data da emissão | Data do sistema no momento do envio |
| nDV | N | infGTV | N | 1-1 | 1 |  | Número do Dígito Verificador | Campo Dígito Verificador do Anexo Cadastro de GTV |
| qCarga | N | infGTV | N | 1-1 | 11 | 4 | Quantidade de volumes/malotes | Campo Quantidade de Volumes/Malotes do Anexo Cadastro de GTV |
| infEspecie | S | infGTV |  | 1-n |  |  | Informações das espécies transportadas | - |
| tpEspecie | N | infEspecie | N | 1-1 | 1 |  | Tipo da espécie: 1 - Numerário; 2 - Cheque; 3 - Moeda; 4 - Outros | Campo Tipo da Espécie do Anexo Cadastro de GTV |
| vEspecie | N | infEspecie | N | 0-1 | 13 | 2 | Valor Transportado em espécie indicada | Campo Valor Transportado do Anexo Cadastro de GTV |
| rem | S | infGTV |  | 1-1 |  |  | Informações do remetente da GTV | - |
| CNPJ | N | rem | N | 1-1 | 14 |  | Número do CNPJ (Essa informação será preenchida somente se o remetente for pessoa jurídica.) | Se remetente do GTV igual a filial, retornar GFILIAL.CGC da filial indicada.  Se remente do GTV igual a cliente/fornecedor, retornar FCFO.CGCCFO do cliente/fornecedor informado. |
| CPF | N | rem | N | 1-1 | 11 |  | Número do CPF (Essa informação será preenchida somente se o remetente for pessoa física.) | Se remetente do GTV igual a filial, retornar GFILIAL.CGC da filial indicada.  Se remente do GTV igual a cliente/fornecedor, retornar FCFO.CGCCFO do cliente/fornecedor informado. |
| IE | N | rem | C | 0-1 | 14 |  | Inscrição Estadual | Se remetente do GTV igual a filial, retornar GFILIAL.INSCRICAOESTADUAL da filial indicada.  Se remente do GTV igual a cliente/fornecedor, retornar FCFO.INSCRESTADUAL do cliente/fornecedor informado. |
| UF | N | rem | C | 1-1 | 2 |  | Sigla da UF | Se remetente do GTV igual a filial, retornar GFILIAL.ESTADO da filial indicada.  Se remente do GTV igual a cliente/fornecedor, retornar FCFO.CODETD do cliente/fornecedor informado. |
| xNome | N | rem | C | 1-1 | 60 |  | Razão social ou nome do remetente da GTV | Se remetente do GTV igual a filial, retornar GFILIAL.NOME da filial indicada.  Se remente do GTV igual a cliente/fornecedor, retornar FCFO.NOME do cliente/fornecedor informado. |
| dest | S | infGTV |  | 1-1 |  |  | Informações do destinatário da GTV | - |
| CNPJ | N | dest | N | 1-1 | 14 |  | Número do CNPJ (Essa informação será preenchida somente se o destinatário for pessoa jurídica.) | Se destinatário do GTV igual a filial, retornar GFILIAL.CGC da filial indicada.  Se destinatário do GTV igual a cliente/fornecedor, retornar FCFO.CGCCFO do cliente/fornecedor informado. |
| CPF | N | dest | N | 1-1 | 11 |  | Número do CPF (Essa informação será preenchida somente se o destinatário for pessoa física.) | Se destinatário do GTV igual a filial, retornar GFILIAL.CGC da filial indicada.  Se destinatário do GTV igual a cliente/fornecedor, retornar FCFO.CGCCFO do cliente/fornecedor informado. |
| IE | N | dest | C | 0-1 | 14 |  | Inscrição Estadual | Se destinatário do GTV igual a filial, retornar GFILIAL.INSCRICAOESTADUAL da filial indicada.  Se destinatário do GTV igual a cliente/fornecedor, retornar FCFO.INSCRESTADUAL do cliente/fornecedor informado. |
| UF | N | dest | C | 1-1 | 2 |  | Sigla da UF | Se destinatário do GTV igual a filial, retornar GFILIAL.ESTADO da filial indicada.  Se destinatário do GTV igual a cliente/fornecedor, retornar FCFO.CODETD do cliente/fornecedor informado. |
| xNome | N | dest | C | 1-1 | 60 |  | Razão social ou nome do destinatário da GTV | Se destinatário do GTV igual a filial, retornar GFILIAL.NOME da filial indicada.  Se destinatário do GTV igual a cliente/fornecedor, retornar FCFO.NOME do cliente/fornecedor informado. |
| placa | N | infGTV | C | 0-1 |  |  | Placa do veículo | Campo Placa do Anexo Cadastro de GTV |
| UF | N | infGTV | C | 0-1 | 2 |  | UF da placa onde o veículo está registrado | Campo UF do Anexo Cadastro de GTV |
| RNTRC | N | infGTV | C | 0-1 |  |  | RNTRC do transportador (Informar somente se os campos placa e UF estiverem sendo informados.) | DFILIAL.RNTRC do cadastro da filial emitente do GTV |

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* GFILIAL - Cadastro de Filiais
* DFILIAL - Dados Fiscais do Cadastro de Filiais
* FCFO - Cadastro de Clientes/Fornecedores

### Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/

 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | <FI9\_FILIAL+FI9\_IDDARF+FI9\_STATUS> |
| **02** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_EMISS+FI9\_IDDARF> |
| **03** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_PREFIX+FI9\_NUM+FI9\_PARCEL+FI9\_TIPO> |

|  |  |
| --- | --- |
| **Campo** | <AAA\_PERESP> |
| **Tipo** | <N> |
| **Tamanho** | <6> |
| **Valor Inicial** | <Varia de acordo com o tipo informado. Por exemplo, quando o campo “tipo” for date, neste campo pode ser informado uma data>. |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | <Referência Mínima para Cálculo> |
| **Título** | <Ref.Calc.> |
| **Picture** | <@E999.99> |
| **Help de Campo** | <Informar o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação> |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
