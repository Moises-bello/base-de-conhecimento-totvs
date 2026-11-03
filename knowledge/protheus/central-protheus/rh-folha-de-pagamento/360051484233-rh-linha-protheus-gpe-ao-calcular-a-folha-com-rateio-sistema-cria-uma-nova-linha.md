---
article_id: 360051484233
category: RH - Folha de Pagamento
content_hash: 337f7b5c681e86ffe1301c4697825bbfce2f6d101d3b9067fd9e459e23dfd9aa
fetched_at: '2026-06-28T22:44:11.959105+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular a folha com rateio, sistema cria uma
  nova linha com origem U
type: support-article
updated_at: '2024-09-13T17:19:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051484233-RH-Linha-Protheus-GPE-Ao-calcular-a-folha-com-rateio-sistema-cria-uma-nova-linha-com-origem-U
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355276211479) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Ao calcular a folha com rateio, sistema cria uma nova linha com origem U. O que fazer?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - GPE – Todas as versões

**Solução**Para que o rateio seja calculado corretamente na folha de pagamento e não gere a linha com origem U na programação de rateio, a configuração das verbas deve ser:

- Uma verba com o campo de rateio igual B (Base);  
- Outras verbas com o campo de rateio iguala a S (Sim) ou N (Não);

Caso tenha mais verbas cadastradas com o campo rateio = B, o sistema se perde, não calcula o rateio corretamente e gera a linha com origem U indevidamente.

**Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
