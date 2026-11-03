---
content_hash: 243a36aa8d7a17806bdaa2b99019bf20d855ac633faa9c3f92c458c9b0de38be
fetched_at: '2026-06-29T00:09:38.598633+00:00'
page_id: '427049339'
product: rm
source: tdn-rm
title: API de JobScheduler
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+JobScheduler
version: 70
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

     Serão apresentados 4 métodos, os quais foram implementados na API de JobScheduler, são eles:

* GET
* POST
* PUT
* DELETE

falseObservação:

Caso o Job **não** seja **recorrente** o comportamento será o seguinte:

Ainda não executado:  "status": "active"

Executado com ou sem erro:  "status": "completed"

Cancelado ou Desativado: "status": "inactive"

Job recorrente:

Ainda não foi executado: "status": "active"

Todas as outras opções: "status": "inactive",

A Api de JobScheduler também realiza buscas pelo status do agendamento, são eles:

* Sucess
* Pending
* Running
* Failure

---

**Recorrência do Job:recurrencyType**

Um job pode ser criado para ser agendado e pode ser criado com alguma recorrência.

São permitidos os seguintes tipos de recorrência: Diário (daily), semanal (weekly) e mensal (monthly).

No swagger é possível visualizar o schema desses itens. Veja a seguir um exemplo:

js

* Para recorrências do tipo daily, a propriedade "firstExecution" enviada é usada apenas para identificar o fuso horário do cliente e são considerados os valores do objeto daily para criar a data de agendamento.   
  Como o tipo é diário, ele continuará executando todos os dias nas horas definidas em hour e minute.

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar Todos os Agendamentos de Job)

---

falseGetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order(Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** jobScheduleID

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler?order=jobScheduleID>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalse1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** jobScheduleID

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler?order=-jobScheduleID>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

falseFilterfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** status

**Valor:** pending

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler?status=pending>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.4 - Paginação

---

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginaçãofalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 1

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler?page=1&pageSize=1>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler?fields={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** jobScheduleId

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler?fields=jobScheduleId,firstExecution>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar o Agendamento pelo JobId)

---

Parâmetros

**Expand:** Parâmetro opcional, usado para determinar a(s) propriedade(s) expandables que devem ser retornadas expandidas.

**Exemplo:** ?expand=roles - Nesse exemplo, os perfis associados ao usuário serão retornados na resposta da requisição.

**Valores padrão:** Caso não sejam preenchidos todas as propriedades expandables serão retornadas sem serem expandidas.

falseGetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler/{jobId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**JobId:** 1

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler/1>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um agendamento de job)

---

falsePostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler>

**Obs.:** Se o Host estiver executando local (3camadas = false) não é possível criar um agendamento de job. Neste cenário, para executar o job imediatamente, é preciso que no Body da requisição a recorrência esteja como 'false' e não sejam enviadas as propriedades "ScheduleDateTime" e .

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)true

**Propriedades obrigatórias:**

firstExecution, processID, recurrent, executionParameter

executionParameter: UserName, Context, ProcessName, HostName, PrimaryKeyList, PrimaryKeyNames, processStartDate, processEndDate, completeInvoicing

falseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.2.2 - Post {IdJob}/Trigger

---

falsePostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler/{jobID}/trigger

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**JobID**: 3

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler/3/trigger>

**Obs.:** Se o Host estiver executando local (3camadas = false) não é possível criar um agendamento de job. Neste cenário, para executar o job imediatamente, é preciso que no Body da requisição a recorrência esteja como 'false' e não sejam envidas as propriedades "scheduleDate" e tipo de recorrência.

falseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.2.3 - Post {IdJob}/Restart

---

falsePost

Funcionalidade para reiniciar um Job.  
• Não é permitido executar o restart em Jobs que não foram executados.  
• Todos os outros tipos de Job´s podem ser reiniciados.   
• Após a reinicialização o Job é executado pelo JobServer independente da data de agendamento.   
• Após a execução, caso o Job seja agendado, o mesmo é reprogramado para a próxima recorrência.

falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler/{jobID}/restart

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**JobID**: 1

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler/1/restart>

**Obs.:** Se o Host estiver executando local (3camadas = false) não é possível criar um agendamento de job. Neste cenário, para executar o job imediatamente, é preciso que no Body da requisição a recorrência esteja como 'false' e não sejam envidas as propriedades "scheduleDate" e tipo de recorrência.

falseExemplo de Resultado PositivoVer resultado JSON...falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar um Job)

---

Ao executar a requisição de PUT, informando um JobID, esse processo será desabilitado e um novo será criado.

**Importante**: Existem casos em que o Job não será desabilitado, por exemplo: Jobs já executados ou já desabilitados. Nesses casos, um novo Job será criado normalmente.

false1.3.1 PutfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler/{jobid}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 1

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler/1>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - DELETE

---

## 1.4.1 - Delete (Deletar um Job)

---

Ao executar a requisição de Delete, informando um JobID, esse processo será desabilitado e não excluído da base de dados.

**Importante**: Não é possível desabilitar um job que já foi executado ou que está sendo executado.

false1.4.1 DeleteClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler/{JobID}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8050

**Idjob:** 2

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler/2>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true
