---
content_hash: d210824049b0634b9f508d1803d4f8baeeca0f5aa31e16f4ba3c1edc492367b6
fetched_at: '2026-06-29T00:11:48.710007+00:00'
page_id: '825929878'
product: rm
source: tdn-rm
title: API de Tipo de Documento
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Tipo+de+Documento
version: 3
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API de Tipo de Documento utilizando todos os métodos implementados.

Importante

Recurso disponível a partir da release 12.1.2406.

# 1 - Métodos

---

      Serão apresentados 5 métodos, os quais foram implementados na API de Tipo de Documento, são eles:

* GET
* POST
* PATCH
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todas as contas/caixa)

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order (Retorna os dados ordenados)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes?order=description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalseOrder (Desc)

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes?order=-description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** code

**Valor:** 0005

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes?code=0005>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueFiltros Complexos - OData

Para realizar filtros complexos na API de Tipo de Documento é possível adotar o padrão OData. Para entender melhor sobre a utilização desse padrão, acesse o link da documentação [Utilizando filtros complexos - Exemplos do guia de API - ODATA](https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA).

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

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes?page=1&pageSize=2>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** company

**Campo 2:** code

**Campo 2:** description

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes?fields=company,code,description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar tipo de documento pelo identificador)

---

Parâmetros

Nos parâmetros do GetOne é necessário passar uma chave composta ("id"), por isso informamos "company" que é o código da coligada do tipo de documento que queremos selecionar e o "code" que é o código do tipo de documento, sendo eles separados pelo caractere "|" pipe.

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes/{company}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company:** 1

**Code:** 55

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes/1|55>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um tipo de documento)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PATCH

---

## 1.3.1 - Patch (Atualização parcial de um tipo de documento)

---

falsePatch

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes/{company}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company:** 1

**Code:** TesteApi

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes/1|TesteAPI>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - PUT

---

## 1.4.1 - Put (Atualização completa de um tipo de documento)

---

falsePut

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes/{company}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company:** 1

**Code:** TesteApi

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes/1|TesteAPI>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.5 - DELETE

---

## 1.5.1 - Delete (Exclui uma Conta/Caixa)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/documenttypes/{company}|{code}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company:** 1

**Code:** TesteAPI

**Url Utilizada:** <http://localhost:8051/api/financial/v1/documenttypes/1|TesteAPI>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true
