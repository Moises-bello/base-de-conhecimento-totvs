---
article_id: 22934035700375
category: eSocial - Gerar XML/ Integração Evento
content_hash: 0c434bf5094f6166d928d72bc971d46a84aa06b1e48e1897f0e7d270b3a1383c
fetched_at: '2026-06-28T22:47:13.067287+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Middleware - Como será gerado os eventos S-1200 e
  S-1210 para autônomos do Gestão Financeira que possuem vínculo na Folha de Pagamento
type: support-article
updated_at: '2026-05-27T21:13:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22934035700375-RH-RM-FOP-eSocial-Middleware-Como-ser%C3%A1-gerado-os-eventos-S-1200-e-S-1210-para-aut%C3%B4nomos-do-Gest%C3%A3o-Financeira-que-possuem-v%C3%ADnculo-na-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22934035676695) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como será gerado os eventos S-1200 e S-1210 para autônomos do Gestão Financeira que possuem vínculo na Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.23  
  
**Solução**  
Houve uma modificação na chave do evento S-1200 no leiaute S-1.0 do eSocial, onde a chave passou a ser composta pelo Tipo de Pagamento, Período de Referência e Identificação do Movimento. Em resposta a essa modificação, foi realizada uma alteração na chave dos eventos S-1200 e S-1210 dos autônomos.  
Anteriormente, a tag <ideDmDev> unificava os lançamentos em um único ideDmDev, após a modificação, a chave passa a ser composta pelo número do lançamento. No entanto, quando ocorrer do autônomo possuir vínculo na Folha de Pagamentos, o ideDmDev será gerado de acordo com os quatro últimos números do código do lançamento. Essa adaptação busca seguir as atualizações no leiaute do eSocial e assegurar a conformidade com as mudanças efetuadas.  
No exemplo a seguir, foram adequados os lançamentos identificados pelos códigos 997336 e 997341, bem como um envelope lançado para o funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22933997323287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934035682967)

Foi lançado verbas no envelope de pagamento do funcionário da Folha, com período 1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934035684887)

No XML S-1200, foram geradas duas tags <ideDmDev>, cada uma contendo os quatro últimos números do código do lançamento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22933997332375)

No XML S-1210, foram geradas duas tags <ideDmDev>, cada uma contendo os quatro últimos números do código do lançamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22933997334423)

**Importante**   
Após a atualização, será necessário regerar todos os periódicos dos autônomos do TOTVS Gestão Financeira do período atual.   
Caso haja a necessidade de retificação do XML do S-1210 de períodos anteriores, é necessário enviar uma retificação do evento S-1200, pois os <ideDmDev> serão gerados por lançamento.

**Saiba mais**  
Para mais informações acesse:

[S-1200 e S-1210 - Múltiplos Vínculos - Separação de demonstrativos por lançamento para autônomos do TOTVS Gestão Financeira (Middleware)](https://tdn.totvs.com/pages/releaseview.action?pageId=818466561)   
[S-1200 e S-1210 - Separação de demonstrativos por lançamento para autônomos do TOTVS Gestão Financeira](https://tdn.totvs.com/pages/releaseview.action?pageId=809518899)
