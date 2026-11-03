---
content_hash: 0ae82ea742d6e2f0dcef8a2ad67e0e41d1af6b7668af4ad53920b4bc7245da49
fetched_at: '2026-06-29T00:10:30.917594+00:00'
page_id: '520120242'
product: rm
source: tdn-rm
title: DEDUMOBILE-2453 DT Contexto do EducaMobile não carrega quando o professor loga
  em uma coligada que ele não tem permissão no educacional.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520120242
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Gestão Educacional |
| Módulo: | TOTVS Educa Mobile |
| Função: | Acesso ao contexto |
| Ticket: | 7028177 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2453](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2453) |

## **02. SITUAÇÃO/REQUISITO**

Quando o professor loga no portal em uma coligada que ele não tem permissão no educacional e depois tentar logar no TOTVS Educa Mobile o portal não carrega o contexto para o professor ficando preso o último acesso dele.

## **03. SOLUÇÃO**

Otimizado a validação de contextos educacionais permitidos a um usuário em coligadas diferentes. 

Quando o usuário tiver acesso a pelo menos um contexto educacional válido, o usuário terá acesso a funcionalidade do educacional ao acessar o TOTVS Educa Mobile independente do acesso ao Portal Corpore.Net.

Para ter o acesso ao TOTVS Educa Mobile, o usuário professor, deverá ter acesso: a SUSUARIOFILIAL e GPERMIS.

Uma vez que o usuário não tem acesso ao contexto educacional, será apresentado a mensagem: "Sem acesso a um contexto educacional válido! "
