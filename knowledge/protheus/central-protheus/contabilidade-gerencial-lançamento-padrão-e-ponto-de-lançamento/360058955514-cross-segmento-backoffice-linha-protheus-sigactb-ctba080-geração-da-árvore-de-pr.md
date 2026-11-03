---
article_id: 360058955514
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 89831b39d7a012daf2e493fd0e03f0225ac099360bc88278e1dc2b7fbe545c4f
fetched_at: '2026-06-28T22:40:34.126285+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA080 - Geração da
  árvore de processos da rotina de lançamento padrão
type: support-article
updated_at: '2021-09-03T19:42:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058955514-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Gera%C3%A7%C3%A3o-da-%C3%A1rvore-de-processos-da-rotina-de-lan%C3%A7amento-padr%C3%A3o
---

**Dúvida**Como é gerado a árvore de processos da rotina de lançamento padrão(**CTBA080**) ?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - P12.1.17

**Solução**

Para ativar a árvore, deverá deixar o F12 da rotina conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000513222/mceclip0.png)

Ao sair e entrar na rotina teremos a seguinte estrutura:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000513242/mceclip1.png)  
  
A montagem da árvore com os processos disponíveis para a criação de Lançamentos Padrão na rotina **CTBA080** é feito baseado nas tabelas **CVA e CVG**, onde:

-Na **CVG** está contido o código de cada processo, qual operação ele pertence e uma descrição. Essa tabela é alimentada quando está vazia e o usuário entra na rotina de lançamento padrão(CTBA080) ou pontos de lançamento(CTBA085), portanto geralmente possui um padrão.

-Na **CVA**, é gravado o código do lançamentos padrão e também possui uma referencia ao processo que esse LP está associado a tabela CVG, que acontece através do campo **CVA\_PROCES**, outro campo importante usado na montagem da árvore é o **CVA\_MODULO**, que contém o módulo do LP.

Portanto, para a montagem dos processos da rotina CTBA080, o sistema se baseia nas tabelas CVA e CVG, observando os seus dados e relacionamento para conseguir posicionar os Lançamentos Padrão no processo correto.

**Saiba mais:**

[Lançamento Padrão Partida Simples e Partida dobrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052503314-MP-SIGACTB-CTBA080-LAN%C3%87AMENTO-PADR%C3%83O-DE-PARTIDA-SIMPLES-E-PARTIDA-DOBRADA)

[Lançamento Padrão ctba080](http://tdn.totvs.com/pages/releaseview.action?pageId=344477626)

[Lançamento Padronizados](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba080_lanc_padronizados.htm)
