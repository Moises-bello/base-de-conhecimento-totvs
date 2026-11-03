---
article_id: 360038305194
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: e61c47c244b204dbb102628a1946e8342dcb5ab58b1bed7c7f247e947814fe8e
fetched_at: '2026-06-28T22:36:39.232324+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Quantidade de
  carregamento de embarque exportação
type: support-article
updated_at: '2022-06-09T20:28:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038305194-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Quantidade-de-carregamento-de-embarque-exporta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**A soma das quantidades informadas em cada lote excedeu em XX a quantidade da embalagem (Considerando a quantidade utilizada nos lotes dos outros Containers).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 12.1.17  
  
**Solução**O campo quantidade (EXA\_QTDE) da tela de carregamento de lotes no container se refere à quantidade de embalagens que serão carregadas deste lote e não a quantidade do item.  
Para exemplificar melhor o contexto, considere a quantidade de 10 unidades em duas embalagens (5 unidades cada). Ao carregar este item no container, não faz sentido informar a quantidade de (2,5 unidades) já que não podemos ter a metade de uma embalagem em um container e (1,5 unidades) de embalagens em outro.  
Tendo em vista a possível necessidade de manter o comportamento  no cenário anterior a correção. Pode ser fazer uso do ponto de entrada **ExecBlock("EECAE104",.F.,.F.,{"CARREGA\_TRB"})** para que possa manipular as informações da tabela temporária de controle (TRB).  
  
**Saiba mais**  
[DT PE EECAE104 Containers / Lotes no Embarque](https://tdn.totvs.com/display/PROT/EECAE104+-+Tela+de+carregamento+de+embarque)
