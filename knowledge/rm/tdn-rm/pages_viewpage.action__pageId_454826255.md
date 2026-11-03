---
content_hash: 72ae3422ec2868cd104d4e3a9b3a4951064644776b1f8af6c95d6ab8b3bc8192
fetched_at: '2026-06-29T00:10:12.495843+00:00'
page_id: '454826255'
product: rm
source: tdn-rm
title: Validação de Requisições do ASP.NET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454826255
version: 2
---

Um dos recursos inerentes ao ASP.NET referente à segurança é a Validação do Conteúdo das Requisições. Simplificando todas as questões técnicas, esse recurso visa impedir que sejam enviados conteúdos potencialmente perigosos nos formulários de aplicações ASP.NET, como URLs, Marcações HTML, Scripts, etc.

Mais detalhes em: <https://docs.microsoft.com/pt-br/aspnet/whitepapers/request-validation>

Por padrão, o arquivo Web.Config do TOTVS RM Portal possui com a seguinte seção:

xml
...]]>

Conforme visto no artigo citado anteriormente, essa opção faz o controle do conteúdo das requisições para todo o TOTVS RM Portal. Portanto, **desligá-la**, isto é, **alterar o seu valor para *false*** é uma opção que afeta a segurança.

## Páginas do TOTVS RM Portal que precisam deste recurso

Algumas páginas do TOTVS RM Portal precisam permitir o envio de valores que podem ser bloqueados pela validação padrão do ASP.NET exibindo uma mensagem de erro. Estas páginas são: Cadastro de WebParts e Cadastro de Notícias.

A partir da versão 12.1.24, não será mais necessário desligar a validação de conteúdo para todo o portal, pois foram feitas melhorias nas páginas citadas para que enviem corretamente as informações.

Nas versões 12.1.22.XXX e 12.1.23.XXX também foram feitas as melhorias nas páginas, mas como o arquivo web.Config não é distribuído nos Patches, é preciso fazer uma pequena alteração em outra seção do arquivo:

Onde encontra-se:

xml

Deve-se alterar para:

xml
