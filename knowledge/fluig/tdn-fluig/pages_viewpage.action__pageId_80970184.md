---
content_hash: 2fd16c6b04c5ce70cc441ceabccdcf355732ad6e512755c4216a35ed9f41218f
fetched_at: '2026-06-28T21:35:30.161576+00:00'
page_id: '80970184'
product: fluig
source: tdn-fluig
title: Visualizador de gráficos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=80970184
version: 8
---

# Índice

true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar ao desenvolvedor informações sobre a visualização de gráficos na plataforma Fluig.

# Visualizador de gráficos

O Visualizador de gráficos tem como objetivo principal permitir que outras aplicações possam exibir gráficos customizados dentro da plataforma Fluig. Para isto, basta a aplicação registrar seu serviço de gráfico no Fluig e disponibilizar dois métodos REST: um que informará os parâmetros de configuração do gráfico e outro que disponibilizará os dados.

O Visualizador de Gráficos permite exibição nos formatos de tabela, gráfico de coluna e gráfico de pizza.

## Passos necessários

### **1. Registrar o serviço de dados no TOTVS Fluig Plataforma.**

Para registrar o serviço de dados do gráfico basta enviar uma mensagem assíncrona para o Fluig.

O desenvolvedor deverá usar o evento "REGISTER\_CHART\_SERVICE”. Será necessário passar um objeto do tipo ChartServiceVO com os dados do serviço de dados em questão.

O objeto ChartServiceVO, disponível no pacote com.totvs.technology.wcm.common.chart, é composto dos seguintes elementos:

* String id: código do serviço de gráfico
* String description: descrição do serviço de gráfico
* String ParametersRest: URL do serviço REST que retornará os parâmetros
* String dataRest: URL do serviço REST que retornará os dados do gráfico

**Exemplo:**

javaChartServiceVO

Este registro precisa ser executado cada vez que aplicação é deployada, ou seja, cada vez que a plataforma Fluig subir. Para isto sugerimos que seja criado um *servlet* em sua aplicação com a opção **loadOnStartup = 1**, que se encarregará de realizar esta tarefa.

### **2. Serviços de Parâmetros**

Este serviço REST deverá retornar uma lista de ChartParameterVO, que conterá os parâmetros que seu serviço de dados precisará para fornecer os dados do gráficos. Com base neste serviço a plataforma Fluig construirá a tela de configuração.  
O ChartParameterVO (pacote com.totvs.technology.wcm.common.chart) é composto dos seguintes elementos:

* int code id: código numérico sequencial que será usado para busca dos dados posteriormente
* String title: nome do campo como aparecerá na tela
* String type: tipo de campo (ChartParameterVO.TYPE\_STRING, ChartParameterVO.TYPE\_NUMBER, ChartParameterVO.TYPE\_DATA ou ChartParameterVO.TYPE\_BOOLEAN)
* String AllowedList: se o campo for tipo string, podem ser informadas as opções para o usuário selecionar em uma lista. Estas opções devem ser separadas por “;”
* boolean multipleSelection: true/false, caso permita ou não seleção múltipla se o AllowedList esteja em uso
* String value: Valor inicial se existir

**Exemplo:**

javaChartParameterVO params = new ArrayList<>();
ChartParameterVO param1 = new ChartParameterVO();
param1.setCode(1);
param1.setTitle("Código do Item");
param1.setType(ChartParameterVO.TYPE\_STRING);
param1.setAllowedList(“Item 1;Item 2;Item 3”);
param1.setMultipleSelection(ChartParameterVO.SELECTION\_UNIQUE);
params.add(param1);
ChartParameterVO param2 = new ChartParameterVO();
param2.setCode(2);
param2.setTitle("Exibir somente itens ativos");
param2.setType(ChartParameterVO.TYPE\_BOOLEAN);
params.add(param2);
return params;]]>

### **3. Serviço de Dados**

O serviço REST deverá retornar um ChartVO, com os dados para exibição do gráfico.  
O ChartVO (pacote com.totvs.technology.wcm.common.chart) é composto dos seguintes elementos:

* String title:  título que será exibido no gráfico
* String description: descrição do gráfico
* String type: tipo do gráfico (ChartTypes.column.getName(), ChartTypes.pie.getName(), ChartTypes.table.getName()
* Map<String, Object>[] source: dados do gráfico
* ChartCategoryVO category: categorias
* ChartSerieGroupVO[] seriesGroups: grupos de séries

exemplopPizzajavaExemplo para um Gráfico de pizza[] source = new Map[2];
Map data0 = new HashMap();
data0.put("label","Utilizado");
data0.put("size",80);
source[0] = data0;
Map data1 = new HashMap();
data1.put("label","Livre");
data1.put("size",20);
source[1] = data1;
result.setSource(source);
ChartSerieGroupVO[] seriesGroups = new ChartSerieGroupVO[1];
ChartSerieGroupVO serieGroup = new ChartSerieGroupVO(ChartTypes.pie.getName(),"label");
ChartSerieVO[] series = new ChartSerieVO[1];
ChartSerieVO serie = new ChartSerieVO("size","label");
series[0] = serie;
serieGroup.setSeries(series);
seriesGroups[0] = serieGroup;
result.setSeriesGroups(seriesGroups);
return result;]]>cColunasjavaExemplo para um Gráfico de colunas[] source = new Map[2];
Map data0 = new HashMap();
data0.put("label",”Item 1”);
data0.put("total",100);
data0.put("used",40);
data0.put("free",60);
source[0] = data0;
Map data0 = new HashMap();
data0.put("label",”Item 2”););
data0.put("total",120);
data0.put("used",60);
data0.put("free",60);
source[1] = data0;
result.setSource(source);
ChartCategoryVO category = new ChartCategoryVO("label");
result.setCategory(category);
ChartSerieGroupVO[] seriesGroups = new ChartSerieGroupVO[1];
ChartSerieGroupVO serieGroup = new ChartSerieGroupVO(ChartTypes.column.getName(),"Espaço(Mb)");
ChartAxiVO axis = new ChartAxiVO(20,true,"Espaço(Mb)");
serieGroup.setValueAxis(axis);
ChartSerieVO[] series = new ChartSerieVO[3];
ChartSerieVO total = new ChartSerieVO("total","Espaço Total");
series[0] = total;
ChartSerieVO used = new ChartSerieVO("used","Espaço Utilizado");
series[1] = used;
ChartSerieVO free = new ChartSerieVO("free","Espaço Livre");
series[i] = free;
serieGroup.setSeries(series);
seriesGroups[0] = serieGroup;
result.setSeriesGroups(seriesGroups);
return this.buildResponse(result);]]>tTabelasjavaExemplo para um Gráfico de tabelas[] source = new Map[2];
Map data0 = new HashMap();
data0.put("label",”Item 1”);
data0.put("total",100);
data0.put("used",40);
data0.put("free",60);
source[0] = data0;
Map data0 = new HashMap();
data0.put("label",”Item 2”););
data0.put("total",120);
data0.put("used",60);
data0.put("free",60);
source[1] = data0;
result.setSource(source);
ChartSerieGroupVO[] seriesGroups = new ChartSerieGroupVO[1];
ChartSerieGroupVO serieGroup = new ChartSerieGroupVO(ChartTypes.table.getName(),"Espaço(Mb)");
ChartAxiVO axis = new ChartAxiVO(20,true,"Espaço(Mb)");
serieGroup.setValueAxis(axis);
ChartSerieVO[] series = new ChartSerieVO[4];
ChartSerieVO label = new ChartSerieVO("label","Item");
series[0] = label;
ChartSerieVO total = new ChartSerieVO("total","Espaço Total");
series[1] = total;
ChartSerieVO used = new ChartSerieVO("used","Espaço Utilizado");
series[2] = used;
ChartSerieVO free = new ChartSerieVO("free","Espaço Livre");
series[3] = free;
serieGroup.setSeries(series);
seriesGroups[0] = serieGroup;
result.setSeriesGroups(seriesGroups);
return this.buildResponse(result);]]>
