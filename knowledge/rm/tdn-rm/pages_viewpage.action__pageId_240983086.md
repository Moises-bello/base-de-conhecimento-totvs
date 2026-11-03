---
content_hash: 10bccf2dda7e6aa3176e82d48c8dc94146cb4d1d97774f0b9765278c6245f275
fetched_at: '2026-06-29T00:08:10.836443+00:00'
page_id: '240983086'
product: rm
source: tdn-rm
title: ER_SAUHRM01-310_Painel_da_Farmárcia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240983086
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAÚDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAUHRM01 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-309 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-310 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-311 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Esta especificação tem como objetivo detalhar a nova melhoria à ser implementada, Um painel denominado, Painel da Farmácia, que tem como objetivo disponibilizar uma visão macro das requisições de medicamentos solicitadas via Prontuário Eletrônico (aprazamentos) e Movimentação de Estoque (requisições avulsas). Esta melhoria foi desenvolvida para ser utilizada através de um dispositivo com saída de vídeo (ex.: Monitor, TV, Tablet, etc) que possua acesso a um navegador (browser) de internet compatível com a tecnologias HTML5 (HTML, CSS3, JS). Este painel possuirá três grupos visões, buscando englobar os cenários correspondentes ao processo do Mapa de Dispensação.

## Definição da Regra de Negócio

**RN001 -**A funcionalidade deve disponibilizar mecanismo que possibilitem cadastrar as Faixas de Períodos para cada Filial e Local de Estoque , necessários para englobar os turnos do Local de Estoque, podendo assim, cadastrar a hora inicial e final do turno.

****RN002**-**Painel 01: Este painel deve disponibilizar as requisições onde a menor data de aprazamento encontra-se na Faixa de Período do turno atual.

* Requisições que foram solicitadas para aplicação imediata.
* Alterações que devem ser aplicadas no turno atual.

 **RN003****-**Painel 02: Este painel deve disponibilizar as requisições onde a menor data de aprazamento encontra-se na Faixa de Período do turno seguinte.

* Requisições que foram solicitadas para aplicação em diversos turnos.
* Alterações que devem ser aplicadas dentro do período do turno seguinte.

**RN004 -**Painel 03: Este painel deve disponibilizar as requisições que não possuem data e hora para a realização do aprazamento.

* Requisições com data entre o dia anterior e o final do dia atual.
* Requisições solicitadas através da rotina de Movimentação de Estoque.

**RN005 -** Todas as requisições devem ser exibidas com os seu número correspondente e com o tempo disponível para aplicação, exibindo em um contador regressivo que leva em consideração a data e hora atual em comparação com a data e hora do aprazamento.

**RN006 -**Todas as requisições devem ser exibidas com cores que levem em consideração  o tempo restante do contador regressivo. Estas cores devem representar três status (Em tempo, Alerta, Urgente).

**RN007 -** Os Painéis devem permitir a sua visualização de forma individual e/ou agrupada.

****RN008 -**** Os Painéis devem atualizar-se automaticamente a cada período de tempo, por exemplo, de 10 em 10 minutos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel da Farmácia | [Visualização] | [Frame HTML -> Painel da Farmácia -> Visão do Painel] | - |
| Faixa de Períodos | [Criação] | [Cadastros-> Outros Cadastros -> Faixa de Períodos] | RN001 |

***Exemplo de Aplicação:***

* *Criar Faixas de Períodos personalizadas de acordo com os turnos dos locais de estoque.*
* *Visualizar todas as requisições oriundas do Prontuário Eletrônico e do Local de Estoque em uma visão macro e intuitiva.*

***Tabelas Utilizadas***

* *SZFAIXAPERIODO – Faixas de Períodos.*
* *SZMOVIESTOQUE – Movimentação de Estoque.*
* *SZAPRAZAMENTO *–* Aprazamentos.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
