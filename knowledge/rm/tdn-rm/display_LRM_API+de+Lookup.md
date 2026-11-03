---
content_hash: 09bc3a987ef0455222fe29ca2225b7208390338a66f294b3b002fe6a9fa3065d
fetched_at: '2026-06-29T00:11:49.629107+00:00'
page_id: '836045070'
product: rm
source: tdn-rm
title: API de Lookup
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Lookup
version: 10
---

# Sumário

---

Sumário

# Objetivo

---

A **API de Lookup** é uma API com intuito de trazer apenas dados para identificação de registros. **(A partir da versão 12.1.2406,)**  
É implementada a partir da rota da API principal, e é apartada do sistema de permissionamento do RM.

# 1 - Métodos

---

      Utilizado um único método implementado:

* GET

# 2 - GET

---

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/{rota}/lookup

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Rota:** companies

**Url Utilizada:** localhost:8051/api/framework/v1/companies/lookup

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 2.1 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/{rota}/lookup?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Rota:** companies

**Campo 1:** nickname

**Campo 2:** federalId

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/lookup?fields=nickname,federalId](http://localhost:8051/api/glb/v1/companies?fields=nickname,federalId)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 2.2 - Order (Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/{rota}/lookup?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Rota:** companies

**Campo:** nickname

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/companies/lookup?order=nickname](http://localhost:8051/api/glb/v1/companies?order=nickname)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 2.3 - GetOne (Recuperar um único registro pelo identificador)

---

Parâmetros

**Expand:** Foi desabilitado para esta Api.

falseGetOne

**Máscara de Url:** [http://http://{domínio}:{porta}/api/framework/v1/{rota}/lookup/{id](http://http//{domínio}:{porta}/api/framework/v1/{rota}/lookup/{id)}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8099

**Rota:** companies

**Id: 6**

**Url Utilizada:** localhost:8051/api/framework/v1/companies/lookup[/6](http://localhost:8051/api/glb/v1/companies/6)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true
