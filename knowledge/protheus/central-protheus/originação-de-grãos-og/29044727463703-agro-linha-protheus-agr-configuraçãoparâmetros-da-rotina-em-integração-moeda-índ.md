---
article_id: 29044727463703
category: Originação de Grãos (OG)
content_hash: b27cf0773f49953a9bb9be4ba114ca8d7acd2c4863d97a52150e4673023bf7ec
fetched_at: '2026-06-28T22:45:37.764902+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração/Parâmetros da Rotina em Integração
  moeda, índice, commodities
type: support-article
updated_at: '2025-05-06T12:34:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29044727463703-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-em-Integra%C3%A7%C3%A3o-moeda-%C3%ADndice-commodities
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29044735416983) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Quais são os principais parâmetros em **Configuração/Parâmetros da Rotina em Integração moeda, índice, commodities**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Principais parâmetros:**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** |
| [MV\_AGRO200](https://tdn.totvs.com/x/bpEOFQ) | URL: Utilizada para realizar a autenticação de integração com a M2M. |  |
| [MV\_AGRO201](https://tdn.totvs.com/pages/viewpage.action?pageId=353276354) | E-mail para realizar a autenticação para a geração do Token e integração M2M. |  |
| [MV\_AGRO202](https://tdn.totvs.com/pages/viewpage.action?pageId=539531069) | Password para realizar a autenticação para a geração do Token e integração M2M. |  |
| [MV\_AGRO203](https://tdn.totvs.com/x/KZIOFQ) | URL: Utilização do Token para solicitar a cotação Atual - Passada |  |
| [MV\_AGRO204](https://tdn.totvs.com/x/rpIOFQ) | URL: Utilização do Token para solicitar a cotação Atual - Futura |  |

**Pré-requisitos:**

* Parâmetros [MV\_AGRO200](https://tdn.totvs.com/x/bpEOFQ), [MV\_AGRO201](https://tdn.totvs.com/pages/viewpage.action?pageId=353276354),[MV\_AGRO202](https://tdn.totvs.com/pages/viewpage.action?pageId=539531069) , [MV\_AGRO203](https://tdn.totvs.com/x/KZIOFQ) e [MV\_AGRO204](https://tdn.totvs.com/x/rpIOFQ) configurados.
* Possuir nas rotinas os campos de integração devidamente configurados.
