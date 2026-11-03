---
content_hash: 94420d3de6a0ae7291290b5893060ea0b8ee46d4ee5b3395f350381e2a0447f1
fetched_at: '2026-06-29T00:08:38.873361+00:00'
page_id: '285670848'
product: rm
source: tdn-rm
title: ER_SAUHRM02-1272 - PEP x RM 12.1.16 - Aleta de Receitas, Atestados e Orientações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285670848
version: 106
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Gestão Hospitalar |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | [R\_SAU\_HRM1617](http://jiraproducao.totvs.com.br/browse/SAUHRM02) | **IRM/EPIC1** | SAU\_BACKLOG-1329 |
| **Requisito/Story/Issue1** | SAUHRM02-1261 | **Subtarefa1** | SAUHRM02-1272 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Implementar uma interface do PEP 2 para carregar os dados da instituição na integração com o PEP 2.

 

(Obrigatório)

## Definição da Regra de Negócio

Interface a ser implementada é a InstitutionWrapper. Nela contém os dados da instituição (Unidade de Atendimento) como CNPJ, endereço e contato. Estes dados serão coletados do prestador principal da unidade de faturamento.

Será implementada na camada de integração entre o RM Saúde e o PEP 2. Os dados serão exibidos nos receituários, atestados e orientações no PEP 2.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
