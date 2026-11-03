---
article_id: 22934545285143
category: eSocial - Gerar XML/ Integração Evento
content_hash: dd08b997cd7710529dfd427a4766ed09da14d70d12e091c4e8c970ee1431bbb1
fetched_at: '2026-06-28T22:47:12.012168+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como é gerado no XML S-1200 e S-1210 os demonstrativos
  por lançamento para autônomos do TOTVS Gestão Financeira
type: support-article
updated_at: '2026-05-27T21:13:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22934545285143-RH-RM-FOP-eSocial-Como-%C3%A9-gerado-no-XML-S-1200-e-S-1210-os-demonstrativos-por-lan%C3%A7amento-para-aut%C3%B4nomos-do-TOTVS-Gest%C3%A3o-Financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22934517222935) Tempo aproximado para leitura: **00:02:20 min**  
  
**Dúvida**  
Como é gerado no XML S-1200 e S-1210 os demonstrativos por lançamento para autônomos do TOTVS Gestão Financeira?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.23  
  
**Solução**  
Houve uma modificação na chave do evento S-1200 no leiaute S-1.0 do eSocial, onde a chave passou a ser composta pelo Tipo de Pagamento, Período de Referência e Identificação do Movimento. Em resposta a essa modificação, houver alteração na chave dos eventos S-1200 e S-1210 dos autônomos.  
Anteriormente, a tag <ideDmDev> unificava os lançamentos em um único ideDmDev, após tal alteração no leiaute a chave passa a ser composta pelo código do lançamento. Essa adaptação busca seguir as atualizações no leiaute do eSocial e assegurar a conformidade com as mudanças efetuadas.  
No exemplo a seguir, analisaremos os dois lançamentos, identificados pelos códigos 7144 e 7139.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934545260823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934545262103)

No XML S-1200, foram gerados dois <ideDmDev> com o código do lançamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934545262999)![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934545264535)

No XML S-1210, foram gerados dois <ideDmDev> com o código do lançamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934517230359)

**Importante!**   
Após a atualização, será necessário regerar todos os periódicos dos autônomos do TOTVS Gestão Financeira do período atual.   
Caso haja a necessidade de retificação do XML do S-1210 de períodos anteriores, é necessário enviar uma retificação do evento S-1200, pois os <ideDmDev> serão gerados por lançamento.  
  
Saiba mais  
Para mais informações acesse:

[Como será gerado os eventos S-1200 e S-1210 para autônomos do Gestão Financeira que possuem vínculo na Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22934035700375)
