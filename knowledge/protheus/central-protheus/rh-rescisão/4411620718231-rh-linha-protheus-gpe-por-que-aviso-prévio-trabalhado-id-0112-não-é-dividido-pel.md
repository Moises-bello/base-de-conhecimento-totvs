---
article_id: 4411620718231
category: RH - Rescisão
content_hash: f7086a4554c8048b4c49a2195e379728e834a28b41b8012d7d1ab9eb4093a23f
fetched_at: '2026-06-28T22:43:53.502534+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que aviso prévio trabalhado id 0112, não é
  dividido pelos dias mês conforme configuração mnemônico P_DIASRES = 1
type: support-article
updated_at: '2025-05-20T19:20:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411620718231-RH-Linha-Protheus-GPE-Por-que-aviso-pr%C3%A9vio-trabalhado-id-0112-n%C3%A3o-%C3%A9-dividido-pelos-dias-m%C3%AAs-conforme-configura%C3%A7%C3%A3o-mnem%C3%B4nico-P-DIASRES-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18548433011479) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que aviso prévio trabalhado id 0112, não é dividido pelos dias mês conforme configuração mnemônico P\_DIASRES = 1?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Conforme legislação o cálculo do aviso prévio sempre será pela base 30 dias, assim em caso de aviso prévio trabalhado o id 0112 sempre será dividido por 30, mesmo o mnemônico P\_DIASRES = 1.

Em rescisão a divisão pelos dias mês conforme P\_DIASRES = 1 se aplica ao saldo de salário id 0048.

**Exemplo:**

**P\_DIASRES = 1**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18548440331159)

**Rescisão aviso trabalhado data demissão 15.10.2023**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18548433021079)**

**2.100,00 \ 30 \* 15 = 1.050,00**

**Saiba mais**  
Para adquirir mais conhecimento acesse o *link* abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=630371324>

[RH - Linha Protheus - GPE - Como calcular rescisão de acordo com os dias do mês ou sempre por 30 (divisão salário) (P\_DIASRES)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025315674-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-acordo-com-os-dias-do-m%C3%AAs-ou-sempre-por-30-divis%C3%A3o-sal%C3%A1rio-P-DIASRES-?source=search)
