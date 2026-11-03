---
content_hash: b32272d9b4c41bf6030e8a2f3e70bdf9381a6b045ab461b49ede296995183449
fetched_at: '2026-06-29T00:08:22.740146+00:00'
page_id: '269439381'
product: rm
source: tdn-rm
title: ER_SAUHRM02-324_Atendimento_-_Recepção_-_Dados_de_um_Paciente_-_NOME_SOCIAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269439381
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM-1617 |
| **Requisito** | SAUHRM02-324 | **Subtarefa** | SAUHRM02-354 |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Incluir campo para informar nome social em todas as telas em que é apresentado o nome do paciente para que seja feita a devida identificação.

## Definição da Regra de Negócio

 

RN001 - Incluir o campo na tela do prontuário RM, substituindo o campo de nome. Incluir na página identificação o campo Nome Social.

 

RN002 - Incluir o campo no relatório da prescrição, alterando o relatório interno e o relatório do book.

 

RN003 - Incluir o campo na tela de checagem da enfermagem, no cabeçalho e no botão, exibir preferencialmente o nome social quando existir.

 

RN004 - Tela de pesquisa de pacientes, alterar os campos de consulta e as telas de listagem de registros

 

RN005 - Na tela de agenda de atendimento, incluir o campo no grid de listagem, no relatório interno (concatenar o nome social entre parênteses) e na tela de edição

 

RN006 - Na tela de agenda de cirurgias, incluir o campo no grid de listagem e na tela de edição

 

RN007 - Tela de controle de ocupação de leitos, incluir o campo na pesquisa rápida pelo paciente e informações do leito

 

RN008 - Na tela de controle de leitos, ajustar o controle de visitantes e mudança de plantão

 

RN009 - No controle de pedido de exames, incluir o campo na grid de visualização de registros e na tela de edição

 

RN010 - Menu Tesouraria, incluir campo na tela de Controle de Solicitação p/ Emissão de Nota Fiscal / Recibos

 

RN011 - No Toten de pronto atendimento, dar prioridade para exibir o nome social

 

RN012 - No Painel da classificação de risco, incluir a coluna com o nome social em destaque, e na chamada do paciente utilizar o nome social

 

RN013 - Incluir o campo de nome social na tela de agenda online

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Prontuário Eletrônico do Paciente | Alteração | Prontuário | RN001, RN002, RN003 |
| Pesquisa Clientes e Atendimentos | Alteração | Diversos locais | RN004 |
| Agenda de Atendimento | Alteração | Atendimento/Agendamento/Agenda de Atendimentos | RN005 |
| Agenda de Cirurgia | Alteração | Atendimento/Agendamento/Agenda de Cirurgias | RN006 |
| Controle de Ocupação de Leitos | Alteração | Atendimento/Internação/Controle de Ocupação de Leitos | RN007, RN008 |
| Controle de Pedidos de Exames | Alteração | Unidades Diagnóstico/Controle de Pedidos de Exame | RN009 |
| Tesouraria | Alteração | Tesouraria/ Controle de Solicitação p/ Emissão de Nota Fiscal / Recibos | RN010 |
| Atendimento | Alteração | Atendimento/Pronto Atendimento / Ambulatório/Toten de Pronto Atendimento | RN011 |
| Atendimento | Alteração | Atendimento/Pronto Atendimento / Ambulatório/Painel de Classificação de Risco | RN012 |
| Agenda Online | Alteração | - | RN013 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
