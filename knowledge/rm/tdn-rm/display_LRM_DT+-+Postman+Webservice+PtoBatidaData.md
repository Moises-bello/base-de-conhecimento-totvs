---
content_hash: 5c65da8b550c8c49fee65a9e3f9382579207206bbf9b68dc1450dd1f27a1a373
fetched_at: '2026-06-29T00:11:31.379225+00:00'
page_id: '737553473'
product: rm
source: tdn-rm
title: DT - Postman Webservice PtoBatidaData
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Postman+Webservice+PtoBatidaData
version: 42
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | Webservice  PtoBatidaData |
| Função: | Webservice |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHJORNRM-2961](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2961) |

## **02. SITUAÇÃO/REQUISITO**

Quando é executada a chamada JSON esta sendo demonstrada uma mensagem.

## **03. SOLUÇÃO**

Atualizado o processo de envio das informações  no webservice PtoBatidaData.

**04. EXEMPLO DE UTILIZAÇÃO**

Este documento tem por objetivo demonstrar a configuração para utilização do Data Server PtoBatidaData em aplicativos de terceiros.

11Parametrização RM

Será necessário editar o arquivo RM.Host.Service.exe.config e RM.Host.exe.config, que estão na pasta ***<diretório de instalação do RM>\RM.Net:*** *e inserir as tags abaixo:*

*<add key="HTTPPort" value="8051" />  
 <add key= "defaultDB" value ="CorporeRM"/>*

2Parametrização Método GET

Para o método GET deverá realizar as seguintes configurações:

1-Informe  a URL : [HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData](HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData/1$_$00002$_$2022-07-05$_$720).

Os dados retornados são referentes aos existentes na tabela ABATFUN.

Se o usuário desejar filtrar os registros, será necessário a passagem dos parâmetros, estes devem incluídos separado por $\_$, e com a / após o dataserver PtoBatidaData.

 Exemplo: <HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData/1$_$00002$_$2022-07-05$_$720> 

**Observação:** Quando utilizamos o filtro, os dados retornados no campo "JUSTIFICA" e "DCHORA" são setados com um valor padrão, pois são utilizados nos processos de exclusão e alteração de registros via WebService. Na ABATFUN **não existem** esses campos eles existem apenas para controle, não referenciando informações de outras tabelas.

|  |  |
| --- | --- |
| Campo | Retorno |
| 1 | Código da Coligada |
| 00002 | Chapa do funcionário |
| 2022-07-05 | Ano, Mês e Data batida |
| 720 | Hora da batida |

2-Informe o Usuário e a senha utilizados para acessar a base de dados, no menu Authorization.

3-No Headers utilize o parâmetro Codcoligada preencha com o  value desejado.

3Parametrização Método POST 

Para o Método Post informe a URL <HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData> e no campo Body informe a seguinte estrutura, conforme exemplo:

{  
      "CODCOLIGADA": 1,  
      "CHAPA": "00002",  
      "DATA": "2022-07-14T00:00:00-03:00",  
      "BATIDA": 1380,  
      "STATUS": "D",  
      "NATUREZA": 0,  
      "CODIGOTERMCOL": null,  
      "DATAINSERCAO": "2022-09-06T12:06:14-03:00",  
      "DATAAPROV": null,  
      "NOME": null,  
      "CODSECAO": null,  
      "DESCSECAO": null,  
      "JUSTIFICA": "Batida incluída via WebService",  
      "DCHORA": " ",  
      "DCBATDIA": null,  
      "DATAREFERENCIA": "14/07/2022 00:00:00",  
      "IDJORNADA": null,  
      "IDAAFDT": null,  
      "COLIGADARESP": null,  
      "CHAPARESP": null,  
      "RECCREATEDBY": "mestre",  
      "RECCREATEDON": "2022-09-06T12:06:15-03:00",  
      "RECMODIFIEDBY": "mestre",  
      "RECMODIFIEDON": "2023-02-03T08:45:35-03:00",  
      "TIPOBATIDA": null,  
      "IDAPORTARIA373": null,  
      "NATUREZAALTERADA": null,  
      "DATAREFERENCIAALTERADA": 0  
   }

4Parametrização Método DELETE 

Para o Método DELETE será necessário acrescentar os parâmetros conforme registro que se deseja deletar, exemplo : [/1$\_$00002$\_$2022-07-14$\_$1380](HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData/1$_$00002$_$2022-07-14$_$1380), juntamente com a URL ficando conforme abaixo:

**05. ASSUNTOS RELACIONADOS**

[Webservice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007851192-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%B5es-Utilizando-o-SoapUI-para-consumir-DataServers-RM-via-WebServices)
