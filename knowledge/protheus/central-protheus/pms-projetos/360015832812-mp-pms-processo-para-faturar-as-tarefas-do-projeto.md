---
article_id: 360015832812
category: PMS - Projetos
content_hash: 70550c067476f586164baa82f2e5601dd71b53ac5b762fa3d160de79709f008c
fetched_at: '2026-06-28T22:37:15.040753+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - Processo para faturar as Tarefas do Projeto
type: support-article
updated_at: '2021-04-29T21:12:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015832812-MP-PMS-Processo-para-faturar-as-Tarefas-do-Projeto
---

**Dúvida**

Processo para Faturar as Tarefas do Projeto  
   
 **Ambiente**

Microsiga Protheus - A partir da versão 11.80  
   
**Solução :**

Para gerar um faturamento através do SigaPMS, efetue o seguinte processo:

1. Alterar a estrutura da tarefa e deixar o campo **AF9\_FATURA**=SIM este campo está localizado na aba Vendas/Remessas.
2. Entre na rotina **PMSA600** Atualização - Projetos- Med.Vendas/Remessa, selecione o projeto e clique no botão Faturar, abrirá a tela Med.Vendas/Remessa mostrando o projeto.
3. Selecione a tarefa que irá faturar ou posicione o projeto, após isto informe o % a ser faturado ou o valor - clique no botão adicionar e confirmar para gerar o pedido de venda.
4. São levados para o pedido de venda os produtos mencionado na **AFA\_PRODUT.**

Acesse a FAQ para visualizar os detalhes:  **[Processo para Faturar o Projeto](http://tdn.totvs.com/display/PROT/PMS0003_Processo+para+Faturar+o+Projeto%C2%A0)**
