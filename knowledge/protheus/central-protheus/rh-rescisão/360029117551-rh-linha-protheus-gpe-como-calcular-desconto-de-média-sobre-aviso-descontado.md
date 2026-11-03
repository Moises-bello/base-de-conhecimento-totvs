---
article_id: 360029117551
category: RH - Rescisão
content_hash: 4c67ecff9e38c4e6374050842598916c8624fd6db14434acb1929a9d9d61cfec
fetched_at: '2026-06-28T22:43:48.585474+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular desconto de média sobre aviso descontado
type: support-article
updated_at: '2025-07-15T18:24:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029117551-RH-Linha-Protheus-GPE-Como-calcular-desconto-de-m%C3%A9dia-sobre-aviso-descontado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33487609284759) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como fazer com que o sistema calcule na rescisão o desconto de média sobre aviso descontado  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**1. Parametrizar o mnemônico **P\_DESCMEDA** (DESC MEDIA A. PREVIO ("S"-SIM / "N"-NAO) com **"S"**:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030143292)  
2. Cadastrar uma **nova verba** de desconto e relacionar ao **ID 0972**-Desc. Media A. Prévio Rescisão:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030143412)3. Na Tabela **S043**, para o tipo de rescisão em questão deixar a coluna **AVISO PRÉVIO** com **D**:  
  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030143572)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
