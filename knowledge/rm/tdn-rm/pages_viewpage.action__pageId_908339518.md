---
content_hash: b9daebf412d6f8a303dcbe35436cee73142231db9d2da214497eee980ccafb8c
fetched_at: '2026-06-29T00:12:03.387993+00:00'
page_id: '908339518'
product: rm
source: tdn-rm
title: 4- Customização das imagens do banner do login unificado dos portais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=908339518
version: 5
---

O login unificado dos portais, permite que a instituição realize a customização da imagens do banner na página de login.

As alterações das imagens **não são de responsabilidade da TOTVS**, pois estão ligadas à customização realizada pelo próprio cliente.

As customizações das imagens**devem ser realizadas em cada servidor web existente.**

Desta forma é **altamente necessário sempre** que tiver uma atualização de patch o cliente **salve as informações antes da atualização, e após a mesma, faça as modificações anteriormente realizadas**.

Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador do Portal. **Diretório:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\web\app\Edu\loginportais\config

Parâmetro "portalAluno", "portalProfessor" e "portalGestaoEducacional" - Banner interno das plataformas

Deve ser configurado o banner das plataformas, se esta ativo e a url de cada portal que deseja associar ao login unificado. Para alterar as imagens, basta adicionar ou remover imagens desejadas no **diretório do login do portal** e no **arquivo config.json**.

**Diretório:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\web\app\Edu\loginportais\assets\img\banners-plataformas

O nome da imagem da lista no **arquivo config.json** deve ser o mesmo nome da imagem no diretório do portal.

Apenas uma imagem

Cada plataforma é permitido apenas uma imagem de banner

Tamanho das imagens

Para que o banner tenha uma boa apresentação sugerimos que a imagem tenha a **dimensão de 201 (largura) x 200(altura)**.

Parâmetro "imgBannersLogin" - Banner tela de login

Deve ser configurado os banners que são exibidos na tela de login do portal. Para alterar as imagens, basta adicionar ou remover imagens desejadas no **diretório do login do portal** e no **arquivo config.json**.

**Diretório:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\web\app\Edu\loginportais\assets\img\banners-login

O nome da imagem da lista no **arquivo config.json** deve ser o mesmo nome da imagem no diretório do portal.

Tamanho das imagens

Para que o banner tenha uma boa apresentação sugerimos que a imagem tenha a **dimensão de 640 (largura) x 592 (altura)**.

## Para incluir um novo banner, seguir os passos abaixo:

**1-** Acessar o arquivo no diretório: **C:\RM\Atual\Release\FrameHTML\web\app\Edu\loginportais\assets\img\banners-login** e Incluir a nova imagem.

**2-** Após incluir a nova imagem, acessar o diretório: **C:\RM\Atual\Release\FrameHTML\web\app\Edu\loginportais\config** e incluir o novo nome do banner no arquivo no config.json
