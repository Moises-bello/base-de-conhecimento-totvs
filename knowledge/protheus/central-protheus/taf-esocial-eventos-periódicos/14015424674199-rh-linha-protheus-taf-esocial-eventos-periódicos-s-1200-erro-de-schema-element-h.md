---
article_id: 14015424674199
category: TAF - eSocial - Eventos Periódicos
content_hash: 603cf0cac85d1aa840cfa7c807b389cdd76bb2ddc6d171efc33f3ad847613c25
fetched_at: '2026-06-28T22:45:19.003979+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200 - Erro de
  Schema: Element ''{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00}qtdRubr'':
  This element is not'
type: support-article
updated_at: '2026-06-24T12:21:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14015424674199-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-Erro-de-Schema-Element-http-www-esocial-gov-br-schema-evt-evtRemun-v-S-01-01-00-qtdRubr-This-element-is-not
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23702808408599) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Ao tentar transmitir o evento **S-1200** para o eSocial, é apresentada a inconsistência, **erro de Schema**:

*Erro de schema: Element '{[http://www.esocial.gov.br/schema/evt/evtRemun/v\_S\_01\_01\_00}qtdRubr':](http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00%7DqtdRubr':) This element is not expected. Expected is ( {[http://www.esocial.gov.br/schema/evt/evtRemun/v\_S\_01\_01\_00}ideTabRubr](http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00%7DideTabRubr) ).*

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1200 - Todas as versões

**Causa**O erro de Schema ocorre quando uma informação não foi preenchida, foi preenchida incorretamente ou falta tag obrigatória no XML do TAF.

O erro específico informa a tag **<ideTabRubr>**, observe trecho do **XML  S-1200**, abaixo, grupo **<itensRemun>** a tag obrigatória **<ideTabRubr>** não é apresentada, em nenhum dos itens de remuneração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14014971260055)

Correto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14015211554455)

**Solução**

Verifique o compartilhamento da Tabela **T3M**, tabela que é consultada pelo sistema, para que a rubrica seja localizada no TAF (tabela C8R).  
   
A tabela **T3M**, por padrão, deve ser **compartilhada**;

Abaixo o Link, com a informação completa: 

[Como deve ser definido o Compartilhamento de Tabelas SIGAGPE X SIGATAF](https://tdn.totvs.com/display/public/PROT/Como+deve+ser+definido+o+Compartilhamento+de+Tabelas+SIGAGPE+x+SIGATAF)

Trecho do documento, referente á tabela T3M:  
![](https://totvssuporte.zendesk.com/attachments/token/nZ4yzRZmw6OhjMEnqBSMWwplA/?name=image.png)

Realize a manutenção se necessário;
