---
content_hash: ac8a2e4d738ce62bbbf39ffc76f3b5f1bd8c21846bbaddfc336214a03ae4acf9
fetched_at: '2026-06-29T00:11:38.071361+00:00'
page_id: '781210167'
product: rm
source: tdn-rm
title: API de Conflitos
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Conflitos
version: 2
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

Para mais informações sobre consumo de Licença, [veja aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=419548455#APIsdeFrameworkM%C3%B3duloServi%C3%A7osGlobais-5-ConsumodeLicen%C3%A7aspeloLicenseServer).

# 1 - Métodos

---

Serão apresentados 4 métodos, os quais foram implementados na API de Riscos, são eles:

* GET
* POST
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os conflitos)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/conflicts

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada:** 7

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/conflicts>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - GetOne (Recuperar conflito pelo Identificador)

---

false1.1.2 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/conflicts/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada:** 7

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/conflicts/7>

js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um conflito)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/conflicts

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada:** 7

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/conflicts>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar um conflito)

---

false1.3.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/conflicts/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada:** 7

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/conflicts/20>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - DELETE

---

## 1.4.1 - Delete (Deletar um conflito)

---

false1.4.1 DeleteClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/company/{Id da coligada}/conflicts/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Coligada:** 7

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/company/7/conflicts/20>

falseResultado esperado

Será retornado o respondeCode = 204 e a resposta em branco.
