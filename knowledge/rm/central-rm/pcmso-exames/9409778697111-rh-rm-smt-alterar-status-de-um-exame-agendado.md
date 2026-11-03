---
article_id: 9409778697111
category: PCMSO / Exames
content_hash: 575f2e29cdcfa626b5c83e238f1c211cac054195e880ae95e9224b573bc7bea0
fetched_at: '2026-06-28T22:47:42.130730+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT - Alterar status de um exame agendado
type: support-article
updated_at: '2025-11-24T17:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9409778697111-RH-RM-SMT-Alterar-status-de-um-exame-agendado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036951408791) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como alterar o status de um exame agendado de pendente para realizado ou cancelado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - **Todas as versões.**  
  
**Solução**Para alterar o status de um exame agendado siga os passos abaixo:

* **Alterar para Não Realizado**:  
  - Acesse o menu **PCMSO | Agenda de Exames** e selecione o(s) exame(s) desejado(s) que esteja com o status pendente e acesse a opção **Processos | Concluir Agendamentos como Não Realizados**. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611326290455)- Ao aparecer a mensagem: *Tem certeza que deseja concluir os agendamentos selecionados com a situação 'Não Realizada'?*, clique em **Sim**.   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611372484631)  
    
  - Após finalizar a execução do processo, o status vai esta alterado para **Não Realizado**.   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611372485399)
* **Alterar para Realizado:**  
  - Acesse o menu **PCMSO | Agenda de Exames** e selecione o(s) exame(s) desejado(s) que esteja com o status pendente e acesse a opção **Processos | Assistente Lançamento Exames**:   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611372486167)  
  - Ao abrir o assistente clique em avançar e no passo **Definir dados da consulta clinica para analise dos exames** informe os dados da consulta como: **código, tipo de consulta, data, nome e registro do médico**.  
    
  **Observação:** Se o exame estiver vinculado a uma Consulta, o processo não vai iniciar com a etapa "Dados da Consulta". E ao final da execução do processo, a Consulta poderá ter o seu status alterado.    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611326296983)  
    
  - No passo de **Seleção de Exames,** será carregado o exame conforme o informado na agenda.   
  Para inserir o resultado do exame, basta dar um **duplo clique sobre o nome do exame desejado**, o sistema irá abrir uma janela para que os dados do exame sejam preenchidos.    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611326298135)Os campos tipo de exame, data do exame e entidade são de preenchimento obrigatório. Caso algum dos exames selecionados para o lançamento não tenha os dados do resultado preenchido, o assistente não permitirá avançar para o próximo passo.  
    
  Ao concluir o lançamento dos exames e inclui um registro com os dados da consulta e os exames realizados no Prontuário do funcionário. E na agenda de exames ele irá ficar como realizado.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611372495127)  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31611372497175)

**Saiba Mais**

Para maiores informações, acesse: 

- [Exames](https://tdn.totvs.com/display/public/LRM/Exames)

- [Agenda de Exames](https://tdn.totvs.com/display/public/LRM/Agenda+Exames)

- [Assistente Lançamento de Exames](https://tdn.totvs.com/pages/releaseview.action?pageId=452719650)
