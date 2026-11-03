---
article_id: 360035826013
category: RH - Cadastros
content_hash: 1d6f8fb532ac72aa93fa87b96f4565c88f935252cca4137ed7589a9c126f8199
fetched_at: '2026-06-28T22:44:53.030103+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Hora extra indevida quando o horário do funcionário
  é móvel
type: support-article
updated_at: '2026-01-15T14:14:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035826013-RH-Linha-Protheus-PON-Hora-extra-indevida-quando-o-hor%C3%A1rio-do-funcion%C3%A1rio-%C3%A9-m%C3%B3vel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34217649602967) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
O que verificar quando está apontando hora extra indevida quando configurado para o funcionário o horário móvel?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para que o apontamento de Horas Extras não seja apontado indevidamente será necessário acessar o cadastro da Regra de Apontamento do funcionário em **Atualizações > Cadastro do Ponto > Regra de Apontamento** e verificar se o campo **Sincr.Interv** está =**SIM**.   
  
Caso esteja com SIM, o sistema irá considerar o horário de entrada para sincronizar com intervalo, ou seja, se funcionário entrar na empresa uma hora mais cedo terá que sair para intervalo uma hora mais cedo. Caso contrário irá gerar hora extra.

Para não considerar esta regra o campo **Sincr.Interv** precisa estar **=NÃO**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046004474)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
