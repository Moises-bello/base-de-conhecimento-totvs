---
article_id: 360015427792
category: esocial - Periódicos
content_hash: 9c1f82fda6b8fc68b912dda4734ba8b7909731cd09551b7af324ed157341af56
fetched_at: '2026-06-28T22:47:09.365898+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Evento S-1200 para autônomos cuja categoria não demandam
  o envio do evento S-2300
type: support-article
updated_at: '2025-08-13T12:17:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015427792-RH-RM-FOP-eSocial-Evento-S-1200-para-aut%C3%B4nomos-cuja-categoria-n%C3%A3o-demandam-o-envio-do-evento-S-2300
---

**Dúvida**  
O que é gerado no evento S-1200 quando a categoria eSocial não demanda o envio do evento S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário Início?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
De acordo com o [leiaute do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica), um trabalhador cujo envio do **S-2300** não tiver ocorrido por **não ser obrigatório**, deve possuir um evento de remuneração com os dados dos grupos **infoComplem** e **infoComplCont** preenchidos:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406621551127)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406622994583)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406623073943)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406623090455)

O TOTVS Folha de Pagamento irá avaliar se, para o CPF a ser gerado o S-1200, existe ou não um S-2300 aceito pelo RET na fila de eventos do eSocial. Caso o sistema não encontre um S-2300, as *tags* **infoComplem** e **infoComplCont**são geradas no S-1200. Caso exista um S-2300 na fila de eventos, as *tags* supracitadas não são geradas.  
  
**Saiba mais**  
Para visualizar o **passo a passo** de geração do evento S-1200 e S-1210 dos autônomos do Gestão Financeira, acesse:   
[- Geração do S-1200 e S-1210 para autônomos do Gestão Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015349532)
