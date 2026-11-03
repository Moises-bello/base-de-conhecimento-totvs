---
content_hash: 92f64259db4657bb581d80b96531a6561b24f6392e8458c5e0991a4bd0177fa8
fetched_at: '2026-06-29T00:12:09.537190+00:00'
page_id: '947313428'
product: rm
source: tdn-rm
title: API de Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=947313428
version: 7
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API de Cliente/Fornecedor utilizando todos os métodos implementados.

# 1 - Métodos

---

      Serão apresentados 4 métodos, os quais foram implementados na API de Cliente/Fornecedor, são eles:

* GET
* POST
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os clientes/fornecedores)

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order (Retorna os dados ordenados)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor?order=name>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalseOrder (Desc)

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor?order=-name>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** MainNIF

**Valor:** 111.111.111-11

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor?MainNIF=111.111.111-11>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.4 - Paginação

---

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor?page=1&pageSize=2>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** companyId

**Campo 2:** code

**Campo 3:** name

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor?fields=companyId,code,name>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar cliente/fornecedor pelo identificador)

---

Parâmetros

Nos parâmetros do GetOne é necessário passar uma chave composta ("companyInternalId"), por isso informamos "companyId" que é o código da coligada do Cliente/Fornecedor que queremos selecionar e o "code" que é o código do Cliente/Fornecedor, sendo eles separados pelo caractere "|" pipe.

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor/{companyId}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**companyId:** 1

**code:** RM

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor/1|RM>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um Cliente/Fornecedor)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)trueColigada do contexto

Para que o cliente/fornecedor seja incluído corretamente e os parâmetros do TOTVS Gestão Financeira sejam validados, é necessário que, no corpo da requisição, seja informada a propriedade "CurrentCompanyId" e o seu valor, que corresponde à coligada do contexto. 

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar por completo um Cliente/Fornecedor)

---

falsePut

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor/{company}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company:** 0

**Code:** F57598

**Url Utilizada:** <http://localhost:8051/api/fin/v1/CustomerVendor/0|F57598>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)trueColigada do contexto

Para que o cliente/fornecedor seja atualizado corretamente e os parâmetros do TOTVS Gestão Financeira sejam validados, é necessário que, no corpo da requisição, seja informada a propriedade "CurrentCompanyId" e o seu valor, que corresponde à coligada do contexto. 

# 1.5 - DELETE

---

## 1.5.1 - Delete (Excluir um Cliente/Fornecedor)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/fin/v1/CustomerVendor/{companyId}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company:** 1

**Code:** F00001

**Url Utilizada:** [http://localhost:8051/api/fin/v1/CustomerVendor/1|F00001](http://localhost:8051/api/fin/v1/CustomerVendor/1|F57598)

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

---

Para mais informações sobre o mapeamento de campos da API, consulte a documentação [API de Cliente/Fornecedor](https://api.totvs.com.br/apidetails/CustomerVendor_v1_000.json).
