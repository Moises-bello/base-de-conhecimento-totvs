---
content_hash: 8386a0e9826eba892dbd67e0efd69c1d17bb402295c9da9b5ab35372006564d1
fetched_at: '2026-06-29T00:10:19.258476+00:00'
page_id: '4813156'
product: rm
source: tdn-rm
title: Como Tornar um anexo de um cadastro Obrigatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813156
version: 4
---

BLOCK

Como Tornar um anexo de um cadastro Obrigatório

FAQ: **Como Tornar um anexo de um cadastro Obrigatório**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Avaliação

* **Introdução**

Em muitos cadastros existe a possibilidade de definir campos do cadastro como obrigatórios, porem em existe a necessidade de colocar alguns anexos também como obrigatórios. O intuído deste documento é mostrar como é possível colocar um anexo como obrigatório.

Solução

* ***Desenvolvimento/Procedimento***

Para melhor exemplificação iremos utiliza o anexo “Tributo do Produto”.

1. Acessar o menu Cadastro / Seguranças / Administrativa / Actions Anexas. Incluir um novo registro, informar na “Action Principal” o ID “EstPrdAction” – Produtos, na “Action Anexo” o ID “EstTrbPrdAction” - Tributos do Produto.

Acessar o menu Cadastro / Seguranças / Administrativa / Preferências de Anexos, onde serão apresentadas as abas de permissões gerais, por perfil e usuário. Escolha o tipo de permissão desejado e insira uma nova preferência, informando como ID de anexo da Action o ID cadastrado anterior, marcando a opção Obrigatória.

* **Informações Adicionais**

*- A inclusão obrigatória de um registro no anexo NÃO valerá para as situações:*

*Telas de exibição, ou seja, não são telas de cadastro*

*- Quando uma tela for Extended Action*

*Mas o que é uma tela Extended Action?*

*Extended Action é um anexo que NÃO é exibido como uma pasta, e sim como uma tela adicional que aparecerá sobre a tela .NET.*

*Todas as telas Extended Action serão apresentadas como links, listados em uma nova pasta Informações Adicionais, exibida na edição de uma tela .NET. Uma vez clicado no link, a tela Extended Action aparecerá sobre a tela .Net, permitindo suas configurações adicionais.*

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/09/como-fazer-como-tornar-um-anexo-de-um.html>
