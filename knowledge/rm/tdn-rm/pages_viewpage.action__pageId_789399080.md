---
content_hash: af7d68cc5b26e784b507cb49563f471122c03e19bba9215e1b5ca800ff458ebb
fetched_at: '2026-06-29T00:11:39.680685+00:00'
page_id: '789399080'
product: rm
source: tdn-rm
title: 06. Cadastro e configuração do banner para o aplicativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789399080
version: 13
---

O cadastro que permite configurar o banner para apresentação no aplicativo, está disponível no menu **'Sistema' Educacional | Acesso Menu|****Atividades acadêmicas | Central de Comunicações | eduCONNECT| Banner.**

Ao acessar o menu Banner, é possível cadastrar mensagens publicitárias que serão apresentadas para os usuários do aplicativo.

**Título:** responsável pela descrição do banner. Esse título não será apresentado no aplicativo, servirá exibido apenas na tela de visão de cadastro de banner no TOTVS Educacional para que o usuário do sistema possa identificar de forma mais simples e rápida cada banner sem ter que editar o registro.

**Link da Imagem:** o campo link da imagem tem como objetivo determinar a imagem a ser exibida. Basta informar a **URL pública do arquivo de imagem**, ou seja, o endereço acessível publicamente que aponta diretamente para o arquivo da imagem e não para uma página que a contenha.

**Link da ação:** caso queira redirecionar o usuário do aplicativo para outra página, basta informar o link neste campo.

**Data Inicial e Data Final:** determinam período em que o banner será apresentado no mural. A data inicial é preenchida automaticamente de acordo com a data corrente, mas é possível informar uma data anterior ou posterior a data atual. A data final determina o dia em que encerra a apresentação do banner.

****Ativo**:** indica se o banner está ativo ou não, através deste parâmetro que o usuário determina se o banner será apresentado no mural.

**Ordem:** o campo ordem tem como objetivo definir a ordem de apresentação de cada banner.

Exemplo 1:

Existem 2 Banners com a ordem de apresentação = 1

A data do banner 1 é do dia 01/12/2017 á 31/12/2017

A data do banner 2 é do dia 15/12/2017 á 15/02/2018

A ordem de apresentação será: a partir do banner 1

Exemplo 2: Existem 3 Banners

A data do banner 1 é do dia 01/12/2017 á 31/12/2017 com ordem 2

A data do banner 2 é do dia 15/12/2017 á 15/02/2018 com ordem 1

A data do banner 3  é do dia 15/12/2017 á 15/02/2018 com ordem 3

A ordem de apresentação será: banner 2, 1 e 3 (isto ocorrerá quando estiverem no mesmo intervalo de datas)

A seguir um exemplo de banner sendo exibido dentro do aplicativo. A área destacada em vermelho é onde o banner será exibido dentro do aplicativo.

As dimensões recomendadas da imagem para o Banner são 343 x 145 px, pois temos uma grande variedade de dimensões de dispositivos no mercado e a imagem pode sofrer uma distorção ao ser exibida em cada dispositivo.

O **Cadastro de Banner** permite selecionar o contexto para qual o banner será cadastrado.

O aplicativo irá exibir os banners por contexto apenas se o .

Por padrão, o sistema irá carregar o contexto atual que o usuário está logado.

O sistema só irá exibir contextos (Coligada, Filial e Nível de ensino) cujo usuário que está realizado o cadastro tiver permissão (SUSUARIOFILIAL como "Sistema" ou "Sistema e Portal") e o mesmo GUID do contexto logado parametrizado no sistema.

Na visão, o contexto em que o banner foi cadastrado será exibido.

Foi desenvolvido também o processo **"Replicar Banner eduCONNECT"** que permite replicar um determinado banner cadastrado em um contexto para outros contextos que tiverem o mesmo GUID cadastrado.

Ao executar o processo, é possível selecionar para quais contextos o banner será replicado.

Observe que o sistema não realiza a replica caso identifique que o banner já estava cadastrado em um determinado contexto.

Para que o processo seja habilitado deve-se estar marcado o  e ter o acesso permitido nas **permissões de usuário (Acesso a menus | Atividades acadêmicas | Central de comunicações | eduCONNECT | Banner | Replicar Banner eduCONNECT)**
