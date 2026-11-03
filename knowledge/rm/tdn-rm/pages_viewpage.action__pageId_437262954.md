---
content_hash: 79e68540352002945e76558c7899dbc38c1dac73dc38c7d3628d535bcc2dcb34
fetched_at: '2026-06-29T00:09:51.799787+00:00'
page_id: '437262954'
product: rm
source: tdn-rm
title: 4319987 PORTALMOBILE01-6179 DT Customização de rota para login externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437262954
version: 2
---

# Customização de rota para login externo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | TOTVS Educacional. |
| **Módulo:** | Corpore.Net. |
| **Função:** | Login. |
| **Situação/Requisito:** | Para fazer login externo o corpore net não fazia o caminho correto para que o login externo funcionasse. |
| **Solução/Implementação:** | Foram criadas tags no Web Config para o Login Externo.  **Web.Config da FrameHTML:** <!-- Indica a URL do portal [Corpore.NET](http://corpore.net/) utilizado para efetuar login através da FrameHTML. Se existir esta tag no web.config, não será utilizado a parametrização realizada no RM.exe. --> <!-- <add key="UrlCorporeNet" value="<http://localhost/Corpore.Net/>" />  **Web.Config da pasta Public do [Corpore.Net](http://corpore.net/)****:** <!-- Indica a URL da FrameHTML no qual será redirecionado após o login efetuado no [Corpore.Net](http://corpore.net/). Se existir esta tag no web.config, não será utilizado a parametrização realizada no RM.exe. --> <!-- <add key="UrlFrameHTML" value="<http://localhost:8020/>" /> -->. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
