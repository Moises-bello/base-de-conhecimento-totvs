---
content_hash: c4910f3df76503d46ac6bb4419f3c83c1f599f808d3c4caca14009ec45492342
fetched_at: '2026-06-29T00:10:53.893187+00:00'
page_id: '589523300'
product: rm
source: tdn-rm
title: FISCAL01-13860 DT Cadastro de Parâmetros de Processos para ser por Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589523300
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Parâmetros de Processos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14604 |

## **02. SITUAÇÃO/REQUISITO**

Ajustar o cadastro de Parâmetros de Processos para ser por Filial  
Parâmetro para utilizar somente os novos cadastros na rotina EFD

Critérios de Aceite:

Permitir Criar o cadastro de parâmetros de processo por Filial  
Criar Documentação sobre o novo cadastro  
Criar teste automatizado para o cenário

## **03. SOLUÇÃO**

No cadastro de Parâmetros de Processo foi implementado o campo Código da Filial, este campo será preenchido automaticamente quando for incluído novo parâmetro de processo com a filial de contexto.

Foi implementado o parâmetro HabilitaNovoCadParamProcesso para o fiscal, este parâmetro será interno para ser utilizado nas rotinas.

Obs: No script solicitado será atualizado o campo código da filial do registros dos parâmetros de processo já existentes com o código da filial parametrizado no parâmetro Filial Matriz em DPARAMETROS.
