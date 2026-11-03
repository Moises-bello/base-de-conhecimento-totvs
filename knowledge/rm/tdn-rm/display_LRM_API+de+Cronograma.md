---
content_hash: ec376a95dbef522d860efc1211ff6e0095374716aca0fb969eb17ec51e771b74
fetched_at: '2026-06-29T00:11:16.372600+00:00'
page_id: '667353562'
product: rm
source: tdn-rm
title: API de Cronograma
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Cronograma
version: 22
---

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API para inserção de cronograma.

Importante:

Para acessar as API´s abaixo é necessário atribuir permissão para o usuário nas seguintes funcionalidades

1. Planilha de atividades
2. Cronograma
3. Acesso ao projeto

# 1 - API de entrada de Cronograma Planejado

---

Esta API permitirá a entrada de valores no cronograma planejado.

O cronograma da tarefa será removido e será preenchido com os valores enviados nesta chamada.

O campo de cost deve enviar o valor da tarefa relativo ao período de datas.

O campo de percentage deve enviar o percentual da tarefa relativo ao período de datas. Os dois campos podem ser enviados juntos, desde que o parâmetro do projeto para cronograma defina que use percentual ou valor.

Estas datas podem incluir mais de período do projeto. O valor será distribuído proporcional pelas datas informadas.

O campo de warning irá retornar uma lista de avisos que não provocaram erros.

**Máscara de Url:** http://{domínio}:{porta}/api/construction-projects/v1/planningInput

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 2 - API de entrada de Cronograma Medido

---

Esta API permitirá a entrada de valores no cronograma medido.

O campo accumulatedPercentageCompleted deve seta preenchido com o percentual total das medições até o período indicado pela data do campo measuredIn. O percentual será calculado com a diferença do somatório dos períodos anteriores com o percentual enviado. Este resultado pode ser um percentual negativo.

O cronograma medido dos períodos posteriores ao informado, serão removidos.

**Máscara de Url:** http://{domínio}:{porta}/api/construction-projects/v1/measuredInput

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 3 - API de entrada de Cronograma Realizado

---

Esta API permitirá a entrada de valores no cronograma Realizado.

O campo accumulatedPercentageCompleted deve seta preenchido com o percentual total das medições até o período indicado pela data do campo accomplishedIn. O percentual será calculado com a diferença do somatório dos períodos anteriores com o percentual enviado. Este resultado pode ser um percentual negativo.

O cronograma realizado dos períodos posteriores ao informado, serão removidos.

Alterado para que as API's de planejado e de realizado atualizem os campos de data inicio e fim do planejamento ou realizado, respectivamente, no PERT.

Estas datas serão atualizadas apenas se forem menor que a data inicial ou maior que a data final.

A data início real somente será alterada se o percentual enviado for maior que 0 (zero).

A data fim real somente será alterada se o percentual enviado for maior ou igual a 100.

**Máscara de Url:** http://{domínio}:{porta}/api/construction-projects/v1/accomplishedInput

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 4 - API de Cálculo de Cronograma

---

Esta API permitirá a execução do cálculo do cronograma

As parâmetros deverão identificar qual projeto e planilha deverá ser calculado.

**Máscara de Url:** http://{domínio}:{porta}/api/construction-projects/v1/calculate-schedule

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 5 - API de Cálculo de Envio de Custos Incorridos

---

Esta API permitirá a execução de custos incorridos no cronograma.

O campo de parâmetro de entrada serve para definir o tipo de agrupamento. (groupingType)

Valores possíveis:

0-Nenhum

1-Por dia

2-Por mês

**Máscara de Url:** <http://localhost:8051/api/construction-projects/v1/appropriatedSchedule>

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 6 - API de Serviços para cópia de parâmetro

---

Esta API permitirá a execução de serviços para a copia de parâmetro.

* Copiar os parâmetros de um projeto para outro

**Máscara de Url:** [http://localhost:8051/api/construction-projects/v1/copy-parameters](http://localhost:8051/api/construction-projects/v1/copy-parameters "Follow link")

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 7 - API de Serviço para atualizar parâmetro de períodos do projeto

---

Atualizar os períodos de um projeto com base nos parâmetros de data inicio, periodicidade e quantidade de períodos

Valores possíveis para o campo typeOfPeriods

0   - Personalizado  
1   - Diario  
-7   Semanal  
7   - SemanalCorridos  
-15 - Quinzenal  
15  - QuinzenalCorridos  
30  - Mensal  
-10 - Dezena  
10  - DezenaCorridos

**Máscara de Url:** [http://localhost:8051/api/construction-projects/v1/schedule-Parameters](http://localhost:8051/api/construction-projects/v1/schedule-Parameters "Follow link")

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

# 8 - Obter dados de cronograma através de SOAP

---

É possível obter os dados do cronograma através de SOAP. Para maiores detalhes do uso do SOAP: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007851192-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Utilizando-o-SoapUI-para-consumir-DataServers-RM-via-WebServices>

Os campos após o nome do DataSever são os parâmetros que devem ser passados na seguinte ordem:

* Tipo Planilha (0 - Atividade / 1 - Serviço)
* Tipo do Cronograma (conforme codificação abaixo)
* Identificador do Cenário (0 - Principal / 1 a 4 - Cenários)
* Exibe colunas de valor (true / false)

Tipos de Cronograma:

P - Planejado

R - Realizado

M - Medido

A - Apropriado

T - Todos

B - Base

falseExemplo do XML de entradaVer XML...js1XMLtrue




PrjCronogramaPlanilhaAtividadeData/0/[0,0,true]

CODCOLIGADA=1 AND IDPRJ=2

CODCOLIGADA=1;IDPRJ=2;CODUSUARIO='mestre'
]]>
