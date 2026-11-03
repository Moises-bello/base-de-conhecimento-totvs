---
content_hash: 7a818d778fc9a94d3d3e8533cfdbeb57c5e9e3d8e453246f706c4a931668c1a0
fetched_at: '2026-06-29T00:09:50.712867+00:00'
page_id: '435107270'
product: rm
source: tdn-rm
title: API de Perfil
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Perfil
version: 16
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

Para mais informações sobre consumo de Licença, [Veja Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=419548455#APIsdeFrameworkM%C3%B3duloServi%C3%A7osGlobais-5-ConsumodeLicen%C3%A7aspeloLicenseServer).

# 1 - Método

---

     Foi implementados na API de Perfil somente o método GET.

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os perfis cadastrados na coligada)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/glb/v1/roles

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles](http://localhost:8099/api/rm/glb/v1/roles)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order(Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

---

**Padrão scim:**

**SortBy:** define o campo que será ordenado.

**SortOrder:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente.

**Exemplo 1:** ?sortBy=campo1&sortOrder=ascending (Ascendente)

**Exemplo 2:** ?sortBy=campo1&sortOrder=descending (Descendente)

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** id

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?order=id](http://localhost:8099/api/rm/glb/v1/roles?order=id)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalse1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** id

**Tipo de Ordenação:** Descendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?order=-id](http://localhost:8099/api/rm/glb/v1/roles?order=-id)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

false1.1.3 FilterfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** id

**Valor:** DBA\_G

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?id=DBA\_G](http://localhost:8099/api/rm/glb/v1/roles?id=DBA_G)

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

---

**Padrão scim:**

**StartIndex:** valor inicial do índice do registro que será retornado.

**Count:** quantidade máxima de registros que serão apresentados.

**Exemplo 1:** ?startIndex=2&count=2

false1.1.4 PaginacaofalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 2

**Valor2:** 2

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?page=2&pageSize=2](http://localhost:8099/api/rm/glb/v1/roles?page=1&pageSize=2)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

---

**Padrão scim:**

**Attributes:** define quais campos serão apresentados no resultado.

**Exemplo 1:** ?attributes=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

false1.1.5 FieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?fields={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campos:** id

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?fields=id](http://localhost:8099/api/rm/glb/v1/users?fields=processID,status,scheduleID,executionID)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - Fields &Order (Retornar os campos específicos em ordem)

---

Parâmetros

**Expand:** Parâmetro responsável pela especialização e ordenação de campos em um resultado.

**Exemplo:** ?fields=id&order=-id - Nesse exemplo, serão retornados o campo "id" de perfis e em ordem descendente.

---

**Padrão scim:**

**Attributes:** define quais campos serão apresentados no resultado.

**Exemplo 1:** ?attributes=campo1&sortBy=campo2&sortOrder=descending

false1.1.6 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?filelds={{campo}}&Order={{campo}}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor Campo Fields:** id

**Valor Campo Order:** id

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?fields=id&order=-id](http://localhost:8051/api/glb/v1/roles?fields=id&order=-id)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.7 - Filter by Application and Activation (Retornar os perfis ativos/inativos de uma aplicação(sistema) )

---

Parâmetros

**Expand:** Parâmetros responsáveis por receber o código da aplicação(sistema) e status de ativação

**Exemplo:** ?application=Id&isActive=1 - Nesse exemplo, serão retornados os perfis da aplicação(sistema) "Id" que estão ativos.

false1.1.7 Filter by Application and ActivationfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/roles?application={{códigoAplicação}&isActive={{0|1}}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor Campo application:**G

**Valor Campo isActive:**1

**Url Utilizada:** [http://localhost:8051/api/framework/v1/roles?application=G&isActive=](http://localhost:8051/api/glb/v1/roles?fields=id&order=-id)1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true
