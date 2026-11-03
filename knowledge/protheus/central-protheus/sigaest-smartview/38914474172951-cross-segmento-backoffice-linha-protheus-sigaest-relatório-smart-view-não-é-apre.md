---
article_id: 38914474172951
category: SIGAEST - SMARTVIEW
content_hash: 8e1ea849b6a46479342474f43cdfd2c11f291aeb0df1000f5807da432577d0f2
fetched_at: '2026-06-28T22:38:47.135552+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Relatório Smart View
  não é apresentado para agendamento no Schedule
type: support-article
updated_at: '2026-03-24T14:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38914474172951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Relat%C3%B3rio-Smart-View-n%C3%A3o-%C3%A9-apresentado-para-agendamento-no-Schedule
---

O Scheduler Smart View da TOTVS permite agendar a execução automática de relatórios criados no Smart View no Protheus. Para que os relatórios apareçam no agendamento do Schedule, é necessário que estejam vinculados ao Protheus, o que ocorre automaticamente ao acessar o Smart View pelo menu do sistema. Caso não apareçam, basta abrir o relatório no Protheus para realizar o vínculo e disponibilizá-lo para seleção.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38914486613527) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como inserir uma visão do Smart View para seleção no agendamento do Schedule no Configurador?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
O Scheduler Smart View da TOTVS é uma funcionalidade que permite agendar a execução automática de relatórios criados no Smart View, otimizando a extração de informações sem interromper as operações do ERP.

Veja um vídeo do processo:

[![Smart View.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39256975009815)](https://youtu.be/sawLbiaG-Gg?si=GBHcVxcbqbt2gunX)

Ao acessar a rotina de Schedule do SIGACFG, é apresentado o botão "+ Smart View":

![Smart View 01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38914486615575)

Se, ao clicar no botão "+ Smart View" não for apresentado algum relatório, significa que o mesmo não foi vinculado ao Protheus.

O vínculo pode ser verificado na rotina de "Integração Smart View" (APCFG770), que fica disponível no SIGACFG acessando a opção "Ambiente", agrupador "Smart View".

![Smart View 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38914486617239)

Esta amarração é realizada automaticamente ao acessar o Smart View no Protheus, ou seja, caso a rotina do Smart View não esteja disponível na rotina de "Integração Smart View" (APCFG770), é possível que ele não tenha sido acessado anteriormente no Menu do Protheus.

Para solucionar, basta acessar o relatório do Smart View, que deseja agendar no Schedule, através do Menu do Protheus, e ele reaizará o vínculo e disponibilizará o mesmo para seleção.

**Saiba mais:**

[Executando recursos no Schedule](https://tdn.totvs.com/x/SKoMNw)

[Amarração Protheus x Smart View](https://tdn.totvs.com/x/Nbs0Kg)
