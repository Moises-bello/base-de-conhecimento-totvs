---
content_hash: 89bb8e9e7550b3d7ad80e1a4d53bc597e6d8c28c1ab4f8f84ab5da2a3472cdfd
fetched_at: '2026-06-29T00:11:29.226027+00:00'
page_id: '734382635'
product: rm
source: tdn-rm
title: 3- Customização de conteúdo escrito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=734382635
version: 20
---

O portal do professor, permite que a instituição realize a customização dos conteúdos escritos no portal.

A TOTVS **não se responsabiliza** por alterações em arquivos decorrentes de customizações realizadas pelo cliente. Portanto, é indispensável que, antes de cada atualização de patch ou versão, o cliente realize o backup de suas modificações e as reaplique após o processo, uma vez que o conteúdo original pode ser sobrescrito.

Recurso compartilhado

Os **conteúdos escritos são compartilhados por todas as telas do portal.** Dessa forma, se a alteração do valor da "variável" será refletida em todos os lugares do portal que a usam.

Servidor web

As customizações dos **conteúdos escritos devem ser realizadas em cada servidor web existente.**

****1º**-** Acessar a pasta **"FrameHTML\web\app\Edu\PortalDoProfessor\assets\i18n"**, no diretório onde está instalado o portal.

O sistema disponibiliza um arquivo para cada idioma suportados, sendo assim, a customização deverá ser realizada nos arquivo(s) de idioma(s) desejado()s):

* **Português (Brasil):** general-pt.json
* **Inglês (Estados Unidos):** general-en.json
* **Espanhol (Espanha):** general-es.json

**2º-** Edite o arquivo "**general-XX.json**" com algum editor de sua preferência, onde **XX** corresponde ao idioma desejado.
