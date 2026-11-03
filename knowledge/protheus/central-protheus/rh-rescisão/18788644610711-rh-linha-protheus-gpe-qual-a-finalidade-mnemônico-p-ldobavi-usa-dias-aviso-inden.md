---
article_id: 18788644610711
category: RH - Rescisão
content_hash: e1a627db04433ce0dca9ef43adb03c2427651542cd2626e9b298d036aaa55816
fetched_at: '2026-06-28T22:43:53.758361+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Qual a finalidade mnemônico P_LDOBAVI (usa dias
  aviso indenizado para calcular férias em dobro)
type: support-article
updated_at: '2025-05-09T19:18:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18788644610711-RH-Linha-Protheus-GPE-Qual-a-finalidade-mnem%C3%B4nico-P-LDOBAVI-usa-dias-aviso-indenizado-para-calcular-f%C3%A9rias-em-dobro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18788658056599) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual a finalidade mnemônico P\_LDOBAVI (usa dias aviso indenizado para calcular férias em dobro)?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Conforme entendimento da Lei 12.506/2011, a projeção do aviso prévio conta como tempo de serviço, e por esta razão esses dias sempre foram considerados para cálculo de férias em dobro.

Porém entendimento diferente do TST, conforme [explicado pela nossa consultoria de segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=309396016), implica na não utilização destes dias para tal finalidade. Devido não existir legislação especifica sobre o assunto, foi criado o mnemônico **P\_LDOBAVI**para efetuar este controle.

O valor padrão do mnemônico é **.T.**, ou seja, os dias de aviso prévio continuam sendo utilizados no cálculo de férias em dobro.

Caso a projeção não deva ser utilizada, o mnemônico deve ser alterado para **.F.**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=751505636>

<https://tdn.totvs.com/pages/releaseview.action?pageId=309396016>

[MP - GPE - Criação do mnemônico P\_LDOBRES para cálculo de férias em dobro na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017420572-MP-GPE-Cria%C3%A7%C3%A3o-do-mnem%C3%B4nico-P-LDOBRES-para-c%C3%A1lculo-de-f%C3%A9rias-em-dobro-na-rescis%C3%A3o?source=search)
