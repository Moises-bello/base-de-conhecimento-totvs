---
content_hash: afa7b9367dba017c0390b28ba3cc8b73312273bf0c34ee2bd762c73544723e35
fetched_at: '2026-06-29T00:08:23.860633+00:00'
page_id: '270095504'
product: rm
source: tdn-rm
title: ER_SAUHRM02-500_Monitor Clínico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270095504
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | GESTÃO HOSPITALAR - RM | **Módulo** | Monitor Clínico |
| **Segmento Executor** |  | | |
| **Projeto1** | SAUHRM02 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-504 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-500 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-562 |
| **Chamado2** |  | | |
| **País** | ( **X** ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Esta especificação tem como objetivo detalhar as melhorias à serem implementadas na ferramenta Monitor Clínico integrado ao produto TOTVS Gestão Hospitalar. A melhoria consiste-se em realizar ajustes na ferramenta Monitor Clínico para que a mesma esteja apta para utilização em ambiente de homologação. Tais melhorias visam aproximar as funcionalidades disponibilizadas pelo Monitor Clínico do cenário de negócio do centro cirúrgico com base nos usuários chave (Anestesistas). 

## Definição da Regra de Negócio

**RN001**- Na tela de pesquisa por pacientes é necessário informar o número do prontuário para realizar a pesquisa e não o código do paciente.

**RN002**- Após a monitorização do paciente o relatório da ficha anestésica deve impresso a partir do registro de informação de cirurgia do paciente monitorado.

****RN003****-O Monitor Clínico deve apresentar as informações referentes à pressão arterial do paciente, tanto no momento da monitorização quando no relatório gerado pela RN002.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Pesquisa de Paciente | [Alteração] | Login / Pesquisa de Paciente | RN001 |
| Relatório do Monitor Clínico | [Alteração] | Cuidados com o Paciente / Centro Cirúrgico / Registro de Informação de Cirurgia | RN002 |
| Monitorização do Paciente | [Alteração] | Login / Pesquisa de Paciente / Iniciar Monitorização | RN003 |

***Exemplo de Aplicação:***

* *Permitir a geração de um relatório de monitorização do paciente com todas as intercorrências e seus respectivos cenários.*
* *Registrar as ações tomadas em cada intercorrência do paciente.*

***Tabelas Utilizadas***

* MCT002\_PARAMETER: Tipos de sinais vitais a serem monitorados.
* MCT004\_SCENARIOALERT: Alertas.
* MCT014\_SCENARIOALERT\_ACTIONS

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
