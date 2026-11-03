---
content_hash: 8fdbd7be32eb87f251ac0b3906d1fc6ef63b7752b3d7a395f37cf14a77b7f02d
fetched_at: '2026-06-28T21:35:18.785558+00:00'
page_id: '185735401'
product: fluig
source: tdn-fluig
title: Como criar um widget que busque conteúdo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185735401
version: 69
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar todo o processo de desenvolvimento de um *widget* integrado a vários possíveis tipos de fonte de dados. Cada sessão contém apenas o código necessário para o entendimento de cada assunto específico abordado. Para ver o resultado final do desenvolvimento, baixe os projetos abaixo:

**Projeto 01:** [*Widget* de Notícias](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse) (integra-se com [formulário](http://tdn.totvs.com/pages/viewpage.action?pageId=185735401#ComocriarumWidgetquebusqueconte%C3%BAdo-Interno%28formul%C3%A1rios%29)):

noticiasImagem 1Imagem 2

**Projeto 02:** [*Widget* de Aniversariantes](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse) (integra-se com [formulário](http://tdn.totvs.com/pages/viewpage.action?pageId=185735401#ComocriarumWidgetquebusqueconteúdo-Interno(formulários)) ou [serviço soap do RM](http://tdn.totvs.com/pages/viewpage.action?pageId=185735401#ComocriarumWidgetquebusqueconteúdo-ExternoutilizandoserviçosSOAP)):

aniversarioImagem 1Imagem 2

Vamos desenvolver um *widget* que mostre notícias cadastradas no Fluig Plataforma. Não deixe de conferir o [projeto completo](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse).

# Criar projeto Fluig

Em primeiro lugar, devemos ter disponível um projeto Fluig onde desenvolveremos nosso *widget* utilizando o Fluig Studio. Para isso podemos seguir os [passos para criação de um projeto Fluig](http://tdn.totvs.com/pages/viewpage.action?pageId=185735250).

# Criar *widget*

Em seguida, criaremos um *widget*. Para isso podemos seguir os [passos para criação de um *widget*](http://tdn.totvs.com/pages/viewpage.action?pageId=113803693#ConstruçãodecomponentesWCMnoFluigStudio-CriaçãodeWidget).

Veja o exemplo em nosso repositório [aqui](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse).

# Desenvolvendo o *widget*

Agora que temos a estrutura básica, podemos começar a desenvolver o código personalizado e inserir as propriedades que desejamos para esse *widget*.

Para isso, podemos começar com o arquivo de configurações *application.info*. É nele que ficam registradas informações como título, descrição, arquivos de visualização, componentes a serem utilizados etc.

## Arquivo application.info

Abaixo o arquivo application.info detalhado:

textEclipseapplication.infotrueNota

Para saber mais, acesse a documentação .

## Uso do conceito Super *widget*

Iremos utilizar o conceito de Super *widget* na construção de nosso *widget*. Para mais detalhes acesse o guia [Super *widget*](http://style.fluig.com/javascript.html#super-widget).

Precisamos adicionar a classe css *super widget* na *div* que instancia o *widget*, tanto no arquivo de edição (edit.ftl) como no arquivo de visualização (view.ftl).

xmlEclipse
