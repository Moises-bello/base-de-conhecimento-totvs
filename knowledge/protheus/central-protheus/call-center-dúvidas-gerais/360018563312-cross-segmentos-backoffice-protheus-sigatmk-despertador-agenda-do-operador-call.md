---
article_id: 360018563312
category: Call Center - Dúvidas Gerais
content_hash: e2b2f44b8fe1231e2505915b0df4af7273d1e00cd658537e3d6b797f17e7014e
fetched_at: '2026-06-28T22:41:26.657715+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Despertador Agenda do Operador
  (Call Center)
type: support-article
updated_at: '2024-04-25T13:15:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018563312-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Despertador-Agenda-do-Operador-Call-Center
---

**Dúvida**

Como configuro o despertador?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**Para configurar, realize os seguintes passos:

**1.** Criar uma Lista de Contato / Lista de Cobranças;

**2.** Operador deverá possuir o mesmo perfil de atendimento (**U7\_TIPOATE**) do configurado na lista (**U4\_TIPO**);

**3.** No Schedule, Configurador, criar Agente através do configurador em Ambiente → Schedule → Schedule → Agent;

**4.** No Configurador → Ambiente → Schedule → Schedule → pasta Agendamentos → Cadastro: Configurar a execução da função **TMKLEMBRE** conforme a necessidade. No campo rotina não é necessário passar por parâmetro empresa / filial na versão. Esta informação deverá ser informada no campo Empresa/Filial;

**5.**No Configurador: Habilitar o parâmetro **MV\_WFMESSE** = .T.;

**6.** É necessário introduzir no menu do módulo SIGATMK a rotina Messenger (WFATASKRMT) para recebimento das mensagens;

**7.** Após identificar no Monitor do Schedule a execução do TMKLEMBRE como finalizada, acessar a função Messenger.

**IMPORTANTE**: Acesse o ambiente do Call Center na rotina Messenger (WFATASKRMT) e deixe a tela **Gerenciador de Tarefas** ativa para visualizar as pendências do Operador.

Clique em **Mensagens /Itens em Aberto** para visualizar informações sobre a Lista ou Pendências da Agenda.

**Saiba mais:**

**[Despertador - Agenda do Operador (Call Center) - P12](https://tdn.totvs.com/x/X4blG)**
