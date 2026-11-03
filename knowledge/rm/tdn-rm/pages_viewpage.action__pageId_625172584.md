---
content_hash: 5b373e8264537b71b394f9d2263c1c7d7a1a26dbc5e143ebc71aa5755f1f28c6
fetched_at: '2026-06-29T00:11:04.104578+00:00'
page_id: '625172584'
product: rm
source: tdn-rm
title: FISCAL01-15862 - DT - Evento R-2010 - Classificação CNO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625172584
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF - RM |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15862 |

## **02. SITUAÇÃO/REQUISITO**

INTERPRETAÇÃO DE DEMANDA:  
Cliente informa que ao enviar o evento R-2010 da Reinf as informações relacionadas ao CNO estão indo com inconsistência para o E-CAC.

Geração da Issue de legislação para tratativa de acordo com a central colaborativa abaixo:  
[https://centraldeatendimento.totvs.com/hc/pt-br/community/posts/360051966754-REINF-Gera%C3%A7%C3%A3o-do-REgistro-R2010-com-CNO-e-mais-de-um-CNPJ-](https://centraldeatendimento.totvs.com/hc/pt-br/community/posts/360051966754-REINF-Gera%C3%A7%C3%A3o-do-REgistro-R2010-com-CNO-e-mais-de-um-CNPJ- "Follow link")

BENEFÍCIOS ALCANÇADOS  
O Correto seria o Evento R2010 agrupar CNO e CNPJ, se tem 10 cnpj's faz 10 eventos R2010, com o mesmo CNO, porém com os CNPJS corretos.

## **03. SOLUÇÃO**

Ajuste para que seja verificado o CNPJ  do cli/for além do CNO na geração do R-2010 para agrupar os eventos.
