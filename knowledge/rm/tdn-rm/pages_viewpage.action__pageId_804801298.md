---
content_hash: 54379336bd058ece0e5ee41f325a7858bc2b7869a182975a107b86859b35e651
fetched_at: '2026-06-29T00:11:43.376597+00:00'
page_id: '804801298'
product: rm
source: tdn-rm
title: Customização Novos portais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804801298
version: 7
---

Para realizar a customização dos portais é necessário realizar os seguintes passos:

* instalar e configurar o module federation no projeto no qual será feita a customização.
* instalar a biblioteca educational-custom, que foi criada para auxiliar na customização.

Deve ser verificado a versão do angular no qual o portal em que está realizando a customização se encontra, a versão do angular no projeto de customização deve ser o mesmo do portal. A versão do module federation deve ser seguir a versão do angular (<https://www.npmjs.com/package/@angular-architects/module-federation>).

Para configurar o projeto customizado executar os seguintes comandos:

1. npm install @angular-architects/module-federation@xx.x.x, onde o x deve ser substituído pela versão na qual é compatível com a versão do angular no projeto, ver <https://www.npmjs.com/package/@angular-architects/module-federation>. Por exemplo, para a versão 12 do angular, conforme a documentação, o x deve ser substituído por 12.0.0, ficando o comando assim: npm install @angular-architects/module-federation@12.0.0
2. ng add @angular-architects/module-federation
3. npm install @totvs/educational-custom --registry "<https://npm.totvs.io>"
