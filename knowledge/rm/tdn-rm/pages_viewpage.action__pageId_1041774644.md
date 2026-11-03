---
content_hash: cc32ed1d5c00ad35557a79fa0bca04dbd63e5dbe8d11cc25a3d4d13632dc7a86
fetched_at: '2026-06-29T00:05:49.809723+00:00'
page_id: '1041774644'
product: rm
source: tdn-rm
title: 6- Customizar o título que é exibido na aba do browser
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1041774644
version: 2
---

O título que é exibido na aba do browser é o texto que está cadastrado na expressão **appName** que está localizado nos arquivos de expressões na pasta assets\i18n. Para customizar o título que é exibido basta alterar esse texto para o desejado.

Caso deseje que no título também seja exibido o nome da página que o usuário está acessando no momento, basta editar o arquivo **config.json** e adicionar a tag **showRouteNameTitle** com o valor **true**. Quando essa tag está adicionada ao arquivo config.json com o valor true, o nome da página corrente é exibido no título concatenada com o texto que está na expressão **appName.**

Exemplo: vamos supor que a expressão appName esteja com o texto Portal do professor e o usuário esteja acessando o recurso de avaliações, então será exibido no título: Portal do professor - Avaliações.
