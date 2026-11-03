---
article_id: 6318894473495
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: a5884b31e1eec2e7aefbb58d8a02d51d505332c28a85f6887a0239f4fab48cf2
fetched_at: '2026-06-28T22:45:21.196880+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: TAF - Rotinas Comuns - Monitor eSocial do Futuro (TAF do Futuro) - Não foi
  possível obter o detalhe da inconsistência. Realize a transmissão novamente.
type: support-article
updated_at: '2024-05-23T19:59:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6318894473495-TAF-Rotinas-Comuns-Monitor-eSocial-do-Futuro-TAF-do-Futuro-N%C3%A3o-foi-poss%C3%ADvel-obter-o-detalhe-da-inconsist%C3%AAncia-Realize-a-transmiss%C3%A3o-novamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00min** **Dúvida**

Ao tentar transmitir um evento pelo monitor da rotina eSocial do Futuro (TAF do Futuro), ocorre inconsistência com a seguinte mensagem:

*"Não foi possível obter o detalhe da inconsistência. Realize a transmissão novamente."*

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6318748687255/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - Monitor eSocial do Futuro - TAFA552 - Todas as versões  
  
**Solução**Este erro ocorre ao tentar transmitir os eventos na versão do layout 02\_05\_00 do eSocial.

Para correção:

1. Ajuste o sistema para o layout simplificado S\_01\_00\_00, conforme documentação no link abaixo:

[Automação Fiscal - Atualização - Código da Resposta: 403 - Leiaute do evento invalido, alterar leiaute eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6280966412183)

2. Exclua o evento do TAF, e refaça a reintegração, após, transmita o evento novamente;
