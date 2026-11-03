---
content_hash: d24f5b25238ca0cec33c1046dd7db2ad0d6ecbd3024004015b6912c580c3ae10
fetched_at: '2026-06-29T00:11:12.647650+00:00'
page_id: '656059023'
product: rm
source: tdn-rm
title: Arquitetura e Portabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquitetura+e+Portabilidade
version: 8
---

O documento de Portabilidade e Arquitetura possui orientações de configurações do ambiente que devem ser utilizadas em sua empresa, buscando o melhor desempenho e usabilidade do sistema. As informações contidas neste documento têm como objetivo apresentar, principalmente, quais as versões que devem ser utilizados para correto funcionamento do Portal de Imóveis. 

#ff9000Componentes de SO

Servidor WEB (APACHE ou IIS), por padrão a ferramenta é instalada no IIS. Neste servidor devemos ter:

* PHP versão 7.3.17 ou superior
* OBS: obrigatoriamente o PHP deve ficar instalado na pasta c:\TOTVS\php
* PHP Manager 1.2 ou superior
* URL Rewrite 2.0 ou superior
* SQL Server Native Cliente 12.0 (se banco for sql server)
* Microsoft C++ Redistributable 2015 update 3RC ou superior
* Microsoft ODBC Driver para SQL Server para php 7.
#ff9000Banco de dados

O produto funciona com SQL Server 2012 ou superior ou MySQL 8.0 ou superior. Os scripts de criação destes bancos de dados ficam na pasta de instalação do PVI conforme caminho abaixo:

* C:\TOTVS\FrameHTML\web\app\Imb\PVI\db (se instalação for no Windows)
#ff9000CORS

 A comissão 2.0 no Portal de Imóveis utiliza os recursos do RM.Host, para isso, habilitamos o Compartilhamento de recursos com origens diferentes ([CORS](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS)). Por padrão, essas configurações do CORS estarão liberadas integralmente no Portal de Imóveis a partir da versão 12.1.2205. Caso seja necessário bloquear algumas destas configurações, o Web.config do portal de imóveis na pasta /PVI/api, deverá ser alterado.

Tags Alteradas

Alteramos então essas duas tags, adicionando o `*` . Quando o cliente desejar bloquear, deverá adicionar o domínio do Host, permitindo dessa forma somente o domínio do   RM.Host  
<httpProtocol>  
    <customHeaders>  
      <add name="Access-Control-Allow-Origin" value="\*" />  
      <add name="Access-Control-Allow-Headers" value="\*" />  
    </customHeaders>  
  </httpProtocol>
