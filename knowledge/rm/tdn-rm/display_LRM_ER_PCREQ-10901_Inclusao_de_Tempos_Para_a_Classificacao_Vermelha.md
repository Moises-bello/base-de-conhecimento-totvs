---
content_hash: c5b40dfa16dd01f41a28b74e5124693393addca775f83ce67497b2746338c65c
fetched_at: '2026-06-29T00:08:07.882425+00:00'
page_id: '237395195'
product: rm
source: tdn-rm
title: ER_PCREQ-10901_Inclusao_de_Tempos_Para_a_Classificacao_Vermelha
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10901_Inclusao_de_Tempos_Para_a_Classificacao_Vermelha
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10841 "PCREQ-10841") |
| **Requisito** | * [PCREQ-10901](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10901 "PCREQ-10901") | **Subtarefa** | * [SAU\_DEV-4793](http://jira.totvs.com.br/browse/SAU_DEV-4793) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Este documento tem como objetivo a especificação do requisito de Inclusão de Tempos para a Classificação Vermelha, no Painel de Classificação de Risco do TOTVS Gestão Hospitalar.

## Definição da Regra de Negócio

 **RN001**

* Na tela de Parâmetros Gerais, criar um parâmetro na aba de Registro e Controle, que servirá para determinar se o novo comportamento estará ativo ou não.

    **RN002**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Exemplo de Aplicação:**

1. Acesse o menu "Atendimento > Pronto Atendimento/Ambulatório > Painel de Classificação de Risco";
2. Selecione a Unidade de Atendimento e o Médico;
3. Caso não exista, inclua um novo plantão para o médico desejado (aba Plantão), bem como a especialidade atendida pelo médico;
4. Acesse o menu "Cadastro > Registro e Controle > Totem" e cadastre um novo Totem, associando a unidade de atendimento desejada;
5. Acesse o menu "Atendimento > Pronto Atendimento/Ambulatório > Totem de Pronto Atendimento";
6. Clique sobre o a unidade desejada e chame algumas senhas;
7. Acesse o menu "Atendimento > Pronto Atendimento/Ambulatório > Painel de Classificação de Risco";
8. Na aba "Registro de Triagem", dê um duplo clique sobre uma das senhas chamadas;
9. Preencha os dados obrigatórios, classificando como Emergência e clique em Salvar;
10. Acesse a aba "Registro de Atendimento";
11. Dê um duplo clique sobre o registro que está com a classificação vermelha;

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
