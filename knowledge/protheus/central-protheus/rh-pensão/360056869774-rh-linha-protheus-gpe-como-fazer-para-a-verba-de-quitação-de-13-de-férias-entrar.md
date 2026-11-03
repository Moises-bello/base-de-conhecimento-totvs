---
article_id: 360056869774
category: RH - Pensão
content_hash: f0c62c94a9a170f6d8a544c49e944c268c2a32cd9f7fe1c4bd0efbab2257c84f
fetched_at: '2026-06-28T22:43:35.155702+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer para a verba de quitação de 1/3 de férias
  entrar para a composição da pensão férias na folha
type: support-article
updated_at: '2025-04-16T13:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056869774-RH-Linha-Protheus-GPE-Como-fazer-para-a-verba-de-quita%C3%A7%C3%A3o-de-1-3-de-f%C3%A9rias-entrar-para-a-composi%C3%A7%C3%A3o-da-pens%C3%A3o-f%C3%A9rias-na-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24903479506583) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como fazer para a verba de quitação de 1/3 de férias entrar para a composição da pensão de férias na folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O sistema buscará para o cálculo de pensão alimentícia férias referente a quitação de 1/3 férias pago na folha pelas verbas de 1/3 de férias referentes a MP cujos códigos são definidos nos mnemônicos **P\_ADIPGFE** e **P\_ADIPGAB**, porém é necessária a realização dos procedimentos abaixo:  
**1.** Aplique o pacote abaixo:  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus?source=search)  
  
**2.** Parametrize a verba de Quitação 1/3 de férias com o campo Ref. a Fer e Pensao Alim. com SIM:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099480333)  
  
**3.** Relacione no mnemônico **P\_ADIPGFE** a verba de quitação 1/3 férias e no mnemônico **P\_ADIPGAB** a verba de quitação 1/3 abono pecuniário, conforme exemplo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099480653)  
  
**4.** Informe a verba de Quitação 1/3 férias no campo Verb. Bs. Calc no cadastro de beneficiários para cálculo da pensão e no campo verba Férias a verba que será efetuado o cálculo da pensão:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099481393)  
  
**5.** Calcule a folha de pagamento, sistema irá calcular o valor da pensão referente a verba 1/3 quitação férias informada/gerada na folha, conforme parametrizado no cadastro de Beneficiário:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097171874)

**Saiba mais:**

[RH - Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004995674-RH-Pens%C3%A3o)

[DRHPAG-39342 DT Cálculo do 1/3 de férias referente a MP na folha](https://tdn.totvs.com/pages/viewpage.action?pageId=562489402)
