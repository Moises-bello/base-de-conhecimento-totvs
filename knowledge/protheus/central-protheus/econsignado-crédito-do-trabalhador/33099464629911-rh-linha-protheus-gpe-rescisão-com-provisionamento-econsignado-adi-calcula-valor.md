---
article_id: 33099464629911
category: eConsignado (Crédito do Trabalhador)
content_hash: be7fbaa99a3cbb2b38b7d64b9a500e5e7b53128b66c018b3e139bcb95cca311e
fetched_at: '2026-06-28T22:43:07.387566+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão com provisionamento eConsignado ADI calcula
  valor liquido incorreto ID 0126
type: support-article
updated_at: '2025-06-27T18:46:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33099464629911-RH-Linha-Protheus-GPE-Rescis%C3%A3o-com-provisionamento-eConsignado-ADI-calcula-valor-liquido-incorreto-ID-0126
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33099464613911) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**  
Por que rescisão com provisionamento eConsignado ADI calcula valor liquido incorreto ID 0126?  
  
**Ambiente**

TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

O cálculo rescisão com provisionamento eConsignado ADI calcula valor liquido incorreto ID 0126 devido incidência Sim Emp. Cons nos  IDS 1974 e 1975 (IDS  provisionamento ADI).

Os IDS 1974 e 1975 não possuem nenhuma incidência. Somente a verba de desconto eConsignado natureza 9253 deve ter incidência Sim Emp. Cons.

**Cadastro IDS:**

**ID 1974**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33099464615063)

**ID 1975**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33099480440599)

**Saiba Mais:**Para adquirir maior conhecimento acesse o link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=944703898>
