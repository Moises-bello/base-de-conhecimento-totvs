---
content_hash: 0ff81a8090fea24b117ac4f60a99eb571a8a677a38c277142be79ca36cd2776a
fetched_at: '2026-06-29T00:11:38.059260+00:00'
page_id: '781209727'
product: rm
source: tdn-rm
title: API de Riscos
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Riscos
version: 3
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

Serão apresentados 4 métodos, os quais foram implementados na API de Riscos, são eles:

* GET
* POST
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os riscos)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/risks

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada**: 7

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/risks>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

1.1.1.2 - Order (Resultado Ordenado)

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

false1.1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/glb/v1/framework/v1/sod-matrix/company/{Id da coligada}/risks?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada**: 7

**Campo:** active

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/risks?order=-alertId>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - GetOne (Recuperar risco pelo Identificador)

---

false1.1.2 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/risks/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada**: 7

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/risks/20>

js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um risco)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/risks

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada**: 7

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/risks>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar um risco)

---

false1.3.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/risks/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada**: 7

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/risks/20>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - DELETE

---

## 1.4.1 - Delete (Deletar um risco)

---

false1.4.1 DeleteClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/risks/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada**: 7

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/risks/20>

falseResultado esperado

Será retornado o respondeCode = 204 e a resposta em branco.
