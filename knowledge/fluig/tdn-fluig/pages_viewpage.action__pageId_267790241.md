---
content_hash: 9870848135ac533b2ac65e087e5ea73161a857f4f10d3f99fe9919e6bd3e1d4f
fetched_at: '2026-06-28T21:35:23.893330+00:00'
page_id: '267790241'
product: fluig
source: tdn-fluig
title: DES - Como acessar o banco do Protheus através de uma página pública?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267790241
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Preciso desenvolver uma pagina pública, mas precisarei disponibilizar uma tabela do Protheus ou parte dela. Ex.: Alguns produtos.

Como faço para esta página pública acessar o banco do Protheus? Preciso de algum banco intermediário ou esse acesso pode ser direto?

Observação: WS Soap, Banco e TOTVS Fluig Plataforma em servidores separados

# Solução

Orientamos desenvolver uma widget dentro da página pública. Este irá recuperar os dados de um dataset, que será alimentado por algum Web Service, que consumirá dados do banco do Protheus.

É de grande importância ter total domínio no desenvolvimento e experiência no acesso de dados a bancos, pois um filtro mal desenvolvido pode acarretar em diversos problemas de performance visto que é uma página pública e vários usuários podem estar acessando e requisitando informações do Protheus simultaneamente, o que poderia até derrubá-lo.
