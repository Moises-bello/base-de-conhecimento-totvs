---
article_id: 360011048311
category: Cadastros
content_hash: df290905e44c3a6da78043b4e828c8ae3867b43b20ac4f143f5dbf6e456b7593
fetched_at: '2026-06-28T22:46:28.552404+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Calcular redução de jornada noturna (hora reduzida)
type: support-article
updated_at: '2025-10-15T16:16:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011048311-RH-RM-PTO-Calcular-redu%C3%A7%C3%A3o-de-jornada-noturna-hora-reduzida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981712801943) Tempo aproximado para leitura: 00:01:45 min  
  
Dúvida**Como calcular (parametrizar) a redução de jornada noturna no sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12  
  
**Solução**

1º) Acessar o cadastro do horário (Aba Cadastros | Horários por Intervalo), editar o horário desejado e marcar a flag "Considera redução da jornada noturna".​

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008389712)

2º) Ajustar as batidas da jornada no cadastro de horário de acordo com a redução da jornada noturna, pois o sistema não faz a redução de forma automática, simplesmente gera as ocorrências de forma reduzida.

Exemplo:

**Horário referência****22:00 - 01:00 - 02:00 - 05:00**

22:00 as 23:00 ~ 52:30 min                                    à 22:00 as 22:52 (+00:52)

23:00 as 00:00 ~ 52:30 min                                    à 22:52 as 23:45 (+00:53)

00:00 as 01:00 ~ 52:30 min                                    à 23:45 as 00:37 (+00:52)

01:00 as 02:00 ~ intervalo refeição (01:00)           à 00:37 as 01:37 (+01:00)

02:00 as 03:00 ~ 52:30 min                                    à 01:37 as 02:30 (+00:53)

03:00 as 04:00 ~ 52:30 min                                    à 02:30 as 03:22 (+00:52)

04:00 as 05:00 ~ 52:30 min                                    à 03:22 as 04:15 (+00:53)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008427211)

3º) Cadastrar os eventos do RM Chronus com os códigos de cálculo de 0044 até 0054 que se referem a jornada noturna reduzida, e depois nos parâmetros do Sindicato na etapa 17 - Eventos associar estes eventos aos seus respectivos eventos do RM Labore.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008389812)

**Saiba mais**Para mais informações sobre cadastro de horários, acesse o link [cadastro de horários.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719175)
