---
article_id: 360035133174
category: RH - Férias
content_hash: 348df52488d17776a0575ca9d160a426dbafbe580f80d1a8be8d7a4d73b28582
fetched_at: '2026-06-28T22:43:58.004486+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de médias as verbas de Horas Extras estão
  sendo calculados de forma errada entre a coluna valor origem e a coluna valor atual
type: support-article
updated_at: '2025-09-24T11:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133174-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias-as-verbas-de-Horas-Extras-est%C3%A3o-sendo-calculados-de-forma-errada-entre-a-coluna-valor-origem-e-a-coluna-valor-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27273612607895) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Horas extras estão sendo calculados de forma errada entre a coluna valor origem e a coluna valor atual, no cálculo de médias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Verifique o cadastro de funcionários em **Atualizações > Funcionários > Funcionários (GPEA010)** na aba funcionais, o campo Horas Dia **“RA\_HRSDIA”.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27273612615447)**

Este campo é preenchido automaticamente quando preenchemos o campo  **Hrs. Mensais “RA\_HRSMES”.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27273672324119)**

Ocorre que o campo **"RA\_HRSDIA",**pode ser manipulado pelo usuário, importante verificar se as horas dias corresponde com o resultado do campo **RA\_HRSMES.**

Caso não esteja correto, ajustar, após ajuste, emitir o demonstrativo de médias novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27273672325527)

**Saiba Mais**[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052314713-RH-Linha-Protheus-GPE-Mem%C3%B3ria-de-c%C3%A1lculo-das-f%C3%A9rias)
