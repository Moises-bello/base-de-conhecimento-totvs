---
article_id: 4409624492823
category: Manutenção de Ativos (SIGAMNT)
content_hash: 9d62696bbe849b99f18ef186a4e095e51bc7758f69faa6479a7822f47eca591c
fetched_at: '2026-06-28T22:42:34.141544+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Inclusão de Novas Tarefas em Ordem de Serviços
  Preventivas
type: support-article
updated_at: '2023-07-21T13:41:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409624492823-Manufatura-Linha-Protheus-MNT-Inclus%C3%A3o-de-Novas-Tarefas-em-Ordem-de-Servi%C3%A7os-Preventivas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16192884468631)*** Tempo aproximado para leitura: **00:02:20 min****Dúvida**Como adicionar uma tarefa não prevista em uma **Ordem de Serviço Preventiva**?  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para criar uma **O.S - Ordem de Serviço Preventiva** é necessário que se tenha uma **Manutenção - MNTA120**. Esta tem por objetivo controlar as manutenções preventivas e consequentemente irá determinar as tarefas, etapas, insumos e inclusive controlar as paradas necessárias para a ordem de serviço preventiva a ser executada.  
Sendo assim, as **Tarefas** que não forem informadas na **Manutenção** não poderão ser relacionadas à **O.S** **Preventiva** por não terem sido previstas no processo de manutenção do bem. Desse modo, tem-se certeza de que o executante da **Manutenção Preventiva** irá executar apenas as tarefas pré-definidas pelo planejador.  
  
Caso se deseje adicionar uma tarefa em uma **O.S Preventiva** para um bem é necessário adicionar tal tarefa na **Manutenção** do **Bem** referente a essa **O.S** para que seja possível seu uso nas **O.S Preventivas** já existentes e passar a gerá-las com tal **Tarefa**.  
 **Exemplo**Nesse caso temos uma **O.S Preventiva** relacionada a uma **Manutenção** que tem apenas a **Tarefa 0**, sendo assim ao gerar uma **O.S Preventiva** por essa manutenção temos uma **O.S** com a **Tarefa 0**.  
  
Em **Atualizações / Controle de Oficina / Manutenção / Manutenção - MNTA120**, criada a **Manutenção** a seguir:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409633501079)**

Em **Atualizações /** **Controle de Oficina / Ordem de Serviço / Manual - MNTA410**, criada a **O.S Preventiva** em relação a **Manutenção** acima:

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409633542039)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409633585047)**

Em **Atualizações / Controle de Oficina / Retorno de OS / Retorno Mod. 2 - MNTA435**, ao selecionar a **O.S** gerada percebe-se que é não é possível adicionar tarefas não previstas na **Manutenção**:

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409633627799)**

Em **Atualizações / Controle de Oficina / Manutenção / Manutenção - MNTA120**, adicionado uma outra **Tarefa** a **Manutenção** em questão:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409624440471)

Em **Atualizações / Controle de Oficina / Retorno de OS / Retorno Mod. 2 - MNTA435**, ao selecionar a **O.S** gerada percebe-se que agora é possível a inclusão da **Tarefas** informada na **Manutenção**:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409633687703)
