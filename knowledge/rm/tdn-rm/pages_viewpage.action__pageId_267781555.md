---
content_hash: d99ae7c5135a57743da1ad1fb8c003414a6d560b1448e816b3a02d2943d72987
fetched_at: '2026-06-29T00:08:19.336436+00:00'
page_id: '267781555'
product: rm
source: tdn-rm
title: ER_SAUHRM02-30_Pedido_de_exames_INTEGRAÇÃO_PEP_2.0_e_RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267781555
version: 110
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | GESTÃO HOSPITALAR - RM | **Módulo** | Prontuário Eletrônico / Unidade de Diagnóstico / Integrações |
| **Segmento Executor** |  | | |
| **Projeto1** | SAUHRM01 | **IRM1** | [SAUHRM01-389](http://jiraproducao.totvs.com.br/browse/SAUHRM01-389) |
| **Requisito1** | [SAUHRM02-30](http://jiraproducao.totvs.com.br/browse/SAUHRM02-30) | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-38 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

    Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Integração de Pedidos de Exames entre o PEP 2.0 e o RM quando há integração com sistema terceiros, como por exemplo outros sistemas de laboratório ou diagnóstico por imagem.

## Definição da Regra de Negócio

***RN001 -***Quando ocorrer uma solicitação de exame complementar através do Prontuário do Paciente em uma Unidade de Atendimento que estiver parametrizada para Integrações de Diagnóstico por Imagem e Integra PEP - Exames Complementares, deve ocorrer a integração para o sistema terceiro.

1. As seguintes integrações podem ser parametrizadas:
   1. Carestream
   2. Philips
   3. Tuxxon
   4. Pixeon
   5. Agfa

***RN002 -***Quando ocorrer uma solicitação de exame complementar através do Prontuário do Paciente em uma Unidade de Atendimento que estiver parametrizada para Integrações de Laboratório e Integra PEP - Exames Complementares, deve ocorrer a integração para o sistema terceiro.

1. As seguintes integrações podem ser parametrizadas:
   1. Softlab
   2. Matrix
   3. TCM - Esmeralda Visual
   4. Shift
   5. AgileWork
   6. Layout  Totvs
   7. AGFA

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrizar Unidade de Atendimento | [Parametrização] | Cadastros > Uso Geral > Unidades de Atendimento > Unid Atendimento**\*** > Integrações > Diagnóstico por Imagem | RN001 |
| Solicitação de Exames Complementares | [Alteração] | Prontuário > Paciente**\*** > Avaliações Complementares > Exame de Diagnóstico por Imagem\* | RN001 |
| Parametrizar Unidade de Atendimento | [Parametrização] | Cadastros > Uso Geral > Unidades de Atendimento > Unid Atendimento**\*** > Integrações > Laboratório | RN002 |
| Solicitação de Exames Complementares | [Alteração] | Prontuário > Paciente**\*** > Avaliações Complementares > Exame de Laboratório\* | RN002 |

***\***Selecionar um registro para seguir com as Opções de Menu*

***Exemplo de Aplicação:***

* *Exames Solicitados através do PEP 2.0 são integrados .*

***Tabelas Utilizadas***

* *SZUNIDATEND – Unidade de Atendimento*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
