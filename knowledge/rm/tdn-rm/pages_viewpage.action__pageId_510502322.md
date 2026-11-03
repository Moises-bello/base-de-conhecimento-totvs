---
content_hash: 616b92e34e262bb4e2a43dc01ff6c6752ffaf2002380f580a760c2c04cfda623
fetched_at: '2026-06-29T00:10:26.039490+00:00'
page_id: '510502322'
product: rm
source: tdn-rm
title: FISCAL01-10228 Registro R-1000 - API Validações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=510502322
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10228 |

## **02. SITUAÇÃO/REQUISITO**

## Cadastros

Ao acessar o menu EFD-REINF → “Eventos Cadastrais” devem ser listados todos os Eventos do tipo R-1000. O cadastro poderá ser acionado somente pela Filial Matriz ou Filial SCP. Os campos seguirão o padrão de estrutura definidos para os Eventos da EFD-REINF.

A inclusão do registro R-1000 será realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo.

## Validações

* Não pode ser incluído um Evento R-1000 enquanto existir outro R-1000 não encerrado, ou seja com a data de fim de período em branco;
* Não pode existir mais de um R-1000 para o mesmo período, ou seja o inicio do novo R-1000 deverá ser posterior ao fim do período do último R-1000;
* Apenas o R-1000 mais recente pode ser alterado.

## **03. SOLUÇÃO**

Foi criada a API referente ao registro R-1000 com as seguintes validações:

* Não pode ser incluído um Evento R-1000 enquanto existir outro R-1000 não encerrado, ou seja com a data de fim de período em branco;
* Não pode existir mais de um R-1000 para o mesmo período, ou seja o inicio do novo R-1000 deverá ser posterior ao fim do período do último R-1000;
* Apenas o R-1000 mais recente pode ser alterado.
* Não é possível alterar a data fim do R-1000, se a nova data for inferior a data final dos filhos de R-1000

## **03. DEMAIS INFORMAÇÕES**

Url para acesso da API de validação do R-1000:

GET Todos: <http://localhost:8052/api/fiscal/v1/eventoreinf/>  
GET 1: <http://localhost:8052/api/fiscal/v1/eventoreinf/1|1>  
POST: <http://localhost:8052/api/fiscal/v1/eventoreinf>  
PUT: <http://localhost:8052/api/fiscal/v1/eventoreinf/1|1>  
PATCH: <http://localhost:8052/api/fiscal/v1/eventoreinf/1|1>  
DELETE: <http://localhost:8052/api/fiscal/v1/eventoreinf/1|1>
