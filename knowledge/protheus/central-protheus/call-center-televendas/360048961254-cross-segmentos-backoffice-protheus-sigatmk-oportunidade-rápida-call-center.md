---
article_id: 360048961254
category: Call Center - Televendas
content_hash: 1a982af85a87ec51fe8e2a07603a68094baa207f6f6c6a3178ad696b8a0aad87
fetched_at: '2026-06-28T22:41:30.260597+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Oportunidade Rápida Call
  Center
type: support-article
updated_at: '2024-04-25T14:36:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048961254-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Oportunidade-R%C3%A1pida-Call-Center
---

**Dúvida**

Como ativar oportunidade rápida no Call Center (**TMKA271**)?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

Ao executar a rotina de Atendimento **Telemarketing(TMKA272)**, o Operador pode criar um agendamento (tarefa) através da funcionalidade de Envio da Tarefas.

Esta funcionalidade está disponível no caminho***Outras* Ações → Envio de Tarefas da tela do Atendimento Telemarketing**, e estas tarefas criadas ficam disponíveis no módulo Faturamento (SIGAFAT). Durante o acompanhamento do Atendimento Telemarketing, o operador pode inserir uma Ocorrência/Ação que, ao ser confirmada a sua finalização, gere uma Oportunidade através da funcionalidade Oportunidade Rápida.

Se o Operador do Atendimento Telemarketing criar uma nova atividade destinada ao vendedor que será responsável pela tal Oportunidade, esta atividade não é refletida na agenda do vendedor no módulo SIGACRM.

Desta forma, são necessárias as seguintes configurações:

1. Configure o parâmetro **MV\_CRMGAGE,** que possibilitará o controle desta nova funcionalidade. Caso este parâmetro não esteja configurado em seu ambiente, a rotina considerará como configuração padrão, o seu conteúdo igual a **2**. Por isso, configure este parâmetro conforme a sua necessidade de uso.

2. Cadastre uma **Ação** na rotina de **Cadastro das Ações** em **SIGATMK → Atualizações → Telemarketing → Ações**, que:

2.1. Gere uma **Oportunidade** (**UQ\_OPORTU = 1**) quando a **Ocorrência/Ação** for finalizada no **Atendimento Telemarketing;**

2.2. Permita a **seleção de um Usuário** **CRM** (**UQ\_USUCRM = 1**).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074320473)

3. Na rotina de **Manutenção do Atendimento Telemarketing**, o operador deverá finalizar a **Ocorrência/Ação**, alterando o seu status para **encerrado**. Em seguida, deve ser efetivada a sua gravação ao acionar o botão **Salva;****![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073121974)**
