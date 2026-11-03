---
article_id: 35525001991191
category: Financeiro
content_hash: 1829b3fa829c20f174c935a6bc2e12d39cc53c1b06396e8e80cc7bf301cdaf3a
fetched_at: '2026-06-28T22:38:03.174382+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Alteração
  de valores regastados
type: support-article
updated_at: '2025-10-09T19:06:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35525001991191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Altera%C3%A7%C3%A3o-de-valores-regastados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35525001961623) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
É possível manipular os valores calculados pelo sistema no momento do resgate?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2310  
  
**Solução**  
Atualmente, no padrão do sistema **não é permitido alterar manualmente os valores do resgate**, mantendo os campos **desabilitados** para edição.

No entanto, caso seja necessário **customizar o processo**, é possível utilizar o **ponto de entrada FA181VLR**.

Esse ponto de entrada permite que, **no momento do resgate de uma aplicação**, sejam **ajustados os valores calculados pelo sistema**, tanto para o **valor principal** quanto para o **valor de juros**.

**Importante:**  
O ponto de entrada **FA181VLR não está disponível** para **aplicações baseadas em cotas (come cotas)**.

Para exemplo de uso, clique na documentação de referencia: [FA181VLR - No resgate da aplicação permite alterar os valores calculados pelo sistema](https://tdn.totvs.com/pages/releaseview.action?pageId=829296985)
