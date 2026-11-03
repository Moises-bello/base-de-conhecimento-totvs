---
article_id: 11269726795031
category: RH - Rescisão
content_hash: fa4807c03d6484f74ffb32ba7ed24f4dff305170e4fe7729d5b62112fbdea6f8
fetched_at: '2026-06-28T22:43:48.351033+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Como conferir valor do ID 1676-FGTS 13º Devolução
  calculado em rescisão
type: support-article
updated_at: '2026-04-08T18:51:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11269726795031-RH-Linha-Protheus-GPE-Como-conferir-valor-do-ID-1676-FGTS-13%C2%BA-Devolu%C3%A7%C3%A3o-calculado-em-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23809213090583) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como conferir valor do ID 1676-FGTS 13º Devolução calculado em rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**O ID 1676 se trata de um ID tipo base desconto, quanto há devolução de FGTS 13º salário, assim a rescisão calcula o ID quando houver calculo de FGTS 13º salário no cálculo da 2ª parcela superior ao calculado em rescisão.

**Exemplo:**

**Cadastro ID 1676**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23809259637271)**

**Cálculo roteiro 132**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269532456343)**

Base FGTS 13 salário: 974,36 + 1059,56 = 2.033,92

2.033,92 \* 8% = 162,71

**Cálculo rescisão**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269629249047)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269630814615)**

Base FGTS 13 salário: 85,95 + 1332,47 + 399,74 = 1.818,16

1.818,16 \* 8% = 145,45

**162,71 - 145,45 = 17,26 Valor ID 1676**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[RH - Linha Protheus - GPE - Novos Identificadores de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004848372-RH-Linha-Protheus-GPE-Novos-Identificadores-de-C%C3%A1lculo?source=search)

[RH - Linha Protheus - GPE - Por que rescisão gera id 1672 indevidamente quando a data de demissão contabiliza 12/12 avos de 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11062854403095-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-gera-id-1672-indevidamente-quando-a-data-de-demiss%C3%A3o-contabiliza-12-12-avos-de-13%C2%BA-sal%C3%A1rio?source=search)
