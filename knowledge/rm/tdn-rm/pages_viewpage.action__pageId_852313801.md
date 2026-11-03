---
content_hash: 1e6bdceb0c10a86c764310f8bcaa2b8e5824c535a30fc2ca7fdc0f2efb97386c
fetched_at: '2026-06-29T00:11:53.831053+00:00'
page_id: '852313801'
product: rm
source: tdn-rm
title: Preparando o Ambiente (SQL)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852313801
version: 5
---

**1.** Primeiramente baixe o **Sql Server** <https://learn.microsoft.com/pt-br/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16#download-ssms>                                                     **2.** Todas essas configurações tem que está habilitadas no **SQL Configuration.**

---

**3.** Agora abra o **Sql Server** e deixe a configuração conforme a imagem, **OBS:** o nome da maquina é individual de cada DEV, escreva 'hostname' no **CMD** para saber o seu.

---

**4.** O acesso na maquina está pronto, mas para entra na linha RM da Totvs temos que habilitar e modificar algumas configurações do SQL.

---

**5.** Acesse essas configurações e deixa a senha de acordo com o nome do usuário. O usuário e senha rm é somente um exemplo, o ideal seria acessar com **usuário e senha  'sa'**.

---

**6.** Em sequência acessar usando a autenticação do SQL.

---

**7.** Depois de acessar no login 'sa', abra o seguinte Script, Gere uma nova query no banco e cole esse script já configurado no banco desejado, com isso finalizamos a configuração do SQL.

400
