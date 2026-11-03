---
content_hash: faba1a80742a26ba9d556d3bd56abfa395cc9babb6f09d35fcbcd1cb28c0e6f1
fetched_at: '2026-06-29T00:08:42.466833+00:00'
page_id: '287073896'
product: rm
source: tdn-rm
title: ER SAUHRM03-973 Migração Registro de Atendimento - BPA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287073896
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar - RM | **Módulo** | Registro de Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM\_MIGRACAO | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-18 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-884 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-973 |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Este documento tem como objetivo especificar o requisito de Registrar lançamentos de BPA no Registro de Atendimento.

## Definição da Regra de Negócio

**Funcionalidade:**

Como um usuário do TOTVS Gestão Hospitalar com permissão de Registrar Atendimentos  
Eu quero lançar Registros de BPA para Pacientes Externos   
Para que seja possível manter o registro das ações ambulatoriais de forma consolidada.

**Cenário 01: Acessar os Registros de BPA **para atendimentos Externos****  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E o convênio do paciente é SUS  
E Selecionar um atendimento existente  
E o tipo de Atendimento seja EXTERNO  
E certificar que a sub-aba Registro de BPA está visível  
Quando clicar na sub-aba Registro de BPA  
Então exibir os Registros de BPA Existentes

**Cenário 02: Visibilidade da sub-aba Registros de BPA ****para atendimentos Externos com APAC******  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E o convênio do paciente é SUS  
E Selecionar um atendimento existente   
E o tipo de Atendimento é EXTERNO  
Quando há lançamentos APAC registrados para o atendimento  
Então certificar que a sub-aba Registro de BPA NÃO está visível

**Cenário 03: Visibilidade da sub-aba Registros de BPA para atendimentos Internos**  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E o convênio do paciente é SUS  
E Selecionar um atendimento existente   
E o tipo de Atendimento seja INTERNO  
Então certificar que a sub-aba Registro de BPA NÃO está visível

**Cenário 04: Inserir Registros de BPA**  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E o convênio do paciente é SUS  
E Selecionar um atendimento existente  
E o tipo de Atendimento seja EXTERNO  
Quando clicar na sub-aba Registro de BPA  
e clicar em novo registro  
e Certificar que os dados do paciente já estão preenchidos  
e preencher os dados obrigatários  
e clicar em Salvar  
Então o Registro de BPA deve ser inserido com sucesso

**Cenário 05: Visibilidade da sub-aba Registros de BPA para pacientes Não SUS**  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E o convênio do paciente não é SUS  
E Selecionar um atendimento existente   
E o tipo de Atendimento seja EXTERNO  
Então certificar que a sub-aba Registro de BPA NÃO está visível

\*Central de Atendimentos está disponível apenas na nova MDI, sendo necessário realizar a pesquisa da action pelo módulo Executar.

|  |  |  |
| --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Aba Registros de BPA | [Criação] | Central de Atendimento (tela principal - pesquisar via Action na nova MDI) / Aba Dados do Atendimento - Sub-aba Registro de BPA |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
