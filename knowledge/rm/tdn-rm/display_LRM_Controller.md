---
content_hash: 43bf0254d32768e24b7d1a39bc233c10866e28c30617fdef6cdf60b49220e96e
fetched_at: '2026-06-29T00:08:39.022330+00:00'
page_id: '286005594'
product: rm
source: tdn-rm
title: Controller
type: documentation
url: https://tdn.totvs.com/display/LRM/Controller
version: 4
---

Após Instalar o TOTVS RM Portal deverá ser realizado os passos abaixo:

**1º-** Edite o arquivo "**edu-contantes.global.config.js**" com algum editor de sua preferência e altere o valor da variável **EDU\_CONST\_GLOBAL\_CUSTOM\_CONTROLLER**em "**ocorrencias"**para **true**.

**2º-**Acesse o caminho: "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js\aluno\ocorrencias**". Crie uma pasta com o nome "**custom**".

**3º-** Acesse ao caminho "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js\templates**" e faça uma cópia do arquivo "**ocorrencias-list.controller.js**" para a pasta "**custom**".

Template

 

**4º-** Edite o arquivo com o editor de sua preferência e faça as alterações desejadas.

 

Exemplo simples:

 

Edição do controller, ao acessar a página de ocorrências, é exibido um alerta na tela.
