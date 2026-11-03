---
content_hash: 0d60246f46bbee55ff7d5e8d6211d6baa18b373fd61becd03f53037f2d61d648
fetched_at: '2026-06-29T00:06:25.916351+00:00'
page_id: '224451015'
product: rm
source: tdn-rm
title: ER_PCREQ-9951_Restrições_por_Grupo_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224451015
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Saúde |
| **Projeto1** | PDR\_SAU\_V12 | **IRM1** | PCREQ-9841 |
| **Requisito1** | PCREQ-9951 | **Subtarefa1** | SAU\_DEV-4132 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Criar grupos de exames e restringir o agendamento destes grupos. 

Um exame pode fazer parte de vários grupos e, ao agendar, o sistema deve verificar se a quantidade de exames que pertencem ao grupo foi ultrapassada e restringir o agendamento.

### (Obrigatório)

## Definição da Regra de Negócio

Permitir a criação de grupos de exames.

Ao criar um grupo, é possível inserir vários exames que irão compor este grupo. Neste cadastro, é possível informar a quantidade máxima de exames por dia.

Um exame pode fazer parte de vários grupos.

Ao agendar um exame, o sistema valida todos os grupos nos quais o exame está contido. Para cada um destes grupos, o sistema valida se a quantidade já agendada (incluindo os outros exames contidos no grupo) é maior que a definida no cadastro do grupo de exames. Caso ultrapasse a quantidade máxima, o sistema emite um alerta e não permite o agendamento.

Caso a quantidade máxima do grupo seja definida para "0" (zero), a quantidade é ilimitada, ou seja, o sistema não irá restringir o agendamento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
