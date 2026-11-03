---
article_id: 360020445132
category: RH - Cálculo Adiantamento
content_hash: 5a36bb5a0b1b212afc106fc7f6dd25847b125b6ebd87fa7e684fc7fc4e99bc3f
fetched_at: '2026-06-28T22:43:14.206534+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Ao deixar o percentual do adiantamento zerado no
  cadastro do funcionário e lançar o valor manualmente o sistema não realiza o cálculo
type: support-article
updated_at: '2024-07-15T13:35:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020445132-RH-Linha-Protheus-GPE-Ao-deixar-o-percentual-do-adiantamento-zerado-no-cadastro-do-funcion%C3%A1rio-e-lan%C3%A7ar-o-valor-manualmente-o-sistema-n%C3%A3o-realiza-o-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24789677050647) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao deixar o percentual do adiantamento zerado no cadastro do funcionário e lançar o valor do adiantamento manualmente o sistema não realiza o cálculo, como realizar o cálculo desta forma?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da Versão 12.1.17.  
  
**Solução**Para solucionar essa ocorrência, aplique o pacote acumulado, deve ser aplicado primeiramente em base teste com backup do RPO:  
  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus?source=search)

**Importante!**  
A fórmula CHKPERC não deve ser desabilitada, do contrário, funcionários que não possuem percentual e nem verba lançada serão calculados até o final do roteiro, causando perda de performance e cálculo incorreto caso exista alguma verba lançada indevidamente na RGB.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24789733824279)  
  
**Saiba mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=557345637>

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
