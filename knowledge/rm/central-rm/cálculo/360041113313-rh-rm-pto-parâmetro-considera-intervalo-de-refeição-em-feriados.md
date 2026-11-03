---
article_id: 360041113313
category: Cálculo
content_hash: 21ff3b63a2ff54c1de6d8986a6f161d9ee94d3951664a9c8ebc0c9982703fb76
fetched_at: '2026-06-28T22:46:29.205708+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Parâmetro "Considera intervalo de refeição em feriados"
type: support-article
updated_at: '2025-02-21T19:57:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041113313-RH-RM-PTO-Par%C3%A2metro-Considera-intervalo-de-refei%C3%A7%C3%A3o-em-feriados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503040418071) Tempo aproximado para leitura: 00:00:35 min  
  
Dúvida**Como funciona o parâmetro do sindicato, "Considera intervalo de refeição em feriados"?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões.  
  
**Solução**Este parâmetro faz com que o sistema aplique  a ausência de refeição do horário para os dias de feriado,  e desconsidera as horas extras deste intervalo caso o funcionário efetue apenas as batidas de entrada e saída da empresa.

Observação: O parâmetro não é aplicado para horários que possuem o cadastro de limite de refeição.  
  
Segue exemplo:

Horário associado ao funcionário, com ausência de refeição cadastrada  das 12:00 as 13:30. Com o parâmetro desmarcado.  O produto gerou todo o intervalo como extra de feriado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053532414)

Com o parâmetro marcado, o sistema irá descartar da jornada o intervalo da ausência  de refeição, contabilizando os demais intervalos como extra de feriado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053532514)
