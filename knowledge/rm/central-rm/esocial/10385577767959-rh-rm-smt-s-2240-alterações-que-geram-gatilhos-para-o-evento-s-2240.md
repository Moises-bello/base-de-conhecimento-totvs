---
article_id: 10385577767959
category: eSocial
content_hash: ae7d6d7b3340376b962453dc280b4eeb59e3da5fb5a9ce019b56d3edbd93c9f1
fetched_at: '2026-06-28T22:47:39.087778+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: RH - RM - SMT - S-2240 - Alterações que geram gatilhos para o evento S-2240
type: support-article
updated_at: '2026-06-02T14:43:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10385577767959-RH-RM-SMT-S-2240-Altera%C3%A7%C3%B5es-que-geram-gatilhos-para-o-evento-S-2240
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16037019919895) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Quais alterações geram gatilhos para o evento S-2240?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir da versão **12.1.28**  
  
**Solução**  
Os gatilhos do evento S-2240 são gerados à partir de registros unitários e/ou registros massivos.  
  
Registros unitários são aqueles que alteram apenas um funcionário por vez. São eles:

* **Funcionário**  
  - Rescisão tipo Transferência
* **Alterações de Campos do Cadastro**  
  - Alteração de Função  
  - Alteração de Seção  
  - Alteração de Tomadores de Serviço
* **Posto de Trabalho**  
  - Vinculação e Desvinculação.

Registros Massivos são os registros que afetam um ou mais funcionários por alteração e consequentemente podem gerar vários registros na fila de eventos. São eles:

* **Alterações na Função**  
  - Incluir/Excluir um Quadro de Lotação  
  - Alteração das Informações sobre a Função  
  - Alteração na Descrição para o PPP  
  - Anexo Quadro de Lotação

* **Atividades**  
  - Inclusão/Exclusão de Atividade na Tarefa  
  - Inclusão/Exclusão de Atividade ao Quadro de Lotação  
  - Inclusão/Exclusão de Atividade na Função  
  - Inclusão/Exclusão de Atividade nas Funções do Posto de Trabalho

* **Tarefas**  
  - Alteração na Descrição das Tarefas  
  - Administração de Tarefas

* **Avaliações de Risco**  
  - Inclusão/Exclusão/Alteração em Avaliações de Risco (alteração apenas dos campos pertinentes ao eSocial)

* **Riscos**  
  - Alteração no Tipo de Agente  
  - Anexo EPI / EPC - Inclusão/Exclusão/Alteração  
  - Anexo Níveis de Risco  
  - Alteração no Limite de Tolerância  
  - Anexo EPI Nível de Risco - Inclusão/Exclusão/Alteração

* **Tipo de Agente Nocivo**  
  - Alteração do Tipo de Agente Nocivo eSocial

* **EPI**  
  - Alteração do CA ou Nome

* **Responsável pelos Registros Ambientais**  
  - Inclusão/Exclusão/Alteração de Responsáveis

* **Posto de Trabalho**  
  - Vinculação e Desvinculação através do Assistente  
  - Alteração na Descrição da Função do Posto

* **Alterações Globais de Campos do Cadastro**  
  - Alteração global de Função  
  - Alteração global de Seção  
  - Alteração global de Tomadores de Serviço

**Importante:**

* Todas as alterações que geram gatilhos massivos serão geradas via *JobServer*em *background*.
* Quando existir duas alterações na mesma data, ambos os gatilhos serão gerados com a operação Inclusão. O controle de retificação da tag <indRetif> será realizado na geração do XML.

**Saiba Mais**  
Para mais informações, acesse:

- [S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://tdn.totvs.com/pages/releaseview.action?pageId=469451357)

- [RH - RM - SMT - Gerar o evento S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007674022)
