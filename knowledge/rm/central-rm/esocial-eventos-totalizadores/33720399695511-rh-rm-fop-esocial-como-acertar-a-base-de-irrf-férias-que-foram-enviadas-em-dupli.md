---
article_id: 33720399695511
category: eSocial - Eventos Totalizadores
content_hash: b536f39716903d389da2b76009c9222c7715c1e0570b71834d7de1bacbbdec14
fetched_at: '2026-06-28T22:47:06.971843+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP - eSocial  - Como acertar a Base de IRRF Férias que foram enviadas
  em duplicidade no eSocial
type: support-article
updated_at: '2026-05-27T21:19:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33720399695511-RH-RM-FOP-eSocial-Como-acertar-a-Base-de-IRRF-F%C3%A9rias-que-foram-enviadas-em-duplicidade-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33720434969239) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como acertar a Base de IRRF Férias que foram enviadas em duplicidade no eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da release 12.1.24.  
  
**Solução**  
Para solucionar a duplicidade de IRRF de Férias no eSocial, será preciso:  
1. Criar evento com Código de Cálculo 381- Base de IRRF Férias Envelope;  
Este deverá ser do tipo "**Base de Cálculo**", sem incidência e com o código da Natureza da Rubrica (eSocial) igual a **9939-Outros valores tributáveis**. Essa é a rubrica indicada no sistema para os eventos do tipo base de calculo que são considerados como valores tributáveis para o eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33720399673623)

2. Encaminhar o S-1010 Gerado na fila de eventos não periódicos, para o eSocial;  
3. Enviar os eventos periódicos S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social  e  S-1210 - Pagamentos de Rendimentos do Trabalho. E caso trabalhar com Tomador de Serviços, distribuir o mesmo para correta geração do XML S-1200.

**Saiba Mais:**  
[Como acertar a Base de IRRF Férias que foram enviadas em duplicidade no eSocial?](https://tdn.totvs.com/pages/releaseview.action?pageId=415705088#ErroseA%C3%A7%C3%B5es-1831861203)
