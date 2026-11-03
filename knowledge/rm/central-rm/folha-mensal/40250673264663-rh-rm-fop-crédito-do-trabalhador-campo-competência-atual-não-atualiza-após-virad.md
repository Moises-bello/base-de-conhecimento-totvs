---
article_id: 40250673264663
category: Folha Mensal
content_hash: 95506ab940a19f4532d65e7ccc53e8bf677d4ac146b872709e27ec40d534e108
fetched_at: '2026-06-28T22:46:57.918466+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Campo competência atual não atualiza
  após virada de competência
type: support-article
updated_at: '2026-06-18T16:40:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40250673264663-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Campo-compet%C3%AAncia-atual-n%C3%A3o-atualiza-ap%C3%B3s-virada-de-compet%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40250683221783) Tempo aproximado para leitura: **00:01:14min**  
  
**Dúvida**

O sistema não realiza a atualização automática do campo 'Competência Atual' nos empréstimos consignados após o encerramento da competência da folha de pagamento, gerando necessidade de manutenção manual.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2410.319

12.1.2502.229

12.1.2506.179

12.1.2510.112

12.1.2602 e superiores

**Solução**  
O campo Competência Atual nos empréstimos consignados não é processado de forma automática pela rotina de virada de competência do sistema.

A atualização deste campo ocorre exclusivamente através da importação mensal do arquivo do Crédito do Trabalhador. O arquivo disponibilizado pelo órgão responsável contém o campo específico que alimenta a base de dados do sistema, atualizando a competência de acordo com o período importado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40250683223191)

**Saiba mais:**

[RH - RM - FOP - Crédito do Trabalhador - Campo Competência Atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37541406086295-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Campo-Compet%C3%AAncia-Atual)
