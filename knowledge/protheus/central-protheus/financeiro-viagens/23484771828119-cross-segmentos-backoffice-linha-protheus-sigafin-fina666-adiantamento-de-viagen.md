---
article_id: 23484771828119
category: Financeiro - Viagens
content_hash: e3d3d170391b84b9fd098690e2dacf21112f2145eba00b7fea7db41061f28b81
fetched_at: '2026-06-28T22:38:21.399608+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA666 - Adiantamento
  de Viagens acumula ao solicitar '
type: support-article
updated_at: '2024-05-15T14:43:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23484771828119-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA666-Adiantamento-de-Viagens-acumula-ao-solicitar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23484771733015) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo **Financeiro**, ao realizar uma viagem com adiantamento pela **FINA666** para a viagem, o valor fica acumulativo, ou seja, não respeita o valor da **FINA691 - Assistente de Configuração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23484771741847)

**Exemplo**   
Viagem de 14/05/2024  a 17/05/2024, onde o valor de adiantamento deveria ser 1.000,00 conforme configuração acima e está gerando 3.000,00 indevidamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23484771753495)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois no **FINA691 - Assistente de Configuração**, na aba de **Adiantamentos**, a opção de **Dt. base cálculo** está igual a **2 - Inic. Viagem**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23484771762711)

**Solução**Acessar a **FINA691** em **Adiantamentos** e alterar o campo **Dt. base cálculo**para **1 - Pedido,**

com isso, o adiantamento se manterá conforme cadastrado no **Assistente**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23484771777431)

**Saiba mais:**  
[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12) **![](https://centraldeatendimento.totvs.com/hc/article_attachments/23484771782551)**
