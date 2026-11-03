---
content_hash: c1f4b7bd9b207cfe18615b80940b25d106efb8dd4d1f67dfa259ed36942bfd7a
fetched_at: '2026-06-29T00:10:53.948842+00:00'
page_id: '590040491'
product: rm
source: tdn-rm
title: SEFIP - Licença Maternidade - Incidência Exclusiva do Segurado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590040491
version: 42
---

# Objetivo:

---

Tratamento para afastamento temporário por motivo de Licença Maternidade conforme manual 8.4 da SEFIP, veja abaixo:

*"4.7.4 – Afastamento temporário por motivo de licença-maternidade (movimentações Q1, Q2, Q3, Q4, Q5, Q6 e Q7) a partir da competência 11/2015.*  
*Nesta situação, existe a obrigação de recolhimento para o FGTS sobre a remuneração que seria devida ao trabalhador, caso não estivesse afastado, durante todo o período de afastamento.*  
*Mas para a Previdência, em relação à parte patronal, a partir da competência 11/2015 só existe a obrigação de recolhimento das contribuições sobre a remuneração relativa aos dias trabalhados. Mantendo-se a contribuição da segurada sobre a base integral (valor correspondente aos dias trabalhados mais os dias de afastamento por motivo de licença maternidade).*  
*Assim, os campos Remuneração sem 13º Salário e Base de Cálculo da Previdência Social têm valores diferentes. O empregador/contribuinte deve informar a efetiva base de cálculo da Previdência no campo Base de Cálculo da Previdência Social.*

***Exemplo:***  
*Empregado afastado em 06/09/2020 por licença maternidade, com remuneração*  
*mensal de R$ 1.500,00:*  
*de 01/09 a 05/09 – 05 dias trabalhados;*  
*de 06/09 a 30/09 – 25 dias de licença.*

*Na GFIP/SEFIP da competência setembro, informar:*

*• campo Remuneração sem 13° Salário – valor correspondente à remuneração que seria devida, caso o trabalhador não estivesse afastado (para incidência do FGTS) – R$ 1.500,00;*  
*• campo Base de Cálculo da Previdência Social – valor correspondente aos 05 dias trabalhados (para incidência da Previdência) – R$ 250,00;*  
*• campo Movimentação – 05/09/2020 (dia imediatamente anterior ao efetivo afastamento) e o código Q1;*  
*• campo Ocorrência - 05, 06, 07 ou 08, conforme o caso;*  
*• campo Valor Descontado do Segurado – valor do efetivo desconto do trabalhador;*  
*• os demais campos devem ser informados de acordo com as instruções deste Manual."*

---

1true1Cadastro de EventosCadastro dos eventos

**Cadastros | Eventos**

Os eventos com códigos de cálculos de salário maternidade (CC017, CC178) deverão ter o parâmetro "**Incidência Exclusiva do Segurado**" marcado, conforme print abaixo:

O evento de "13º Salário Licença Maternidade pago na Rescisão" código de cálculo 373, deverá ter o parâmetro "**Incidência Exclusiva do Segurado**" marcado, conforme print abaixo:

O evento de "13º Salário Licença Maternidade" código de cálculo 371, deverá ter o parâmetro "**Incidência Exclusiva do Segurado**" marcado, conforme print abaixo:

1Folha MensalFolha Mensal

**Funcionário | Anexo Histórico de Afastamentos**

**Funcionários | Anexo Envelope de Pagamento**

Lançamento do evento de Licença Maternidade com código de cálculo 17 e do evento de Dias Trabalhados com código de cálculo 2:

  

**Encargos | SEFIP**

Na geração do arquivo com a movimentação do afastamento da funcionária será considerado nos campos:

Ocorrência: o código de ocorrência equivalente conforme o manual da SEFIP;

Valor Descontado do Segurado: o valor descontado de INSS no envelope do funcionário;

Base de Cálculo da Previdência Social:  os valores dos eventos que incidem INSS.

falseAtenção

A adequação na SEFIP para o Salário Maternidade estará disponível a partir dos patchs:

* 12.1.27.337
* 12.1.28.246
* 12.1.29.192
* 12.1.31.103
* Ou superiores
1RescisãoRescisão

Funcionária teve o afastamento por Licença Maternidade no período 02/01/2020 a 30/04/2020:

No lançamento das verbas de rescisão, foi lançado o evento com código de cálculo 373 - 13º Rescisão Licença Maternidade:

Ao gerar a SEFIP será gerado o arquivo com os valores:

Ocorrência: o código de ocorrência equivalente conforme o manual da SEFIP;

Valor Descontado do Segurado: o valor descontado de INSS no envelope do funcionário;

Base de Cálculo do 13º Salário da Previdência Social | Referente a Competência do Movimento: os valores dos eventos que incidem INSS de 13º Salário;

**ATENÇÃO**: A movimentação do afastamento da funcionária por licença Maternidade não é levada neste exemplo, pois o afastamento é em competência anterior a rescisão:

falseAtenção

A adequação na SEFIP para o 13º Salário Maternidade na rescisão estará disponível a partir dos patchs:

* 12.1.29.266
* 12.1.31.171
* 12.1.32.111
113ª Salário13ª Salário

Funcionária teve o afastamento por Licença Maternidade no período 03/03/2021 a 30/06/2021:

No lançamento da verbas de 13ª Salário foi lançado no evento com código de cálculo 371 - Segunda Parcela 13ª Licença Maternidade Provento:

Ao gerar a SEFIP 13 será gerado o arquivo com os valores:

Ocorrência: o código de ocorrência equivalente conforme o manual da SEFIP;

Valor Descontado do Segurado: o valor descontado de INSS no envelope do funcionário;

Base de Cálculo do 13º Salário da Previdência Social | Referente a Competência do Movimento: os valores dos eventos que incidem INSS de 13º Salário;

**ATENÇÃO:** A movimentação do afastamento da funcionária por licença Maternidade não será levada na SEFIP 13, independente do período em que o afastamento ocorreu.

Relatório Analítico GPS:

falseAtenção

A adequação na SEFIP para o 13º Salário Maternidade estará disponível a partir dos patches:

* 12.1.31.281
* 12.1.32.228
* 12.1.33.158
1Licença Maternidade AdoçãoAdoção

Funcionária teve o afastamento por Licença maternidade por Adoção.

No lançamento da verbas de 13ª Salário foi lançado o evento com código de cálculo 371 - Segunda Parcela 13ª Licença Maternidade Provento:

Ao gerar a SEFIP 13 será gerado o arquivo com os valores:

Ocorrência: o código de ocorrência equivalente conforme o manual da SEFIP;

Valor Descontado do Segurado: o valor descontado de INSS no envelope do funcionário;

Base de Cálculo do 13º Salário da Previdência Social | Referente a Competência do Movimento: os valores dos eventos que incidem INSS de 13º Salário;

**ATENÇÃO:** A movimentação do afastamento da funcionária por licença Maternidade não será levada na SEFIP 13, independente do período em que o afastamento ocorreu.

Relatório Analítico GPS:

falseAtenção

A adequação na SEFIP para o 13º Salário Maternidade estará disponível a partir dos patchs:

* 12.1.31.281
* 12.1.32.228
* 12.1.33.158
1Salario Maternidade AdoçãoAdoção

Parametrizador | Folha Normal | Salário Maternidade 1/2

Tratamento no evento de salario maternidade para as rotinas Guia de INSS, Folha Analítica e SEFIP, passando a verificar a incidência do evento que esta informado nos parâmetros, ao invés de forçar a incidência somente pelo fato do evento estar informado no parametrizador, como era em patches anteriores.

Cadastro de Eventos

Funcionária teve o afastamento por Licença Maternidade Adoção no período 15/02/2022 a 14/06/2022:

Envelope de Pagamento

Guia de INSS

 

Folha Analítica

SEFIP
