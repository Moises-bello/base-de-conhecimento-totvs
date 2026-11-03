---
content_hash: a043a58619300be5b66aff675faf6df249a6bcbb225ae67e7f42fb9407eaf966
fetched_at: '2026-06-29T00:06:24.048987+00:00'
page_id: '224110716'
product: rm
source: tdn-rm
title: ER_PCREQ-4656_Farmácia_OFFLINE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224110716
version: 123
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Saúde |
| **Projeto1** | PDR\_SAU\_V12 | **IRM1** | [PCREQ-4653](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-4653 "PCREQ-4653") |
| **Requisito1** | [PCREQ-4656](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-4656 "PCREQ-4656") | **Subtarefa1** | SAU\_DEV-2044 |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### (Obrigatório)

## Objetivo

 Permitir o processamento de requisições mesmo com a integração de estoque com o EMS ou Protheus inativa.

### (Obrigatório)

## Definição da Regra de Negócio

1. Ao perceber que a integração do estoque entre RM e EMS ou Protheus esteja instável ou inativa, é necessário habilitar o parâmetro "Estoque OFFLINE" disponível em: "Opções/Parâmetros/Integração RM Nucleus" aba "Geral"
2. Com o parâmetro marcado, ao acessar as telas "Movimentação de estoque", "Mapa de dispensação" e suas respectivas telas de edição, será exibida uma label informando que o estoque encontra-se offline
3. Com o estoque offline, ao processar uma requisição os itens são lançados na conta e o aprazamento é liberado normalmente mas a requsição é marcada com o status "Offline" e não é realizada a baixa no estoque. A baixa só será realizada quando a integração com o EMS  ou Protheus for reativada e o usuário realizar novamente o processamento da requisição.
4. Ao tentar processar uma requisição no modo offline que já tenha sido processada, o sistema exibirá um aviso informando que só é possível processar novamente com a integração Online.
5. Quando a integração for reativada, deve-se desmarcar o parâmetro descrito no item 1 e realizar o processamento das requisições marcadas como "OFFLINE". O processamento seguirá normalmente apenas para a baixa no estoque, já que os lançamentos e aprazamentos foram liberados anteriormente.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
