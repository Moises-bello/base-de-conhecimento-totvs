---
content_hash: eab3cabedfc1c2472320624f070ce462886f495346bf17ae3b77ae2f31aa673e
fetched_at: '2026-06-29T00:08:39.109270+00:00'
page_id: '286010086'
product: rm
source: tdn-rm
title: ER_PEP2_Dados_de_antropometria
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PEP2_Dados_de_antropometria
version: 100
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | [R\_SAU\_HRM1617](http://jiraproducao.totvs.com.br/browse/SAUHRM02) | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | [SAUHRM02-1255](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1255) | **Subtarefa1** | [SAUHRM02-1271](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1271) |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Este documento tem como objetivo especificar o requisito que trata da disponibilização de um novo tipo de item de enfermagem denominado "Antropometria". Este novo tipo servirá para mensurar medidas do paciente na integração entre RM Saúde e PEP 2. Os itens cadastrados no RM Saúde aparecerão em um painel específico para dados de antropometria dentro do PEP 2.

 

### (Obrigatório)

## Definição da Regra de Negócio

**RN001-** Disponibilizar um novo tipo para o cadastro de itens de enfermagem no RM Saúde chamado "Antropometria"

**RN002-** Implementar na integração entre RM Saúde e PEP 2 a parte que carrega os dados de antropometria. No PEP 2, existe um painel específico para informar as medidas de antropometria do paciente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de itens de enfermagem | [Alteração] | [Cadastros -> Cuidados com o paciente -> Prescrição Médica -> Itens da Enfermagem] | Novo tipo: Antropometria |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
