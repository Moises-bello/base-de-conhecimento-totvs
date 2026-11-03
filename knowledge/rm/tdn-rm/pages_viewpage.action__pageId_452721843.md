---
content_hash: 83393d26c5658b048aee3c4f91c99469c8555696e4373a226590e0ac73e7bc48
fetched_at: '2026-06-29T00:10:11.684513+00:00'
page_id: '452721843'
product: rm
source: tdn-rm
title: Parametrização do GED - API  de Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452721843
version: 5
---

# Sumário

---

Sumário

# Objetivo

---

     Esse documento tem o objetivo de exemplificar o uso da API de Parâmetros para configurar o GED.

# 1 - Método

---

     Para configurar o GED será usada a . Nessa API, é necessário utilizar o filtro "group.name" para informar qual servidor de parâmetros a API irá utilizar para apresentar os parâmetros.

     O group.name para configurar o GED é: ConParametrosData.

false

* A propriedade systemParameterId é composta pelo group.CustomData|parameterCode, onde group.CustomData é o parâmetro (HCPARAMETROS.NOMECOLUNA) e parameterCode é o campo a ser alterado do parâmetro.

     A tabela que armazena os dados do GED é a HCPARAMETROS. O filtro group.customData deve ser preenchido com o valor do campo HCPARAMETROS.NOMECOLUNA desejado. Veja alguns exemplos abaixo.

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar os parâmetros do GED)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name=ConParametrosData&group.customData={{parametro}}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url's Utilizada:**

* [http://localhost:8051/api/framework/v1/systemParameters?group.name=ConParametrosData&group.customData=GED\_SERVIDOR](http://localhost:8051/api/glb/v1/system-parameters?group.name=ConParametrosData&group.customData=GED_SERVIDOR)
falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

     Alguns parâmetros do GED são alterados pelo campo HCPARAMETROS.VALORSTR, outros devem ser armazenados no campo HCPARAMETROS.VALORINT.

     Parâmetros a serem atualizados em HCPARAMETROS.VALORINT:

* GED\_ATIVA\_INTEGRACAO\_FLUIG
* GED\_ATIVACERTIFICACAOVISAO
* GED\_COD\_PASTA\_RAIZ
* GED\_CODEMPRESA
* GED\_FLUXOAPROVACAOVISAO
* GED\_TIPOLOG

     Parâmetros a serem atualizados em HCPARAMETROS.VALORSTR:

* GED\_COD\_GRUPO\_USUARIO
* GED\_MATRICULA
* GED\_PORTA
* GED\_PORTA\_FTP
* GED\_SENHA
* GED\_SERVIDOR
* GED\_TIPO\_PROTOCOLO
* GED\_USUARIO
* GED\_USERPASSWORD

## 1.2.1 - Post (Atualiza o valor de um parâmetro)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters](http://localhost:8099/api/rm/glb/v1/systemParameters)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualiza o valor do parâmetro)

---

false1.3.1 PostfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters/{systemParameterId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** GED\_SERVIDOR|HCPARAMETROS.VALORSTR

**Url Utilizada:** http://localhost:8051/api/framework/v1/systemParameters/GED\_SERVIDOR|HCPARAMETROS.VALORSTR

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)true
