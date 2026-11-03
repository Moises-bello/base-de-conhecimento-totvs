---
article_id: 360007510032
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 48f9d4f471f1e3ce6cb6d55e9801984d5a2d0bec2622d309c184201a673e695a
fetched_at: '2026-06-28T22:40:32.362049+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Origem do lançamento
  contábil
type: support-article
updated_at: '2022-06-06T19:55:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007510032-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Origem-do-lan%C3%A7amento-cont%C3%A1bil
---

**Ocorrência**

* Como identificar origem do lançamento contábil Tabela CT2 ?

**Ambiente**  
Protheus – Protheus – A partir da versão 11.80

**Solução**

Sistema grava os campos abaixo:

* CT2\_ROTINA - neste campo o sistema grava a rotina que originou o lançamento.
* CT2\_ORIGEM - Este campo será gravado quando o campo CT5\_ORIGEM for configurado no cadastro do lançamento padrão.
* CT2\_LP - Campo é preenchido com o código do lançamento padrão utilizado para contabilização do lançamento.
* CT2\_LOTE - A capa do lote é o identificador do lançamento contábil. As informações nela inseridas, este número é sugerido pelo sistema.

Documentações relacionadas

* [Lotes de Contabilidade](http://tdn.totvs.com/display/public/PROT/Lotes+de+Contabilidade)
* [CTBA102 Lançamento contábil](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba102.htm)
* [CTBA101 Lançamentos contábeis](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba101.htm)
* [MV\_CTBLOTE - Geraçãovalidação número](http://tdn.totvs.com/pages/releaseview.action?pageId=6070786)
* [MV\_CAPLOTE - Definição de Chave - Geração Validação](http://tdn.totvs.com/pages/releaseview.action?pageId=6070785)
* [CTBPRXDOC - Controle da numeração](http://tdn.totvs.com/pages/releaseview.action?pageId=6068643)
