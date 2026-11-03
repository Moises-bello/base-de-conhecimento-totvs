---
content_hash: 9b9342be430fda2afec1d95bd03d8e559dc6dd7923c4849f1710e2af8771ca19
fetched_at: '2026-06-29T00:10:16.014474+00:00'
page_id: '467766849'
product: rm
source: tdn-rm
title: DT PORTAL TOP - Instalação e Configuração do Portal TOP Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=467766849
version: 5
---

# MONITOR DE OBRAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Obras e Projetos. |
| **Função:** | Portal TOP Web |
| **Situação/Requisito:** | Instalação e configuração do Portal TOP Web. |
| **Solução/Implementação:** | * Executar a instalação do TOTVS RM Portal. * O portal deve ser acesso via endereço dentro do aplicativo FrameHTML:   + <http://localhost/web/app/prj/PortalTopWeb/index.html> * O instalador deve configurar o MIME Type .json automaticamente no IIS. * **Atenção:** Será necessário configurar **manualmente**:   + Instalar o componente **Rewrite** no IIS:     - <https://www.iis.net/downloads/microsoft/url-rewrite>   + Configurar o endereço da API utilizando a porta 8051 dentro do arquivo "\config\**config.json**"   + Inserir a tag "**DefaultDB**" no RM.Host.exe.config     - Não é necessário configurar a tag "ApiPort" que utiliza a porta 8051 por padrão) |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | [TOPORCAPLAN001-6827](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-6827) |
| **Requisito:** | [TOPORCAPLAN001-6796](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-6796) |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
