---
article_id: 4418618747799
category: RH - Férias
content_hash: 5a151b18cff8c53784bc031bc0493d30af79b5e478af7913c5fb49a2e059ce85
fetched_at: '2026-06-28T22:43:58.066846+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular o DSR sobre médias no cálculo das
  férias
type: support-article
updated_at: '2025-08-11T20:50:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418618747799-RH-Linha-Protheus-GPE-Como-calcular-o-DSR-sobre-m%C3%A9dias-no-c%C3%A1lculo-das-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17323173811223) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como gerar/calcular o **DSR sobre médias no cálculo das férias?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Existe a opção do cálculo do DSR sobre médias de férias, para isso é necessário efetuar as seguintes configurações: Em **Atualizações > Definições de Cálculo > Verbas**, localize a verba com **ID 0082 - Média de férias em valor** e no campo **Verba DSR** informe a verba com **ID 0080 - DSR sobre médias de férias**

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-20-27.png?version=1&modificationDate=1561633733117&api=v2)

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-21-22.png?version=1&modificationDate=1561633733080&api=v2)

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-22-0.png?version=1&modificationDate=1561633733047&api=v2)  
  
Ainda em **Atualizações > Definições de Cálculo > Verbas**, localize a **verba com ID 0075 - Média de férias em valor** e no campo **Verba DSR** informe a **verba com ID 0080 - DSR sobre médias de férias**

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-25-59.png?version=1&modificationDate=1561633732900&api=v2)

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-25-27.png?version=1&modificationDate=1561633732933&api=v2)  
  
Ainda em **Atualizações > Definições de Cálculo > Verbas**, localize a **verba com ID 0076 - Média de férias em valor** e no campo **Verba DSR** informe a verba com **ID 0081 - DSR sobre médias de férias:**

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-29-50.png?version=1&modificationDate=1561633732823&api=v2)

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-30-28.png?version=1&modificationDate=1561633732790&api=v2)

Ainda em **Atualizações > Definições de Cálculo > Verbas**, localize a **verba com ID 0083 - Média de férias em valor** e no campo **Verba DSR**  informe a **verba com ID 0081 - DSR sobre médias de férias**

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-32-21.png?version=1&modificationDate=1561633732753&api=v2)

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-33-9.png?version=1&modificationDate=1561633732720&api=v2)

Para efetuar o cálculo entre na rotina **Miscelânea > Cálculos > Férias > Selecione a matricula do funcionário > Cálculo:**

\*\*\* No exemplo vou demonstrar o cálculo de DSR sobre médias em um funcionário que vai tirar férias parciais e partidas:

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-36-42.png?version=1&modificationDate=1561633732683&api=v2)

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-37-51.png?version=1&modificationDate=1561633732650&api=v2)

Demonstrativo de médias:

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_7-43-53.png?version=1&modificationDate=1561633732613&api=v2)

Soma-se as verbas com DSR preenchido, no casos são as verbas de média horas e média valor, tanto do mês quanto do mês seguinte:

Verbas: 132 + 133 + 139 +140 = Total das médias

Valores: 42,84 + 10,71 + 222,73 +  55,68 = 331,96

\*\*Valor Equivalente a 15 dias de férias.

Demonstrativo de médias: $663,91

663,91 / 30 \* 15 = 331,96

Apura-se o DSR: ((Total das verbas de DSR \* Horas de descanso) / Horas Trabalhadas.)

((331,96 \* 29,3332) / 175,9992) =55,33

Apura-se a quantidade a ser paga nas férias: (DSR Médias / 30 ) \* Férias do período)

((55,33 / 30) \* 12) = 22,13 - VERBA 137

Apura-se a quantidade a ser paga nas férias: (DSR Médias / 30 ) \* Férias do período)

((55,33 / 30) \* 3) = 5,53 - VERBA 138

\*\*\* O valor das horas trabalhadas e horas de descanso são calculadas de acordo com o cadastro de períodos do mês. O sistema considera as informações dos campos de Dias Uteis e Nº Dias DSR:

Dias Uteis \* 7,33 (composição feita através da formula padrão 220 / 30) = Horas trabalhadas

Nº Dias DSR \* 7,33 (composição feita através da formula padrão 220 / 30) = Horas de Descanso

![](https://tdn.totvs.com/download/attachments/498457080/image2019-6-27_8-3-37.png?version=1&modificationDate=1561633732550&api=v2)

O sistema proporcionaliza as médias de acordo com a quantidade de dias pagos de férias e proporcionaliza o DSR de acordo com os dias trabalhados do mês. 

**Saber Mais:**

[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgKFbLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ8aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwNzI2MTU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtbSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIilmODFjMTMzNC00ZDZiLTQ1YzQtOTE5Ny1lNWY3ZTFmYTk3MmIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjw6FsY3VsbyBkZSBtw6lkaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--8916e1709383e4ba2fc755d2edc741df005bb426)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXLXHuBgc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzc3MjYzNTE1OTI4NTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItby1kZW1vbnN0cmF0aXZvLWRlLW0lQzMlQTlkaWFzLXBhcmEtZiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIikwM2FmZTI3ZS02MjJjLTRmNTgtYjk3ZC02NGViY2IzMjgyMTcGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVSMDgwBjsIVDoScmVzdWx0c19jb3VudGkC7QM%3D--83d730077e25e69719eebcd24557865227a62001)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052314713-RH-Linha-Protheus-GPE-Como-imprimir-relat%C3%B3rio-de-mem%C3%B3ria-de-c%C3%A1lculo-das-f%C3%A9rias)  
[RH - Linha Protheus - GPE - O que analisar quando o Relatório de Médias de Férias apresenta valor diferente do Cálculo das Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhyxirUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0MTg1ODY3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTy1xdWUtYW5hbGlzYXItcXVhbmRvLW8tUmVsYXQlQzMlQjNyaW8tZGUtTSVDMyVBOWRpYXMtZGUtRiVDMyVBOXJpYXMtYXByZXNlbnRhLXZhbG9yLWRpZmVyZW50ZS1kby1DJUMzJUExbGN1bG8tZGFzLUYlQzMlQTlyaWFzBjsIVDoOc2VhcmNoX2lkSSIpYWNiMzZlOWItODllZS00ZmEzLTkxODctMmI0ZTliN2UxMjZiBjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIXcmVsYXRvcmlvIGRlIG1lZGlhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--3cade786302b03bdf9aecbfa373dea3227757d5e)
