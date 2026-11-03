---
content_hash: f119a5d68c9b6e9c02c1ae505890305659357d89f23593ab596c27a76496f33a
fetched_at: '2026-06-28T21:35:19.369691+00:00'
page_id: '201751064'
product: fluig
source: tdn-fluig
title: ARQ - Como alterar a porta de acesso na atualização 1.5.13 ou anterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201751064
version: 15
---

Atenção

Esta página foi revisada para considerar as configurações para a atualização 1.5.13 e anteriores.

Caso possua uma atualização 1.6 ou superior, acesse: .

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.13 e anteriores

# Ocorrência

Como faço para alterar a porta de acesso ao TOTVS Fluig Plataforma nas versões anteriores a 1.6?

# Solução

Para alterar a porta de acesso siga os seguintes passos:   
  
1- Logar com o wcmadmin e editar a URL de acesso, em configurações do sistema.   
2 - Parar os serviços (FLUIG, MemCached, RealTime).   
3 - Verificar dentro dos arquivos abaixo o nome do servidor e da porta antiga e mudar para a nova:

**[diretório\_instalação]\jboss\standalone\configuration\standalone.xml**

 Parâmetros a ser alterados:

xml 


]]>

**[diretório\_instalação]\jboss\solr\solr.xml**

 Parâmetros a ser alterados:

* hostPort = "PORTA"

Se o servidor de Indexação (Solr) estiver hospedado em um servidor diferente da plataforma, não altere o parâmetro hostPort no arquivo solr.xml.

# Observações

Caso seu ambiente seja integrado com o Identity você precisa alterar a URL de acesso também lá, após realizar essa alteração deve-se entrar novamente com o wcmadmin, ir em autenticação, realizar teste de conexão novamente e salvar as informações, assim ele vai atualizar os dados.
