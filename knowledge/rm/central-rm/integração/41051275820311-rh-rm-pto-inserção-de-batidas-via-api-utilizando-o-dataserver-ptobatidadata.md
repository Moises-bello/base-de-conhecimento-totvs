---
article_id: 41051275820311
category: Integração
content_hash: ce9cca7b22a5a3a7bc598c75d86e6304eab3bbefabf677522d29dc0de1b1a5ae
fetched_at: '2026-06-28T22:46:34.615079+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: RH - RM - PTO - Inserção de batidas via API utilizando o dataserver PtoBatidaData
type: support-article
updated_at: '2026-06-08T14:14:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41051275820311-RH-RM-PTO-Inser%C3%A7%C3%A3o-de-batidas-via-API-utilizando-o-dataserver-PtoBatidaData
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41051275811095) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Para conexão via Webservice/API, como realizar a utilização do Data Server PtoBatidaData em aplicativos de terceiros?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**

### **Método GET**

##### Para o método GET deverá realizar as seguintes configurações:

1-Informe  a URL : [HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData](http://localhost:8051/RMSRestDataServer/rest/PtoBatidaData/1$_$00002$_$2022-07-05$_$720).

Os dados retornados são referentes aos existentes na tabela ABATFUN.

Se o usuário desejar filtrar os registros, será necessário a passagem dos parâmetros, estes devem incluídos separado por $\_$, e com a / após o dataserver PtoBatidaData.

 Exemplo: [HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData/1$\_$00002$\_$2022-07-05$\_$720](http://localhost:8051/RMSRestDataServer/rest/PtoBatidaData/1$_$00002$_$2022-07-05$_$720)

**Observação:** Quando utilizamos o filtro, os dados retornados no campo "JUSTIFICA" e "DCHORA" são setados com um valor padrão, pois são utilizados nos processos de exclusão e alteração de registros via WebService. Na ABATFUN **não existem**esses campos eles existem apenas para controle, não referenciando informações de outras tabelas.

|  |  |
| --- | --- |
| Campo | Retorno |
| 1 | Código da Coligada |
| 00002 | Chapa do funcionário |
| 2022-07-05 | Ano, Mês e Data batida |
| 720 | Hora da batida |

![](https://tdn.totvs.com/download/attachments/737553473/image2023-2-6_16-36-10.png?version=1&modificationDate=1675712170537&api=v2)

2-Informe o Usuário e a senha utilizados para acessar a base de dados, no menu Authorization pelo tipo Basic Auth.  
![](https://tdn.totvs.com/download/attachments/737553473/image2023-2-6_16-47-44.png?version=1&modificationDate=1675712864763&api=v2)

3-No Headers utilize o parâmetro Codcoligada preencha com o  value desejado.  
![](https://tdn.totvs.com/download/attachments/737553473/image2023-2-6_16-52-38.png?version=1&modificationDate=1675713159090&api=v2)

### **Método POST**

Para o Método Post informe a URL [HTTP://LOCALHOST:8051/RMSRestDataServer/rest/PtoBatidaData](http://localhost:8051/RMSRestDataServer/rest/PtoBatidaData) e no campo Body informe a seguinte estrutura, conforme exemplo:

```
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
      "IDJORNADA": null,
      "IDAAFDT": null,
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
```

### **Método DELETE**

Para o Método DELETE será necessário acrescentar os parâmetros conforme registro que se deseja deletar, exemplo : [/1$\_$00002$\_$2022-07-14$\_$1380](http://localhost:8051/RMSRestDataServer/rest/PtoBatidaData/1$_$00002$_$2022-07-14$_$1380), juntamente com a URL ficando conforme abaixo:

![](https://tdn.totvs.com/download/attachments/737553473/image2023-2-6_14-35-50.png?version=1&modificationDate=1675704950513&api=v2)

**Saiba mais**  
[DT - Postman Webservice PtoBatidaData](https://tdn.totvs.com/display/public/LRM/DT+-+Postman+Webservice+PtoBatidaData#1-4)
