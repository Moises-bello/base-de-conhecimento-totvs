---
article_id: 20504540323991
category: Financeiro - Contas a Receber
content_hash: 02860f309874aec45451d137248674a04c2d7f4df2d9b6cc9e0aaaf6a2f22227
fetched_at: '2026-06-28T22:38:12.744503+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA022 - Criar novos
  tipos de carteira e realizar a contabilização
type: support-article
updated_at: '2024-01-12T13:19:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20504540323991-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA022-Criar-novos-tipos-de-carteira-e-realizar-a-contabiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20504534289431) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como criar novos tipos de carteira e realizar a contabilização?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA022 - Todas as versões

**Solução**A criação de uma nova **situação de cobrança** determinará qual **Lançamento Padrão** (**LP**) utilizará para contabilizar, como exemplo:  
Criar uma situação chamada **Teste** com as mesmas características da **cobrança simples**, só mude o **nome** e o **código**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20504540289943)

Quando realiza uma **transferência de carteira** de **0** para **Teste,** o sistema irá executada a **LP541** **"Na transferência para Carteira de Cobrança Simples/Cartório no Contas a Receber  (1/H)" Rotina FINA060.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20504540293655)

Caso realize a baixa desse movimento, o sistema executará a **LP521 - "Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber  (1/H)"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20504534295063)

Dependo da característica que adicione na sua **situação de cobrança**, o sistema busca uma das **LPs** que tenha a mesma particularidade das LPs cadastradas no sistema, desta forma, realiza a contabilização das novas **situações** **de cobranças**.

**Saiba Mais:**

[Situação de Cobrança (FINA022 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=415715057)

[Lançamento padrão Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)
