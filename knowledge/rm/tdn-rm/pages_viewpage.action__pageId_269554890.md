---
content_hash: 7ed2bc21ecb3d79dcd3dafaf0933e05ac569a2da9e2d299d1638f334b8df9ef1
fetched_at: '2026-06-29T00:08:23.282733+00:00'
page_id: '269554890'
product: rm
source: tdn-rm
title: Aprovação_por_Workflow_Integração_TOTVS Aprovações e Atendimento_X_RMNucleus_BRA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269554890
version: 142
---

# Aprovação por Worflow(Fluxo de Trabalho) - Integração TOTVS Aprovações e Atendimento X RMNucleus

## Visão Geral do Programa

O WorkFlow (Fluxo de Trabalho) é um recurso implementado pelo RMNucleus X TOTVS Aprovações e Atendimento, com a finalidade **APROVAR / REPROVAR** atendimentos(TOTVS Aprovações e Atendimento), gerados pelos movimentos(RMNucleus), a partir, de etapas e fluxo de etapas pré-definidas pelo administrador .

## Descrição do Processo:

1. O usuário logado deve estar vinculado a um atendente no TOTVS Aprovações e Atendimento.
2. Parametrizar um tipo de movimento para utilizar aprovação por Workflow(1.1.XX), acessando os parâmetros do tipo de movimento na etapa Workflow;
3. Ao incluir/salvar um movimento parametrizado para utilizar aprovação por Workflow  (no RMNucleus),  será gerado um atendimento  no TOTVS Aprovações e Atendimento;
4. O atendimento gerado seguirá um fluxo de etapas de acordo com os critérios definidos Tipo de Atendimento. Basta clicar no botão Avançar Tarefa que o atendimento será encaminhado para a primeira etapa e assim por diante até o final(aprovado ou reprovado);
5. Caso o atendimento seja aprovado, o mesmo, estará disponível para ser faturado/recebido;
6. Caso haja, alteração do movimento o atendimento criado será substituído por um novo atendimento e o processo de aprovação retornará a sua etapa inicial.

## IMPORTANTE!!!

1. A aprovação existente não pode funcionar simultaneamente a aprovação por WorkFlow;
2. Se um tipo de movimento de solicitação de compras (1.1.01 por exemplo) estiver parametrizado para utilizar aprovação por WorkFlow, os movimentos inseridos somente estarão disponíveis para Cotação se forem aprovados no TOTVS Aprovações e Atendimento;
3. Os atendimentos gerados por movimentos que precisam de aprovação, deverão ser aprovados para que possam ser recebidos/faturados no RMNucleus;
4. Na visão de movimentos estará disponível um filtro para movimentos aprovados, não-aprovados e em aprovação para faturamento:
5. Enquanto o atendimento estiver percorrendo o fluxo, o mesmo pode ser repassado através do recurso de repasse livre, para qualquer atendente. Nesse caso, o atendimento sairá do fluxo e para que o atendimento retorne ao fluxo, o usuário deverá clicar no botão de comando Avançar Tarefa, o atendimento seguirá novamente o fluxo partindo da etapa em que parou;
6. Quando uma ocorrência já está no meio de um fluxo (já passou da primeira tarefa) e clicamos em "Avançar Etapa", o sistema apresentará (com base na tarefa atual) uma tela com uma caixa de seleção que é a condição de passagem. O atendente (usuário) deverá escolher uma das condições e a sua escolha definirá qual será a próxima tarefa (e quem irá receber a ocorrência) de acordo com o fluxo cadastrado;

## Cadastros Necessários:

## No Gestão de Relacionamento com o Cliente - TOTVS Aprovações e Atendimento**:**

Criando Atendente vinculado ao usuário:

Acessar Guia Atendentes e criar atendentes que participarão do processo de aprovação:

Criando o Tipo de Atendimento e Grupo de Atendimento:

Definindo as etapas:

Para cada etapa criada é possível configurar os seguintes itens de acordo com a necessidades:

Definindo o fluxo de etapas:

Para incluir novas etapas no fluxo, deve-se clicar em incluir novo:

 

Criando o Grupo de Atendimento:

Definindo a Classificação do Atendimento:

## Parametrização **RMNucleus:**

Acessar os parâmetros do tipo de movimento que deseja aprovação por Workflow, etapa **Workflow.**

**Tabelas Envolvidas:**

**TMOV |****TMOVATEND |****HATENDIMENTOBASE | HATENDENTE**

**Conteúdos Relacionados:**

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.Agilis.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.atendentes.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.atendimentos.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.tiposAtendimentos.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.GrupoAtendimentos.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.parametros.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.transferencia.aspx>

*Links dos principais conceitos e processos.*

*divs*
