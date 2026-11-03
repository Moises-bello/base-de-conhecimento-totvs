---
article_id: 360018884032
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 6fb0ba83aca5be4fa022c27896f61e8efb7787bee4b9f00550d8fd692d40c919
fetched_at: '2026-06-28T22:40:32.374530+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA102/CTBA101 -  LANÇAMENTO
  DE PARTIDA DOBRADA E PARTIDA SIMPLES COM  DUAS CONTAS INFORMADAS
type: support-article
updated_at: '2022-06-07T20:41:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018884032-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-CTBA101-LAN%C3%87AMENTO-DE-PARTIDA-DOBRADA-E-PARTIDA-SIMPLES-COM-DUAS-CONTAS-INFORMADAS
---

**Dúvida**

* Partida dobrada com as mesma conta no debito e credito
* Partida Simples com conta debito e credito

**Ambiente**

PROTHEUS – Contabilidade gerencial – A partir da versão 11.80  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

Rotina de lançamentos não permite  incluir um lançamento de partida dobrada informando a mesma conta no debito e credito, exceto se houver centro de custo no debito e credito o lançamento será validado.

Em lançamento de partida simples, é possível informar uma conta no débito e no credito.  
O sistema permite que lançamentos do tipo débito (por exemplo) tenham a conta crédito informada. Vale ressaltar que esse procedimento é meramente informativo, pois os saldos a crédito (desse exemplo) não serão gerados. Esse é um recurso que é utilizado quando se emite o Razão Contábil, mostrando dessa forma quem é a Contra-Partida da conta deste lançamento.

Links

Parâmetro que permite validar oposta ao tipo de lançamento

[CTBA102 - MV\_CTBVLP - Validação quando é incluído uma partida de Débito/Crédito e é preenchido uma conta oposta](https://tdn.totvs.com/display/PROT/CTBA102+-+MV_CTBVLP+BRA)

Mais informações

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/ctba101_pasta_lancamentos_bra.htm>
