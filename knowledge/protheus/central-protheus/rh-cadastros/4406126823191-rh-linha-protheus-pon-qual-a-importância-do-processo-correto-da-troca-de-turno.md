---
article_id: 4406126823191
category: RH - Cadastros
content_hash: c38e65b98cc3da06cadbc941677de98c1689b17c426fbb44ab79923d05c8655b
fetched_at: '2026-06-28T22:44:53.105949+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Qual a importância do processo correto da Troca
  de Turno
type: support-article
updated_at: '2026-02-04T19:02:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406126823191-RH-Linha-Protheus-PON-Qual-a-import%C3%A2ncia-do-processo-correto-da-Troca-de-Turno
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18701962204823) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Qual a importância do processo correto da rotina de Troca de Turno?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A **Troca de Turno** é necessária para a **montagem dos calendários** mensais do Ponto, o que consequentemente impacta no correto funcionamento das rotinas do módulo, como a **Leitura/Apontamento** e a impressão de relatórios como **Espelho de Ponto** e arquivo fiscal **AEJ**.  
  
Para cada Período de Apontamento, **deve existir um registro com o primeiro dia do período**, mesmo quando **não houver efetivamente** uma troca de Turno, Sequência ou Regra de Apontamento.  
  
Segue um exemplo: período vigente de **01/10 à 31/10**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19465167125783)  
  
Obrigatoriamente deverá existir um registro com a data de 01/10, mesmo que o funcionário não tenha efetivamente uma troca de Turno/Sequência/Regra de Apontamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19465196503831)  
  
Esse comportamento deve ocorrer no momento em que é processado o **Fechamento Mensal** do período, pois o sistema de forma **automática** abre o novo **Período de Apontamento** e na sequência cria um registro de **Troca de Turno** com o primeiro dia deste novo período.   
Caso o funcionário não tenha nenhuma alteração de Turno/Sequência/Regra de Apontamento, basta manter na rotina o registro que foi criado.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios)
