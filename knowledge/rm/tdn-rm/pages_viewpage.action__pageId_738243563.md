---
content_hash: 92b014a037ec5fe4bd7a5293d79dbc4e267e4822de202b11cdba6afd12fc898e
fetched_at: '2026-06-29T00:11:31.497418+00:00'
page_id: '738243563'
product: rm
source: tdn-rm
title: Configuração na Google Play
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=738243563
version: 27
---

Nesse roteiro iremos demonstrar como realizar a criação do aplicativo e as configurações iniciais na sua loja Google Play.

# Sumário

---

Sumário

# Permissão de acesso a loja

---

A TOTVS ficar responsável em realizar as publicações, atualizações de aplicativos e certificados., por isso é necessário que seja concedido a permissão de administrador para o usuário [educonnect@totvs.com.br](mailto:educonnect@totvs.com.br)

Pode ser que esta etapa não seja necessária pois pode ser que já exista, validar antes de seguir.

No menu lateral clique em **"Usuários e permissões"**.

Clique em **"Convidar novos usuários"**.

Informe o e-mail **"educonnect@[totvs.com.br](http://totvs.com.br)"** dê a permissão de administrador como mostrado na imagem abaixo e clique em **"Convidar usuário"**.

# Criação e preparação da loja

---

Ao entrar na página do sua aplicação clique em **"Criar app"** no canto superior esquerdo.

Selecione as opções abaixo, informe o nome da sua aplicação e clique em **"Criar app".**

Após o preenchimento das informações necessárias e clique em **"Criar aplicação"**

No menu "**Presença na loja**" e selecione a opção **"Página "Detalhes do app" principal"**.

**Recursos da página de detalhes**

Preencha os campos de "**Nome de aplicação**" de acordo com os dados informados pelo cliente no formulário.

Importante

As informações do campo "**Breve Descrição**" e "**Descrição Completa"** deve ser conforme o padrão abaixo.

**Breve Descrição:** *Canal de comunicação ágil e acessível que conecta toda a comunidade acadêmica.*

**Descrição completa:** *Canal de comunicação ágil e acessível que conecta toda a comunidade acadêmica com as principais informações e serviços educacionais.* *Um universo com várias funcionalidades e serviços da instituição na palma da mão, e em um ambiente inteiramente pensado para tornar sua experiência mais rápida e interativa.*

**Elementos gráficos**

Na publicação final do APP, iremos considerar as imagens que foram enviadas no formulário preenchido pelo cliente, pois as mesmas serão tratadas pelo time de UX do TOTVS Educacional.

No campos "**Ícone da Aplicação**" insira o ícone de resolução 512x512 passado pelo Designer

Em "**Recurso gráfico**" insira o banner do aplicativo (banner.png) a ser exibido na loja.

Nos demais campos, insira as imagens de acordo com as suas respectivas descrições.

Posteriormente clique em "**Salvar**"

No menu "**Presença na loja**" e selecione a opção **"Configurações da loja"**.

Clique em editar e preencha os campos "Categoria de apps" com os valores abaixo:

Preencha as informações de contato de acordo com o que o cliente disponibilizou no formulário

No menu "**Politicas e programas**" e selecione a opção **"Conteúdo do app"**.

**Política de Privacidade**

Informar o link TDN para política de privacidade do eduCONNECT: 

<https://educonnect-portal.azurewebsites.net/privacidade/termos.html>?n=[NOME DO APP]

Se o app chama "Notre Dame" por exemplo, a url ficará:  <https://educonnect-portal.azurewebsites.net/privacidade/termos.html?n=Notre%20dame>

Essa alteração é para que o termo busque através dos parâmetros na querystring e faça alterações no conteúdo do termo para que exiba o nome do app invés do nome Meu eduCONNECT, pois as lojas tem questionado a diferença do nome contido no termo e o nome do app. . 

**Anúncios**

**Acesso a Apps**

Clicar em em "**+ Adicionar instruções**" para inserir novas "**Informações de Acesso**"

Preencher os campos de acordo com os dados do usuário de acesso app pra que a loja possa autenticar e realizar as devidas validações

Em em alguns casos principalmente para cliente CLOUD recomendamos utilizar o usuário ES-00700, para maiores informações [clique aqui](https://tdn.totvs.com/display/GDPA/10+-+Submetendo+APP+para+Loja#id-10SubmetendoAPPparaLoja-Usu%C3%A1rioES-00700)

**Classificação de Conteúdo**

O endereço de email é do cliente. Esta informação está no formulário

Finalize o questionário clicando na opção **“Concluir****”**posteriormente será apresentado um resumo  das classificações, então clique em "**Salvar**"

**Público-alvo e Conteúdo:**

Importante

Mesmo que o cliente tenha informado as faixas etárias de "Até 5 anos", "6-8" e "9-12", não realize a marcação das mesmas, sob pena de o aplicativo ser rejeitado na revisão realizada pela loja.

Marque APENAS as seguintes faixas etárias:

 

Clique em avançar e será mostrada a confirmação, posteriormente clique em "**Salvar**"

**Apps de noticias**

**Segurança dos dados**

Clique em próximo e continue o preenchimento da **informações pessoais**

Salve os dados e prossiga para **informações financeiras**

Após concluir clique em salvar e prossiga para "**Local aproximado**"

Após concluir clique em salvar e prossiga para "**Local exato**"

Após concluir clique em salvar e prossiga para "**Identificadores do dispositivo e outros**"

Após concluir clique em salvar e prossiga para "**ID de publicidade**"

Após concluir clique em salvar e prossiga para "**Apps governamentais**"

Após concluir clique em salvar e prossiga para "**Recursos financeiros no seu app**"

Após concluir clique em salvar e prossiga para "Apps de saúde"

Após concluir clique em "**Salvar**" e finalizamos a parametrização da parte de Segurança dos dados

No menu **"Produtos"** e selecione a opção **"Preços do app".**

Confirme se o o app esta como "**Gratuito**"

Até aqui a Loja esta preparada podendo seguir com a solicitação de publicação do aplicativo.
