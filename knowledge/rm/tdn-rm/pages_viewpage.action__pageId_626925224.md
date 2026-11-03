---
content_hash: c541ecd2584b07913a5dcbc9655fcce2605063a2591778c9e855c8a4eaaf18dc
fetched_at: '2026-06-29T00:11:04.451915+00:00'
page_id: '626925224'
product: rm
source: tdn-rm
title: DT-Filtro de usuário e perfil - RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626925224
version: 6
---

## ****01. DADOS GERAIS****

Linha RM​

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | RM Portal - Filtro de usuário e perfil |
| País: | Brasil |
| Ticket: | [11713008](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D%20%3D%20%2211713008%22) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-13771](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-13771) |

## **02. SITUAÇÃO/REQUISITO**

Ao informar um filtro de usuário por filial no chefe/supervisor, o sistema não estava respeitando o filtro e enviava o e-mail de sugestão de férias para todos os chefes e supervisores independente da filial que o funcionário estava lotado.

## **03. SOLUÇÃO**

O envio de email para os gestores (chefes/supervisor/Externo), além de observar as regras já existentes de chefe e subordinados, passou a filtrar os gestores do subordinado, aplicando o filtro de usuário e de perfil vinculado ao usuário e perfil dos gestores.

## **04. ASSUNTOS RELACIONADOS**

* [Sugestão de Férias - Linha RM](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718768)
* [Filtros do RM Portal](https://tdn.totvs.com.br/display/LRM/Filtros+do+RM+Portal)
