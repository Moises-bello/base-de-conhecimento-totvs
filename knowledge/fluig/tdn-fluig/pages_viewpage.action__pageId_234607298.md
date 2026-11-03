---
content_hash: 5491b41dd728a9cd9519146a45c9f3b93f4a3a8f7de77e2dc807fa916b77cf68
fetched_at: '2026-06-28T21:35:22.086676+00:00'
page_id: '234607298'
product: fluig
source: tdn-fluig
title: ARQ - Como resolver problema na autenticação via AD após queda de DNS secundário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234607298
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

**Ambiente:** Windows

# Ocorrência

Ao utilizar a autenticação da plataforma integrada com o Active Directory, estamos tendo um problema quando um DNS fica inacessível.

Na configuração do arquivo **standalone.xml** (a partir da atualização 2.0) ou **domain.xml** (da atualização 1.6 até 1.8.2), trecho *Authentication*, foram alteradas as informações para o nome do servidor do AD, que anteriormente apontavam para o endereço IP. A plataforma funciona normalmente, porém quando o DNS secundário fica fora, o acesso à plataforma é interrompido, informando que o usuário e senha são inválidos. Como fazer para que isso não aconteça?

# Solução

A partir do momento em que é configurada a autenticação via LDAP, a plataforma utilizará a senha do *Active Directory* para o acesso dos usuários. Contudo, só será possível realizar o login quando a conexão com o AD está disponível, do contrário será exibida mensagem de erro de usuário e senha inválidos.

Quando um DNS secundário cai, para a zona integrada ao *Active Directory*, é o mesmo que a queda de todo o DNS.

Você precisará configurar uma replicação de *Active Directory,* conforme observação da própria Microsoft em [Adicionando um servidor DNS secundário a uma zona](https://technet.microsoft.com/pt-br/library/cc816885(v=ws.10).aspx).
