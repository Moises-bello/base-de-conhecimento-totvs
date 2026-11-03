---
content_hash: 4dcba1c5529da4cebf2c6f05da491063842ad1cfa6f1bf8f47af52468badee8f
fetched_at: '2026-06-29T00:08:27.836760+00:00'
page_id: '271647366'
product: rm
source: tdn-rm
title: ER SAUHRM02-588 Agendar Exames com melhor distribuição entre as agendas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271647366
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM/EPIC1** | SAUHRM02-481 |
| **Requisito/Story/Issue** | SAUHRM02-588 | **Subtarefa** | SAUHRM02-599 |
| **Chamado/Ticket** | 198251 | | |
| **País** | ( X  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

  *Este documento tem como objetivo especificar o requisito de Agendar Exames com melhor distribuição entre as agendas dos médicos.*

### Definição da Regra de Negócio

 **RN001 -**  Criar parâmetro geral na aba Registro e Controle III, "Não agrupar por agendas no agendamento de Exames"  para utilizar a rotina  e "Não identificar agenda no agendamento de Exames " para ocultar o nome do médico executante do agendamento.

**RN002 -**  No Agendamento de Exames, ao marcar o parâmetro, exibir os horários para agendamento agrupados por exames, datas e horários disponíveis.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gerais | [Alteração] | [Opções-> Parâmetros -> Parâmetros Gerais] | **RN001** |
| Agendamento de Exames | [Alteração] | [Atendimento -> Agendamento -> Agenda de atendimentos ] | **RN002** |

### Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
