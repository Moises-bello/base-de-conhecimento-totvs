---
content_hash: 66c9a0036fcde431c9eecce2a6b417690419901fbc29ca5515759e38f5324277
fetched_at: '2026-06-29T00:08:34.971106+00:00'
page_id: '274856283'
product: rm
source: tdn-rm
title: ER Resultados de Exames Tuxxon no PEP 2
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+Resultados+de+Exames+Tuxxon+no+PEP+2
version: 106
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | Unidade de Diagnóstico |
| Segmento Executor | Saúde |  |  |
| Projeto | SAUHRM02 | IRM | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-73 |
| Requisito | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-745 | SubTarefa | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-776 |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |

   

## Objetivo

 Possibilitar a integração de exames de imagem Tuxxon com o PEP 2, através do módulo de resultados online.

## Definição da Regra de Negócio

*RN001 - Solicitação de exames de imagem, em unidades de atendimento integradas com Tuxxon e  PEP 2 deve-se permitir acessar o resultado através dos resultados online.*

*RN002 - Solicitação de exames de imagem, em unidades de atendimento integradas com Tuxxon e PEP 2 deve-se acessar o resultado através dos resultados online.*

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Unidade de Diagnóstico / Solicitações de Exame | [Alteração] | Unidade de Diagnóstico / Pedidos de Exame | RN001 |
| RM.Sau.Integracoes | [Alteração] |  | RN002 |
| RM.Sau.UnidadeDiagnostico | [Alteração] |  | RN002 |

***Exemplo de Aplicação:***

* *Realizar a solicitação de exames através do PEP RM / PEP2 e visualizar o resultado através dos respectivos prontuários.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
