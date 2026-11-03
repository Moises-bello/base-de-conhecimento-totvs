---
article_id: 8591084213655
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4485c1d2bc1a59f94308506922271935df2757677d48931e3b77755b0e0bbc50
fetched_at: '2026-06-28T22:47:11.911417+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao enviar S-2230 ocorre o erro: 106 - Foi localizado
  no sistema um evento em duplicidade, com o evento a ser enviado, mesmo Contrato,
  Motivo de Afastamento e Data'
type: support-article
updated_at: '2025-12-29T14:42:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8591084213655-RH-RM-FOP-eSocial-Ao-enviar-S-2230-ocorre-o-erro-106-Foi-localizado-no-sistema-um-evento-em-duplicidade-com-o-evento-a-ser-enviado-mesmo-Contrato-Motivo-de-Afastamento-e-Data
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24346849890711) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao transmitir o evento S-2230, o governo retorna a mensagem de erro **Código do erro: 106 Descrição: Foi localizado no sistema um evento em duplicidade, com o evento a ser enviado, mesmo Contrato, Motivo de Afastamento e Data.**As datas podem ser de Início, Término ou ambas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8589460177943)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - Todas as versões  
  
**Causa**  
Essa inconsistência ocorre quando já consta no ambiente do governo (RET) um afastamento para a mesma matrícula com o mesmo código de afastamento e mesma data (data início ou data término, ou ambas).  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Identifique no XML S-2230 o grupo **afastamento**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8590706057623)

2. Acesse a movimentação trabalhista do funcionário no portal do eSocial (portal do governo) e identifique se há algum afastamento cadastrado com o mesmo código de afastamento e mesma data de início, ou data de término, ou com as datas início e término iguais;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8590761592855)

3. Verifique a necessidade do envio do evento, ou se o mesmo deverá ser encaminhado como retificação, ou somente com data término. Ex.: Encontrado no governo registro com mesma data de início. Deve-se verificar então se há necessidade de enviar novamente o evento e, neste caso, umas das informações (matrícula, motivo de afastamento e data) devem ser diferentes.  
  
**Saiba mais**  
Para mais informações sobre o S-2230 acesse:  
     • [S-2230 - Afastamento Temporário](http://tdn.totvs.com/pages/viewpage.action?pageId=364908488)   
     • [Ações no sistema que podem gerar um evento S-2230](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360002979931)
