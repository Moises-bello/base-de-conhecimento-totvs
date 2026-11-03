---
article_id: 360020712551
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 8b8912ad35b939dc2ebf571dd498e37f2fc55da25c133b8df46d7d670e62be77
fetched_at: '2026-06-28T22:40:32.310705+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Como efetuar
  um Lançamento de Partida Simples
type: support-article
updated_at: '2022-05-26T13:39:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020712551-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-efetuar-um-Lan%C3%A7amento-de-Partida-Simples
---

**Dúvida**Como efetuar um lançamento de Partida Simples, ou seja é considerado apenas o débito ou o crédito ocorrido no fato.  
  
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12

**Solução**

Para que seja possível efetuar um lançamento de partida simples, em que é considerado apenas o débito ou o crédito ocorrido no fato, é necessário efetuar a configuração dos seguintes parâmetros:

**MV\_PRELAN:**

Indica se o Lançamento Contábil será automaticamente lançado ou passara por Pré-lançamento.

 S=Sempre

N=Nunca

 D=Doc. Inconsistente  

**MV\_ALTLCTO**

Permite alterar os lançamentos contábeis de integração. No caso de não permitir a alteração de   lançamentos, e se estes tenham alguma inconsistência de valor  ou entidades contábeis não   existentes, o lançamento será obrigatoriamente gravado como pré-lançamento.

 

**MV\_CONTBAT:**

Não permite confirmar a inclusão/alteração de um lançamento

contábil quando o débito não bater com o crédito.

 

**MV\_CONTSB:**

Indica se a contabilização será feita, mesmo que os valores de

débito e crédito não batam. Se estiver com "S", gravará o

lançamento contábil sem verificação de valores. Caso contrário,

dependerá da configuração de MV\_CONTBAT.

 

**MV\_CONTSLD:**

Indica se a validação de débito e crédito do lançamento

contábil será efetuada por tipo de saldo (evitando que sejam

gerados lançamentos à débito e à credito em tipos de saldo

diferentes. Se não for necessário efetuar esta validação,

preencher o conteúdo com “N”.

 

Na rotina CTBA101, é necessário alterar  nos parâmetros F12 a pergunta Verif. lanc. 1/2 = Nao.

   
![](https://totvssuporte.zendesk.com/attachments/token/ZrVU6u7CtCAKeQqqYXsncdays/?name=inline-738290863.png)

* CTBA102 Exemplo de lançamento partida simples:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086481053/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086482493/mceclip1.png)

* CTBA101 Exemplo de lançamento partida simples

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085290594/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085291794/mceclip1.png)

Veja como configurar [LANÇAMENTO PADRÃO DE PARTIDA SIMPLES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052503314-MP-SIGACTB-CTBA080-LAN%C3%87AMENTO-PADR%C3%83O-DE-PARTIDA-SIMPLES-E-PARTIDA-DOBRADA?source=search)

 

Saiba mais

<http://tdn.totvs.com/display/public/mp/SIGACTB+-+Diversos+--+24238>
