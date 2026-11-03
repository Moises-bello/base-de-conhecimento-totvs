---
content_hash: 41e7baaa25a22b36d906ff6cff573f5b9c75aa226f237bb751a81617c3509a07
fetched_at: '2026-06-29T00:09:22.117635+00:00'
page_id: '422545976'
product: rm
source: tdn-rm
title: Bloco T - Lucro Arbitrado
type: documentation
url: https://tdn.totvs.com/display/LRM/Bloco+T+-+Lucro+Arbitrado
version: 4
---

Este bloco demonstra a apuração do IRPJ e da CSLL para o regime de apuração do Lucro Arbitrado. O regime de tributação será determinado pelo cadastro dos Tributos e pelos Eventos Tributários criados para eles. Ele é composto pelos seguintes registros:

BLOCOTleftT001 T001 

**Abertura do bloco T**

Registro de controle gerado automaticamente pelo processo da ECF. Informa se existe ou não movimentação no bloco T.

T030T030

**Identificação dos Períodos e Formas de Apuração do IRPJ das Empresas Tributadas pelo Lucro Arbitrado**

Será gerado um registro para cada Período de Apuração cadastrado e encerrado para os Tributos IRPJ e CSLL.

T120T120

**Apuração da Base de Cálculo do IRPJ com Base no Lucro Arbitrado**

Este registro é obrigatório e demonstra a composição da base de cálculo para o tributo IRPJ. Será gerado com a informação do Detalhamento da Apuração do Período de Apuração deste Tributo. Para a correta geração deste registro é imprescindível a gravação do código da Tabela Dinâmica da ECF no Evento Tributário referente a este Tributo.

T150 T150

**Cálculo do IRPJ com Base no Lucro Arbitrado**

Este registro detalha o cálculo do IRPJ com base no Lucro Arbitrado. As Deduções aplicadas serão carregadas do Detalhamento da Apuração do Período de Apuração do IRPJ. Para a correta geração deste registro é imprescindível a gravação do código da Tabela Dinâmica da ECF no Evento Tributário referente a este Tributo.

T170T170

**Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado**

Este registro é obrigatório e demonstra a composição da base de cálculo para o tributo CSLL. Será gerado com a informação do Detalhamento da Apuração do Período de Apuração deste Tributo. Para a correta geração deste registro é imprescindível a gravação do código da Tabela Dinâmica da ECF no Evento Tributário referente a este Tributo.

T181T181

**Cálculo da CSLL com Base no Lucro Arbitrado**

Este registro detalha o cálculo do CSLL com base no Lucro Arbitrado. As Deduções aplicadas serão carregadas do Detalhamento da Apuração do Período de Apuração do CSLL. Para a correta geração deste registro é imprescindível a gravação do código da Tabela Dinâmica da ECF no Evento Tributário referente a este Tributo.

T990T990

**Encerramento do Bloco T**

Registro de controle gerado automaticamente pelo processo da ECF.
