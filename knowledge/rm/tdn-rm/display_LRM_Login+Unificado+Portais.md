---
content_hash: 1aca1c8393988a806962fa8d93473196b9c6f3f6c79bc574592fd3571d8374ca
fetched_at: '2026-06-29T00:12:01.465294+00:00'
page_id: '895597582'
product: rm
source: tdn-rm
title: Login Unificado Portais
type: documentation
url: https://tdn.totvs.com/display/LRM/Login+Unificado+Portais
version: 4
---

Configuração:

 - apiServer: utilizado para definir qual será a url base que as api utilizam, caso não seja preenchido será usado a mesma url do portal. Por exemplo, se a url do portal é <http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,> então a url que será utilizada será a mesma.

  -  portalAluno:

         - exibir: configura se a plataforma do portal do aluno será exibida para logar  
         - banner: configura qual a imagem que será exibida na opção de logar no portal

          - url: configura a url do portal. Caso deixe em branco será utilizada a mesma url do portal de login. Por exemplo, se a url do portal é [http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais](http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,) então a url do portal do aluno será  [http://escolatotvs.com.br/FrameHTML/web/app/edu/](http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,)portaleducacional

  -  portalProfessor:

         - exibir: configura se a plataforma do portal do professor será exibida para logar  
         - banner: configura qual a imagem que será exibida na opção de logar no portal

          - url: configura a url do portal. Caso deixe em branco será utilizada a mesma url do portal de login. Por exemplo, se a url do portal é [http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais](http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,) então a url do portal do aluno será  [http://escolatotvs.com.br/FrameHTML/web/app/edu/](http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,)portaldoprofessor

  -  portalGestaoEducacional:

         - exibir: configura se a plataforma do portal gestão educacional será exibida para logar  
         - banner: configura qual a imagem que será exibida na opção de logar no portal

          - url: configura a url do portal. Caso deixe em branco será utilizada a mesma url do portal de login. Por exemplo, se a url do portal é [http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais](http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,) então a url do portal do aluno será  [http://escolatotvs.com.br/FrameHTML/web/app/edu/](http://escolatotvs.com.br/FrameHTML/web/app/edu/loginportais,)portalgestaoeducacional

-imgBannerLogin: configura as imagens que serão exibidas na página de login. Caso queira exibir mais de uma imagem, em formato de carrosel, deve adicionar mais uma entrada com a tag name entre chaves, onde o valor da chave name deve ser o nome da imagem. Por exemplo: {name: "banner1.svg"}, {name: "banner2.svg"}

Após logar será exibido quais plataformas o usuário possui permissão para logar. Ao clicar na plataforma o usuário será redirecionado para o portal escolhido.
