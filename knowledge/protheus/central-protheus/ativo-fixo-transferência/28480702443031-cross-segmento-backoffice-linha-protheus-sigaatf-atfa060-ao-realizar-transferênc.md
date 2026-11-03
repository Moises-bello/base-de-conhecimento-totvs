---
article_id: 28480702443031
category: Ativo Fixo - Transferência
content_hash: 69233fbbc7cfda397249753ba1cbf4afed73af603654f179ef127db409985421
fetched_at: '2026-06-28T22:41:52.242704+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF- ATFA060 - Ao realizar
  transferência de entidades contábeis o sistema apresenta HELP: AF060TDOK'
type: support-article
updated_at: '2024-12-12T18:09:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28480702443031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Ao-realizar-transfer%C3%AAncia-de-entidades-cont%C3%A1beis-o-sistema-apresenta-HELP-AF060TDOK
---

**Dúvida**

 Ao tentar realizar a transferência do ativo sistema apresenta mensagem: Help :AF060TDOK

**Problema**: A transferência parcial só pode ser realizada entre filiais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28480702413207)

**Ambiente:**  
Protheus - Ativo Fixo – Todas as versões  
  
  
**Solução:**

A transferência parcial de ativos com quantidade superior a 1 é permitida somente entre filiais.

Por esse motivo, ao realizar a transferência, o sistema poderá exibir a seguinte mensagem:  
**"AF060TDOK: A transferência parcial só pode ser realizada entre filiais."**

Se houver necessidade de ajustar entidades contábeis ou grupos dentro da mesma filial, o processo deverá ser realizado **apenas após o desmembramento dos itens**.

Para desmembrar os itens, utilize a rotina **ATFA251**. Após o desmembramento, os ajustes poderão ser efetuados conforme a necessidade inicial.

Saiba Mais:  
[Aquisição por Transferência](http://tdn.totvs.com/pages/releaseview.action?pageId=6067616)

[ATFA060 - Como funciona a rotina de Transferência de ativo entre filiais e contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015091671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Como-funciona-a-rotina-de-Transfer%C3%AAncia-de-ativo-entre-filiais-e-cont%C3%A1bil)

[Transferência entre Filiais](https://tdn.totvs.com/pages/releaseview.action?pageId=6067606)
