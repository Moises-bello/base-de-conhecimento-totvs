---
article_id: 22569173356695
category: PMS - Projetos
content_hash: 36c7835b928d75633214bfe73ac74996b8f4a2706c60f176a9f426ce576ad6b6
fetched_at: '2026-06-28T22:37:14.865222+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Apontamento de mão de obra
  em hora extra do recurso
type: support-article
updated_at: '2024-04-05T12:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22569173356695-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Apontamento-de-m%C3%A3o-de-obra-em-hora-extra-do-recurso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22569173252887) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como realizar apontamento de mão de obra em hora extra do recurso?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

Se o recurso “ELETRICISTA” pré-apontou no dia 08/05 que sua hora de início foi 08h00 e a hora fim foi 20h00, o intervalo total é de 12 horas, porém, o calendário amarrado a este recurso prevê uma jornada de 8 horas diárias, iniciando as 08h00, havendo recesso das 12h00 às 13h00 (para horário de almoço) e finalizando a jornada às 17h00.

**Como resolver:**  
Assim, o pré-apontamento só considerará as horas apontadas dentro desse intervalo. Para que haja contabilização das horas sobressalentes, é necessário cadastrar uma exceção de calendário.

Como cadastrar exceção (rotina PMSA330):  
Passo 1)

Selecionar a data que deseja incluir a Exceção de calendário (exemplo: dia 07/Setembro (Feriado Nacional).

Passo 2)

Significa que nenhum recurso pode realizar um apontamento nesta data em nenhum horário e em qualquer projeto.

Passo 3)

Caso tivéssemos inserido o projeto e um recurso nos campos abaixo significa que esta exceção de calendário é valida somente para um determinado Projeto e somente o recurso informado não poderá realizar o Apontamento de horas.

Neste exemplo, como os campos não estão preenchidos a Exceção de Calendário está ativa para qualquer Recurso e qualquer Projeto.

![](https://tdn.totvs.com/download/attachments/274630068/image2020-9-1_9-35-36.png?version=1&modificationDate=1598963736943&api=v2)
