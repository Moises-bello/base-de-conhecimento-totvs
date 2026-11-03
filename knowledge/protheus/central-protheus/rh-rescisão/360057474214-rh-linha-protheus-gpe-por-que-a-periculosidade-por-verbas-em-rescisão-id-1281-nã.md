---
article_id: 360057474214
category: RH - Rescisão
content_hash: ffca0290ad5c3c0942d58f48c428190ab9b8c76f29c6847eab26781e6b5f392d
fetched_at: '2026-06-28T22:43:49.838716+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que a periculosidade por verbas em rescisão
  id 1281 não é calculada somente pelo salário base quando o mnemônico P_RESADISB
  está com o conteúdo .T.
type: support-article
updated_at: '2025-07-21T12:32:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057474214-RH-Linha-Protheus-GPE-Por-que-a-periculosidade-por-verbas-em-rescis%C3%A3o-id-1281-n%C3%A3o-%C3%A9-calculada-somente-pelo-sal%C3%A1rio-base-quando-o-mnem%C3%B4nico-P-RESADISB-est%C3%A1-com-o-conte%C3%BAdo-T
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19350511783831)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Por que a periculosidade por verbas em rescisão ID 1281 não é calculada somente pelo salário base quando o mnemônico P\_RESADISB está com o conteúdo .T. ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**O ID 1281 se trata da periculosidade por verbas mês, assim em rescisão o cálculo considera a configuração cadastro sindicato e verbas com incidência Sim para periculosidade.

O mnemônico P\_RESADISB contendo o conteúdo .T. em rescisão calculará o adicional de periculosidade considerando o salário base somente para as verbas indenizatórias (aviso prévio indenizado, férias vencidas, proporcionais e 13 salário).

**Exemplo:**

**P\_RESADISB.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19350540279191)**

**Cadastro sindicato.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19350540281111)**

**Rescisão.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19350511791895)

**Valor hora extra e DSR hora extra com Sim periculosidade.**

**1.000,00 + 136,36 + 20,98 \* 30% = 347,20 valor periculosidade sobre verbas ID 1281.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19350540286743)

**Periculosidade verbas indenizatórias férias proporcionais e 13 salário.**

**2.500,00 \* 30% = 750,00 \ 12 \* 3 = 187,50**

**Saiba mais**[MP - GPE - Como considerar apenas o salário base para adicionais pagos sobre verbas em verbas indenizatórias (mnemônico P\_RESADISB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026402653-MP-GPE-Como-considerar-apenas-o-sal%C3%A1rio-base-para-adicionais-pagos-sobre-verbas-em-verbas-indenizat%C3%B3rias-mnem%C3%B4nico-P-RESADISB-?source=search)

[RH - Linha Protheus - GPE - Como configurar o cálculo de periculosidade sobre Salário + Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038877614-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-de-periculosidade-sobre-Sal%C3%A1rio-Verbas?source=search)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
