---
article_id: 4409367498519
category: Movimento
content_hash: f55bff9235f3eea892dbe982dbe2083202d9697f3237e9f7ac826176f354d124
fetched_at: '2026-06-28T22:46:36.061310+00:00'
product: rm
section_id: 1500000861602
source: central-rm
title: RH - RM - PTO - Como gerar o cálculo do movimento rescisório do ponto
type: support-article
updated_at: '2025-11-07T21:41:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409367498519-RH-RM-PTO-Como-gerar-o-c%C3%A1lculo-do-movimento-rescis%C3%B3rio-do-ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16273646124183) Tempo aproximado para leitura: **00:00:15 min** **Dúvida**

Como calcular o movimento rescisório de ponto do funcionário, para enviar para o módulo de Folha de Pagamento?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**

Através desse processo é possível realizar o cálculo rescisório do funcionário, para gerar o movimento de ponto, pagar/descontar do funcionário com base em sua data de demissão.  
   
**Importante:** Para ser realizado cálculo do movimento de ponto para rescisão, o sistema tem como referência da data de demissão do funcionário. Dessa forma, a rescisão, já dever ter sido cadastrada a rescisão no módulo de Folha de Pagamento (não há necessidade de a rescisão ter sido calculada).

Parar gerar o movimento siga os passos abaixo:

* Acesse no módulo de Automação de Ponto o menu **Movimento | Rescisão** e ao abrir o assistente clique em avançar:    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693899031)
* Selecione a chapa do funcionário, e defina a parametrização, conforme o desejado e clique em avançar:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693910551)

As próximas telas do assistente vão depender das opções de parametrização marcadas, basta que o usuário faça o proposto pela etapa do assistente, até finalizar o processo para que o sistema calcule o movimento rescisório referente às horas apuradas.

* **Etapa 1 -** **Visualizar funcionários:** Abre a visão de funcionários para que o usuário faça a gestão de ponto. Por ela e possível acessar a edição do espelho de ponto.   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693915799)
* **Etapa 2 -** **Executar recálculo:** Realiza o recálculo do movimento do funcionário para o período atual e/ou futuro. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693923351)**
* ****Etapa 3 - Executar Compensação e/ou Lançamento do banco de horas:**** Irá aparecer a mensagem, que '*será filtrado os funcionários com rescisão no período atual'* para ser feita a

  compensação. Ao clicar no botão OK, será aberta o processo para realizar a compensação e lançamento do banco de horas.      
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693927447)  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693934999)  
  **Observação**: Mesmo que tenha sido selecionado a etapa de compensação e o funcionário não utilize cartão de ponto, não será apresentada a mensagem para ser realizado a compensação.
* **Etapa 4 - Executar o lançamento de Eventos para o TOTVS Folha de Pagamento:** Definição dos eventos a lançar para o movimento de integração da folha, tanto para o período atual como futuro.

  **Atenção!**  Caso o usuário, selecione um funcionário cuja rescisão tenha sido cadastrada com data posterior ao período atual do ponto e, não houver período futuro cadastrado na Automação de Ponto, o sistema abre a tela de cadastro de período para que o usuário cadastre esse período e, em seguida, continue o processo de rescisão.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693944343)
* Ao executar dos processos, conforme as etapas selecionada, será apresentada a tela que a rotina foi finalizada:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36189693954583)

**Saiba mais:**

[Movimento Rescisório de Ponto](https://tdn.totvs.com/pages/releaseview.action?pageId=452719290)  
[TOTVS RH - Linha RM - PTO - Como zerar o saldo do banco de horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012284812)  
[TOTVS RH - Linha RM - PTO - Como zerar o saldo do banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018164972)  
[TOTVS RH - Linha RM - PTO - Como lançar eventos para a Folha de Pagamento de funcionários demitidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409222041623)
