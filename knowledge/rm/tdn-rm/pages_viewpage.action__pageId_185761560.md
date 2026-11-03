---
content_hash: cc6e874b159009283c2691fc7c89c2044882506db2546609aeaeba91dca3d366
fetched_at: '2026-06-29T00:05:58.417067+00:00'
page_id: '185761560'
product: rm
source: tdn-rm
title: 1. Configuração do RM Host
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185761560
version: 4
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso.

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

O serviço que disponibiliza o acesso aos dataservers do CorporeRM via REST utiliza o alias do banco de dados definido na tag **DefaultDB**. Portanto, para a ativação desse serviço é necessário que esta tag esteja definida. Todos as chamadas aos serviços Rest serão autenticadas com o usuário e senha definidos nas tags **FrameHTMLUser** e **FrameHTMLPassword**caso não sejam informados, o serviço retornará uma mensagem de erro solicitando os mesmos.

# Exemplo do RM.Host.exe.config

]]>
