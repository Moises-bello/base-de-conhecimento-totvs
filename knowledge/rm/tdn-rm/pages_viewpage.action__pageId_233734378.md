---
content_hash: 451b8ae6342301cf94f1cfaa96b6313086bd025bc567d644265526f6534d21c1
fetched_at: '2026-06-29T00:06:27.528398+00:00'
page_id: '233734378'
product: rm
source: tdn-rm
title: ER_ PCREQ-9986_Duplo_Click_Painel_Classificação_de_Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233734378
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Duplo Click no Painel de Classificação de Risco (Painel de Atendimento Médico)

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-9983 |
| **Requisito1** | PCREQ-9986 | **Subtarefa1** | SAU\_DEV-4176 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

O objetivo desta implementação é estabelecer as ações que o médico pode realizar ao dar um duplo clique sobre um determinado paciente no painel de classificação de risco.

Esta ação tem como finalidade evitar que um paciente seja chamado no painel, quando o médico não tiver esta intenção.

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel de Classificação de Risco | [Alteração] | Atendimento -> Pronto Atendimento/Ambulatório -> Painel de Classificação de Risco | RN01 |

**RN01: Ações disponíveis no duplo clique na grid**

Quando o médico der um duplo clique num determinado paciente da fila de atendimento, o sistema deverá exibir uma tela com as seguinte opções:

* Chamar: fará a chamada do paciente no painel de chamados se ainda não estiver em atendimento
* Somente Abrir o Prontuário: abre o prontuário do paciente para que o médico visualize algum dado anterior a este atendimento
* Cancelar: fecha a tela com as opções

### Opcional

## Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
