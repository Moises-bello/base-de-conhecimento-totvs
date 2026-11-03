---
content_hash: d278918112d5a5c1f4241a29a187747f97cf9918221b007e5ab007090b0ee47e
fetched_at: '2026-06-29T00:11:32.062228+00:00'
page_id: '743697040'
product: rm
source: tdn-rm
title: 4- Customização da logo do menu lateral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=743697040
version: 16
---

O portal do professor, permite que a instituição realize a customização da logo do menu lateral.

false

Essa funcionalidade está disponível a partir do patch: 12.1.2306

As alterações das imagens **não são de responsabilidade da TOTVS**, pois estão ligadas à customização realizada pelo próprio cliente.

A customização realizada via parametrização no RM.exe **é prioritária** sobre a customização via diretório.

Customização via parametrização no RM.exe

Para realizar a configuração, acesse:**Gestão Educacional  | Configurações | Configuração | Parâmetros | 15.04 - RM Portal | 15.04.03 - RM Portal Educacional - Novo Portal do Professor**

Customização via arquivo direto no diretório

O sistema permite a customização das imagens direto no diretório, para isto acesse a pasta **"web\app\Edu\PortalDoProfessor\assets\img\logos-menu"**, no diretório onde está instalado o portal.

O sistema disponibiliza um arquivo para a imagem quando o menu estiver expandido e outra quando o menu estiver recolhido:

* **Imagem menu expandido:** marca-menuA.png
* **Imagem menu recolhido:** marca-menuB.png

Desta forma é **altamente necessário sempre** que tiver uma atualização de patch o cliente **salve as informações antes da atualização, e após a mesma, faça as modificações anteriormente realizadas**.

Resolução adequada

Para que as imagens fique com uma resolução adequada, é necessário que identificação da imagem tenha os seguintes tamanho, além disso, todas as imagens deverão seguir o mesmo padrão de configuração.

* **Imagem menu expandido:** 224px X 24px
* **Imagem menu recolhido:** 30px X 30px
