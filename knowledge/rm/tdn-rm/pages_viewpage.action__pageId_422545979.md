---
content_hash: 7b3926f30af9f2bbaca3e0babb10a55ce63ebbec320faf9a4d81befbe8963735
fetched_at: '2026-06-29T00:09:22.134145+00:00'
page_id: '422545979'
product: rm
source: tdn-rm
title: Bloco P - Lucro Presumido 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545979
version: 4
---

Este registro irá demonstrar o cálculo do IRPJ e CSLL para empresas que os apuram pelo regime de Lucro Presumido. O regime de tributação será determinado pelo cadastro dos Tributos mais o Eventos Tributários criados para os mesmos. Ele é composto pelos seguintes registros:

BLOCOPleftP001P001

**Abertura do Bloco P**

Registro de controle gerado automaticamente pelo processo da ECF. Informa se existe ou não movimentação no bloco P.

P030P030

**Identificação dos Períodos de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido**

Será gerado um registro para cada Período de Apuração cadastrado e encerrado para os tributos IRPJ e CSLL.

P100P100 

**Balanço Patrimonial**

Apresenta o balanço patrimonial com base nas contas referenciais para o período de apuração. O saldo inicial pode ser replicado do registro E010/E015 ou preenchido. O saldo final será recuperado do registro K155/K156. Caso o bloco K não possua dados e for SCP (0000.TIP\_ECF = 2), o saldo final poderá ser preenchido.

P130 P130

**Demonstração das Receitas Incentivadas do Lucro Presumido**

Este registro não será gerado.

P150P150

**Demonstração de Resultado**

Apresenta a apuração a demonstração do resultado do exercício. Os valores serão recuperados do registro K356 se 0010. TIP\_ESC\_PRE for igual a "C" (contábil) e calculados pela própria ECF. Atenção: Caso 0010. TIP\_ESC\_PRE for igual a "L" (livro caixa), este registro não será preenchido.

P200P200

**Apuração da Base de Cálculo do Lucro Presumido**

Este registro irá demonstrar a formação da base de cálculo do Lucro Presumido para o IRPJ. Ele será gerado com base nos itens de Detalhamento da Apuração no Período de Apuração do IRPJ. Portando é imprescindível para a geração deste registro a informação do código da Tabela Dinâmica da ECF no Evento Tributário referente a ele.

P230P230

**Cálculo da Isenção e Redução do Lucro Presumido**

Este registro não será gerado.

P300P300

**Cálculo do IRPJ com Base no Lucro Presumido**

Demonstra o cálculo efetivo do IRPJ para o Lucro Presumido aplicando-se as deduções Legais. Estas deduções são carregadas do Detalhamento da Apuração do Período de Apuração do IRPJ.

P400P400 

**Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido**

Este registro irá demonstrar a formação da base de cálculo do Lucro Presumido para a CSLL. Ele será gerado com base nos itens de Detalhamento da Apuração no Período de Apuração da CSLL. Portando é imprescindível para a geração deste registro a informação do código da Tabela Dinâmica da ECF no Evento Tributário referente a ele.

P500P500 

**Cálculo da CSLL com Base no Lucro Presumido**

Demonstra o cálculo efetivo da CSLL para o Lucro Presumido aplicando-se as deduções Legais. Estas deduções são carregadas do Detalhamento da Apuração do Período de Apuração da CSLL.

P990P990

**Encerramento do Bloco P**

Registro de controle gerado automaticamente pelo processo da ECF.
