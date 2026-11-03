---
content_hash: c28f38505a201a22d101fa10c40015b49bd715068f0a34d1b8ae6780b5e28560
fetched_at: '2026-06-28T21:35:22.913469+00:00'
page_id: '242389332'
product: fluig
source: tdn-fluig
title: DES - Exemplo de utilização API Pública -  /social/community/addParticipants
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242389332
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Tipo de API:** API Pública

# Ocorrência

Veremos a seguir, um exemplo simples de utilização da API Pública da plataforma.

# Procedimentos

0.5falsesamplesfadetrue1Passo 1

Primeiramente, será necessário realizar download da extensão Advanced REST client, a mesma esta disponível na Chrome Store ([link](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=pt-BR)):

true2Passo 2

Em seguida, acesse o endereço http://[endereco\_fluig]:[porta]/api'. Será exibida a lista de API públicas disponíveis (vide imagem abaixo).

Para este exemplo, utilizaremos a API Communities.

true3Passo 3

 Localize o método /social/community/addParticipants e clique sobre a opção *Mount Point*:

true4Passo 4

Copie a URL exibida na barra de endereço do navegador:

Abra a extensão Advanced REST client e preencha os parâmetros, conforme exemplo abaixo:

Para facilitar, seguem os parâmetros informados na imagem acima:

xmltrue

true5Passo 5

Clique no botão *Send*:

Caso o procedimento tenha sido executado com sucesso, será exibido status: **200 OK**

Assim, os usuários devem ter sido adicionados na comunidade.
