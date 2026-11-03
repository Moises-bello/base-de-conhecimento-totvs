---
article_id: 360050452433
category: RH - Cadastros
content_hash: 63b240debdc4924869dfe69ea36e137719486855475a7cd72da09f0225809f20
fetched_at: '2026-06-28T22:44:52.956784+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Configuração de Tolerância para horas Não Realizadas
  por período
type: support-article
updated_at: '2025-12-16T13:00:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050452433-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-de-Toler%C3%A2ncia-para-horas-N%C3%A3o-Realizadas-por-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34325180266007) Tempo aproximado para leitura: 00:01:00 min**  
  
**Duvida**  
Como configurar a Tolerância para horas Não Realizadas por período?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para os exemplos abaixo, foi considerado um funcionário com horário **08:00 - 12:00 - 13:00 - 17:00** e tolerância de 10 minutos diários.

Em **Atualizações > Cadastros Ponto > Regra de Apontamento**, defina uma tolerância de 10 minutos apenas para a **tolerância de horas não realizadas**.

![Capturar5.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar5.PNG?version=1&modificationDate=1579725730167&api=v2)

**Observação:** Não será possível preencher o campo **Tol. Hr. NReal** caso o campo **Tol. S. A. Per.** ou o campo **Tol. Atr. Per.** estiverem preenchidos com algum valor.

No apontamento, o sistema irá somar **atrasos** e **saída antecipada**, como se fossem um único **evento negativo** do dia, e verificar se ultrapassaram a **tolerância cadastrada**.

As **marcações** que geraram **descontos** estão destacadas em **vermelho**, pois, somadas, ultrapassam a **tolerância de 00:10**.

Para o dia **08/01/2020**, o sistema somou os dois eventos (**atrasos** e **saída antecipada**) e, como o resultado ultrapassou a **tolerância de 10 minutos**, ambos os eventos foram apontados.

![Capturar6.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar6.PNG?version=1&modificationDate=1579726287457&api=v2)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
