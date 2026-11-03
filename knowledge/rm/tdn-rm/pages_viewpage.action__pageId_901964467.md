---
content_hash: 7b8f54a11ac1a1927d2dc20b60139c4843e2e96f06a7590f86897482f90e0cf1
fetched_at: '2026-06-29T00:12:02.630259+00:00'
page_id: '901964467'
product: rm
source: tdn-rm
title: 2- Customização de conteúdo escrito do login unificado dos portais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901964467
version: 4
---

O login unificado dos portais, permite que a instituição realize a customização dos conteúdos escritos no portal.

As alterações nos arquivos **não são de responsabilidade da TOTVS**, pois estão ligadas à customização realizada pelo próprio cliente.

As customizações dos **conteúdos escritos devem ser realizadas em cada servidor web existente.**

Desta forma é **altamente necessário sempre** que tiver uma atualização de patch o cliente **salve as informações antes da atualização, e após a mesma, faça as modificações anteriormente realizadas**.

Lembrando que a cada atualização de patch ou versão, as informações dos conteúdos escritos podem sofrer alterações.

Recurso compartilhado

Os **conteúdos escritos são compartilhados por todas as telas do portal.** Dessa forma, se a alteração do valor da "variável" será refletida em todos os lugares do portal que a usam.

**1º-** Acessar a pasta **"FrameHTML\web\app\Edu\loginportais\assets\i18n"**, no diretório onde está instalado o portal.

O sistema disponibiliza um arquivo para cada idioma suportados, sendo assim, a customização deverá ser realizada nos arquivo(s) de idioma(s) desejado()s):

* **Português (Brasil):** general-pt.json
* **Inglês (Estados Unidos):** general-en.json
* **Espanhol (Espanha):** general-es.json

**2º-** Edite o arquivo "**general-XX.json**" com algum editor de sua preferência, onde **XX** corresponde ao idioma desejado.
