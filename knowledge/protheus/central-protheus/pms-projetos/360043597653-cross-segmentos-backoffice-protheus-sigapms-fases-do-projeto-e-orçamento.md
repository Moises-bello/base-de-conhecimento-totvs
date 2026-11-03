---
article_id: 360043597653
category: PMS - Projetos
content_hash: e10100d79339ac4d5e4c1c9bd69b1c5f4c20064649fda00ae0880a1ad916b7d4
fetched_at: '2026-06-28T22:37:14.905552+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Fases do Projeto e Orçamento
type: support-article
updated_at: '2024-02-23T11:50:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043597653-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Fases-do-Projeto-e-Or%C3%A7amento
---

**Dúvida**

Descritivo de cada fase do Orçamento e Projeto

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80  
  
**Solução**O Gestão de Projetos permite que sejam definidos status para os Orçamentos, cada Status, também chamado de fase, possui propriedades, que são definidas no cadastro de Fase, assim, podemos dizer que a Fase é o modelo de negócio utilizado, para a elaboração de Orçamentos.

**Fases default do Orçamento :**

01. Orçamento Atualizado : Este orçamento se encontra em fase de atualização e não poderá gerar projeto.  
02. Orçamento Aprovado : Este orçamento já foi aprovado, esta aguardando a geração do projeto e não poderá ser mais alterado  
03. Orçamento Rejeitado : Este orçamento foi rejeitado e não poderá ser mais alterado.   
04. Orçamento em Projeto : Este orçamento já gerou um projeto para execução e não poderá mais ser alterado."

**Fases default do Projeto:**

01. Projeto em Atualização : Opção invalida nesta fase do projeto  
02. Aprovado em Planejamento : Este projeto esta em fase de planejamento e não poderá ser alterado  
03. Aprovado em Execução : Este projeto já se encontra em execução. Verifique a fase atual do projeto  
04. Projeto Finalizado Executado : Este projeto já foi finalizado e não poderá ser mais alterado  
05. Projeto Aguardando Liberação : Este projeto esta aguardando liberação e não poderá ser alterado nesta momento;

![fases.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4405940967575)

**Operações não Permitidas com Fases em Elaboração :**

- Modificar a estrutura do projeto (criar e eliminar tarefas, EDTs, recursos de cada tarefa, etc.);  
- Agrupar tarefas em diferentes EDTs, associar as tarefas umas com outras, etc.;  
- Associar documentos;  
- Iniciar e finalizar revisões;  
- Etc.

- Fazer qualquer apontamento, tanto de planificação como de execução;  
- Apontar datas reais de progresso das tarefas;  
- Gerar planejamentos

**Operações permitidas : Fase de aprovação do projeto:**  
- Modificar datas e durações das tarefas;  
- Modificar despesas das tarefas;  
- Modificar alocação de recursos nas tarefas;  
- Modificar relacionamentos entre tarefas;  
- Etc.  
**Operações não permitidas:**  
- Modificar a estrutura do projeto (criar e eliminar tarefas, EDTs, recursos de cada tarefa, etc.);  
- Fazer qualquer apontamento, tanto de planificação como de execução;  
- Apontar datas reais de progresso das tarefas;  
- Etc

Tabela : AEA - Fases do Projeto

**Detalhes em :**[PMS0035 - Fases\_do\_Projeto\_e\_Orçamento](https://tdn.totvs.com/x/UsIYI)
