---
content_hash: b9fb823f39df68d31d52ec9f7bb2cb96886dd2158f291fb5698e69d84bcfd713
fetched_at: '2026-06-29T00:12:06.860774+00:00'
page_id: '916404683'
product: rm
source: tdn-rm
title: FISCAL01- 25154 - Cadastro de Classificação Fiscal de Bens e Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=916404683
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | MIT |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25154 |

## **02. SITUAÇÃO/REQUISITO**

Com o objetivo de padronização e redução dos erros de validação de documentos eletrônicos, vamos implementar o conceito de **Classificação Fiscal de Mercadorias e Serviço**s: **NCM** (Nomenclatura Comum do Mercosul) para mercadorias e **NBS** (Nomenclatura Brasileira de Serviços) para serviços.

Com este fim, implementaremos o Cadastro com os seguintes campos:

* Identificador
* Tipo: Mercadoria ou serviço
* NCM (habilitar quando o Tipo for Mercadoria)
* Referência
* Código EX
* NBS (habilitar quando o Tipo for Serviço)
* Descrição (não obrigatório)
* % Red de alíquota
* Ativo

## **03. SOLUÇÃO**

Foi disponibilizado um novo cadastro que pode ser acessado através do Módulo Gestão Fiscal | Cadastros | Na divisão de "Globais" opção Mais | Classificação Fiscal de Bens e Serviços. 

**Campos Disponibilizados:**

* **Identificados**: Quantidade de registros incrementável automaticamente pelo sistema
* **Tipo**: Utilizado para definir se o cadastro é referente a um Produto ou Serviço
* **NCM**: Nomenclatura Comum do Mercosul
* **Referência**: Referência do NCM
* **Código EX:**Código EX do  NCM
* **NBS**: Código NBS(Nomenclatura Brasileira de Serviços) do serviço
* **Descrição:**Descrição da mercadoria ou serviço
* **Redução de Alíquota:**Valor da redução da alíquota
* **Ativo:**Indicativo do Status do registro, marcado é ativo e desmarcado é inativo

Tela para inclusão dos novos registros:

Disponível à partir da biblioteca 12.1.2502
