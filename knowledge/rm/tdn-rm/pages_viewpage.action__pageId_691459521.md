---
content_hash: a9fe2684913fec62cbac75671b1bdc509e7960aa07147a001a679b6d84ea15e4
fetched_at: '2026-06-29T00:11:21.294442+00:00'
page_id: '691459521'
product: rm
source: tdn-rm
title: Novo Lançamento de Horário Planejado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=691459521
version: 44
---

## **01. VISÃO GERAL**

Neste lançamento o sistema irá considerar um intervalo calculado para cada batida do horário planejado, permitindo assim que no lançamento seja verificado a necessidade de lançar ou não as batidas faltantes/selecionadas na execução do lançamento.

Caso o horário tenha limite de refeição, o intervalo considerado será o mesmo para a entrada/ saída da refeição.

**Importante:**

* Para utilizar o novo lançamento, será necessário incluir a tag "*<add key="PtoUsarNovoLancamento" value="true" /**>***" nos arquivos RM.Host.exe.config  e RM.Host.JobRunner.exe.config. Esses arquivos geralmente estão localizados no caminho C:\Totvs\CorporeRM\RM.Net ou no caminho definido pelo usuário  no momento da instalação da BibliotecaRM.
* Caso não utilize o fracionamento de jobs é necessário que a tag <add key=*"IsolateProcess" value="false" /*> seja inserida também no arquivo RM.Host.exe.config.
* No final do processo de lançamento, será demonstrado no  Log que o processo foi realizado utilizando a nova regra.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Exemplo 1

Horário semi-flexível com Limite de refeição

| **Horário** | **08:00** | **12:00** | **14:00** | **18:00** |
| --- | --- | --- | --- | --- |
| Limite de Refeição |  | 10:00 | 16:00 |  |
| Batida Realizada |  | 10:30 |  |  |

***Atenção:***

O sistema irá considerar a regra abaixo para realizar o  lançamento das batidas:

| **Horário** | **08:00** | **12:00** | **14:00** | **18:00** |
| --- | --- | --- | --- | --- |
| Limite de Refeição |  | 10:00 | 16:00 |  |
| Intervalo Calculado | 01:00 as 10:00 | 10:00 ás 16:00 | 10:00 as 16:00 | 16:00 as +01:00 |

Visualização do Horário cadastrado

## 

Visualização do espelho do funcionário no dia 02/04/2022 :

Realizado o processo de lançamento de batidas pelo horário planejado, selecionado as batidas de Entrada e saída da jornada e entrada/ saída do limite de refeição.

Considerando que existe apenas a batidas de 10:30 e esta batida está dentro do intervalo calculado das batidas de refeição teremos o seguinte resultado:

2Exemplo 2

Horário semi-flexível com Limite de refeição

| **Horário** | **08:00** | **12:00** | **14:00** | **18:00** |
| --- | --- | --- | --- | --- |
| Limite de Refeição |  | 10:00 | 16:00 |  |
| Batida Realizada |  | 15:30 |  |  |

Realizado o processo de lançamento de batidas pelo horário planejado, selecionado as batidas de Entrada e saída da jornada e entrada/ saída do limite de refeição.

Considerando que existe apenas a batidas de 15:30 e esta batida está dentro do intervalo calculado das batidas de refeição teremos o seguinte resultado:

3Exemplo 3

Horário semi-flexível com Limite de refeição

| **Horário** | **08:00** | **12:00** | **14:00** | **18:00** |
| --- | --- | --- | --- | --- |
| Limite de Refeição |  | 10:00 | 16:00 |  |
| Batida Realizada |  | 11:00 | 14:00 | 15:30 |

Realizado o processo de lançamento de batidas pelo horário planejado, selecionado as batidas de Entrada e saída da jornada e entrada/ saída do limite de refeição.

Considerando que existe *batidas ímpares*  11:00-14:00-15:30 teremos o seguinte resultado:

**Observações:**

* O Novo lançamento tem como premissa *não lançar batidas* que resultaria em batidas ímpares, desta forma no exemplo acima,  a batida de entrada/saída da jornada não será lançada.
* Considerando o exemplo acima, somente será lançada a batida de entrada ou saída, se no lançamento de batidas for marcado apenas *entrada* ou apenas *saída da jornada*, formando um par com uma das batidas 11:00 ou 15:30.

1. Considerando o lançamento marcando apenas *Entrada da Jornada, teremos o seguinte resultado*:

2-Considerando o lançamento marcando apenas *Saída da Jornada, teremos o seguinte resultado*:

4Exemplo 4

Horário semi-flexível com Limite de refeição

| **Horário** | **08:00** | **12:00** | **14:00** | **18:00** |
| --- | --- | --- | --- | --- |
| Limite de Refeição |  | 10:00 | 16:00 |  |
| Batida Realizada |  | 14:00 | 15:30 |  |

Realizado o processo de lançamento de batidas pelo horário planejado, selecionado as batidas de Entrada e saída da jornada e entrada/ saída do limite de refeição.

Realizado o processo de lançamento de batidas pelo horário planejado, selecionado as batidas de Entrada e saída da jornada e entrada/ saída do limite de refeição.

Considerando que existe apenas as batidas de 14:00 e 15:30 e esta batida está dentro do intervalo calculado  das batidas de refeição teremos o seguinte resultado:
