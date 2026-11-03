---
content_hash: 8920aa5a4942d6d548ad3e0dd6159dbd597c59a5e28dff24e5eee002165daa68
fetched_at: '2026-06-29T00:10:38.189742+00:00'
page_id: '544192404'
product: rm
source: tdn-rm
title: Instalador Portal - Porta 80 como padrão para os portais FrameHTML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544192404
version: 17
---

A partir da versão **12.1.28** o Portal RM FrameHTML passa a ser instalado na porta 80 (DefultWebSite) por padrão, utilizando o Alias "FrameHTML".

Essa mudança reflete apenas no Instalador MSI, que é responsável pela instalação completa e configuração do ambiente.

A instalação procederá de forma normal e após a instalação, ao acessar o IIS, o usuário poderá perceber a mudança realizada, conforme imagem abaixo:

Clientes Portais Educacional

Com a alteração na instalação dos portais, será necessário o ajuste das URL's nas configurações do sistema e as disponibilizadas para seus usuários, para mais informações acesse o link abaixo:

<https://tdn.totvs.com/x/X3mPI>

**Observações:**

O instalador **12.1.28.exe** do portal RM não realiza alterações nas configurações de porta, sendo mantida a mesma da instalação realizada.

Caso o cliente deseje utilizar os portais na porta 80, pode realizar a alteração manualmente ou utilizar o instalador "msi" da 12.1.28, realizando a desinstalação e posterior instalação.

Para configurar sua instalação manualmente, vide manual a seguir: [Instalador Porta 80](https://tdn.totvs.com/x/DQTsFg)
