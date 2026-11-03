---
content_hash: b04d4415ca4b448418119ec3cc7f78d4236504d9f3657824a76cfa64fc1d1e09
fetched_at: '2026-06-29T00:09:22.196601+00:00'
page_id: '422545985'
product: rm
source: tdn-rm
title: Bloco U - Imune/ Isenta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545985
version: 5
---

Este bloco demonstra o cálculo do IRPJ e da CSLL para as empresas do regime de apuração Imunes ou Isentas. O regime de Apuração será determinado com base nos Tributos cadastrados e os Eventos Tributários criados para eles. Ele é composto pelos seguintes registros:

BLOCOUleftU001U001

**Abertura do Bloco U**

Registro de controle gerado automaticamente pelo processo da ECF.

U030U030

**Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas**

Será gerado um registro para cada Período de Apuração cadastrado e encerrado para os Tributos IRPJ e CSLL.

U100U100

**Balanço Patrimonial**

Apresenta o balanço patrimonial com base nas contas referenciais para o período de apuração. O saldo inicial pode ser replicado do registro E010/E015 ou preenchido. O saldo final será recuperado do registro K155/K156. Caso o bloco K não possua dados e for SCP (0000.TIP\_ECF = 2), o saldo final poderá ser preenchido.

U150U150

**Demonstração do Resultado**

Apresenta a demonstração do resultado das empresas imunes e isentas.

U180U180

**Cálculo do IRPJ das Empresas Imunes e Isentas**

Neste registro será detalhado o cálculo do IRPJ. As Deduções serão carregadas dos itens do Detalhamento da Apuração no Período de Apuração. Para que este registro seja corretamente gerado é imprescindível que sejam informados os códigos da Tabela Dinâmica da ECF nos itens do Evento Tributário criado para o IRPJ.

U182U182

**Cálculo da CSLL das Empresas Imunes e Isentas**

Neste registro será detalhado o cálculo da CSLL. As Deduções serão carregadas dos itens do Detalhamento da Apuração no Período de Apuração. Para que este registro seja corretamente gerado é imprescindível que sejam informados os códigos da Tabela Dinâmica da ECF nos itens do Evento Tributário criado para a CSLL.

U990U990

**Encerramento do Bloco U**

Registro de controle gerado automaticamente pelo processo da ECF.
