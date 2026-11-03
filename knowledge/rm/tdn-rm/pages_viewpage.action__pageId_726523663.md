---
content_hash: 15e1ab6680fc17f5b3fa310a6d3097797f9a9be96a8d2938e1cf9f1fd70cf4e1
fetched_at: '2026-06-29T00:11:27.541610+00:00'
page_id: '726523663'
product: rm
source: tdn-rm
title: Parametrização do perfil de acesso ao App
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=726523663
version: 17
---

Foi criado uma TAG  específica para comunicação entre o App e o ERP, onde o acesso e a sincronização do aplicativo estarão condicionados pela autorização do parâmetro de atributo de acesso "App Minha Contagem de Estoque".

Para configurar acesse Serviços Globais/Segurança/Perfil selecione o usuário,  entre em Acesso a Menus em seguida Estoque/Inventário, por ultimo habilite a TAG "App Minha Contagem de Estoque", conforme tela abaixo:

Caso a TAG esteja desabilitada o usuário conseguirá acessar o App, mas não será possível receber os inventários para realização da contagem e também não enviará para o ERP as contagens realizadas.

Será apresentando a mensagem abaixo:

Aviso:

O usuário logado não tem privilégios suficientes para efetuar essa operação.
