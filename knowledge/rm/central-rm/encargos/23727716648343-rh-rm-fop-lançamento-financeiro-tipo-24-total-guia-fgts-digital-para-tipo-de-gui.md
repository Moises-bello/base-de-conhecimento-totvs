---
article_id: 23727716648343
category: Encargos
content_hash: df31dc16568c7d7af321daa845761030b1e736c32cc67bf031b05159cf27d963
fetched_at: '2026-06-28T22:46:52.256344+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro tipo 24 Total Guia FGTS Digital para
  tipo de guia Rescisório + mensal
type: support-article
updated_at: '2024-06-20T12:21:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23727716648343-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-Total-Guia-FGTS-Digital-para-tipo-de-guia-Rescis%C3%B3rio-mensal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23727716621463) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar o lançamento financeiro FGTS digital para parametrização tipo de guia rescisório + mensal?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos Patches 12.1.2306.264, 12.1.2310.213 e 12.1.2402.155  
  
**Solução**

O lançamento financeiro tipo 24 - Total Guia FGTS Digital será parametrizado em encargos | parâmetros financeiros | Tipo 24 | Rescisório + mensal e será utilizado quando houver rescisão do dia 01 á 09 do mês paras os tipos de rescisão que podem sacar o FGTS e que na geração da rescisão teve a marcação da flag FGTS MÊS ANTERIOR SERÁ RECOLHIDO NO FGTS DIGITAL.

**Importante**: É de responsabilidade da organização verificar se já foi recolhido ou não o FGTS do mês anterior que é levado no dia 20 do mês subsequente.

Sugerimos que seja cadastrados três parametros financeiros do tipo 24 com códigos e lançamentos ativos diferentes, um para cada tipo de guia:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727702501783)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727702503831)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727716626199)

Exemplificando com uma rescisão do tipo 02 - Inic.Empregador sem justa causa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727702506391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727702507927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727716630551)

Para geração do lançamento financeiro acessar encargos | geração de lançamentos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727716631319)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727702510871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727716633367)

Saiba mais: [DT - FGTS Digital - Lançamento Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=834247089#Aba1-2)
