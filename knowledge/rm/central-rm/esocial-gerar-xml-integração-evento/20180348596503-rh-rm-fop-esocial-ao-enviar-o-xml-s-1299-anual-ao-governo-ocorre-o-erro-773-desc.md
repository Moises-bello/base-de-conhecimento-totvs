---
article_id: 20180348596503
category: eSocial - Gerar XML/ Integração Evento
content_hash: 9a12a43c31657ef49adadcb5ce9abedf378fb31f56b130040483d5bd520a73d2
fetched_at: '2026-06-28T22:47:11.907352+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao enviar o XML S-1299 anual ao governo ocorre o
  erro: 773 - Descrição : Falha ao confirmar o fechamento da folha para o Sistema
  DCTF Web (429 - Formato do período de apuração do debito 109901 inválido.'
type: support-article
updated_at: '2024-04-17T17:55:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20180348596503-RH-RM-FOP-eSocial-Ao-enviar-o-XML-S-1299-anual-ao-governo-ocorre-o-erro-773-Descri%C3%A7%C3%A3o-Falha-ao-confirmar-o-fechamento-da-folha-para-o-Sistema-DCTF-Web-429-Formato-do-per%C3%ADodo-de-apura%C3%A7%C3%A3o-do-debito-109901-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20180325609239) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao enviar o XML S-1299 anual ao governo ocorre o erro: Código da Ocorrência: 773 - Descrição : Falha ao confirmar o fechamento da folha para o Sistema DCTF Web (429 - Formato do período de apuração do debito 109901 inválido. O valor do campo paDebito deve ser informado conforme a periodicidade Mensal.).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20180387224471)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O código 109901 refere ao Código de Receita de desconto de contribuinte individual (Autônomo).

**![](https://totvssuporte.zendesk.com/attachments/token/XhNzJlZsxlUy9SmHHew8T4fYA/?name=image.png)**

O erro ocorre pois foi enviado XML S-1200 no período anual, para algum autônomo. Sendo que, para o governo não é válido o pagamento de 13° salário para autônomos.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Identificar para qual autônomo foi lançado evento de 13° salário;

2. Enviar o evento S-3000 de exclusão do S-1200 anual para o governo;

3. Reenviar o S-1299 anual.

**Saiba mais**  
Para mais informações, acesse:

* [RH - RM - FOP - eSocial - Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)
