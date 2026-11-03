---
content_hash: c959956fb8d1c5ed762533b1629d95b47cb039da5e0d7ace00d8367576e5cf72
fetched_at: '2026-06-29T00:08:37.678044+00:00'
page_id: '284880337'
product: rm
source: tdn-rm
title: HTML
type: documentation
url: https://tdn.totvs.com/display/LRM/HTML
version: 5
---

Após Instalar o TOTVS RM Portal deverá ser realizado os passos abaixo:

Informação

No exemplo abaixo, iremos customizar a tela de Ocorrências.

**1º-** Edite o arquivo "**edu-contantes.global.config.js**" com algum editor de sua preferência e altere o valor da variável **EDU\_CONST\_GLOBAL\_CUSTOM\_VIEW** em "**ocorrencias"** para **true**.

**2º-**Acesse o caminho: "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js\aluno\ocorrencias**". Crie uma pasta com o nome "**custom**".

**3º-** Faça uma cópia do arquivo "**ocorrencias-list.view.html**" para a pasta "**custom**".

Dica

Acessando a pasta "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js\templates**", você poderá realizar a cópia do arquivo desejado.

**4º-** Edite o arquivo com o editor de sua preferência e faça as alterações desejadas.

Exemplo:

Na alteração abaixo, foi retirado o componente totvs-list-item-content-detail responsável por montar os detalhes da ocorrência com os campos turma, etapa e observação, deixando os mesmos visiveis diretamente na lista de ocorrências.

Antes da alteração:

Após a alteração:
