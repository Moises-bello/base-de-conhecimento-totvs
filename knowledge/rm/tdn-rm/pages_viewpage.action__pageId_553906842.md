---
content_hash: baf86f823cc007e9b1d2c8a109e96116b9555e1dc5134e5a77842947baa08eda
fetched_at: '2026-06-29T00:10:46.123151+00:00'
page_id: '553906842'
product: rm
source: tdn-rm
title: 9075227 FISCAL01-13436 Adequação LGPD - API REST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553906842
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Data Servers |
| Ticket: | 9075227 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13436 |

## **02. SITUAÇÃO/REQUISITO**

Cliente está realizando um processo de integração entre API REST e RM. Ao acessar o WebService POSTMAN, e realizar uma chamada REST que o usuario tem permissão em apenas uma coligada dentro do RM e que o WebService precisa ser adequado.

## **03. SOLUÇÃO**

Foi implementado o data annotation de segurança da Lib (RMSSecurityFilter) nos seguintes data servers, para as consultas via REST adequando a nova politica da LGPD:

* FisNaturezaData
* FisTrbNaturezaData
* FisDeptoData
* FisLanFiscalEntradaData
* FisLanFiscalSaidaData
* FisLancOutrosDCData
* FisPeriodoApuracaoData
* FisNFeMunicipalData
* FisNFeEstadualData

Informações Adicionais

* Para que um data server tenha o acesso bloqueado via REST é necessário retirar a permissão TODOS os perfis que tenha acesso a sua tag de segurança.
* As requisições do tipo GET  funcionam para o metodo DoReadView.

* Não foi implementado as requisições do tipo PUT e POST para o SaveRecord (Incluir, atualizar ou excluir um registro em determinado DataServer), porém em alguns dataservers ela PODE funcionar

## **04. DEMAIS INFORMAÇÕES**

Para as consultas GET via REST é necessário preencher as informações do cabeçalho (HEADER)  da requisição com os seguintes dados:

* FisNaturezaData - Informar:
  + CODCOLIGADA
  + CODFILIAL
  + EXERCICIOFISCAL
  + CODSISTEMA

* FisTrbNaturezaData - Informar:
  + CODCOLIGADA
  + CODFILIAL
  + EXERCICIOFISCAL
  + CODSISTEMA

* FisDeptoData - Informar:
  + CODCOLIGADA

* FisLanFiscalEntradaData - Informar:
  + CODCOLIGADA
  + CODFILIAL
  + EXERCICIOFISCAL
  + CODUSUARIO

* FisLanFiscalSaidaData - Informar:
  + CODCOLIGADA
  + CODFILIAL
  + EXERCICIOFISCAL
  + CODUSUARIO

* FisLancOutrosDCData - Informar:
  + CODCOLIGADA
  + CODFILIAL
  + EXERCICIOFISCAL

* FisPeriodoApuracaoData - Informar:
  + CODCOLIGADA
  + CODFILIAL
  + EXERCICIOFISCAL

* FisNFeMunicipalData - Informar:
  + CODCOLIGADA

* FisNFeEstadualData - Informar:
  + CODCOLIGADA

Módulos onde os data servers tem acesso:

* FisNaturezaData : RM Liber e RM Nucleus
* FisTrbNaturezaData : RM Liber e RM Nucleus
* FisDeptoData : RM Chronus, RM Testis, RM Saldus, RM Liber, RM Classis - E, RM Fluxus, RM Bis, RM Agilis, RM Bonum, RM Factor, RM Biblios, RM Solum, RM Officina, RM Saude/Janus, RM Labore, RM Classis Net, RM Nucleus, RM Classis - U, RM Vitae, RM Portal e RM SGI.
* FisLanFiscalEntradaData : RM Liber
* FisLanFiscalSaidaData : RM Liber
* FisLancOutrosDCData : RM Liber
* FisPeriodoApuracaoData : RM Liber
* FisNFeMunicipalData : RM Liber e RM Nucleus
* FisNFeEstadualData : RM Liber e RM Nucleus
