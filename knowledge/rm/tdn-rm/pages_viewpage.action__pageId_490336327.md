---
content_hash: ddb980527c7dcce309145ef95af8cabc151a85d52c0fbcd007be170b895822aa
fetched_at: '2026-06-29T00:10:20.261695+00:00'
page_id: '490336327'
product: rm
source: tdn-rm
title: FISCAL01-7847 DT Cadastro de Parâmetros de Processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490336327
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Parâmetros de Processo |
| Ticket: | FISCAL01-7847 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Cadastro de Parâmetros de Processo |

## **02. SITUAÇÃO/REQUISITO**

Criar um novo Cadastro de Parâmetros de Processo em .Net onde será implementado um novo Grupo para Apuração da CPRB - Regime de Caixa.  
  
Nesse processo será necessário parametrizar os Tipos de Documentos que serão utilizados como filtro na seleção dos Lançamentos Financeiros que irão compor a base de cálculo do tributo.

## **03. SOLUÇÃO**

Criação do cadastro de Parâmetros de Processo, disponível em Cadastros / Parâmetros de Processo.

As permissões de perfil para habilitar o acesso, estão disponíveis em 01.01.05:

Recomenda-se que a visão do cadastro seja agrupada por Processo e Grupo de Processo:

Segue abaixo a edição do cadastro:

Regras relacionadas a este cadastro:

* Não é possível inserir uma data final menor do que a data inicial.
* Os campos Processo e Grupo de Processo não podem ser alterados após incluídos.
* Não é permitido incluir mais do que um Parâmetro de Processo para o mesmo período.
* No campo Descrição, quando o Parâmetro de Processo é incluído, o default é preenchido com o Grupo do Processo.
