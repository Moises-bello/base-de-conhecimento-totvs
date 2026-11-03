---
article_id: 23912838650903
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 9d4b8240115843b9a49272b8671f7496a4ff444cb8bb413c22ab11716b06a629
fetched_at: '2026-06-28T22:39:52.206183+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Falha na Integração
  de Atributos. Falha no Download do Arquivo do Portal Único: Cannot Read Property
  ''forEach'' of Undefined'
type: support-article
updated_at: '2024-06-07T14:48:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23912838650903-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Falha-na-Integra%C3%A7%C3%A3o-de-Atributos-Falha-no-Download-do-Arquivo-do-Portal-%C3%9Anico-Cannot-Read-Property-forEach-of-Undefined
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23912832260375) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Esta ocorrendo um erro ao integrar o **Cadastro de Atributos** (EICAT400), sendo exibida uma mensagem:

**"Falha na Integração de Atributos.** **Falha no download do arquivo do portal único: Cannot read property 'forEach' of undefined."**

![erro_atributos.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23912832261271)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – a partir da versão 12.1.27  
  
**Solução**Esta mensagem indica uma possível inconsistência na comunicação com o portal único; confirme a configuração dos parâmetros **MV\_EIC0072**, **MV\_EIC0073** e **MV\_EIC0074**  em seu ambiente.

Os endereços da **URLS** devem estar conforme tabela abaixo:

|  |  |  |
| --- | --- | --- |
| **Parametro** | **Descrição** | **Conteúdo** |
| MV\_EIC0072 | URL do Endpoint de Integração do Portal Único em Produção (URL principal das APIs de integração para a produção | https://portalunico.siscomex.gov.br |
| MV\_EIC0073 | URL do Endpoint de Integração do Portal Único em Treinamento (URL principal das APIs de integração para treinamento | https://val.portalunico.siscomex.gov.br |
| MV\_EIC0074 | Ambiente de Integração com o Portal Único | 1=Produção, 2=Treinamento |

**Saiba mais**

[Atributos Portal Único - EICAT400](https://tdn.totvs.com/pages/releaseview.action?pageId=546680907)
