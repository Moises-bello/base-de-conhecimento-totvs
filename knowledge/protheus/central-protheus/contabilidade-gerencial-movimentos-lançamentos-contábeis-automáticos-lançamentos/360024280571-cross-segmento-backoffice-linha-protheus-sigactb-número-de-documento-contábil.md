---
article_id: 360024280571
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 4725bb84faeb6fddac0daa06aea17a44762569079fcd5e1b504e3eba5b077a57
fetched_at: '2026-06-28T22:40:32.530444+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - NÚMERO DE DOCUMENTO
  CONTÁBIL
type: support-article
updated_at: '2025-09-12T18:35:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024280571-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-N%C3%9AMERO-DE-DOCUMENTO-CONT%C3%81BIL
---

**Dúvida**

* Número do Documento contábil.
* Número de documento de cada contabilização

**Ambiente**

Microsiga Protheus – Contabilidade – A partir da versão 11.80  
  
  
**Solução**

O controle da numeração do documento contábil no ambiente Contabilidade Gerencial (SIGACTB) é realizado de forma seqüencial e diária, respeitando a seguinte chave: DATA+LOTE+SUBLOTE+DOC, ou seja:

· Em uma determinada data, para um lote e sublote específicos, todo novo documento será seqüencial em relação ao documento anteriormente utilizado

· A cada mudança de data, a numeração do documento será reiniciada em “000001”

Resumindo:

· Cada combinação de data + lote + sublote contábil terá um conjunto de documentos contábeis seqüenciais.

O controle da seqüência de numero de documento no ambiente Contabilidade Gerencial (SIGACTB) é baseado nas informações registradas na tabela **CTF** com base nas informações do lançamento contábil (Data, Lote e Sub-lote). Esse controle é fixo dentro do ambiente e mantém integras as informações geradas para o lançamento.

Para configurar o controle da numeração seqüencial do ambiente Contabilidade Gerencial (SIGACTB) para utilizar uma regra diferente de diária deverá ser utilizado o ponto de entrada [CTBPRXDOC,](https://tdn.totvs.com/display/public/PROT/PE+CTBPRXDOC) ***sendo que a sua má utilização irá acarretar em estragos/inconsistências na base de dados do cliente.****Como por exemplo violação de chave primaria e perca de rastreabilidade sendo da alçada do desenvolvedor do ponto de entrada a prevenção desses efeitos**.*

Veja mais :

[SIGACTB - NÚMERO DE LOTE CONTÁBIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-MP-SIGACTB-N%C3%9AMERO-DE-LOTE-CONT%C3%81BIL?source=search)

[*SIGACTB - Origem do lançamento contábil*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007510032-MP-SIGACTB-Origem-do-lan%C3%A7amento-cont%C3%A1bil?source=search)

*[MP - SIGACTB: Oque é a capa de lote no modulo contábil?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018887292-MP-SIGACTB-Oque-%C3%A9-a-capa-de-lote-no-modulo-cont%C3%A1bil-?source=search)*

[MV\_CTBLOTE - Geraçãovalidação número](http://tdn.totvs.com/pages/releaseview.action?pageId=6070786)

[MV\_CAPLOTE - Definição de Chave - Geração Validação](http://tdn.totvs.com/pages/releaseview.action?pageId=6070785)

[CTBPRXDOC - Controle da numeração](https://tdn.totvs.com/display/public/PROT/PE+CTBPRXDOC)

<https://tdn.totvs.com/display/public/PROT/Lotes+de+Contabilidade>
