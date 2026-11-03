---
article_id: 360017419872
category: RH - Rescisão
content_hash: 68896b71533dec9dbc605c083368e857c591693717abaa47f17652a760a9538b
fetched_at: '2026-06-28T22:43:52.240305+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - No cálculo da rescisão está apresentando o Log:
  Tabela de Imposto de Renda (Tabela S002) não cadastrada'
type: support-article
updated_at: '2025-09-10T18:24:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017419872-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-da-rescis%C3%A3o-est%C3%A1-apresentando-o-Log-Tabela-de-Imposto-de-Renda-Tabela-S002-n%C3%A3o-cadastrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34845803614487) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao calcular rescisão, é apresentado Log de Ocorrências com mensagem **Tabela de Imposto de Renda (Tabela S002) não cadastrada**, porém para o ano do cálculo da rescisão há registro na tabela **S002-Imposto de Renda**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012947631)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as Versões.

**Causa**Na rotina **Períodos**, para o período em aberto do cálculo da rescisão que está sendo efetuada, para o roteiro RES, a coluna **Data Pagamento** está preenchida com um ano que **não consta** na **tabela S002** e **diferente do período selecionado**, note no exemplo abaixo que a coluna Data de Pagamento esta preenchida com o ano de 2029 (31/01/2029), sendo que o Período é 01/2019:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012947831)  
  
**Solução**Na rotina **Períodos**, para o **roteiro RES**, ajustar a coluna Data de Pagamento para a **data correta** de acordo com o **Período** em questão, note que no exemplo abaixo, a coluna Data de Pagamento esta de acordo com o **Período selecionado** (ano).

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012948031)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
