---
content_hash: 086d3efff979df38ab4c5f4c101d31f9150bb785b3e8dc7480a3611ae35e94e8
fetched_at: '2026-06-29T00:10:22.460390+00:00'
page_id: '496401668'
product: rm
source: tdn-rm
title: FISCAL01-9386 - Parâmetros de Processo - Anexo Filtro Tributo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496401668
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Parâmetros de Processo |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9386 |

**02. SITUAÇÃO/REQUISITO**

Para cada Tipo de Documento, deve-se informar o Tributo e o CST do mesmo. Para isso, criar um anexo no Filtro de Operações onde o usuário terá que informar o Tributo (lookup para o Cadastro de Tributos) e o CST.

Apesar da especificação contemplar vários campos, vamos criar inicialmente somente os campos necessários para implementação da apuração da CPRB pelo regime de caixa. São eles:

* Código da Coligada
* IDFILTROTRB
* Código do Tributo
* Código do Subgrupo
* Id. Filtro Tipo Operações
* CST

Validação:

1. Não deve ser permitido inclusão de tributos duplicados para um mesmo Filtro de Operação.

**03. SOLUÇÃO**

Criação do cadastro de Filtro de Tributo, referente ao anexo do Filtro de Operação  ([FISCAL01-9574 Anexo Filtro de Operações](http://tdn.totvs.com/pages/viewpage.action?pageId=496036716)), tendo os seguintes campos:

* Código da Coligada
* [Id.do](http://Id.do) Filtro de Tributo
* Código do Tributo
* Id. Filtro Tipo Operações
* CST
* Natureza Receita
