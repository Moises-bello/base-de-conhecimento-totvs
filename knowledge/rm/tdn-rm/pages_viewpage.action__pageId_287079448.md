---
content_hash: d3d35649bf7a5bd8ed7325860b88be1d338853ec09ed7c3d7369727ae9f36b84
fetched_at: '2026-06-29T00:08:42.809754+00:00'
page_id: '287079448'
product: rm
source: tdn-rm
title: ER SAUHRM03-984 Validação do código do dependente (carteira convênio)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287079448
version: 103
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
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-948 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-984 |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Este documento tem como objetivo especificar o requisito de validação de dependente da carteira do convênio no Registro de Atendimento.

### Definição da Regra de Negócio

 

**Funcionalidade:**Como um usuário do TOTVS Gestão Hospitalar com permissão de Registrar Atendimentos  
Eu quero que seja validado a obrigatoriedade do campo código do dependente da carteira do convênio  
Para que os dados do registro de atendimento mantenham-se consistentes

 

**Story 01: Obrigar Código de Dependente no Registro de Atendimento**  
Abrir as Condições Contratuais com Convênios (Cadastros / Faturamento / Condições Contratuais com Convênios)  
E Selecionar uma Condição Contratual com Convênio  
Quando Clicar na Aba Parâmetros 1  
E marcar o checkbox Código Depdenente obrigatório  
E clicar em salvar  
Então o registro de condição contratual de ser salvo com sucesso

****Story**02: Validar Código de Dependente na Inclusão do Registro de atendimento no Formulário**

Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E Incluir um novo atendimento  
E preencher os campos obrigatórios  
E o convênio preenchido, está configurado para Obrigar Código de Dependente  
E sair do campo "Dep.:" sem preencher a informação  
Então apresentar a seguinte mensagem de alerta 'Código do dependente deve ser informado.'

****Story**03: Validar Código de Dependente na Inclusão do Registro de atendimento no Server**  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E Incluir um novo atendimento  
E preencher os campos obrigatórios  
E o convênio preenchido, está configurado para Obrigar Código de Dependente  
E salvar o registro sem que o campo "Dep.:" esteja preenchido  
Então apresentar a seguinte mensagem de alerta 'Código do dependente deve ser informado.'

****Story**04: Validar Código de Dependente na Edição do Registro de atendimento no Formulário**  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E selecionar um atendimento existente  
E preencher os campos obrigatórios  
E o convênio preenchido, está configurado para Obrigar Código de Dependente  
E sair do campo "Dep.:" sem preencher a informação  
Então apresentar a seguinte mensagem de alerta 'Código do dependente deve ser informado.'

****Story**05: Validar Código de Dependente na **Edição**do Registro de atendimento no Server**  
Abrir a Central de Atendimentos\*  
E Pesquisar um paciente  
E selecionar um atendimento existente  
E preencher os campos obrigatórios  
E o convênio preenchido, está configurado para Obrigar Código de Dependente  
E salvar o registro sem que o campo "Dep.:" esteja preenchido  
Então apresentar a seguinte mensagem de alerta 'Código do dependente deve ser informado.'

 

|  |  |  |
| --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Dados do Atendimento | [Alteração] | Central de Atendimento (tela principal - pesquisar via Action na nova MDI) / Aba Dados do Atendimento |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
