---
article_id: 360018943752
category: RH - Folha de Pagamento
content_hash: 32b39b513762b554450e3ab0fb4f90ad83295d30e71be4fcbd6a01c73795cc14
fetched_at: '2026-06-28T22:44:13.449140+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o cálculo de folha complementar
type: support-article
updated_at: '2025-04-15T13:23:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018943752-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-de-folha-complementar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26237237418647)**Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**Como calcular uma folha de pagamento complementar no Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A folha **complementar** no Protheus funciona **apenas** quando a folha que se deseja gerar o complemento está **aberta.** O sistema **não** realiza complementos de folha da finalizada, essa opção é habilitada somente para o roteiro FOL. Para períodos já fechados, pode ser utilizado o roteiro [RTF - Retificação da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10072659249559-RH-Linha-Protheus-GPE-Retifica%C3%A7%C3%A3o-da-folha-de-Pagamento-Roteiro-RTF).

 

Cadastro de Períodos  
•Para calcular uma folha complementar é **necessário** alterar o **Período da folha aberta** para **ativo** **NÃO**.  
**•Criar** um **novo período** de cálculo **igual** ao período que está aberto (data inicial, final e dados da aba calendário devem ser iguais ao pagamento 01. Se ficar diferente, irá gerar verbas de salário, DSR, etc. indevidamente.).  
•Note que no **novo período** o número de **pagamento** é demonstrado como **02.**  
•Também é necessário que as colunas **Per Ativo e Complementar** fiquem com **SIM**.  
![image2016-10-3_11_11_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015068931)

•Após a configuração do período da folha complementar pode ser feito o **lançamento** de uma verba e cálculo da folha **por período.**  
•Note que o Nro. Pagamento é demonstrado como **02.**  
  
![image2016-10-3_11_11_55.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015034732)  
  
![image2016-10-3_11_12_39.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015069171)

Após realizar os lançamentos e calcular a folha de pagamento, o roteiro FOL pode ser fechado.  
**Atenção**: Siga a ordem dos números de pagamento, **primeiro** feche a folha original (pagamento **01)** e **depois** a complementar (pagamento **02).**

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Qual a finalidade do campo Fech Compete no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058234133-RH-Linha-Protheus-GPE-Qual-a-finalidade-do-campo-Fech-Compete-no-cadastro-de-verbas)
