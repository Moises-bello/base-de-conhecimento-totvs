---
content_hash: 6a2e7f017f3dbd9c69b3c85897edded0347a27209f6048782b6e69be5c4ad35a
fetched_at: '2026-06-29T00:09:38.669002+00:00'
page_id: '427494102'
product: rm
source: tdn-rm
title: API de JobExecution
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+JobExecution
version: 12
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

Para mais informações sobre consumo de Licença, [Veja Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=419548455#APIsdeFrameworkM%C3%B3duloServi%C3%A7osGlobais-5-ConsumodeLicen%C3%A7aspeloLicenseServer).

# 1 - Métodos

---

     A API de JobExecution possui apenas o método GET implementado. É possível utilizar os filtros padrões da API para filtrar um registro desejado, ou utilizar a assinatura /jobExecution/{executionId} para retornar um executionId específico.

    O  executionId é composto por duas chaves: "jobScheduleID|execution". Por exemplo: executionId = "200047|3", esta é a chave para retornar a terceira execução do Job 200047.

falseObservação:

A Api de JobExecution também realiza buscas pelo status do agendamento, são eles:

* Success
* Pending
* Running
* Failure

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todas as execuções de jobs realizado na base)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution>

falseExemplo de ResultadoVer resultado JSON...

{

"hasNext": true,  
"items": [  
{  
"executionId": "100001|1",  
"jobScheduleId": "100001",  
"status": "success",  
"createdDate": "",  
"startedDate": "17/11/2008 17:16:05",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100002|1",  
"jobScheduleId": "100002",  
"status": "success",  
"createdDate": "",  
"startedDate": "25/11/2008 15:39:21",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100003|1",  
"jobScheduleId": "100003",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 16:33:00",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100004|1",  
"jobScheduleId": "100004",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:12:03",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100005|1",  
"jobScheduleId": "100005",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:15:13",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100006|1",  
"jobScheduleId": "100006",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:29:24",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100007|1",  
"jobScheduleId": "100007",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:32:35",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100008|1",  
"jobScheduleId": "100008",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:50:26",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100009|1",  
"jobScheduleId": "100009",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 18:01:37",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100010|1",  
"jobScheduleId": "100010",  
"status": "success",  
"createdDate": "",  
"startedDate": "22/05/2009 17:17:12",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100011|1",  
"jobScheduleId": "100011",  
"status": "success",  
"createdDate": "",  
"startedDate": "22/05/2009 17:31:21",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100012|1",  
"jobScheduleId": "100012",  
"status": "success",  
"createdDate": "",  
"startedDate": "25/05/2009 15:55:37",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100013|1",  
"jobScheduleId": "100013",  
"status": "failure",  
"createdDate": "",  
"startedDate": "25/05/2009 15:58:07",  
"user": "",  
"error": "Não foi encontrada a consulta SQL com código \"GLOBAIS.001\"!"  
},  
{  
"executionId": "100014|1",  
"jobScheduleId": "100014",  
"status": "success",  
"createdDate": "",  
"startedDate": "25/05/2009 17:55:33",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100015|1",  
"jobScheduleId": "100015",  
"status": "failure",  
"createdDate": "",  
"startedDate": "25/05/2009 19:01:33",  
"user": "",  
"error": "Não é possível enviar um e-Mail sem que o endereço do remetente seja informado. Por favor preencha o e-mail da Coligada, no Cadastro de Coligadas."  
},  
{  
"executionId": "100016|1",  
"jobScheduleId": "100016",  
"status": "success",  
"createdDate": "",  
"startedDate": "26/05/2009 09:59:01",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100017|1",  
"jobScheduleId": "100017",  
"status": "success",  
"createdDate": "",  
"startedDate": "26/05/2009 10:44:11",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100018|1",  
"jobScheduleId": "100018",  
"status": "success",  
"createdDate": "",  
"startedDate": "26/05/2009 10:45:11",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100018|2",  
"jobScheduleId": "100018",  
"status": "success",  
"createdDate": "",  
"startedDate": "26/05/2009 10:45:21",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100019|1",  
"jobScheduleId": "100019",  
"status": "success",  
"createdDate": "",  
"startedDate": "26/05/2009 10:46:01",  
"user": "",  
"return": ""  
}  
]  
}

## 1.1.2 - Order(Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** jobScheduleId

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution?order=jobScheduleId>

falseExemplo de ResultadoVer resultado JSON...

{

"hasNext": true,  
"items": [  
{  
"executionId": "100001|1",  
"jobScheduleId": "100001",  
"status": "success",  
"createdDate": "",  
"startedDate": "17/11/2008 17:16:05",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100002|1",  
"jobScheduleId": "100002",  
"status": "success",  
"createdDate": "",  
"startedDate": "25/11/2008 15:39:21",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100003|1",  
"jobScheduleId": "100003",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 16:33:00",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100004|1",  
"jobScheduleId": "100004",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:12:03",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100005|1",  
"jobScheduleId": "100005",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:15:13",  
"user": "",  
"return": ""  
}  
]  
}

false1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** jobScheduleId

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution?order=-jobScheduleId>

falseExemplo de ResultadoVer resultado JSON...

{

"hasNext": true,  
"items": [  
{  
"executionId": "102792|1",  
"jobScheduleId": "102792",  
"status": "success",  
"createdDate": "05/12/2018 09:50:19",  
"startedDate": "05/12/2018 09:50:19",  
"user": "rm",  
"return": ""  
},  
{  
"executionId": "102791|1",  
"jobScheduleId": "102791",  
"status": "success",  
"createdDate": "04/12/2018 09:52:09",  
"startedDate": "04/12/2018 09:52:10",  
"user": "rm",  
"return": ""  
},  
{  
"executionId": "102790|1",  
"jobScheduleId": "102790",  
"status": "success",  
"createdDate": "03/12/2018 16:37:33",  
"startedDate": "03/12/2018 16:37:33",  
"user": "rm",  
"return": ""  
},  
{  
"executionId": "102789|1",  
"jobScheduleId": "102789",  
"status": "success",  
"createdDate": "05/10/2018 10:05:20",  
"startedDate": "05/10/2018 10:05:22",  
"user": "rm",  
"return": ""  
},  
{  
"executionId": "102788|1",  
"jobScheduleId": "102788",  
"status": "success",  
"createdDate": "05/10/2018 09:55:30",  
"startedDate": "05/10/2018 09:55:30",  
"user": "mestre",  
"return": ""  
}  
]  
}

## 1.1.3 - Filter (Resultado filtrado)

---

false1.1.3 FilterfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** status

**Valor:** success

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution?status=success>

falseExemplo de ResultadoVer resultado JSON...

{

"hasNext": true,  
"items": [  
{  
"executionId": "100001|1",  
"jobScheduleId": "100001",  
"status": "success",  
"createdDate": "",  
"startedDate": "17/11/2008 17:16:05",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100002|1",  
"jobScheduleId": "100002",  
"status": "success",  
"createdDate": "",  
"startedDate": "25/11/2008 15:39:21",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100003|1",  
"jobScheduleId": "100003",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 16:33:00",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100004|1",  
"jobScheduleId": "100004",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:12:03",  
"user": "",  
"return": ""  
},  
{  
"executionId": "100005|1",  
"jobScheduleId": "100005",  
"status": "success",  
"createdDate": "",  
"startedDate": "02/12/2008 17:15:13",  
"user": "",  
"return": ""  
}  
]  
}

## 1.1.4 - Paginação

---

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

false1.1.4 PaginacaofalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 1

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution?page=1&pageSize=1>

falseExemplo de ResultadoVer resultado JSON...

{

"hasNext": true,  
"items": [  
{  
"executionId": "100001|1",  
"jobScheduleId": "100001",  
"status": "success",  
"createdDate": "",  
"startedDate": "17/11/2008 17:16:05",  
"user": "",  
"return": ""  
}  
]  
}

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

false1.1.5 FieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution?fields={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campos:** status,jobScheduleId,executionId

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution?fields=status,jobScheduleId,executionId>

falseExemplo de ResultadoVer resultado JSON...

{

"hasNext": true,  
"items": [  
{  
"executionId": "100360|866",  
"jobScheduleId": "100360",  
"status": "pending"  
},  
{  
"executionId": "100362|682",  
"jobScheduleId": "100362",  
"status": "pending"  
},  
{  
"executionId": "102767|2",  
"jobScheduleId": "102767",  
"status": "pending"  
},  
{  
"executionId": "102768|2",  
"jobScheduleId": "102768",  
"status": "pending"  
},  
{  
"executionId": "100157|2",  
"jobScheduleId": "100157",  
"status": "success"  
}  
]  
}

## 1.1.6 - GetOne (Recuperar a execução pelo executionId)

---

false1.1.6 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobExecution/{executionId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**executionId:** 100025|3 , onde jobScheduleId = 100025 e o número da execução = 3

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobExecution/100025|3>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true
