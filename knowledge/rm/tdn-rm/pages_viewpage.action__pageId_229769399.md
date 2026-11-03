---
content_hash: 3b4104834a9dacea2176bfd41ae9c47ba9269a2749d3b45470923fb1d5449554
fetched_at: '2026-06-29T00:06:27.019370+00:00'
page_id: '229769399'
product: rm
source: tdn-rm
title: ER_PCREQ-9984_Painéis_de_Chamados_Simultâneos_para_uma_mesma_UNIDADE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=229769399
version: 126
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9983](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9983 "PCREQ-9983") |
| **Requisito** | * [PCREQ-9984](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9984 "PCREQ-9984") | **Subtarefa** | * [SAU\_DEV-4164](http://jira.totvs.com.br/browse/SAU_DEV-4164) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

    O objetivo desta implementação é alterar o funcionamento do Painel de chamados, fazendo com que as senhas chamadas através do Painel de Classificação de Riscos sejam simultaneamente exibidas, em todos os Painéis de Chamados conectados. 

## Definição da Regra de Negócio

**RN001 -**Quando uma senha for chamada através do Painel de Classificação de Riscos, todos os browsers que estiverem conectados ao painel, na respectiva unidade de atendimento, deverão receber e exibir a senha requisitada, simultaneamente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Painel de Chamados] | [Alteração] | - | - |

**Exemplo de Aplicação:**

* Cadastrar um novo Totem através do menu "***Cadastros> Registro e Controle >******Totem***";
* Acessar o menu "***Atendimento > Pronto Atendimento/Ambulatório > Painel de Classificação de Riscos***";
* Incluir um plantão para o dia atual e unidade de atendimento que esteja cadastrada no Totem;
* Acessar o menu "***Atendimento > Pronto Atendimento/Ambulatório > Totem de Pronto Atendimento***";
* Selecionar a unidade desejada e chamar algumas senhas;
* Abrir vários painéis, selecionar a(s) unidade(s) desejada(s) e clicar em  "***Acessar***";
* Acessar novamente o "***Painel de Classificação de Riscos"*** e Chamar a senha desejada (Dependendo da parametrização, a chamada se dará através de um duplo clique)***.***
* Verificar os painéis abertos. Todos deverão ser atualizados conforme a senha chamada.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
