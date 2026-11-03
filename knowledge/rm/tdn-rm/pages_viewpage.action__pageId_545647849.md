---
content_hash: 92614aef395e53f90defcb5c635122717cf97848926d7300a65545b4b18bbc3b
fetched_at: '2026-06-29T00:10:39.082516+00:00'
page_id: '545647849'
product: rm
source: tdn-rm
title: LGPD - Serviços Via WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545647849
version: 17
---

## **01. VISÃO GERAL**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest. 

Estas restrições se aplicam aos registros retornados (restrição de linha) ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso as informações de cadastro que possua permissão e/ou que lhe pertencem, ou seja, informações que fazem referência a sua pessoa, ou caso o usuário seja chefe ou supervisor o mesmo terá acesso aos dados de seus subordinados, [clique](https://tdn.totvs.com/display/LRM/Chefes+e+Supervisores) para mais detalhes sobre o cadastro de chefes e supervisores.

Para os serviços via SOAP as restrições de aplicam aos métodos "ReadView" , "ReadRecord" , SaveRecord e Delete

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi criada a nova permissão de acesso ***"Desconsiderar Filtro de Produto em WebService",***com objetivo de que o sistema passe a fazer filtro de segurança nos DataSevers ao realizar acesso via WebService. O novo parâmetro esta localizado em S**erviços Globais - Segurança - Perfis.**

No caso de o usuário estar vinculado a um perfil que não contenha permissão, os DataSevers retornarão os registros filtrados conforme regra de negócio do produto, caso contrário o sistema continua com o comportamento padrão retornando todos os registros conforme filtro informado pelo usuário.

11Filtro por Chapa

Caso o usuário não tenha permissão no parâmetro ***"Desconsiderar Filtro de Produto em WebService",***os DataSevers retornarão apenas os dados do funcionário que o usuário esteja associado. Em caso de ser chefe ou supervisor, retornará também os dados de seus subordinados.

## **A LISTA DE DATASERVERS COM RESTRIÇÕES:**

| FUNCIONALIDADE | DATASERVER | STATUS |
| --- | --- | --- |
| CADASTRO DE FUNCIONÁRIO | FopFuncData | ATIVO |
| FICHA FINANCEIRA | FopFichaFinancData | ATIVO |
| HISTÓRICO SALARIAL | FopHstSalData | INATIVO |
| SALÁRIO COMPOSTO | FopSalCompostoData | ATIVO |
| ENVELOPE DE PAGAMENTO | FopEnvelopeData | INATIVO |
| ENVELOPE DE PAGAMENTO | FopEnvelopeFeriasData | INATIVO |
| RECIBO DE FÉRIAS | FopFuFeriasReciboData | ATIVO |
| ENCARGO | FopEncargoData | ATIVO |
| GOZO DE FÉRIAS | FopFuFeriasPerData | ATIVO |
| GOZO DE FÉRIAS | FopFuFeriasPerDataBR | ATIVO |
| DEPENDENTES DO FUNCIONÁRIO | FopDependData | ATIVO |
| AFASTAMENTO DO FUNCIONÁRIO | FopHstAftData | ATIVO |
| VÍNCULOS EMPREGATÍCIOS COM OUTRAS EMPRESAS (TERCEIROS) | FopMultVinculosExternoData | ATIVO |
| DADOS DO RESIDENTE OU DOMICILIADO NO EXTERIOR | FopDadosResidExteriorData | ATIVO |
| OBSERVAÇÕES CONTRATUAIS | FopObservacoesData | ATIVO |
| CÓDIGOS FIXOS | FopCodFixData | ATIVO |
| EVENTOS PROGRAMADOS | FopEventoProgramadoData | ATIVO |
| RATEIO FIXO | FopRateioFixoData | ATIVO |
| CONVOCAÇÃO PARA TRABALHO INTERMITENTE | FopConvocacaoData | ATIVO |
| HISTÓRICO DE VALE TRANSPORTE | FopHstValeTrData | ATIVO |
| DADOS PERÍODO AQUISITIVO (FÉRIAS FUTURAS) | FopFuFeriasData | ATIVO |
| DADOS DA RESCISÃO | FopRescisaoData | ATIVO |
| DADOS DO AVISO PREVIO | FopAvisoPrevioData | ATIVO |

OBS: Para que o usuário tenha acesso aos demais DataServers que não receberam a implementação do filtro de segurança do produto, mantendo o comportamento que o sistema já possuía, deverá dar permissão a esse novo parâmetro.

solidExemplos

SEGURANÇA DATASERVER:

**MONTAGEM DE AMBIENTE SOAPUI:**

NOVO PROJETO: <http://localhost:8051/wsDataServer/MEX?wsdl> 

COM O NOME QUE QUISEREM:

**1 - CONFIGURAR O HOST, COM AS TAGS, CASO NÃO AS TENHAM, SEGUE ABAIXO:**

<add key="DefaultDB" value="WEB" />

<add key="HTTPPORT" value="8051" />

APÓS A INSERÇÃO DAS TAGS, SALVAR E INICIAR O HOST COMO ADMINISTRADOR. 

**2 - CONFIGURAR O READVIEW CONFORME ABAIXO, E EXECUTAR:**

A AUTHORIZATION:

OBS: O USUÁRIO QUE SERÁ VALIDADO É O USUÁRIO PREENCHIDO NA **AUTHORIZATION,** O USUÁRIO PREENCHIDO NO CONTEXTO NÃO FAZ DIFERENÇA, MAS A CODCOLIGADA SERÁ VALIDADA A QUE ESTIVER NO CONTEXTO:

EX: NO PRINT ESTÁ VALIDANDO O FUNCIONÁRIO CUJO USUÁRIO DE ACESSO É O ‘TIAGOF’ E COLIGADA 1.

**EXEMPLO 1.**

USANDO UM FUNCIONÁRIO DO QUAL NÃO É CHEFE E NEM SUPERVISOR, OU SEJA NÃO ESTÁ LIGADO A NINGUÉM (PARAMETRIZAÇÃO SOAPUI CONFORME EXEMPLO CITADO ACIMA)

**OBS1:** EM CASO DE A FLAG “***DESCONSIDERAR FILTRO DE PRODUTO EM WEBSERVICE***” ESTAR SEM PERMISSÃO ***(PERMISSÃO VINCULADA AO USUÁRIO EM SERVIÇOS GLOBAIS - SEGURANÇA - USUARIO/PERFIL)***, DEVE ME RETORNAR APENAS A CHAPA EM QUE ESTÁ VINCULADA AO USUÁRIO.

EX:

RETORNO: APENAS A CHAPA DO FUNCIONÁRIO

**OBS2:** EM CASO DE A FLAG “***DESCONSIDERAR FILTRO DE PRODUTO EM WEBSERVICE***” ESTAR COM PERMISSÃO, DEVERÁ  IGNORAR SE ELE ESTÁ VINCULADO A ALGUÉM OU NÃO, E DEVE ME RETORNAR TODOS OS FUNCIONÁRIOS DA COLIGADA PASSADA NO CONTEXTO.

EX:

RETORNO:

**EXEMPLO 2:**

O USUÁRIO É CHEFE DA  SEÇÃO 01.02, E COM A FLAG “***DESCONSIDERAR FILTRO DE PRODUTO EM WEBSERVICE***” SEM PERMISSÃO.

RETORNO: DEVE ME RETORNAR OS FUNCIONÁRIOS PERTENCENTES A SEÇÃO EM QUE O USUÁRIO ESTÁ VINCULADO, NESTE CASO, TODOS PERTENCENTES A SEÇÃO 01.02, INCLUSIVE ELE MESMO.

EX: 

FUNCIONÁRIOS PERTENCENTES A SEÇÃO 01.02.

RETORNO NO SOAPUI:

OBS: ***CORTEI OS ARQUIVOS***, PARA MOSTRAR QUE TROUXE TODOS OS FUNCIONÁRIOS PERTENCENTES A SEÇÃO EM QUE O USUÁRIO ESTÁ VINCULADO COMO CHEFE.

EM  CASO DE A FLAG “***DESCONSIDERAR FILTRO DE PRODUTO EM WEBSERVICE***” COM PERMISSÃO, SEMPRE DEVERÁ ME RETORNAR TODOS OS FUNCIONÁRIOS QUE PERTENCEM A COLIGADA PASSADA NO CONTEXTO (EXEMPLO DEMONSTRADO NO EXEMPLO 1)

## 

2Filtro por Coligada

Caso o usuário não tenha permissão no parâmetro ***"Desconsiderar Filtro de Produto em WebService",***os DataSevers retornarão apenas os dados das coligadas que o usuário tenha permissão de acesso ao cadastro correspondente no produto.

## **A LISTA DE DATASERVERS COM RESTRIÇÕES:**

| FUNCIONALIDADE | DATASERVER | STATUS |
| --- | --- | --- |
| CADASTRO DE CHEFE E SUPERVISOR | FopChefeSupervisorData | ATIVO |
| CADASTRO DE SEÇÃO | FopSecaoDataBR | ATIVO |
| CADASTRO DE EVENTO | FopEventoData | ATIVO |
| CADASTRO DE CENTRO DE CUSTO | FopCCustoData | ATIVO |
| CADASTRO DE FUNÇÃO | FopFuncaoData | ATIVO |
| CADASTRO DE SINDICATO | FopSindicData | ATIVO |

OBS: Para que o usuário tenha acesso aos demais DataServers que não receberam a implementação do filtro de segurança do produto, mantendo o comportamento que o sistema já possuía, deverá dar permissão a esse novo parâmetro.

solidExemplos

SEGURANÇA DATASERVER:

**MONTAGEM DE AMBIENTE SOAPUI:**

NOVO PROJETO: <http://localhost:8051/wsDataServer/MEX?wsdl> 

COM O NOME QUE QUISEREM:

**1 - CONFIGURAR O HOST, COM AS TAGS, CASO NÃO AS TENHAM, SEGUE ABAIXO:**

<add key="DefaultDB" value="WEB" />

<add key="HTTPPORT" value="8051" />

APÓS A INSERÇÃO DAS TAGS, SALVAR E INICIAR O HOST COMO ADMINISTRADOR. 

**2 - CONFIGURAR O READVIEW CONFORME ABAIXO, E EXECUTAR:**

A AUTHORIZATION:

OBS: O USUÁRIO QUE SERÁ VALIDADO É O USUÁRIO PREENCHIDO NA **AUTHORIZATION,** O USUÁRIO PREENCHIDO NO CONTEXTO NÃO FAZ DIFERENÇA, MAS A CODCOLIGADA SERÁ VALIDADA A QUE ESTIVER NO CONTEXTO:

EX: NO PRINT O USUÁRIO DE ACESSO É O ‘TESTE’ E COLIGADA 6.

**EXEMPLO**

USANDO O USUARIO ‘TESTE' QUE POSSUI PERMISSÃO PARA ACESSO NA COLIGADA 6 E NÃO POSSUI PERMISSÃO PARA ACESSO NA COLIGADA 1 .

**OBS:** EM CASO DE A FLAG “***DESCONSIDERAR FILTRO DE PRODUTO EM WEBSERVICE***” ESTAR SEM PERMISSÃO ***(PERMISSÃO VINCULADA AO USUÁRIO EM SERVIÇOS GLOBAIS - SEGURANÇA - USUARIO/PERFIL)***, DEVE RETORNAR REGISTROS CONFORME PERMISSÃO DE SEGURANÇA CADASTRADA NO PERFIL.

EX:

COLIGADA 6 - COM PERMISSÃO DE ACESSO

COLIGADA 1 - SEM PERMISSÃO DE ACESSO

RETORNO: RETORNADOS VALORES SOMENTE DA COLIGADA 6.

##
