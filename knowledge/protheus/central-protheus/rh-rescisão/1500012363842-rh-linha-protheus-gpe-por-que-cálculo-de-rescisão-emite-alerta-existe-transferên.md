---
article_id: 1500012363842
category: RH - Rescisão
content_hash: 1e5dc9bdcf28481b40150ea3cabb2455ba80fac2ce986f67213e84a106d42356
fetched_at: '2026-06-28T22:43:53.526901+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Por que cálculo de rescisão emite alerta: Existe
  Transferência Posterior a Data Informada'
type: support-article
updated_at: '2025-07-24T11:30:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012363842-RH-Linha-Protheus-GPE-Por-que-c%C3%A1lculo-de-rescis%C3%A3o-emite-alerta-Existe-Transfer%C3%AAncia-Posterior-a-Data-Informada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26625499960471)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Por que cálculo de rescisão emite alerta: Existe Transferência Posterior a Data Informada:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019519202)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**A mensagem é gerada pois houve transferência com data superior a data de demissão do funcionário. Não há possibilidade de ser calculada uma rescisão com data anterior a transferência.

**Exemplo:**Transferência de centro de custo com data de 19.01.2021:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019519422)

Ao calcular rescisão com data de 18.01.2021, o sistema emite o aviso:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019519522)

**IMPORTANTE:** Não há uma forma de desfazer ou cancelar uma transferência. Caso tenha feito de forma incorreta, é necessário fazer uma nova transferência no dia posterior a primeira retornando para empresa/filial/centro de custo anterior ou calcular a rescisão com data após a transferência.

****Saiba mais:****[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)  
[MP - GPE - Como cancelar ou desfazer transferências de funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025324694-MP-GPE-Como-cancelar-ou-desfazer-transfer%C3%AAncias-de-funcion%C3%A1rios-?source=search)
