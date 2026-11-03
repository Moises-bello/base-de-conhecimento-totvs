---
content_hash: 9682b73dbc37cbbf296e14a9c64433aa8d7e279e3bc4fed438611acbbaebced9
fetched_at: '2026-06-29T00:11:02.687003+00:00'
page_id: '61933825'
product: rm
source: tdn-rm
title: Manual Gestão de Conteúdo - Portal WEB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61933825
version: 13
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.XX |
| **Processo** | **:** | RM Portal |
| **Subprocesso** | **:** | Manual Gestão de Conteúdo - Portal WEB |
| **Data da publicação** | **:** | 05/07/2013 |

1.Acessando o Portal:   
  
Na máquina que está instalado o Portal, digite <http://localhost/Corpore.Net>

**1.1.** **Primeira** **tela** **do Portal apresentada.**

a. Para continuar, deve-se informar um usuário cadastrado nos sistemas RM.

b. A senha é a mesma utilizada para logar em qualquer sistema RM.

c. O campo Alias configurado, fica no arquivo Alias.dat na pasta RM.NET.

**1.2.** **Alteração** **no layout** **do Portal.**   
  
  
Após digitar usuário e senha, a tela "Início" irá aparecer.

Obs: O Portal poderá ser configurado para abrir a Pagina Principal do Portal ao invés do "Início" no arquivo Web.Config

* Um usuário (vamos considerar que seja o "mestre") que será o responsável por definir as configurações dos WebParts, ou seja, o "mestre" tem que ter um perfil que permita configurar os WebParts.   
    
  Edite o arquivo "Web.config" que fica no diretório "CorporeRM\Corpore.net", e insira as linhas em negrito do texto na TAG "webParts", que ficará assim:   
    
  <webParts>  
  <personalization>  
  **<authorization>**  
  **<allow****users="mestre" verbs="enterSharedScope" />**  
  **</authorization>**  
  <providers>  
  <add name="PrtAspNetTextFilePersonalizationProvider" type="RM.Prt.Utils.TextFilePersonalizationProvider, RM.Prt.Utils.Client"/>  
  </providers>  
  </personalization>  
  </webParts>   
    
    
  Isto determina que o usuário "mestre", neste caso, será o responsável por definir as configurações de WebParts que serão utilizadas por todos os outros usuários.  
  Acessar o Portal com o "mestre" e definir como será posicionamento dos WebParts   
    
  **1.3.****Remoção de****Menu**  
    
    
    
  Para alteração em algum menu do Portal, precisaremos editar o arquivo MENU.XML presente no diretório do Corpore.NET   
    
  Vamos fazer um exemplo removendo o menu Educacional.   
    
     1- Abra o arquivo C:\CorporeRM\Corpore.Net\Menu.XML  
     2- Localize a TAG <ID>MainEducacional</ID>  
     3- Comente a mesma usando os caracteres  
    <!-- <ID>MainEducacional</ID> -->  
     4- Salve o arquivo e atualize a página do Portal.   
    
  Você consegue identificar um Menu quando a tag (linha de comando) é um  
    
  <ID> Main \_\_\_\_\_\_</ID> . Os ID seguido de um Main é um Menu da Página Principal do Portal exceto para MainPortal e MainProcessos.   
    
  **1.4.****Criação do****AutoLogin**  
    
  O Portal WEB, não utiliza o Login Unificado, como é feito nas outras aplicações. Porém é possível criar um autologin para que um mesmo usuário autentique no portal.

  Para que o cliente não precise informar sempre o usuário e senha no RM Portal, o mesmo pode integrar o RM com o AD e utilizar a opção de AutoLogin.   
  Obs. Para isso o mesmo dever realizar a chamado do Portal dentro de um site que o usuário já esteja autenticado.

  Segue abaixo o arquivo  **AutoLogin**como exemplo:  
    
    
    
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"[ "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd|http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd ]">  
  <html xmln[s="http://www.w3.org/1999/xhtm](http://www.w3.org/1999/xhtml)l" >  
  <head>  
  <title>Corpore RM.net - Auto **Login**</title>  
  </head>  
  <body>   
  <span style="font-family:Verdana; background-color:#cecece; border:solid 1px  
  #000000">O **Login** será feito via javascript em 5 segundos.</span>   
  <form action[="http://localhost/corpore.net/](http://localhost/corpore.net/)**login**.aspx?Auto**Login**Type=External**Login**" method="post">  
  <input type=hidden name="user" value="mestre" />  
  <input type=hidden name="pass" value="rm sistemas" />  
  <input type=hidden name="alias" value="CorporeRM" />   
  <input type=submit value="Fazer o **Login** agora" />  
  </form>   
  <script language=javascript>   
  function Auto**Login**OnLoad()  
  {  
  window.setTimeout("ScriptDo**Login**()", 5000);  
  }   
  //Se quiser fazer o **login** ao carregar basta chamar esta função function ScriptDo**Login**()  
  {  
  document.forms[0].submit();  
  }   
  Auto**Login**OnLoad();  
  </script>   
  </body>  
  </html>   
    
    
    
    
  **1.5.****Remoção dos****Links****na****página****de****Login**  
    
  Para alteração na página de Login, será necessário alterar o arquivo WEB.CONFIG. Nas tags indicadas, colocar o valor "false" para remoção.

  Para remoção do Link Currículo:

  <!--Informa se o link para o currículo está visível na página de login-->

  <add key="LoginCurriculoVisible" value="true"/>

  Para remoção do Link Cotação On-line:

  <!--Informa se o link para a cotação está visível na página de login-->

  <add key="LoginCotacaoVisible" value="true"/>

  Para remoção do Link Executor Web:

  <!--Informa se o link para o executor está visível na página de login-->

  <add key="LoginExecutorVisible" value="true"/>

  Para remoção do Link Processo Seletivo:

  <!--Informa se o link para processo seletivo está visível na página de login-->

  <add key="LoginProcSeletivoVisible" value="true"/>

  Para remoção do Link Esqueceu sua senha?:

  <add key="RecoverPassVisible" value="true"/>

  <!--Informa se o controle "Esqueceu sua senha" estará visivel na página de login.–>

  Para remoção da Seleção de Alias:

  Indica se o seletor de alias estará visível para o usuário-->

  <add key="HideAliasSelector" value="true"/>

    
    
  **1.6.****Alteração do Logo da****página inicial**  
    
  Para alteração na imagem de fundo do RM Portal, acesse o arquivo C:\CorporeRM\Corpore.Net\Images\LoginBG.JPG   
    
  Após fazer um back-up da Imagem, faça a alteração nesse arquivo colocando a nova imagem desejada. Ex:   
    
    
    

  Na versão 11.82.35.118 ou superior, o caminho para alteração da imagem do RM Portal é:

  C:\totvs\CorporeRM\Corpore.Net\Images\login

  Arquivo:

  fwlgn\_bg\_web.png

  Após a alteração, reinicie o Serviço do Host, o IIS e limpe o Histórico de Navegação no Browser.

    
    
    
    
  Obs: Por exigência do MEC, o link "Pesquisar acervo" deve estar visível, pois qualquer pessoa deve poder fazer essa pesquisa na Instituição.   
    
    
    
  **1.7.****Outras configurações****do WEB.CONFIG**  
    
  Algumas configurações no portal, são feitas através do arquivo WEB.CONFIG, presente no diretório \CorporeRM\Corpore.NET.   
    
  1- Configurando o Fale Conosco:   
    
  <!--Configurações do link "Fale Conosco": Ativa ou desativa o fale conosco.;  
    
  Em ContactAddress é definido o endereço que será enviado o e-mail. Caso este parâmetro esteja vazio o e-mail é enviado para o responsável pela  
  localidade. -->  
  <add key="EnableCallUs" value="true" />  
  <add key="ContactAddress" value="" />   
    
    
  2.Gestão de Conteúdo e Ferramentas  
    
    
  A parte de Gestão de Conteúdo, é toda aquela que está dentro do Item Portal.   
    
    
  A parte de Ferramentas, é onde se encontram o Cubo de Decisão, Relatórios e Consultas SQL   
    
    
    
  **2.1.****Cubos****de****Decisão**  
    
    
    
    
  Para configuração do CUBO para emissão no Portal WEB, siga as instruções abaixo:   
    
  **2.1.1.****Configuração da****extensão .CUB**  
    
  No Painel de Controle | Ferramentas Administrativas, clique na opção  
    
  **Internet Information** **Services**;   
    
    
    
    
    
  Nas propriedades do Corpore.NET, diretório virtual do Portal RM, acesse a aba **Cabeçalhos** **HTTP**;   
    
    
    
    
    
    
  Localize a opção de **Tipos** **de arquivos** para incluir um novo tipo MIME;   
    
  Clique no botão **Novo** **Tipo**;   
    
    
    
    
   Preencha os campos conforme figura abaixo, e clique em **OK**;   
    
    
    
    
  No Painel de Controle | Ferramentas Administrativas, clique na opção **Fontes** **de** **dados** **(ODBC)**;   
    
    
  Selecione a guia **Fonte** **de** **Dados** **do Sistema** ou **System** **DSN**, clique em **Adicionar** ou **ADD** para criar uma nova fonte de dados;   
    
    
    
    
  Selecione um driver para o qual deseja configurar uma fonte de dados, em seguida clique em **Finalizar** ou **Finish**  
    
  Informe o **Nome** da fonte de dados ODBC, obrigatoriamente **CORPORERMCOM**, e o **Servidor** onde a base de dados está localizada, depois clique em **Próximo** ou **Next**;   
    
    
    
   Selecione a opção de autenticação do Banco de Dados (Exemplo com SQL Server) com LoginID e Senha fornecidos pelo usuário, informe o **Login** **ID** e **Senha** **RM/rm**, respectivamente, e clique em **Próximo** ou **Next**;   
    
    
    
  Marque a opção **Alterar o** **Banco de** **Dados** **Padrão** e selecione a base de dados desejada, em seguida clique em **Próximo** ou **Next**;   
    
    
    
   Marque a opção **Usar** **configurações regionais ao** **exibir** **unidade monetária,** **números,** **datas** **e** **horas**, em seguida clique em **Finalizar** ou **Finish**;   
    
    
    
  Clique no botão **Testar Fonte** **de** **Dados**;   
    
    
    
    
  Clique no botão **OK** após o teste ter sido concluído com sucesso;   
    
    
    
  Verifique que o ODBC **CORPORERMCOM** foi criado, em seguida clique no botão **OK** para concluir;   
    
    
    
    
    
  Nas opções - parâmetros - RM BIS e defina a fonte de dados ODBC conforme abaixo:   
    
    
    
  **Após****Configuração acima,****é importante****verificar****as****questões abaixo.**  
    
    Entrar no IIS > selecionar pasta CorporeRM > Propriedades   
    
    
    
  Em disco virtual clicar em configuração   
    
    
    
    Na tela abaixo verificar se há alguma formato de Cubo. Se sim pode excluir   
    
    
    
    
  3.Configuração de Ambiente  
    
    
    
    
  Alterando o contexto do Portal WEB, você poderá definir a Coligada, a Filial e demais parâmetros.   
    
  **3.1.****Para****configurar a Localidade.**  
    
  O usuário deverá ter acesso a Localidade através do Portal EXE dentro do Menu Cadastro \ Permissões dos usuários   
    
    
    
  Acesse o usuário desejado e entre nos PROCESSOS.   
    
  Esse Cadastro é feito dentro de Cadastros \ Localidade.   
    
    
    
  **3.2.****Para****configurar Filial**  
    
    
    
    
  4.Configurando as WebParts  
    
    
    
  A página inicial do Portal é configurada através das WebParts.   
    
  As WebParts são configuradas no Link Administrar.   
    
    
    
  Ao acessar esse link, você entrará na página abaixo.   
    
  Obs: A tela aberta será aquela que foi visitada por último, no caso abaixo, as notícias.   
    
    
    
  Deve-se configurar primeiramente as WebParts presentes no Portal.   
    
    
    
  As WebParts já configuradas, irão aparecer nessa tela (WebParts).  
    
   Para configurar uma nova WebPart, clique na opção "Novo".   
    
  As novas WebParts criadas, deverão ser liberadas para os Perfis dos usuários por dentro do Portal EXE.   
    
    
    
    
  **4.1****Configurando****Notícias**  
    
    
    
    
  Defina um tipo de WebPart que será criada.   
    
    
    
    1- Inclua o título que será exibido na webpart  
    2- Inclua um caminho onde estará a imagem dessa webpart  
    3- Defina o tipo da webpart   
    
    
    
  No filtro, será definida a Localidade que terá acesso a essa WebPart   
    
  Após selecionar, clique na opção "Salvar / Fechar."   
    
    
  **4.1.1****Publicando Nova****Notícia**  
    
    
    
  Na parte de Administrar do Portal WEB, no link Manter Notícias, clique na opção "Novo", para cadastrar uma nova Notícia.   
    
  Como exemplificado na imagem abaixo, preencha os campos de Título e Corpo da Notícia.   
    
  Na aba de Filtro, deverão ser configuradas as Localidades, Grupo de Usuários e Usuários que poderão acessar e receber essas notícias no Portal.   
    
  Existe na parte superior, a opção para ANEXAR um arquivo para essa notícia.   
    
    
    
  Após configurar os campo do Filtro e preencher os dados da Notícia, clique na opção "Salvar / Fechar" para voltar para tela de Administrar.   
    
    
  **4.2****Configurando Pastas****e****Conteúdos**  
    
    
    
  Para incluir, clique na opção "Novo"   
    
    
    
  Defina o título da pasta, a descrição que ela terá e qual a hierarquia dela na árvore que será montada de pastas.   
    
    
  Defina as Permissões para acesso dessa pasta   
    
    
    
    
    
  Após salvar, a pasta ficará pendente para ser publicada. Entre no link Publicar Pasta e marque a pasta deseja.  
    
    
    
    
    
    
  Entre em Processos (a direita) e clique em Publicar Pasta(s)/Conteúdo(s)   
    
    
  Obs: Esse processo para publicação de pasta, é semelhante ao Publicar Conteúdo.   
    
    
  **4.3****Configurando****Classificados.**  
    
    
    
  Para criar novos classificados, acesse o link Portal->Administrar->Classificados.   
    
  Clique na opção "Novo", para abrir uma nova página.  
    
   Preencha os campos conforme o exemplo abaixo.  
    
  Na aba filtros, defina as localidades que irão ver esse classificado, os grupos de usuários e os usuários.   
    
    
    
  Após salvar o classificado, o mesmo deve ser aprovado para que apareça no Portal.   
    
    
    
  **4.4****Configurando****Aniversariantes**  
    
  Para inclusão de aniversariantes, é necessário a inclusão de uma nova WebPart que acesse o recurso Aniversariante dentro do Portal   
    
    
    
    
  Para inclusão da WebPart, abra a página de Administrar o Portal. Proceda da mesma forma para inclusão da WebPart de Notícias do Item 4.1.   
    
    
    
    
  Defina o Título da WebPart e qual o Controle que será usado.  
    
  Defina também o Filtro, de quem terá acesso a essa WebPart.   
    
  Quando configurado a WebPart dentro da página Principal os aniversário deverão aparecer seguindo os seguintes critérios:   
    
  1- Funcionário dentro do Labore tem data de aniversário, hoje, de ontem ou de amanha.  
  2- Usuário que está acessando o Portal, estar na mesma localidade do funcionário aniversariante.   
    
  OBS: Vale ressaltar que a localidade é configurada dentro do Portal como feito no item 3.1   
    
    
    
  **4.5****Configurando Enquetes**  
    
    
    
  Para criar novas Enquetes, acesse o link Portal->Administrar->Criar Enquetes.   
    
  Clique na opção "Novo", para abrir uma nova página.  
    
  Preencha os campos conforme o exemplo abaixo.   
    
  Na aba filtros, defina as localidades que irão ver essa enquete, os grupos de usuários e os usuários.   
    
    
    
  Após salvar a Enquete (Novo Registro), ficará visível a opção "Anexos", onde poderão ser criadas as Perguntas e respostas usadas nessa enquete.   
    
    
    
    
    
  Ao incluir uma Pergunta, será permitido escolher a forma de resposta da mesma:   
    
  Permitir a escolha de uma única opção como resposta   
  Permitir a escolha de várias opções como resposta  
  Permitir uma resposta aberta pequena  
  Permitir uma resposta aberta grande   
    
    
    
  Após salvar a pergunta da enquete, a mesma poderá ser visualizada da mesma forma que irá aparecer ao acessar o Portal RM.   
    
    
    
  Através do Link "Apuração da Enquete", estará disponível a quantidade de resposta e detalhes dos votos, caso o mesmo não seja "Sigiloso".   
    
    
    
    
    
  **4.6****Configurando Fóruns**  
    
    
  Para criar um novo Fórum, acesse o link Portal->Administrar->Fóruns.   
    
  Clique na opção "Novo", para abrir uma nova página.  
    
  Preencha os campos conforme o exemplo abaixo.   
    
  Na aba filtros, defina as localidades que irão ver esse Fórum, os grupos de usuários e os usuários.   
    
    
    
  **4.7****Configurando Vagas**  
    
  Para inclusão de vagas, é necessário a inclusão de uma nova WebPart que acesse o recurso Vagas dentro do Portal.  
    
    
    
  Para inclusão da WebPart, abra a página de Administrar o Portal. Proceda da mesma forma para inclusão da WebPart de Notícias do Item 4.1.   
    
  Após a inclusão da WebPart para exibir as vagas, acesse o Link Portal->Administrar->Vagas.   
    
    
    
    
  Clique na opção "Novo", para abrir uma nova página.   
    
  Preencha os campos conforme o exemplo abaixo.  
    
  Na aba filtros, defina as localidades que irão ver essa Vaga, os grupos de usuários e os usuários.   
    
    
    
  O campo Localidade de Atuação, será para descriminar no Portal, onde a vaga está disponível.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
