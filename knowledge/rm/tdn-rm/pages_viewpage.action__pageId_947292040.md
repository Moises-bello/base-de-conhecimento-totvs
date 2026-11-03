---
content_hash: 27c9ce30388fd21045d1da565726b95b3388dca27483c32c525e197238ca6989
fetched_at: '2026-06-29T00:12:09.504073+00:00'
page_id: '947292040'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Segurança no PDC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=947292040
version: 4
---

A partir do Release 12.1.2506 e dos Patchs Específicos expedidos a partir de 28/06/2025, é possível de se habilitar uma camada de proteção extra na recuperação de senha do login do Portal do Cliente - PDC.

Para realizar esta ação edite o arquivo *Web.config*, localizado na pasta FRAMEHTML, da instalação do RM, geralmente em *C:\TOTVS\CorporeRM*.

Localize a tag *StackTraceVisible* e verifique se ela está configurada para false. Caso não esteja altere-a para este valor:

Com esta alteração, caso ocorra algum erro na Recuperação de Senha do PDC, o sistema exibirá ao usuário apenas a mensagem de erro abaixo, sem expor nenhum dado técnico ao mesmo, conforme imagem abaixo:

*"E-mail não encontrado. Verifique e tente novamente."*
