---
content_hash: 32c335d597b62dd470c0472dd72b55b823e6ee61d8db7fc20a42bc08c3292b2b
fetched_at: '2026-06-29T00:11:38.277890+00:00'
page_id: '782330052'
product: rm
source: tdn-rm
title: API de Arquivos
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Arquivos
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

Serão apresentados 4 métodos, os quais foram implementados na API de Arquivos, são eles:

* GET ALL
* GET (download do arquivo)
* POST (upload do arquivo)
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os arquivos do conector específico)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/connectors/{{connectorId}}/files

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/connectors/1/files>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Download (Baixar arquivo pelo identificador)

---

false1.1.2 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/files/{{id}}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/files/20>

js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Fazer upload de um arquivo)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/files

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/files>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - DELETE

---

## 1.3.1 - Delete (Deletar um arquivo)

---

false1.3.1 DeleteClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/filerepo/files/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 20

**Url Utilizada:** <http://localhost:8051/api/framework/v1/filerepo/files/20>

falseResultado esperado

Será retornado o respondeCode = 204 e a resposta em branco.
