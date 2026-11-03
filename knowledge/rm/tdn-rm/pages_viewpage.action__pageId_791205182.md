---
content_hash: 7ffef7fa6fa47112e5464c4d6720b7bcd6d7ce51ef846c6003c52e127b73338a
fetched_at: '2026-06-29T00:11:39.925581+00:00'
page_id: '791205182'
product: rm
source: tdn-rm
title: FISCAL01-20761 - NFE - ICMS Monofásica - Combustíveis - Buscar alíquota ADREM
  na inclusão de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=791205182
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Inclusão do item do movimento, campo Alíquota dos tributos informados. |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-20761 |

## **02. SITUAÇÃO/REQUISITO**

NFE - ICMS Monofásica / Combustíveis  - Mudar o serviço de tributação para buscar alíquota por valor preferencialmente na inclusão de Movimento, caso não esteja parametrizado para buscar alíquota por valor, o sistema deve seguir a ordem já existente.

## **03. SOLUÇÃO**

Foi alterado o serviço de tributação para buscar alíquota por valor preferencialmente na inclusão de Movimento, caso não esteja parametrizado para buscar alíquota por valor, o sistema deve seguir a ordem já existente, se no cadastro do tributo estiver parametrizado para buscar alíquota do tipo do movimento, será considerado o parâmetro do tipo de movimento, campo buscar alíquota, caso contrário será considerado a opção cadastrada no tributo.
