---
content_hash: 8d787fef3e06b0d398b9f6b5ede3083657de142d4d2a0c17241f4e374a43f2ba
fetched_at: '2026-06-29T00:08:16.496155+00:00'
page_id: '247922904'
product: rm
source: tdn-rm
title: ER_SAUHRM01-341_Cota_extra_e_Data_de_controle_no_Controle_de_glosa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-341_Cota_extra_e_Data_de_controle_no_Controle_de_glosa
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Faturamento |
| **Segmento Executor** | RM | | |
| **Projeto1** | SAUHRM01 | **IRM1** | SAUHRM01-325 |
| **Requisito1** | SAUHRM01-326 | **Subtarefa1** | SAUHRM01-341 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 O objetivo deste documento é definir as regras e melhorias no controle de glosa, com a adição das informações de Cota-extra e data de controle.

### (Obrigatório)

## Definição da Regra de Negócio

**RN 01: Cota-extra e  Data de Controle**

A definição de conta-extra seria o valor que o convênio pagou a mais e que não foi identificado. Além do valor a maior que é identificado no controle de glosa, este campo servira para armazenar o valores que "sobrarem".

A data de controle normalmente seria a data em que o valor caiu na conta.

**RN 02: Glosa total com possibilidade de recurso**

O controle de glosa atual somente permite a glosa total com perda, ou seja, não é possível recursar os valores. Neste caso, é necessário implementar a funcionalidade de "Glosa total automática". Neste cenário, o sistema fará a glosa total de cada conta e possibilitará que as mesmas sejam recursadas.

O funcionamento deve ser o seguinte: Inicie o processo de glosa da fatura, selecione todas as contas e clique no botão “Glosa Total Automática”. Ele funcionará como a Liberação Automática.

Será solicitado a informação da Data de Controle.

**RN 03: Liberação automática com data de controle por conta**

Ao realizar a Liberação automática, o sistema deve solicitar a data de controle e o valor da cota-extra

**RN 04: Estorno de Cota-extra**

Uma vez identificado que uma conta possui valor de cota-extra, habilitar o botão de "Estorno de cota-extra", onde ao clicar, deve aparecer a mesma tela de "Conclusão de revisão da conta", com os campos: data do estorno, valor do estorno e usuário.

**RN 05: Data de entrada na grid de paciente**

Incluir a coluna Data de entrada do paciente na grid que exibe as contas da fatura.

**RN 06: Valor da conta na pesquisa dentro do controle de glosa**

Incluir o valor da conta na grid de Pesquisa Conta-Hospitalar, que é chamada da tela de Controle de Glosa, botão "Pesquisa Conta"

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Controle de Glosa | [Alteração] | Faturamento -> Controle de Glosa | RN01 a RN06 |

***Tabelas Utilizadas***

* *SZCONTROLEGLOSA - Controle de glosa*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
