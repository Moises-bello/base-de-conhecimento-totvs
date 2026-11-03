---
content_hash: c7e02e0b0ce7137a8033d5b6062e178b4c4bf6b82a2300bb7297475951076f3c
fetched_at: '2026-06-28T21:35:19.098307+00:00'
page_id: '190515881'
product: fluig
source: tdn-fluig
title: ARQ - A plataforma reinicia intermitentemente e fica indisponível durante o
  tempo de reinicialização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190515881
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Ambiente:** Windows

**Banco de Dados:** SQL Server

# Ocorrência

O serviço da plataforma reinicia intermitentemente e o sistema fica indisponível durante o tempo de reinicialização.

# Causa

A plataforma pode ter perdido a conexão com o banco de dados e até a conexão ser restabelecida o sistema fica indisponível.

# Solução

0.5falsesamplefadetrue1A partir da 2.0

* Acesse o servidor da plataforma e navegue até a pasta de instalação;

* Acesse [diretório\_instalação]\appserver\standalone\log;

* Edite o arquivo **server.log** e procure por "**Could not create connection**";

* Se o problema for de conexão com o banco de dados SQL Server, o erro será parecido com o exemplo a seguir:

javaLog "Could not create connection"true

Nesse caso:

* Verifique se as propriedades de conexão com o banco de dados foram alteradas (em caso positivo, é necessário alterar em [diretório\_instalação]\appserver\standalone\configuration\standalone.xml);

* Certifique-se de que uma instância do SQL Server esteja rodando no host e aceitando conexões TCP/IP na porta;

* Certifique-se também de que as conexões TCP na porta não estejam bloqueadas pelo firewall.
21.6 até 1.8.2

* Acesse a pasta de instalação da plataforma;

* Acesse [diretório\_instalação]\appserver\domain\servers\[fluig server]\log;

* Edite o arquivo **server.log** e procure por "**Could not create connection**";

* Se o problema for de conexão com o banco de dados SQL Server, o erro será parecido com o exemplo a seguir:

javaLog "Could not create connection"true

Nesse caso:

* Verifique se as propriedades de conexão com o banco de dados foram alteradas (em caso positivo, é necessário alterar em [diretório\_instalação]\appserver\domain\configuration\domain.xml);

* Certifique-se de que uma instância do SQL Server esteja rodando no host e aceitando conexões TCP/IP na porta;

* Certifique-se também de que as conexões TCP na porta não estejam bloqueadas pelo firewall.
31.5.13 e anteriores

* Acesse o servidor da plataforma e navegue até a pasta de instalação da plataforma;

* Acesse jboss\standalone\log;

* Edite o arquivo **server.log** e procure por "**Could not create connection**";

* Se o problema for de conexão com o banco de dados SQL Server, o erro será parecido com o exemplo a seguir:

javaLog "Could not create connection"true

Nesse caso:

* Verifique se as propriedades de conexão com o banco de dados foram alteradas (em caso positivo, é necessário alterar em [diretório\_instalação]\jboss\standalone\configuration\standalone.xml);

* Certifique-se de que uma instância do SQL Server esteja rodando no host e aceitando conexões TCP/IP na porta;
* Certifique-se também de que as conexões TCP na porta não estejam bloqueadas pelo firewall.
