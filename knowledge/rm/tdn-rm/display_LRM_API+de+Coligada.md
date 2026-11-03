---
content_hash: aca6cf7078adc5ff1c164084f96a6188239947db1226ffec1b7cab51e257a0a5
fetched_at: '2026-06-29T00:09:52.179168+00:00'
page_id: '438273309'
product: rm
source: tdn-rm
title: API de Coligada
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Coligada
version: 36
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

      Serão apresentados 4 métodos, os quais foram implementados na API de Usuários, são eles:

* GET
* POST
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todas as coligadas)

---

falseGetAll

**fMáscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies/

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies](http://localhost:8051/api/glb/v1/companies)

Importante

A partir da versão 12.1.2310, o resultado não é filtrado pelo perfil de segurança do usuário, mantendo o mesmo padrão da MDI, trazendo todas as coligadas.

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order (Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/campanies?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** nickname

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies?order=nickname](http://localhost:8051/api/glb/v1/companies?order=nickname)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalseOrder (Desc)

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** nickname

**Tipo de Ordenação:** Descendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies?order=-nickname](http://localhost:8051/api/glb/v1/companies?order=-nickname)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/campanies?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** state

**Valor:** MG

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies?state=MG](http://localhost:8051/api/glb/v1/companies?state=MG)

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

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies?page=1&pageSize=2](http://localhost:8051/api/glb/v1/companies?page=1&pageSize=2)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** nickname

**Campo 2:** federalId

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies?fields=nickname,federalId](http://localhost:8051/api/glb/v1/companies?fields=nickname,federalId)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar coligada pelo identificador)

---

Parâmetros

**Expand:** Parâmetro opcional, usado para determinar a(s) propriedade(s) expandables que devem ser retornadas expandidas.

**Exemplo:** ?expand=roles - Nesse exemplo, os perfis associados ao usuário serão retornados na resposta da requisição.

**Valores padrão:** Caso não sejam preenchidos todas as propriedades expandables serão retornadas sem serem expandidas.

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8099

**Id:** 00001

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/6](http://localhost:8051/api/glb/v1/companies/6)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalseGetOne expandable

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies/{id}?expand={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 6

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/6?expand=subsidiary](http://localhost:8051/api/glb/v1/companies/6?expand=subsidiary)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir uma Coligada)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies](http://localhost:8051/api/glb/v1/companies)

falseObservação:

Para incluir uma imagem no corpo (Body) na hora de realizar um POST (inclusão de registro), a imagem deve ser informada no formato Array de Byte.

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar uma Coligada)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 12

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/12](http://localhost:8099/api/rm/glb/v1/companies/12)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - PATCH

---

## 1.4.1 - Patch (Atualização parcial de uma Coligada)

---

falsePatch

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 12

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/12](http://localhost:8099/api/rm/glb/v1/companies/12)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - DELETE

---

## 1.4.1 - Delete (Desativa uma Coligada)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/companies/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 12

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/12](http://localhost:8099/api/rm/glb/v1/users/Teste_01)

falseExemplo de Configuração

Ao realizar um "DELETE", a coligada não será excluída será somente desativada.

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 201 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true
