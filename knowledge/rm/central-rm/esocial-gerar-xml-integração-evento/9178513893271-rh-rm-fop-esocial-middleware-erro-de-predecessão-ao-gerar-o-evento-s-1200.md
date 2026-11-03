---
article_id: 9178513893271
category: eSocial - Gerar XML/ Integração Evento
content_hash: beb00cbed26b4d799b79007be88046053453522bac1040c8bc2a6ec931c30661
fetched_at: '2026-06-28T22:47:13.074998+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Middleware - Erro de Predecessão ao gerar o evento
  S-1200
type: support-article
updated_at: '2024-06-21T19:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9178513893271-RH-RM-FOP-eSocial-Middleware-Erro-de-Predecess%C3%A3o-ao-gerar-o-evento-S-1200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao transmitir o evento S-1200 é apresentada a mensagem **Erro de predecessão ao enviar o evento S-1200 - ID IDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX: Necessário enviar primeiramente o evento de admissão (S-2200 / S-2300) do funcionário chapa XXXXX**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse incidente ocorre quando não há no RM o registro do evento S-2200 ou S-2300 do funcionário em questão com status Aceito RET e com número do Recibo.   
  
**Solução**Para solucionar essa ocorrência, há duas alternativas:

1. Criar gatilho do evento S-2200 do funcionário na Fila de Eventos, incluir o número do recibo que já consta no eSocial e alterar o evento para **Aceito RET** através do banco de dados. Após envie o evento S-1200 ao eSocial.  
2. Acesse **Configurações | Parametrizador | eSocial | Integração com Middleware | Outros Parâmetros** e marque a flag **Desativar predecessão de envio de eventos**, assim não será exigido o evento S-2200 ou S-2300 na fila de eventos para transmiti-lo. Após envie o evento S-1200 ao eSocial.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9178381219991/mceclip0.png)

**Observação**  
Caso o evento S-2200 ou S-2300 não esteja no ambiente do Governo, deverá inclui-lo  na Fila de Eventos e enviá-lo ao eSocial. Após tente transmitir o S-1200 novamente.
