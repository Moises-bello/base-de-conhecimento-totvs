---
content_hash: 99552ae2bb63222a4cbb78b50f937716a0a70ae328ce353af73b6f64bd8fafee
fetched_at: '2026-06-29T00:10:22.019251+00:00'
page_id: '496027077'
product: rm
source: tdn-rm
title: FISCAL01-9297 DT Regra de ICMS Fórmula da Base de Calculo do ICMS Desonerado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496027077
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro da Regra de ICMS |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000381 |

## **02. SITUAÇÃO/REQUISITO**

Nesta issue iremos criar um campo na Regra do ICMS para que o usuário informe a fórmula da base de cálculo do ICMS desonerado.

Regras:

* Só podem ser informadas fórmulas do Módulo de Materiais;
* Colocar regra de visibilidade no campo para que o usuário não o veja caso o sistema não possua integração com a Gestão de Materiais.

 2. Alterar o serviço de seleção de natureza para retornar a Fórmula da BC do ICMS desonerado.

## **03. SOLUÇÃO**

No cadastro da Regra do ICMS na aba Dados ICMS foi implementado o campo "Fórmula Base de Cálculo do ICMS Desonerado" e ele fica visível quando o campo "ICMS Desonerado" é marcado.

Na classe de retorno do serviço de seleção de natureza foi disponibilizado o novo campo "Fórmula Base de Cálculo do ICMS Desonerado" para utilização de terceiros.
