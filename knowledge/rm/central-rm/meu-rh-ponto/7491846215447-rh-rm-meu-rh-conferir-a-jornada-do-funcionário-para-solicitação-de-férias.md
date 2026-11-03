---
article_id: 7491846215447
category: Meu RH - Ponto
content_hash: 0c931e14b65220db6d96ddb76213d4e51bd71e55d30991f8e6313c2edc332dde
fetched_at: '2026-06-28T22:47:30.307816+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Conferir a Jornada do funcionário para solicitação de férias
type: support-article
updated_at: '2026-02-25T15:20:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7491846215447-RH-RM-Meu-RH-Conferir-a-Jornada-do-funcion%C3%A1rio-para-solicita%C3%A7%C3%A3o-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24086650188183) Tempo aproximado para leitura: **00:03:08 min**  
  
**Dúvida**  
Como descobrir o dia de descanso e compensado conforme horário do funcionário, para marcação de férias no Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões  
  
**Solução**  
A marcação é controlada por um parâmetro que verifica o horário vinculado ao funcionário, mesmo que ele não realize a batida de ponto deverá ter um horário válido contemplando as datas ou poderá ocorrer o erro: **Início de Férias não pode ser programado para até dois dias antes de feriado, descanso ou dia compensado.**  
Caso apresente esse erro poderá solucionar seguindo as orientações do documento: [RH - RM - Meu RH - Erro ao sugerir Férias quando início é de até dois dias antes de feriado, descanso ou dia compensado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418002657047)

Um modo bastante eficiente é verificar através do caminho **Folha de Pagamento | Funcionário |** **Anexos | Horário Planejado | Histórico de Horários.**

![](https://totvssuporte.zendesk.com/attachments/token/V4rkzaaCVRjZpvUE2VDVsMvfP/?name=image.png)

Edite o horário vigente e clique em **Visualizar Horário**, lembre-se do índice que está informado nessa tela.

![](https://totvssuporte.zendesk.com/attachments/token/ksqL3MRuhaDNppUNBxSzXfgJ6/?name=image.png)

Para conferir, selecione o **horário/índice** e clique em **Atualizar** para carregar a grade de horário se será um dia como feriado, compensado, descanso mesmo.

![](https://totvssuporte.zendesk.com/attachments/token/aEvrXw0H5cauLIJK5kZXCwu0f/?name=image.png)

Segue um **exemplo real** de problema: ao sugerir férias para o dia **25/02 (terça-feira)**, ocorre um **erro**. Ao verificar a Jornada do funcionário, constatamos que a configuração define a **quarta-feira como dia de descanso**.

**Dica:** No campo "Data Fim", insira uma data posterior ao início das férias do funcionário. Dessa forma, será possível verificar se os dias subsequentes ao início das férias são de descanso ou compensados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27991757175703)

Para solução, a tela que contempla os parâmetros necessários é localizada em **Folha de Pagamento | Configurações | Parametrizador | RM Portal | edite o grupo de acesso | Férias.**

Caso seja um funcionário com **horário diferenciado** ou não bata ponto, pode criar simplesmente um novo **grupo de quiosque** para esses funcionários e deixar **desmarcada** a flag para não impedir em nenhum momento.

![](https://totvssuporte.zendesk.com/attachments/token/b0eLbcBF8rasYgcAuDXadCIyB/?name=image.png)

Caso analisando o horário esteja impedindo em dia **Compensado**, poderá marcar a flag para também **Desconsiderar dia Compensado**:

![](https://totvssuporte.zendesk.com/attachments/token/4oDnjvFtEoHCQhDvoncbt15wF/?name=image.png)
