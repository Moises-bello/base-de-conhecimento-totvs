---
article_id: 4825224237079
category: RH - Rescisão
content_hash: a08be4ea9c8618f201a9e02405e877b203553fe8cb779f34142d983348b4cd28
fetched_at: '2026-06-28T22:43:49.902233+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que rescisão calcula insalubridade sobre verbas
  (id 1282) sobre salário mínimo e calcula insalubridade verbas indenizatórias sobre
  o salário mês
type: support-article
updated_at: '2025-04-16T14:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4825224237079-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-calcula-insalubridade-sobre-verbas-id-1282-sobre-sal%C3%A1rio-m%C3%ADnimo-e-calcula-insalubridade-verbas-indenizat%C3%B3rias-sobre-o-sal%C3%A1rio-m%C3%AAs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26681381348887) Tempo aproximado para leitura: **00:01:00 min** **Dúvida** Por que rescisão calcula insalubridade sobre verbas (id 1282) sobre salário mínimo e calcula insalubridade verbas indenizatórias sobre o salário mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O cálculo da insalubridade é definido em cadastro Sindicato aba Peric\Insal. A rescisão calcula o id 1282 sobre o salário mínimo, devido a configuração no cadastro de Sindicato aba Peric\Insal campo RCE\_BCALIN = 1 e a insalubridade verbas indenizatórias foram calculadas sobre o salário mês devido o mnemônico  P\_RESADISB = .T.

Para todos os valores de rescisão serem calculados pelo salário mínimo, o campo RCE\_BCALIN deve ser preenchido com 1 e o mnemônico  P\_RESADISB = .F.

**Cadastro Sindicato**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4825090416151)

**P\_RESADISB**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4825099419543)

**Saiba mais**[RH - Linha Protheus - GPE - Como considerar apenas o salário base para adicionais pagos sobre verbas em verbas indenizatórias (mnemônico P\_RESADISB)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026402653-MP-GPE-Como-considerar-apenas-o-sal%C3%A1rio-base-para-adicionais-pagos-sobre-verbas-em-verbas-indenizat%C3%B3rias-mnem%C3%B4nico-P-RESADISB-?source=search)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
