---
content_hash: b5646139f32f84b41cfc77c4fb832c175bb465e26a28ca620ccaa344030e33f1
fetched_at: '2026-06-29T00:05:59.034847+00:00'
page_id: '189307580'
product: rm
source: tdn-rm
title: TBC - Exemplo Web Service Consulta SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/TBC+-+Exemplo+Web+Service+Consulta+SQL
version: 21
---

**Introdução**

---

      Este serviço disponibiliza acesso direto as consultas SQL do sistema.

**Como funciona**

---

**1)** Para o uso deste serviço, é necessário uma consulta SQL. Neste exemplo teremos uma consulta simples que é necessário dois parâmetros para execução da mesma, como mostra abaixo. Para mais informações como criar uma consulta SQL no RM [clique aqui](https://tdn.totvs.com/display/public/LRM/Trabalhando+com+Consultas+SQL).

sqlSQL

**2)** Logo após selecionarmos a consulta SQL, devemos configurar o serviço em um aplicativo para que possamos consumir o mesmo. Após configurado, é necessário passarmos os parâmetros para termos acesso ao resultado da consulta, como mostra abaixo.

xmlXML




wsConsultaSQL

1

G

CODSISTEMA=G;NOMESISTEMA=RM BIS;
]]>

**Observações:** Conforme no Bloco de Código acima temos de informar os dados da consulta. Onde *"CodSentenca"* é o código da consulta SQL, *"codColigada"* é o código da coligada onde está a consulta, *"codSistema"* é o contexto de onde a consulta foi criada, *"parameters"* são os parâmetros da consulta(se a consulta possuir).

Informando os Parâmetros Corretamente

Ao informar um parâmetro tem que respeitar a ordem do nome e dos valores de acordo com o SQL criado para que possa trazer os dados corretamente do retorno SQL.

SELECT \*  
FROM GSISTEMA (**NOLOCK)**  
WHERE **CODSISTEMA =:CODSISTEMA** **//Primeiro parâmetro**  
AND **NOMESISTEMA =:NOMESISTEMA** **//Segundo parâmetro**

**//Primeiro parâmetro**

| Nome | Valor |
| --- | --- |
| **CODSISTEMA** | **G** |

**//Segundo parâmetro**

| Nome | Valor |
| --- | --- |
| **NOMESISTEMA** | **RM BIS** |

**<tot:parameters>CODSISTEMA=G;NOMESISTEMA=RM BIS;</tot:parameters>**

ATENÇÃO

Caso seja informado a ordem invertida dos campos e valor terá erros no retorno da consulta.

Se conter Espaços na Frente dos Parâmetros também retornara erro no retorno da consulta.

**3)** Após ser configurado e passado todos os parâmetros necessários, temos enfim o resultado da consultaSQL, como mostra no código abaixo.

xmlRAW




RB
RM BIS
1
9999
-32305
G
11.0.0.7
12.1.2302.0
TOTVS Inteligência de Negócios
507
0
RM
2014-07-07T15:32:15
totvs-upg
2023-01-04T04:24:06
]]]]>
]]>

---

**Para utilização dos Web Services através do aplicativo "Totvs Web Service Test", clique [aqui](http://tdn.totvs.com/x/yBdFCg).**

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 12.1.2302 |
| **Processo** | Web Services |
| **Subprocesso** | Utilizando WsConsultaSQL |

|  |  |
| --- | --- |
| Status do Documento: | Finalizado |
| Data: | 17/01/2023 |
| Versão: | 12.1.2302 |
| Versão Anterior: | 12.1.34 |
| Autores: |  |
