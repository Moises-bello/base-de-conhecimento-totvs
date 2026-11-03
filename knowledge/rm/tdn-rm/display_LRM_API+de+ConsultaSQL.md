---
content_hash: 455510641bcc0d0a8d2ec4ffcec26b054b008864456c57409f660106a3b021db
fetched_at: '2026-06-29T00:10:38.135015+00:00'
page_id: '543093560'
product: rm
source: tdn-rm
title: API de ConsultaSQL
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+ConsultaSQL
version: 24
---

# Sumário

---

10Sumário

# Objetivo

---

     Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

     Esta API irá retornar o resultado de uma consulta SQL cadastrada na base de dados.

# 1 - Métodos

---

     A API de ConsutltaSQL implementa somente o método GET.

# 1.1 - GET {codSentenca}/{codColigada}/{codSistema}

---

     1.1.1 - Get (Retorna todas as colunas da consulta Sql do sistema)

false1.1.1 GetfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/consultaSQLServer/RealizaConsulta/{codSentenca}/{codColigada}/{codSistema}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**codSentenca: 1.01**

**codColigada: 1**

**codSistema: A**

**Url Utilizada:** http://localhost:8051/api/framework/v1/consultaSQLServer/RealizaConsulta/1.01/1/A

falseExemplo de ResultadoVer resultado JSON...

[  
{  
"CHAPA": "00001",  
"NOME": "ITAMAR MENDES DA SILVEIRA",  
"CODHORARIO": "0020"  
},  
{  
"CHAPA": "00002",  
"NOME": "JOAO DA SILVA JORDAM",  
"CODHORARIO": "0004"  
},  
{  
"CHAPA": "00003",  
"NOME": "MARIA CONCEICAO DE ASSIS",  
"CODHORARIO": "0017"  
},  
{  
"CHAPA": "00004",  
"NOME": "ADALBERTO DE JESUS LIMA",  
"CODHORARIO": "0014"  
},  
{  
"CHAPA": "00005",  
"NOME": "ALESSANDRA LOPES DE ABREU",  
"CODHORARIO": "0007"  
},  
{  
"CHAPA": "00006",  
"NOME": "FERNANDO HENRIQUE VALLE KURTEN",  
"CODHORARIO": "0008"  
},  
{  
"CHAPA": "00007",  
"NOME": "JOAQUIM FARIAS DAMASCENO",  
"CODHORARIO": "0009"  
},  
{  
"CHAPA": "00008",  
"NOME": "ZELIA APARECIDA DA SILVA",  
"CODHORARIO": "0010"  
},  
{  
"CHAPA": "00009",  
"NOME": "BEATRIZ MENGA DA LUZ",  
"CODHORARIO": "0011"  
},  
{  
"CHAPA": "00010",  
"NOME": "ANTONIO GATES BILL",  
"CODHORARIO": "0001"  
},  
{  
"CHAPA": "00011",  
"NOME": "MARCELO MATTAR DINIZ",  
"CODHORARIO": "0006"  
},  
{  
"CHAPA": "00012",  
"NOME": "ANA LUIZA DE SOUZA PRATES",  
"CODHORARIO": "0012"  
},  
{  
"CHAPA": "00013",  
"NOME": "ALEXANDRE COTTA LEAO",  
"CODHORARIO": "0013"  
},  
{  
"CHAPA": "00014",  
"NOME": "PEDRO DE ALCANTARA",  
"CODHORARIO": "0002"  
},  
{  
"CHAPA": "00015",  
"NOME": "LEOPOLDO DOS SANTOS DE OLIVEIRA NETO",  
"CODHORARIO": "0015"  
},  
{  
"CHAPA": "00016",  
"NOME": "MURICIO DA CRUZ SOUTO",  
"CODHORARIO": "0001"  
},  
{  
"CHAPA": "00017",  
"NOME": "ENIO DA COSTA ANTUNES",  
"CODHORARIO": "0017"  
},  
{  
"CHAPA": "00018",  
"NOME": "TEREZA LIMA PEREIRA SOARES",  
"CODHORARIO": "0008"  
},  
{  
"CHAPA": "00019",  
"NOME": "ADRIANA TEIXEIRA LOBO",  
"CODHORARIO": "0002"  
},  
{  
"CHAPA": "00021",  
"NOME": "CARLOS ALBERTO MARRONE",  
"CODHORARIO": "0004"  
},  
{  
"CHAPA": "00036",  
"NOME": "FABIANO FRANCA MOREIRA",  
"CODHORARIO": "0001"  
}  
]

## 1.1.2 - Parameters(Parâmetros da sentença SQL)

Parâmetros

**Parameters:** parâmetro responsável pela execução da consulta, deve ser informado como URL encode.

**Exemplo:** ?parameters=CODCOLIGADA%3D0%3BCODCOLIGADA1%3D10

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/consultaSQLServer/RealizaConsulta/1/1/A/?parameters=CODCOLIGADA%3D0%3BCODCOLIGADA1%3D10

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**codSentenca: 1**

**codColigada: 1**

**codSistema: A**

**Url Utilizada:** http://localhost:8051/api/framework/v1/consultaSQLServer/RealizaConsulta/1/1/A/?parameters=CODCOLIGADA%3D0%3BCODCOLIGADA1%3D10

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Context (Contexto para execução da sentença SQL)

Contexto

As Sentenças SQL cadastradas na Coligada Global (coligada zero) são executadas levando em consideração todas as coligadas que o usuário possui permissão.

Exemplo: Um usuário possui permissão na coligada 1 e na coligada 2 e possui filtro por perfil cadastrados em ambas as coligadas.  Ao executar uma sentença da Coligada Global o sistema irá restringir o resultado de acordo com os filtros cadastrados em ambas as coligadas.

Caso o usuário queira restringir o resultado levando em consideração apenas uma coligada específica, basta informar a coligada no contexto conforme mostrado abaixo.

**Context:** contexto para execução da sentença SQL, deve ser informado como URL encode.

**Exemplos:**

http://{domínio}:{porta}/api/framework/v1/consultaSQLServer/RealizaConsulta/1/0/A/**?context=CODCOLIGADA%3D1**

http://{domínio}:{porta}/api/framework/v1/consultaSQLServer/RealizaConsulta/1/0/A/?parameters=chapa%3D00001**&context=CODCOLIGADA%3D1**

http://{domínio}:{porta}/api/framework/v1/consultaSQLServer/RealizaConsulta/1/0/A/**?context=CODCOLIGADA%3D1**&parameters=chapa%3D00001

Importante saber que:

* Sentenças SQL cadastradas em uma coligada específica, por exemplo Coligada 1, sempre será executada no contexto da Coligada 1 mesmo que seja informada uma outra coligada no contexto.
* Sentenças SQL cadastradas na Coligada Global será executada preferencialmente na coligada informada no contexto.

Na dúvida consulte o quadro a seguir:

| Coligada da Sentença SQL | Coligada informada no Contexto | Coligada que será Considerada |
| --- | --- | --- |
| 0 | null | 0 |
| 0 | 1 | 1 |
| 1 | null | 1 |
| 1 | 2 | 1 |

Versões:

Disponível a partir das versões 12.1.31.260. 12.1.32.205, 12.1.33.127 e 12.1.34
