---
content_hash: 61cb930dd0283741e77d61a05b22ba22acad336f4198f5a42dbb35df30c98f8b
fetched_at: '2026-06-29T00:11:48.829553+00:00'
page_id: '828422650'
product: rm
source: tdn-rm
title: 17. Desinstalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828422650
version: 7
---

Ao desinstalar o app EduFlow, o próprio sistema operacional (IOS ou Android) fica encarregado de limpar os dados do aplicativo (Banco de dados, preferences) e qualquer pasta criada dentro da raiz do aplicativo.

Em Fevereiro de 2024, pesquisamos se existe algum gatilho que, quando o usuário desinstalar o app, execute algum serviço, para forçar limpar todos os dados do app, para que numa próxima instalação, não venha nenhum dado em cache, porém, não tivemos sucesso. Para IOS, não existe nenhuma opção que faça tal alção. Já para android, as opções que tinham estão obsoletas e funcionavam apenas pra android anterior ao 5.0, pois o google aumento o nível de segurança em cima da intent ACTION\_PACKAGE\_REMOVED.

Também tentamos utilizar o pacote flutter  app\_install\_events, porém, também não obtivemos sucesso, já que por debaixo dos panos , ele usa a intent ACTION\_PACKAGE\_REMOVED.
