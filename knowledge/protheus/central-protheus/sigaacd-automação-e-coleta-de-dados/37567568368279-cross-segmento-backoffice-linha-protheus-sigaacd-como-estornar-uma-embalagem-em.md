---
article_id: 37567568368279
category: SIGAACD - Automação e Coleta de Dados
content_hash: 129389c61c050ce02c5871454a2e134b9fb72b2c9e7db1a73249138d3f0fa808
fetched_at: '2026-06-28T22:39:12.567060+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como estornar uma
  embalagem em andamento?
type: support-article
updated_at: '2026-01-09T19:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37567568368279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-estornar-uma-embalagem-em-andamento
---

No Protheus, para estornar uma etiqueta de embalagem com status igual a três, não é possível fazê-lo diretamente sem finalizar a próxima embalagem em andamento. O estorno deve ser realizado usando o ponto de entrada ACD167VV.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37567539258007) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como realizar o estorno de uma etiqueta de embalagem em andamento quando o campo Status está igual três?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567539258775)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Na rotina de embalagem(ACDV167) não temos como estornar uma embalagem sem ter que finalizar a próxima embalagem, não temos como estornar uma embalagem com a outra em andamento.   
   
Para estornar a embalagem pode usar o ponto de entrada [ACD167VV](https://tdn.totvs.com/pages/releaseview.action?pageId=6090976).

Ao finalizar a embalagem muda o status para 9 finalizado conforme a imagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567539260439)  
 E quando finaliza o processo  de embalagem todo tem como desfazer a separação, conforme a imagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567568359447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567568360343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567539262103)

Caso o ponto de entrada para lhe atender, pode registrar uma melhoria na [Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/posts/360050952374-TOTVS-Portal-do-Cliente-Central-Colaborativa-Melhorias-Busca-na-central-colaborativa)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
