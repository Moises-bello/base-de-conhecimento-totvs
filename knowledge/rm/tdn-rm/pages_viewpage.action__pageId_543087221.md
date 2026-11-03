---
content_hash: 06a10725a3a64240095f5640c91595045b7c447989e27a69e19a05b2eeb93f85
fetched_at: '2026-06-29T00:10:38.056312+00:00'
page_id: '543087221'
product: rm
source: tdn-rm
title: DEDUMOBILE-2909 DT Erro ao selecionar Menu Acadêmico no App EduConnect - Colégio
  Unilavras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543087221
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | APP Meu eduCONNECT |
| Função: | Acadêmico |
| Ticket: | [8352432](https://totvssuporte.zendesk.com/agent/tickets/8352432 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

O Cliente possui integração do RM com LDAP, sendo que ao invés de realizar login no eduCONNECT com um usuário da GUSUARIO, ele loga com um usuário de rede, com isso ao realizar login no educonnect com o usuário de rede e navegar pela parte acadêmica está exibindo um erro, pois está dando erro com o usuário que guardamos.

## **03. SOLUÇÃO**

Otimizado o processo para que seja possível realizar o login no App Meu eduCONNECT quando existir a integração com LDAP.
