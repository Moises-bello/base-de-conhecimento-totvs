---
content_hash: 38c0b54942a4179ac857958290d51a61e216391c4c5b4e0c2dd8c4ae2626004e
fetched_at: '2026-07-02T19:24:21.630762+00:00'
page_id: '268813153'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave ReleaseInactiveConn
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268813153
version: 4
---

Define um intervalo de inatividade, em segundos, para que uma conexão estabelecida do true ao SGBD seja desconectada automaticamente.

A informação contida neste documento aplica-se ao true, build 42.201410119 e superiores.

Para o SGBD MSSQL, deve ser utilizado o true Build 42.20161016 ou superior.

**Valores válidos:**

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita (padrão) |
| > 0 | Habilita intervalo de inatividade, valor informado em segundos. |

**Informações Adicionais**

* A conexão existente entre true e true permanece ativa, mesmo que o true tenha se desconectado do SGBD. Caso a aplicação AdvPL realize uma nova requisição através da conexão, o true vai reconectar-se automaticamente ao SGBD.
* Apenas são desconectadas por inatividade conexões que não estejam dentro de transação, e não tenham queries e tabelas temporárias abertas.
* Para o SGBD **MS SQL Server** não são desconectadas conexões que fizeram abertura de queries.

## Exemplo

No exemplo abaixo, configuramos um time-out de inatividade de conexão com o SGBD de 30 segundos.
