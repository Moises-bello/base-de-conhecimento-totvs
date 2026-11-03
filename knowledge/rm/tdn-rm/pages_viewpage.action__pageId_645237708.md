---
content_hash: febdb127772cf00ef246f3787ea216000c61529662e0ca8604be513ebd15343a
fetched_at: '2026-06-29T00:11:11.051852+00:00'
page_id: '645237708'
product: rm
source: tdn-rm
title: Minhas Inspeções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645237708
version: 8
---

# **TOTVS MINHAS INSPEÇÕES**

Aqui você tem acesso a documentação, requerimentos do sistema e termos legais dos Apps da TOTVS. Utilize o menu abaixo, para navegar por categoria ou escolha o aplicativo na lista geral.

0.5ALL0.5 INTRODUCAOINTRODUÇÃOAuxilia no princípio da utilizaçãoslide

# **Conteúdo**

Olá, seja bem vindo! Esta página tem como objetivo auxiliar os colaboradores quanto a utilização do app "**Minhas Inspeções",** na resolução de problemas em qualquer dispositivo mobile como tablet’s e smartphones.

Aqui você verá:

* O que é o aplicativo.
* Entenderá suas funcionalidades e permissões.
* Todos os passos para configurar e utilizar o aplicativo.
* Resoluções e Dicas de problemas que ocorrem nas lojas principais.
true0.5GUIA DE USOGUIA DE USOInstalando o aplicativo no celularslide50

# **Guia de Uso**

* **Configurações do RM.Host/RM.Host.Service**

Nas configurações do RM.Host/RM.Host.Service devem estar informadas as chaves **DefaultDB** e **ApiPort**.

**DefaultDB:** Chave necessária para que o Host encontre no arquivo Alias.dat qual alias de base de dados será utilizada.

**ApiPort:** Porta de conexão de API do host.

Em alguns casos a chave pode não estar preenchida no arquivo de configuração do host mas por padrão caso a tag não estiver preenchida, o valor para a chave ApiPort é 8051

A porta informada no ApiPort deve estar liberada nas regras de firewall do servidor/máquina para que a comunicação via api funcione corretamente no host.

**WebServiceCulture:**A tag WebServiceCulture é utilizada para alterar a cultura de leitura e conversão dos dados recebidos pelo WebService.

    Para o que a comunicação via api funcione corretamente o valor a ser inserido na chave deve ser "Invariant".

* **Baixar o aplicativo na loja**

* **Configurando URL**

A URL de configuração do app pode ser informada de forma automática pela leitura de QR Code e também pode ser configurada manualmente conforme a segunda imagem.

A porta de configuração deve ser preenchida com **{ UrlServidor: [http://endereçoipv4damaquina:ApiPort](http://endereçoipv4damaquinaApiPort) }**

(Exemplo: { UrlServidor: "<http://192.168.137.1:8051>" } )

Ao realizar  configuração do aplicativo a tela abaixo será exibida e será permitido realizar o login no aplicativo com o usuário do RM.

Caso a url esteja indisponível ou incorreta será exibida uma mensagem de erro.

* **Usar o app com base** **exemplo**: opção para configurar uma base exemplo no app para que o usuário possa realizar, concluir e criar inspeções a partir de templates exemplo sem que o usuário precise inserir seus dados.

Na tela de login do APP ao clicar em configuração, é possível reconfigurar a URL utilizada no app. A reconfiguração pode ser  automática (qr Code) ou manual.

**Esqueci minha senha:**opção para recuperar a senha de login do usuário. Será enviado um token ao email para que seja informado na segunda etapa.

A tela de Configurações também exibe um QR Code para que outros aparelhos possam ser configurados.

* **Automática, com QR Code:** opção para que o usuário reconfigure o APP realizando a leitura de um QR Code.

* **Manual, sem QR Code:** opção para que o usuário reconfigure o APP informando a URL manualmente.

* **Usar o app com base** **exemplo**: opção para configurar uma base exemplo no app para que o usuário possa realizar, concluir e criar inspeções a partir de templates exemplo sem que o usuário precise inserir seus dados.

* **O que é um QRCode?:**exibe informações sobre o que é um QR Code.

true0.5NOVIDADESNOVIDADES DA RELEASEslide50

# **Novidades da Release**

Esse documento deve ser utilizado para expor as principais atualizações do aplicativo nas últimas versões do mesmo, tais como atualização de layout, novas funções ou correção de bug. 

true0.5ESPECIFICACOESESPECIFICAÇÕES DE SERVIÇOslide50

# **Especificações de Serviços**

* **Esqueci minha senha:**Caso o usuário selecione a opção esqueci minha senha, será enviado para o e-mail do usuário um token para alteração da senha.

Ao iniciar o aplicativo caso ele tenha sido configurado corretamente será exibida a tela de login.

O usuário para realizar login deve ser o mesmo usuário de login no RM.

Ao informar usuário e senha corretamente o usuário será direcionado para o menu de funcionalidades do APP.

Caso o usuário acessado não possuir inspeções pendentes a seguinte tela será exibida ao realizar o login do usuário:

* O usuário logado no APP será exibido na parte superior da tela.
* Para configurar novamente o app ou desconectar do usuário logado basta acessar o botão na parte superior direita.

* Abaixo do usuário serão exibidas em roxo as inspeções direcionadas para o usuário logado. Passando para o lado na parte exibida em roxa o APP navegará entre as inspeções direcionadas para o usuário.
* **Próximas verificações:**exibidas todas as inspeções direcionadas para o usuário.
* Ao clicar me uma das próximas verificações a inspeção poderá ser iniciada ou continuar de onde parou

* Na parte inferior é possível realizar uma **pesquisa** entre as inspeções. É possível pesquisar com texto, período da inspeção, data específica ou status.
* Para realizar pesquisas o usuário deve estar conectado a internet.

* Na parte inferior é possível inserir **nova inspeção** e na tela de criação devem ser informados: Título, Formulário, Tarefa ou equipamento associado e Data de realização. Após criada a inspeção os usuários direcionados poderão realizá-la na tela inicial do aplicativo ou o usuário criador da inspeção pode iniciá-la para preenchimento.

Continuando a inspeção o usuário ira responder as questões do formulário. Para cada resposta é permitido a inserção de anexos e de uma observação para a inspeção realizada.

Ao chegar no final do formulário de inspeção, para a última resposta do formulário é necessária a assinatura do usuário que realizou a inspeção:

Após incluir a assinatura o formulário poderá ser Revisado, Salvo como Rascunho ou Finalizado.

As permissões do APP serão informadas no cadastro dos perfis de usuário.

* **Incluir coletores automaticamente através do app Minhas Inspeções**

Caso o usuário tenha permissão, ao realizar o sincronismo no login do usuário o coletor será cadastrado automaticamente na base e estará ativo.

* **Finalizar inspeção e incluir inspeção**

Essas permissões irão controlar os usuários vinculados a esse perfil para que utilizem as funcionalidades.

**Incluir Inspeções:**O usuário que não possuir essa permissão não poderá incluir novas inspeções no app.

**Finalizar Inspeções:**O usuário que não possuir essa permissão não poderá finalizar inspeções. Obs: O usuário sem permissão poderá iniciar uma inspeção e responder os itens mas, ao finalizá-la ela não será enviada.

Caso o usuário não possua alguma permissão, as inspeções não enviadas estarão no menu de notificações  para que possam ser visualizadas.

Os formulários serão criados pelo USUÁRIO e as perguntas do formulário podem ser do tipo:

* **Sim ou não**

A resposta deverá ser sim ou não.

É possível incluir e remover anexos em cada resposta do formulário.

**Observação!**

* Não é possível anexar arquivos com mais de 100Mb de tamanho.

É possível incluir observação nesse tipo de resposta e o campo não é obrigatório.

* **Múltipla Escolha**

A resposta deverá ser uma das opções exibidas.

É possível incluir observação nesse tipo de resposta e o campo não é obrigatório.

* **Data**

A resposta deverá ser uma data.

É possível incluir observação nesse tipo de resposta e o campo não é obrigatório.

* **Valor/Quantidade**

A resposta deverá ser um valor/quantidade.

É possível incluir observação nesse tipo de resposta e o campo não é obrigatório.

* **Lista**

Será exibido em lista as opções a serem escolhidas para resposta.

É possível incluir observação nesse tipo de resposta e o campo não é obrigatório.

* **Código de Barras**

O código de barras pode ser informado manualmente, Ler QR Code e Ler Código de barras a câmera é aberta para leitura.

É possível incluir observação nesse tipo de resposta e o campo não é obrigatório.  
  
**BIM 3D**Dentro do aplicativo temos o item de menu "BIM" na pagina home do Appa

Dentro do BIM temos a inspeção para mostrar os objetos a serem inspecionados no modelo 3D através da tarefa associada a inspeção.

Temos opção de Inspeção, onde podemos buscar as inspeções por:

* Criado em
* Realizado em
* Data inicial e final
* Não avaliado
* Conforme
* Não conforme

Obs: Check-box Adaptativo melhora a visualização de modelos grandes e pesados.

filtro de objeto podemos selecionar todos os objetos referente ao modelo 3D ou selecionar por partes.

  
true0.5faqsPOLÍTICA DE PRIVACIDADEAuxílio na correção de erros aos usuários do Appslide50

# **Política de Privacidade**

O objetivo de desse documento é formalizar o compromisso com a segurança e a privacidade de informações coletadas dos usuários do aplicativo. É composta por clausulas que o cliente final aceita ao acessar ou realizar alguma ação de requerimento de dados no aplicativo.

.columnLayout.two-equal {
width: 100%;
margin: 0 auto;
padding-top: 32px;
text-decoration: none;
background-image: url(https://jiratdncdncontent.blob.core.windows.net/tdn/banners/background.png);
height: 106px;
background-size: cover;
background-repeat: no-repeat;
background-position: center;
height: 230px;
}
.columnLayout.two-equal .innerCell {
padding: 80px;
}
#title-text {
display: none !important;
}
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 30px;
padding-right: 30px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
#main #breadcrumbs {
padding: 0 10px;
}
.main-header {
padding: 0 20px;
}
.page-metadata {
margin-top: -22px;
}
.columnLayout.single .innerCell {
padding: 5px;
display: flex;
flex-wrap: wrap;
padding: 0 200px;
justify-content: center;
padding-bottom: 20px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
div#main {
margin-left: 0px !important;
}
#footer {
margin-left: 0px !important;
}
#main {
padding-left: 0px;
padding-right: 0px;
overflow-x: hidden;
}
.innerCell h1 {
font-size: 32px;
}
.columnMacro {
padding: 10px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #000000!important;
border-bottom-color: #000000 important;}.custom-button
tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a:visited, .aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a:focus, .aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a:hover, .aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a:active {
color: #0052cc;
}
tabs.horizontal-tabs>.columnMacro>.conf-macro>.custom-button:hover{
background: #ffffff!important;
}
]]>
