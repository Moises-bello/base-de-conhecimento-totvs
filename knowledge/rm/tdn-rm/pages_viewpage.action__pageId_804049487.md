---
content_hash: 5a6a8a9422ce479dbcf7aaf2680de1624786e6bd3c31daf4be834194a51f9b07
fetched_at: '2026-06-29T00:11:43.345339+00:00'
page_id: '804049487'
product: rm
source: tdn-rm
title: API de Moedas e Índices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804049487
version: 5
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API de Moedas e Índices utilizando todos os métodos implementados.

Importante

Recurso disponível a partir da release 12.1.2402.

# 1 - Métodos

---

Serão apresentados 5 métodos, os quais foram implementados na API de Moedas e Índices, são eles:

* GET
* POST
* PATCH
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todas as moedas e índices)

---

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies/

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies/>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order (Recuperar os dados ordenados)

---

falseParâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies?order={campo}

Exemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies?order=description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalseOrder (Desc)

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies?order=-description>

falseExemplo de ResultadoVer resultado JSON...js1Resultad (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies/?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** type

**Valor:** M

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies?type=M>

falseExemplo de ResultadoVer resultado JSON...js1Resultad (JSON)true

## 1.1.4 - Paginação

---

falseParâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies?page=1&pageSize=5>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retornar campos específicos no resultado)

---

falseParâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** symbol

**Campo 2:** type

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies?fields=symbol,type>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar moeda ou índice pelo símbolo)

---

Parâmetros

Para recuperar os dados de uma moeda ou índice especifico é necessário informar o símbolo.

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies/{symbol}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Symbol:** R$

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies/R$>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir uma moeda ou índice)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies>

falseExemplo de EntradaVer entrada JSON...js1Entrada (JSON)truefalseExemplo de Resultado PositivoVer resultado JSONjs1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSONjs1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar uma moeda ou índice)

---

falsePut

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies/{symbol}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Symbol:** Fr

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies/Fr>

falseExemplo de EntradaVer entrada JSON...jsEntrada (JSON)falseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - PATCH

---

## 1.4.1 - Patch (Atualizar parcialmente uma moeda ou índice)

---

---

falsePatch

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies/{symbol}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Symbol:** Fr

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies/Fr>

falseExemplo de EntradaVer entrada JSON...jsEntrada (JSON)falseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - DELETE

---

## 1.4.1 - Delete (Excluir uma moeda ou índice)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/currencies/{symbol}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Symbol:** Fr

**Url Utilizada:** <http://localhost:8051/api/financial/v1/currencies/Fr>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 201 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true
