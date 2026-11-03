---
article_id: 1500002958661
category: NFe - Nota Fiscal Eletrônica
content_hash: 70654838fdb2382403f0addade955ce3f5937cb89205a4939aaf4d1fc892eee8
fetched_at: '2026-06-28T22:40:07.010733+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2021.001
type: support-article
updated_at: '2025-07-18T18:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002958661-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2021-001
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2021.001 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

* **NT 2021.001 -** Evento Comprovante de **Entrega da NF-e**

As empresas e as transportadoras continuam utilizando o tradicional **“Canhoto da Nota Fiscal”** contido na representação **impressa da NF-e para comprovação da entrega da mercadoria ao destinatário.**  
  
Para a NF-e, quando a entrega **não estiver relacionada com um Conhecimento de Transporte Eletrônico (CT-e),** criam-se os eventos abaixo a serem gerados pela empresa emitente da NF-e:

* Comprovante de Entrega da NF-e **(tpEvento=110130);**

* Cancelamento do Comprovante de Entrega da NF-e **(tpEvento=110131).**

1. No Protheus, ao acessar a rotina **Nf-e Sefaz**será apresentada a opção de transmissão **Comprovante de Entrega da NF-e**, conforme abaixo.

2. Após selecionada a opção de transmissão de Comprovante de Entrega da NF-e, será apresentada a tela de filtro dos ***documentos eletrônicos para envio do evento, onde:***

3. Será realizado o filtro dos documentos para que seja ***efetuado o envio do evento.***

![20220317_171323.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4835732293143)

4. Para envio do ***evento do cancelamento selecionar opção, abaixo:***

![20220317_172311.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4835738702999)

* ***Saiba mais:***

Para verificar o Boletim Técnico, *[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=625944778)*
