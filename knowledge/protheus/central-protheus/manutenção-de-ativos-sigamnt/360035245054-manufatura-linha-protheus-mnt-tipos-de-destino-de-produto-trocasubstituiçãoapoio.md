---
article_id: 360035245054
category: Manutenção de Ativos (SIGAMNT)
content_hash: 0a7cf7a01be2da6fe8509091ea2d03693156db653b02ffaecfe5187b1c698daa
fetched_at: '2026-06-28T22:42:34.492219+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Tipos de Destino de Produto -  Troca/Substituição/Apoio
type: support-article
updated_at: '2021-09-09T18:59:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035245054-Manufatura-Linha-Protheus-MNT-Tipos-de-Destino-de-Produto-Troca-Substitui%C3%A7%C3%A3o-Apoio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Na rotina **Retorno Mod. 2 - MNTA435** qual o objetivo do campo **Destino** quando o **Insumo** é do tipo **Produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões.  
  
**Solução**O campo **Destino - TL\_DESTINO** é apenas informativo, e indica o destino que foi aplicado o produto no retorno da **O.S. - Ordem de serviço**, podendo ser:

* **Troca**
* **Substituição**
* **Apoio**

**Importante**Para qualquer uma das opções, o produto informado irá baixar o saldo no estoque, caso esteja com o parâmetro de estoque **MV\_NGMNTES** - **Integração Manutenção (MNT) com Estoque (EST)** igual a **S - Sim**.
