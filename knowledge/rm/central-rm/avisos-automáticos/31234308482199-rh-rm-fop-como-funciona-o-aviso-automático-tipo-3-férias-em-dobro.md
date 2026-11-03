---
article_id: 31234308482199
category: Avisos Automáticos
content_hash: b53188352fbb409559e5e999a941814dae9c97c329fd046b6ef65ae4914618f1
fetched_at: '2026-06-28T22:46:40.505169+00:00'
product: rm
section_id: 31224122282519
source: central-rm
title: RH - RM - FOP - Como funciona o aviso automático Tipo 3 - Férias em dobro?
type: support-article
updated_at: '2026-03-16T13:39:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31234308482199-RH-RM-FOP-Como-funciona-o-aviso-autom%C3%A1tico-Tipo-3-F%C3%A9rias-em-dobro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31234338613399) Tempo aproximado para leitura: **00:02:42 min****Dúvida**Como funciona o envio de avisos automáticos do tipo Férias em Dobro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários estiverem para adquiriem férias em dobro. Este aviso tem como finalidade notificar os chefes de que eles terão de pagar as férias dobradas ao funcionário caso este não tire férias imediatamente.

Este aviso verifica no período aquisitivo a data limite de gozo, diferente do aviso tipo 1-Escala de férias (em que as férias já estão marcadas e é o gozo das férias de fato).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31234308455831)

Assumindo 30 dias em Nro Dias Ref. o sistema irá sobre a Data informada em Limite início de Gozo ou seja, sendo 24/03/2025 o sistema enviará mensagens desde a data de 22/02/2025 notificando a necessidade de gozar as férias.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31234338617239)

Será enviado o e-mail informando a Data limite de início de gozo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31234308457879)

**Importante**

Para executar a rotina automaticamente, deverá ser realizado o Agendamento de Job no ambiente conforme as orientações da documentação [Como agendar a execução de um processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-Framework-Linha-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo)
