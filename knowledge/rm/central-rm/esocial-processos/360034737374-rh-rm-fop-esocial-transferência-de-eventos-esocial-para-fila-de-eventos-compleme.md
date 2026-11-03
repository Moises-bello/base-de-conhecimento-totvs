---
article_id: 360034737374
category: esocial - Processos
content_hash: 975cc7d79547c3719272f24e2f3fc2e23a41a57065ef343640b81bca31fc103f
fetched_at: '2026-06-28T22:47:08.430049+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Transferência de eventos eSocial para fila de eventos
  complementar
type: support-article
updated_at: '2024-06-04T19:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034737374-RH-RM-FOP-eSocial-Transfer%C3%AAncia-de-eventos-eSocial-para-fila-de-eventos-complementar
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23529269968535)**Tempo aproximado para leitura: **00:02:30 min****

**Dúvida**Como realizar a transferência de eventos eSocial da fila de eventos para fila de eventos complementar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**A **Fila de Eventos do eSocial Complementar** irá guardar as informações contidas na **Fila de Eventos do eSocial** após a sua transferência pelo processo **Transferência manual da Fila de Eventos do eSocial** ou pela **Liberação de Competência**.

Primeiramente, acesse **Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerias 1/7** e parametrize o período de tempo que o sistema deverá manter os eventos na fila de eventos eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23529257487255)

Posteriormente, será possível realizar a transferência por dois meios: transferência manual da fila de eventos do eSocial e pela liberação de competência. Veja abaixo como realizar os processos:

1. Para transferência manual acesse **eSocial | Fila de Eventos Complementar | Transferência Manual da Fila de Eventos do eSocial;**1.1. Serão transferidos os registros anteriores a data informada no parametrizador;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045125274)

2. Para transferência dos eventos no processo de Liberação de Competência acesse **Folha Mensal | Liberação de Competência;**2.1. Selecione o parâmetro **Transferir Fila de Eventos do eSocial para Fila de Eventos do eSocial Complementar;**2.2.Serão transferidos os registros anteriores a data informada no parametrizador;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23529269987095)

**Importante**O Sistema verifica a data do evento e meses anteriores informado no parametrizador para validar se deve ou não transferi-lo para fila de eventos complementar.  
Para a liberação da fila de eventos complementar será necessário atualizar sua base de dados através do aplicativo RM.Atualizador.exe.

**Saiba mais**Para mais informações acesse:  
      • [Fila de eventos do eSocial Complementar](https://tdn.totvs.com/pages/releaseview.action?pageId=506143967#1-1)
