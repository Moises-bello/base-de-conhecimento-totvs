---
article_id: 360050370373
category: RH - Ponto Eletrônico
content_hash: 3791e6eb14f86ed03de4e37cb3e905726871005df6b0ba30233a479e0d5ea213
fetched_at: '2026-06-28T22:44:58.282049+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar a Tolerância para Hora Extra/Atraso
  e Saída Antecipada por Marcação
type: support-article
updated_at: '2021-09-06T21:25:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050370373-RH-Linha-Protheus-PON-Como-configurar-a-Toler%C3%A2ncia-para-Hora-Extra-Atraso-e-Sa%C3%ADda-Antecipada-por-Marca%C3%A7%C3%A3o
---

**Dúvida**Como configurar a Tolerância para Hora Extra/Atraso e Saída Antecipada por Marcação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para os exemplos abaixo, foi considerado um funcionário com Horário 08:00 - 12:00 - 13:00 - 17:00 e tolerância de 5 minutos por marcação.  
Em Atualizações - Cadastro do Ponto - Regra de Apontamento, defina uma tolerância de 00:05 por marcação para Atrasos/Saídas Antecipadas e Hora Extra, e deixe com 0,00 a tolerância por Período para estes mesmos apontamentos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097208154/mceclip0.png)

Ao apontar, apenas as marcações que ultrapassaram a tolerância de 5 minutos gerarão Atraso, Saída Antecipada ou Hora Extra.   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099513533/mceclip1.png)  
  
**Importante:** quando for utilizada a modalidade de horário móvel livre, o sistema só valida a última marcação do dia, ou seja, se na Tabela de Horário Padrão o turno tiver quatro batidas previstas para o dia, a tolerância acatada será apenas para a última batida do dia, visto que todo o apontamento de eventos é feito apenas ao final do dia.

Para obter mais informações, acesse o Link: <https://tdn.totvs.com/pages/releaseview.action?pageId=496398394>.
