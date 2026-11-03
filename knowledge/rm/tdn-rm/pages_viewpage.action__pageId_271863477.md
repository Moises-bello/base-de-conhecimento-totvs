---
content_hash: f565f06dfd50cb6e686d06c9f6f945e17c8dca8c2f38919167a47fa09aea8d4f
fetched_at: '2026-06-29T00:08:28.875428+00:00'
page_id: '271863477'
product: rm
source: tdn-rm
title: ER SAUHRM02-743 Controle de Segurança em Atualização de Valores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271863477
version: 101
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Utilitários |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM2 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-744 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-743 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-753 |
| **Chamado** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

  Este documento tem como objetivo especificar o requisito de  inclusão de controles de segurança para o uso do utilitário de Atualização de Valores, que visa selecionar uma gama de contas, especificando um ou mais grupos de gasto que necessita-se atualizar valores conforme novas tabelas de valores utilizadas por convênios, facilitando estes ajustes que dispenderiam muito tempo a se fazer manualmente. 

   A Melhoria se faz necessária pois nem todas os usuários devem ter acesso a esta rotina pois esta age diretamente em valores a serem cobrados posteriormente. Dessa forma, após a implementação, será possível restringir usuários e o tipo de operações.

### (Obrigatório)

## Definição da Regra de Negócio

**RN001 - Parametrização**

Será criado um parâmetro que por default estará desmarcado para que as restrições de acesso somente se apliquem quando este for ativado (marcado). 

**RN002 - Atualização de Valores (MDI Antiga)**

Inclusão das rotinas de controle de acesso, conforme configuração prévia do usuário. Ou seja, se o parâmetro estiver marcado e quais grupos de gasto o usuário pode alterar valor e também se este terá permissão para alterar códigos e/ou valores de MatMed.

**RN002 - Atualização de Valores (MDI Nova)**

Inclusão das rotinas de controle de acesso no utilitário migrado para a nova MDI, conforme configuração prévia do usuário. Ou seja, se o parâmetro estiver marcado e quais grupos de gasto o usuário pode alterar valor e também se este terá permissão para alterar códigos e/ou valores de MatMed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrização | [Envolvida] | Opções -> Parâmetros / Parâmetros / Geral | **RN001** |
| Atualização de Valores (MDI Antiga) | [Alteração] | Utilitários -> Utilitários do RM Saúde / Atualização de Valores | **RN002** |
| Atualização de Valores (MDI Nova) | [Alteração] | Utilitários -> Atualização de Valores | **RN003** |

**Exemplo de Aplicação:**

* Marque o parâmetro para aplicar a segurança na rotina de Atualização de Valores;
* Acesse os perfis de usuário;
* Selecione o usuário a ser dadas as permissões;
* Acesse a aba "Acesso a Menus" e dê as permissões desejadas;.
* Acesse a rotina antiga de Atualização de Valores e verifique se a segurança foi aplicada, visualizando se as opções que foram dadas permissões estão habilitadas e as opções que o usuário não tem permissão estão desabilitadas para alteração.
* Acesse a rotina de Atualização de Valores migrada para a nova MDI e verifique se a segurança foi aplicada, visualizando se as opções que foram dadas permissões estão habilitadas e as opções que o usuário não tem permissão estão desabilitadas para alteração.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
