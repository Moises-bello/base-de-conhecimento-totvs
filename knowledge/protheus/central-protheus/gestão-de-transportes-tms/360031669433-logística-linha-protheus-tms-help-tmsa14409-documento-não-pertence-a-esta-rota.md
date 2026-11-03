---
article_id: 360031669433
category: Gestão de Transportes (TMS)
content_hash: 6914a68915ee7def9807e86d7ca84b77a64a1a7777c4957dcd3de6a0e1d98615
fetched_at: '2026-06-28T22:45:29.277467+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - HELP TMSA14409 - Documento não pertence
  a esta rota
type: support-article
updated_at: '2023-08-28T11:38:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031669433-Log%C3%ADstica-Linha-Protheus-TMS-HELP-TMSA14409-Documento-n%C3%A3o-pertence-a-esta-rota
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17081218198551)***Tempo aproximado para leitura: **00:01:12 min**  
**Ocorrência**Ao vincular o documento a viagem é apresentado o *HELP***TMSA14409 - Documento não pertence a esta rota.**  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Falta de parametrização ou parametrização inconsistente.  
  
**Solução**Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/ Logística/ Zonas - OMSA070** e efetue o cadastro de uma zona de entrega.

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043028853)

Acesse **Atualizações/ Logística/ Setores por Zona - OMSA080**e efetue o cadastro dos setores vinculados à zona de entrega.

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360042182094)

Acesse **Atualizações/ Logística/ Pontos por Setor - OMSA090** e efetue o cadastro de pontos por zona e setor

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360042182654)

Acesse **Atualizações/ Logística/ Rotas - OMSA100**e efetue o cadastro das rotas de acordo com a zona e os setores.

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360042182734)

Com estes cadastros, o *HELP* não será mais exibido, se o cliente destinatário estiver dentro dos parâmetros definidos.   
  
Por exemplo, nas configurações de **Pontos por Setor - OMSA090**, configurei por **CEP - Código de Endereçamento Postal** o intervalo **00000-000 até 99999-998**. Em **Atualizações/ Cadastro/ Clientes - MATA030**, meu cliente destinatário está com o **CEP 99999-999**, estando fora do intervalo definido, o *HELP* é apresentado.

![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360042186054)

![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043033293)

![7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043033313)
