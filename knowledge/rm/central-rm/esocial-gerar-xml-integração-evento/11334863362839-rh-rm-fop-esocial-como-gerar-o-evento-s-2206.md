---
article_id: 11334863362839
category: eSocial - Gerar XML/ Integração Evento
content_hash: 094b26b59f4c391755eb6b1d692a0254d5b27faa0f24f3173bf49b6632e71bb1
fetched_at: '2026-06-28T22:47:12.034711+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como gerar o evento S-2206
type: support-article
updated_at: '2023-01-05T19:19:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11334863362839-RH-RM-FOP-eSocial-Como-gerar-o-evento-S-2206
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min****Dúvida**Como gerar o evento S-2206 – Alteração de Contrato de Trabalho na Fila de Eventos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Para que seja gerado o evento é necessário que exista registro de alterações no contrato de trabalho, tais como: remuneração e periodicidade de pagamento, duração do contrato, local, cargo ou função, jornada, etc. Para isso, realize o processo conforme a seguir:

1. Sempre que o usuário realizar uma alteração no cadastro de funcionário, esse dados serão espelhados no histórico do funcionário com as datas de mudança e processamento. Poderá consultar o Histórico do funcionário em **Anexos | Históricos;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11334887845527)

2. Após realizar a alteração no cadastro do funcionário, será gerado um gatilho na fila de eventos para o evento **S-2206 – Alteração de Contrato de Trabalho** do funcionário em questão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11427730283159)

3. Gere o XML e envie ao eSocial.  
  
**Saiba mais:**Para mais informações acesse:- [RH - RM - FOP - eSocial - Não geração de gatilhos S-2206 em casos de alteração contratual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013968731-RH-RM-FOP-eSocial-N%C3%A3o-gera%C3%A7%C3%A3o-de-gatilhos-S-2206-em-casos-de-altera%C3%A7%C3%A3o-contratual?source=search)
