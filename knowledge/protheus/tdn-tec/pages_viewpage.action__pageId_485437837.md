---
content_hash: 2f088662c820489202c26c79da7d8b829005710c8c68d314640a2a3b1a2e7282
fetched_at: '2026-07-02T19:24:24.276908+00:00'
page_id: '485437837'
product: protheus
source: tdn-tec
title: Begin TopClient Thread (<dbaccess-thread-id>,<appserver-ip>,<database>/<datasource-name>,<user-logged-os/renamed-user-protheus>,<user-logged-os>,<hostname>,DBApi
  <from-dbapi-version>)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485437837
version: 1
---

INLINE

A mensagem é registrada quando uma conexão foi estabelecida entre o servidor de aplicação e o gateway do banco de dados.

| Parâmetro | Descrição |
| --- | --- |
| <dbaccess-thread-id> | Corresponde ao processo interno do true que atende àquela conexão. |
| <appserver-ip> | Corresponde ao endereço IP de origem, o IP do true. |
| <database>/<datasource-name> | Corresponde ao ambiente que será utilizado para o acesso ao banco de dados (banco de dados e nome da fonte de dados). |
| <user-logged-os/renamed-user-protheus> | Corresponde ao usuário que solicitou a conexão ao banco de dados através do true. Por padrão, o nome do usuário da sessão do sistema operacional. |
| <user-logged-os> | Corresponde ao nome do usuário da sessão do sistema operacional cuja aplicação solicitou a conexão ao banco de dados através do true. |
| <hostname> | Corresponde ao nome da estação do usuário que solicitou a conexão ao banco de dados. |
| DBApi <from-dbapi-version> | Corresponde a versão da DBAPI utilizada na conexão com o true. |

 A informação que mais utilizamos neste contexto é a <dbaccess-thread-id>, pois qualquer mensagem relacionada a este processo será registrada juntamente a esse valor enquanto ele estiver sendo executado, ao ser registrado no dbconsolel.log, vai informar o número da <thread> ao qual a ocorrência pertence.
