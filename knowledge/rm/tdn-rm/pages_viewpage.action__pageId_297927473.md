---
content_hash: 71a0297438f6d450f71b95d3461c9f446775d03eddf6bf0eac8f831b50fe1832
fetched_at: '2026-06-29T00:08:42.855887+00:00'
page_id: '297927473'
product: rm
source: tdn-rm
title: ER SAUHRM03-987 Tratamento para Validações de CPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=297927473
version: 95
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar - RM | **Módulo** | Registro de Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM\_MIGRACAO | **IRM/EPIC1** | <http://jiraproducao.totvs.com.br/browse/SAUHRM03-18> |
| **Requisito/Story/Issue1** | <http://jiraproducao.totvs.com.br/browse/SAUHRM03-961> | **Subtarefa1** | <http://jiraproducao.totvs.com.br/browse/SAUHRM03-987> |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Este documento tem como objetivo especificar o requisito de realizar as validações necessárias para CPF.

## Definição da Regra de Negócio

**RN001 -** **Verificar se CPF informado é válido**

Verificar se CPF informado é válido ao cadastrar um novo paciente.

**RN002 - Validar no Atendimento parâmetros referentes a CPF**

Ao salvar um atendimento para um paciente, verificar parâmetro se exige CPF tanto para paciente interno como para externo e verificar se foi informada a idade que o paciente é considerado maior de idade.

Para ambos os casos se o CPF não foi informado, deverá ser mostrada uma mensagem obrigando o preenchimento do CPF;

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Validar CPF informado | Alteração | Central de Atendimento / aba Paciente - botão Novo | **RN001** |
| Validar se CPF informado | Alteração | Central de Atendimento / aba Dados do Atendimento - Botão Salvar | **RN002** |

**Exemplo de Aplicação:**

**RN001**

* Acessara **Central de Atendimentos.**
* Na **aba Paciente**, clicar em **Novo.**
* Informar os dados obrigatórios e **o número de CPF inválido.**
* Clicar em **Salvar .**
* Emitir mensagem de CPF Inválido.

**RN002**

* Acessar **RMSaude.exe.**
* **Parâmetros / Parâmetros Gerais, aba Registro e Controle.**
* Informar valor para o campo **"Idade mínima para solicitação de CPF no registro de Atendimento (anos)".**
* Em **Cadastros / Faturamento / Condições Contratuais com Convênios,**selecionar um convênio.
* Na **aba Parâmetros 1**, marcar parâmetro **"Externos/Internos: exigir preenchimento CPF".**
* Acessar **RM.exe (nova MDI).**
* Acessara **Central de Atendimentos.**
* Localizar um paciente.
* Na aba **Dados do Atendimento**, **incluir** um novo atendimento **ou editar** um atendimento já existente.
* Salve o atendimento
* Se o parâmetro **"Externos/Internos: exigir preenchimento CPF"**estiver marcado e o paciente não possuir CPF informado deverá ser emitida uma mensagem informando a obrigatoriedade do mesmo no cadastro do paciente.
* Se o paciente possuir idade maior que a do parâmetro **"Idade mínima para solicitação de CPF no registro de Atendimento (anos)"** e não possuir CPF informado deverá ser emitida uma mensagem informando a obrigatoriedade do mesmo no cadastro do paciente.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
