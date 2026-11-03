---
content_hash: 42ba3415689941bb2a81b2aeb886ce363148e4993e6a43ce6265d497d96dcfc9
fetched_at: '2026-06-28T21:35:25.831531+00:00'
page_id: '315906495'
product: fluig
source: tdn-fluig
title: DES - Na consulta de dataset offline pelo mobile, os valores retornam 'null'
  ou 'undefined'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315906495
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Percebemos que, se na declaração dos campos de um dataset, a grafia do nome dos campos está em minúsculo, o dataset é consumido normalmente na web ou no mobile online. Porém, quando consumindo no mobile jornalizado (*offline*) temos que usar o nome dos campos em maiúsculo para que a consulta não retorne 'null'.

Neste cenário, o que podemos fazer para sempre retornar os valores corretos?

# Solução

Esse comportamento ocorre em virtude da criação das tabelas no banco de dados, que por padrão utiliza as colunas com nomes todo em maiúsculo. Em alguns pontos do desenvolvimento sobre a plataforma é possível que as colunas sejam acessadas somente usando a definição do nome da mesma no banco de dados, ou seja, todo em maiúsculo.

Para evitar esta situação é sugerido que a definição das colunas **seja sempre** **em maiúsculo**, assim indiferente de onde realizemos a consulta, estará sempre respeitando o “padrão“.

Veja os exemplos abaixo:

Note que nesta forma de definição, os campos estão em **minúsculo** portanto, ****não recomendada**:**

jsEclipse

**Recomendamos** a definição das colunas de forma padronizada, com caracteres em **MAIÚSCULO,** veja:

jsEclipse

**Indiferente da funcionalidade usada, o acesso a coluna será sempre da mesma forma e, por esse motivo, é importante que a definição e a consulta estejam padronizadas.**

Confira abaixo o exemplo de **acesso a coluna via desenvolvimento sobre a plataforma**, que funcionará tanto na web quanto no mobile, online e offline:

jsEclipse
