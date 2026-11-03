---
article_id: 360049590294
category: RH - Ponto Eletrônico
content_hash: 980675a07d0a85bd434f42baf3b3cffc1b7f15fd6d1dcd80e2379206cb2617c0
fetched_at: '2026-06-28T22:44:58.279405+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar a Tolerância para Atraso/Saída
  Antecipada e Hora Extra por Período
type: support-article
updated_at: '2021-08-11T23:18:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049590294-RH-Linha-Protheus-PON-Como-configurar-a-Toler%C3%A2ncia-para-Atraso-Sa%C3%ADda-Antecipada-e-Hora-Extra-por-Per%C3%ADodo
---

**Dúvida**Como configurar a Tolerância para Atraso/Saída Antecipada e Hora Extra por Período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para os exemplos abaixo, foi considerado um funcionário com Horário 08:00 - 12:00 - 13:00 - 17:00 e tolerância de 05 minutos por período.  
Em Atualizações - Cad. Ponto - Regra de Apontamento, defina uma tolerância de 0,05 por período para Atrasos/Saídas Antecipadas e Hora Extra, e deixe com 00 os campos que tratam a tolerância por batida:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099625353/mceclip0.png)

Ao apontar, apenas as marcações que ultrapassaram a tolerância de 05 minutos gerarão Atraso, Saída Antecipada ou Hora Extra. No caso da tolerância por período, estes 05 minutos podem ser distribuídos ao longo do dia, conforme os exemplos abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097318914/mceclip1.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099625913/mceclip2.png)

Para obter mais informações, acessar o Link: <https://tdn.totvs.com/pages/releaseview.action?pageId=496398394>
