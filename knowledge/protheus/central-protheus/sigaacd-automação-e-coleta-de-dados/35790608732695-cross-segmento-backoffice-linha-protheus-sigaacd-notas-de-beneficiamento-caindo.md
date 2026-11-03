---
article_id: 35790608732695
category: SIGAACD - Automação e Coleta de Dados
content_hash: c7174eab3e0d593b9b9ecbba9767eeb325e19f2abb9965dc5f651729a2129eac
fetched_at: '2026-06-28T22:39:12.866346+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Notas de Beneficiamento
  caindo em processo de Conferência.
type: support-article
updated_at: '2025-10-21T20:37:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35790608732695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Notas-de-Beneficiamento-caindo-em-processo-de-Confer%C3%AAncia
---

No sistema Protheus, notas de beneficiamento feitas via Pré-Nota ou Documento de Entrada com parâmetros MV\_CONFFIS=S e MV\_TPCONF=1 caem em processo de conferência por padrão. Para ignorar essa conferência, pode-se usar o ponto de entrada SD1140I na Pré-Nota, atualizando o campo F1\_STATCON para vazio, deixando a pré-nota sem status de conferência.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35790608717335) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O que fazer para notas de beneficiamento não cair em processo de conferência?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Por nativo do sistema Protheus, as notas de beneficiamento, quando é realizado através da Pré-Nota ou Documento de Entrada, com a configuração do parâmetro **MV\_CONFFIS**=S  e **MV\_TPCONF**=1, essa notas vão cair em processo de conferência.

Por padrão no caso de entradas de beneficiamento, onde está atrelado a um cliente, estas serão direcionadas para conferência e o fluxo de conferência/liberação pode ser feito normalmente no coletor.

Caso tenha tratamentos diferenciados na conferência do beneficiamento do padrão e queira customizar para ignorar esta conferência, você pode usar o ponto de entrada [SD1140I](https://tdn.totvs.com/display/public/PROT/SD1140I) na Pré-Nota e definir as regras para ignorar a conferência atualizando o campo **F1\_STATCON** vazio e a Pre-Nota de beneficiamento ficará com o status sem conferência.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV120 - Processo de Conferência por Pré-Nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31453142889879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV120-Processo-de-Confer%C3%AAncia-por-Pr%C3%A9-Nota)
