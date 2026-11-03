---
article_id: 15910808697239
category: PMS - Projetos
content_hash: 74ba205275e8b524c03cb9d4308c5cc5a40ecdba7b07d3115471da0e5211fbb1
fetched_at: '2026-06-28T22:37:15.914415+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Help "Saldo de horas insuficiente
  para a realização do apontamento"
type: support-article
updated_at: '2024-03-21T13:55:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15910808697239-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Help-Saldo-de-horas-insuficiente-para-a-realiza%C3%A7%C3%A3o-do-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15910786704279) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao fazer o pré-apontamento de recursos (PMSA701) aparece a mensagem "Saldo de horas insuficiente para a realização do apontamento" ao informar os horários do recurso, como resolver?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**

Essa é a etapa de fazer a alocação do recurso com a tarefa de um projeto.

O erro ocorre pois o campo **"Saldo Horas (AJK\_SLDHR)"** não pode ser maior que o **"Qtd. Horas (AJK\_HQUANT)"**.

O campo **"Saldo Horas (AJK\_SLDHR)"** é gatilhado ao confirmar o recurso na tela **"Recurso (AJK\_RECURS)"** do campo **AF9\_HDURAC.**

**OBS 1:** Para que seja calculado as horas corretamente, deve ser configurado a alocação de recursos na tarefa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15910501844375)

O campo **"Qtd. Horas (AJK\_HQUANT)"** é cálculo da subtração dos campos data na própria tela: **(AF9\_HORAF - AF9\_HORAI)**.

**Exemplo com erro:**

AF9\_HDURAC = **9 horas**  
AFK\_HORAI = 08:00  
AFK\_HORAF = 23:00  
Cálculo de horas na pré-alocação (AFK\_HORAF - AFK\_HORAI): **15 horas**

**O erro ocorre pois 15 > 9** (o apontamento de horas do pré-apontamento não pode ser maior que o intervalo de horários definido no cronograma da tarefa):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15910643805079)

Colocar um intervalo de horas nos campos **AJK\_HORAI** e **AJK\_HORAF** que a quantidade não seja maior que o campo **AF9\_HDURAC**.

**Saiba Mais:**

[Pré-Apontamento Modelo2 (PMSA701 - SIGAPMS)](https://tdn.totvs.com/x/xq0OFQ)
