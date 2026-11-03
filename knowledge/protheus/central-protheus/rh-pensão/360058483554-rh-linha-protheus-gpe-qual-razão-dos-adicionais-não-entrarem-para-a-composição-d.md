---
article_id: 360058483554
category: RH - Pensão
content_hash: 13a4f71d0deddcba4410466651426416b1e64602b9458e4dd20878c858c1305f
fetched_at: '2026-06-28T22:43:35.198157+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Qual razão dos Adicionais não entrarem para a composição
  da base de pensão na folha
type: support-article
updated_at: '2025-04-16T13:26:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058483554-RH-Linha-Protheus-GPE-Qual-raz%C3%A3o-dos-Adicionais-n%C3%A3o-entrarem-para-a-composi%C3%A7%C3%A3o-da-base-de-pens%C3%A3o-na-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24903171624343) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Qual razão dos Adicionais não entrarem para a composição da base de pensão na folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que os adicionais entrem na composição da base de pensão, devem estar configurados com **NÃO** **no campo** **Ref a Férias** e **Ref a 13°** e com **SIM** **no campo** **Pensão**, no cadastro da verba.

Caso estes campos de referência de Férias e 13° estejam com **SIM**, o sistema não validará para o cálculo da folha, pois **o sistema entende que essas verbas só entraram para o cálculo do roteiro especifico FER, 131 e 132.**

**OBS:** Caso o campo **Verbas Base de Cálculo** seja utilizado, no cadastro do Beneficiário, valide se está incluída a verba de adicional, pois sem a inclusão da mesma neste campo não entrará para a composição da base de pensão também.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101093693)

**Saiba mais:**

[RH - Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004995674-RH-Pens%C3%A3o)
