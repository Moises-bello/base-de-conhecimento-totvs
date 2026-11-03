---
content_hash: e06b861eb2441d9c6f9de9c3cf1c5524e79bd4f538d2adc0e27fbaae23a43586
fetched_at: '2026-06-29T00:09:22.130122+00:00'
page_id: '422545978'
product: rm
source: tdn-rm
title: Bloco N - Imposto de Renda e Contribuição Social (Lucro Real)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545978
version: 7
---

Neste bloco são registradas as informações pertinentes ao cálculo do Imposto de Renda e da Contribuição Social para o regime do Lucro Real ou Estimativa.  
Ele é composto dos registros abaixo:

BLOCONleftN001 N001 

**Abertura do Bloco N**

Este é um registro de controle gerado automaticamente pelo processo da rotina que informa se existe ou não movimentação no bloco N.

N030 N030 

**Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empesas Tributadas pelo Lucro Real**

Será gerado um registro para cada Período de Apuração cadastrado e encerrado. A determinação do regime de lucro será feita pelo Evento Tributário.

N500 N500 

**Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízo**

Este registro é gerado e transportado automaticamente pelo PVA com base nas informações contidas no registro [M300](http://tdn.totvs.com/display/LRM/Bloco+M+-+e-LALUR+e+e-LACS).

N600 N600 

**Demonstração do Lucro da Exploração**

Este registro é gerado para as pessoas jurídicas submetidas à apuração trimestral ou anual do imposto sobre a renda com base no lucro real que gozem de benefícios fiscais calculados com base no lucro da exploração, tais como (PN CST nº 49, de 1979).  
***Observação***: Na apuração do registro N600 com código tabela dinâmica 46 e quando a Despesa Financeira ficar maior que a Receita, os Itens tributários serão zerados conforme regra da ECF.

N610 N610 

**Cálculo da Isenção e Redução do Imposto Sobre o Lucro Real**

Este registro não será gerado.

N615 N615 

**Informações da Base de Cálculo dos Incentivos Fiscais**

Este registro não será gerado.

N620 N620 

**Cálculo do IRPJ Mensal por Estimativa**

Este registro será gerado quando o regime de apuração for por Estimativa. Será gerado um registro para cada Período de Apuração cadastrado e encerrado por este regime. As Deduções são geradas com base nos itens do detalhamento dos Períodos de Apuração do IRPJ e totalizados por códigos da Tabela Dinâmica da ECF.  
  
Observação: Caso a opção "**Não zerar se prejuízo**", esteja marcada no evento tributário, as deduções serão apresentas neste registro mesmo se houver prejuízo no período, mais informações na documentação: [Regra de Valores para Deduções e Compensações](https://tdn.totvs.com/pages/viewpage.action?pageId=848369925)

N630 N630 

**Cálculo do IRPJ com Base no Lucro Real**

Será gerado um registro para cada período de apuração cadastrado e encerrado pelo Lucro Real ou Estimativa com Levantamento de Balanço. As informações de Deduções são geradas com base nas informações do detalhamento dos Períodos de Apuração de IRPJ. Os registros são totalizados pelos Códigos da Tabela Dinâmica da ECF.

Observação: Caso a opção "**Não zerar se prejuízo**", esteja marcada no evento tributário, as deduções serão apresentas neste registro mesmo se houver prejuízo no período, mais informações na documentação: [Regra de Valores para Deduções e Compensações](https://tdn.totvs.com/pages/viewpage.action?pageId=848369925)

N650 N650 

**Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa**

Este registro é gerado e transportado automaticamente pelo PVA com base nas informações contidas no registro [M350](http://tdn.totvs.com/display/LRM/Bloco+M+-+e-LALUR+e+e-LACS).

N660 N660 

**Cálculo da CSLL Mensal por Estimativa**

Este registro será gerado quando o regime de apuração for por Estimativa. Será gerado um registro para cada Período de Apuração cadastrado e encerrado por este regime. As Deduções são geradas com base nos itens do detalhamento dos Períodos de Apuração do CSLL e totalizados por códigos da Tabela Dinâmica da ECF.

N670 N670 

**Cálculo da CSLL com Base no Lucro Real**

Será gerado um registro para cada período de apuração cadastrado e encerrado pelo Lucro Real ou Estimativa com Levantamento de Balanço. As informações de Deduções são geradas com base nas informações do detalhamento dos Períodos de Apuração de CSLL. Os registros são totalizados pelos Códigos da Tabela Dinâmica da ECF.

N990 N990 

**Encerramento do Bloco N**

Este é um registro de controle gerado automaticamente pelo processo da ECF.
