---
article_id: 360016453852
category: ADVPL - Classe e Função
content_hash: 51327c5ff1a72120d8dc908b6def22bf145d3c84633f2478f3091b1e2bc32444
fetched_at: '2026-06-28T22:40:15.710903+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criação de Filtro
  em Consulta Padrão
type: support-article
updated_at: '2025-06-16T18:35:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016453852-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-Filtro-em-Consulta-Padr%C3%A3o
---

**Dúvida**Como criar um filtro utilizando consulta Padrão  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A partir da versão 11.80  
  
**Solução**Filtro fixo em consulta padrão

A consulta padrão é a mais utilizada dentro do sistema, ela possui uma flexibilidade enorme, e geralmente atende a necessidades do usuário. Assim como no *Browse* ou **MBrowse** é permitido o uso filtro, as consultas padrões também possibilitam aplicar filtros promovendo agilidade nas buscas.

No entanto, cada filtro criado pelo usuário é exclusivo, ou seja, o filtro não está disponível para os outros usuários. Nesse artigo você aprenderá como configurar um filtro fixo em uma consulta padrão, de modo que esteja disponível para todos os usuários.

Vamos tomar como exemplo a Tabela SB1 (Cadastro de Produtos), perceba que no exemplo abaixo a consulta está trazendo os itens bloqueados e liberados:

[![](https://1.bp.blogspot.com/-jpFfquvyjyI/WMKWZJ8qBXI/AAAAAAAAF94/WHIVmK7Q6akvvjvewTodomydO1NXIOJoQCLcB/s640/Consulta%2BPadr%25C3%25A3o%2Bcom%2BBloqueados.png)](https://1.bp.blogspot.com/-jpFfquvyjyI/WMKWZJ8qBXI/AAAAAAAAF94/WHIVmK7Q6akvvjvewTodomydO1NXIOJoQCLcB/s1600/Consulta%2BPadr%25C3%25A3o%2Bcom%2BBloqueados.png)

Nesse outro exemplo estão sendo exibidos somente os produtos liberados:

[![](https://2.bp.blogspot.com/-eJp2QfIgJWk/WMKXywbgQVI/AAAAAAAAF-E/gxNJSoLPvIoFyFWi9hub0Y608LHd6-tDQCLcB/s640/Consulta%2BPadr%25C3%25A3o%2Bsem%2BBloqueados.png)](https://2.bp.blogspot.com/-eJp2QfIgJWk/WMKXywbgQVI/AAAAAAAAF-E/gxNJSoLPvIoFyFWi9hub0Y608LHd6-tDQCLcB/s1600/Consulta%2BPadr%25C3%25A3o%2Bsem%2BBloqueados.png)

Em um cenário onde há muitos produtos bloqueados, o que é típico com o passa do tempo, a pesquisa torna-se complexa para muitos usuários. Segue abaixo passo-a-passo para ocultar os produtos bloqueados da consulta padrão SB1:

No ambiente Configurador, acesse

1. Base de Dados » Dicionário » Base de Dados » Consultas Padrão
2. Edite a Consulta Padrão SB1 e não opção de Filtro insira a seguinte expressão

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4485337243543/mceclip0.png)

Na tabela SB1 o campo B1\_MSBLQL é responsável por definir se o produtos está bloqueado ou liberado, sendo o valor 1 para produtos bloqueados, e 2 para produtos liberados. Deste modo os produtos bloqueados não serão mais exibidos na consulta padrão SB1 independente do usuário que estiver fazendo uso da mesma.
