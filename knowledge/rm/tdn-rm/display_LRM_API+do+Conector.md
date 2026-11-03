---
content_hash: 14e264085b9c5f7aceda93be29b68e177854d589450859eff0c771859e745b12
fetched_at: '2026-06-29T00:11:38.270065+00:00'
page_id: '782330051'
product: rm
source: tdn-rm
title: API do Conector
type: documentation
url: https://tdn.totvs.com/display/LRM/API+do+Conector
version: 6
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
* PATCH
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os conectores)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - GetOne (Recuperar conector pelo Identificador)

---

false1.1.2 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 3

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors/3>

js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um conector)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar um conector)

---

false1.3.1 PutfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 3

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors/3>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - PATCH

---

## 1.4.1 - Patch (Altera algumas propriedades de um conector)

---

false1.4.1 PatchClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 3

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors/3>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.5 - DELETE

---

## 1.5.1 - Delete (Deletar um conector)

---

false1.5.1 DeleteClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 3

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors/3>

falseResultado esperado

Será retornado o respondeCode = 204 e a resposta em branco.
