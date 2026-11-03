---
content_hash: 0f03ca9ef531c595f69f8df9fdbb2e71493250f10718f3097a25d1213438bfa5
fetched_at: '2026-06-28T21:35:22.893521+00:00'
page_id: '241701520'
product: fluig
source: tdn-fluig
title: DES - Erro ao tentar conectar no webservice durante a exportação de um formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=241701520
version: 3
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig Studio

# Ocorrência

Ao exportar um relatório do TDS ou Eclipse para a plataforma ocorre erro ao tentar conectar no webservice.

A mensagem completa é "Erro ao tentar conectar ao servidor. O servidor está inacessível ao cliente ou a conexão foi recusada".

# Causa

O erro está nas Configurações SOAP do servidor configurado no TDS ou Eclipse. Isso pode acontecer porque o plugin Fluig Studio não está na mesma atualização do que a plataforma no servidor.

# Solução

Verifique qual é a atualização da plataforma no servidor e em seguida verifique qual é a versão do plugin no TDS/Eclipse para saber se precisa atualizar.
