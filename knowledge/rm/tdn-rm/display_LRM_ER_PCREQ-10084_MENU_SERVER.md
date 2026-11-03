---
content_hash: 8f406b2c081e2b6a1272eb557eb26579e7ed33207f64f98863a5c2cc15455271
fetched_at: '2026-06-29T00:06:27.824406+00:00'
page_id: '233735381'
product: rm
source: tdn-rm
title: ER_PCREQ-10084_MENU_SERVER
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10084_MENU_SERVER
version: 143
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** |  | **Framework** |  |
| **Segmento Executor** |  | | |
| **Projeto1** |  | PCREQ-10028 |  |
| **Requisito1** |  | * [R\_FRW\_FRW002](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_FRW_FRW002 "R_FRW_FRW002") |  |
| **País** | ( X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

      Criar um mecanismo para que os itens de menu serão disponibilizados pelo servidor (RM.Host) e não mais pelo cliente (RM.exe e Portal).

      Com essa mudança, teremos os seguintes benefícios:

* Conseguiremos enviar os menus do RM.exe e do Portal para o Fluig.
* A fábrica de software da TOTVS mantém a flexibilidade em suas customizações, antes feitas diretamente no arquivo *menu.xml* e agora no banco de dados. Dessa forma, não necessitamos nos preocupar com atualização de versão, balanceamento de IIS (que necessitava da atualização do *menu.xml* em todos os ambientes), demandando grande esforço.
* Melhor usabilidade para customização dos itens de menu do portal pelo cliente, pois será feito por um cadastro.

Definição da Regra de Negócio

*Todos os produtos possuem o seu respectivo ActionModuleController e nele possui dois métodos sobrescritos (GetModuleMenu e GetProfileMenu) utilizados para retornar a ribbon winforms (com itens a serem apresentados na MDI .NET) e a ribbon profile (com os itens de menu que serão visualizados no portal).*

*Até agora existiam duas estratégias adotadas pelo produto para inserir itens que não serão visualizados na ribbon porém necessitam de permissão (ou seja, devem ser carregadas na treeView de segurança no cadastro de perfil), são elas:*

1. *Inserir esses itens na ribbon profile*
2. *Inserir esses itens na ribbon winforms e setar como visible false para que não sejam apresentados na nova MDI*

*Dessa forma a Lib fazia o merge dos itens de customização, gestão e ambiente na ribbon do produto e apresentava em winforms e na treeView de segurança no cadastro de perfil.*

*A partir de agora os métodos GetModuleMenu e GetProfileMenu estão como obsoletos e serão removidos nas próximas versões (ainda a definir), para isso é necessário que os produtos se adequem da seguinte forma:*

* *Implemente uma classe que herde de**RMSMenuController, defina os itens conforme necessidade (Pages,Groups,Itens e suas respectivas Policies).*  
  + **No modelo antigo tínhamos o xxxActionModuleController (com as policies) e xxxRibbonControl (com os itens de menu) e a ligação entre os itens de menu e suas policies é feita pela tag de segurança, **neste novo modelo está tudo dentro do controller**.**
* *Inserir esse controller na GMENU definindo a coluna MENUTYPE com os valores: 0 = winforms, 1 = Web, 2 = Profile.*
* *Foram criadas 3 propriedades na RMSActionModuleController (que é o ancestral que o produto usa para implementação da Ribbon), são elas:*

  1. *ServerControllerName = Nome do controller que representa a ribbon winforms.*
  2. *ServerWebControllerName = Nome do controller que representa a ribbon web.*
  3. *ServerProfileControllerName = Nome do controller que representa os itens que não pertencem a nenhuma ribbon, porém são itens que necessitam de permissão. Este item está separado para que tenhamos um modelo mais coerente, porém caso o produto utilize o modelo de inserir itens no controller winforms como visible false irá funcionar, porém não é o recomendado pela lib, pois vemos segregar a responsabilidade dos controllers.*
* *Setar a classe xxxActionModuleController com as novas propriedades.*

****1) Comportamento da aplicação Winforms****

*Irá buscar o controller setado na propriedade ServerControllerName e criar uma Ribbon com esses itens + customização, Gestão e Ambiente, lembrando que neste caso o método GetModuleMenu nem será chamado por framework.*

***2) Comportamento da aplicação Web (Portal)***

**Irá buscar todos os controllers inseridos na GMENU com o MenuType = 1, com esses menus em memória irá buscar se existe alguma customização dos itens de menu web na tabela GMENUCUSTOM e realizar as devidas adequações no menu, somente após isso entregar para o portal os itens de menu. O menu.xml é completamente ignorado por framework.**

***3) Comportamento da funcionalidade de gerenciamento de permissões (Perfil)***

*Irá buscar os 3 controllers e montar a treeView de permissões no perfil, vale ressaltar que a treeview não é montada com os itens que possuem tag de segurança 0 (zero) ou "null"; caso um agrupador esteja com 0 (zero) ou "null" ele e seus filhos não serão apresentados.*

***4) Como customizar os itens de menu do portal***

*Esse item será utilizado para customizar o menu do portal, essa customização será utilizada pela fábrica e/ou pelo cliente. Antes era feita diretamente no menu.xml, agora temos um tela onde é permitido realizar a manipulação desses itens com as seguintes regras:*

* *Para itens padrões do sistema só é permitido habilitar/desabilitar*
* *Para itens novos é permitido inserir e colocá-lo em qualquer posição.*
* *Portando um item padrão que eu queira alterar o título, por exemplo, é necessário desabilitar o mesmo e criar um item customizado com a mesma action.*

*A funcionalidade está disponível em Gestão de Conteúdos/Cadastros/Menu Portal.*

***5) Foi criado uma parâmetro para ligar/desligar o menu server.***

*ENABLEMENUSERVER (Default false) e a partir da versão 12.1.16 o Default será true.*

***Tabelas Utilizadas***

1. *GMENU*
   1. *Tabela que armazena os menus do RM, a coluna "MenuType " indica se o item é winforms, web ou profile.*
2. *GMENUCUSTOM*
   1. *Tabela que indica os itens customizados pela fábrica ou pelo cliente, a coluna "MENUTYPE" indica de o item é Padrão ou customizado.*

Customização de itens de menu (somente para o Portal)

Defina se o item será Padrão ou Customizado:

     Para o item Default será permitido alterar a visibilidade, posição  e caption do mesmo:

## Visibilidade:

1. Selecione o tipo do menu como Padrão, e selecione o item de menu desejado na TreeView conforme print abaixo.
2. *Altere a visibilidade do mesmo*
3. *Esse item será removido do portal*

## ***Posição:***

1. *Selecione o tipo do menu como Padrão, e selecione o item de menu desejado na TreeView conforme print abaixo.*
2. *Altere a posição do mesmo.*
3. *A posição será alterado no portal.*

## **Caption:**

1. Selecione o tipo do menu como Padrão, e selecione o item de menu desejado na TreeView conforme print abaixo.
2. *Altere o caption do mesmo.*
3. *O Caption será alterado no portal*  
   *.*

*Para itens customizados é permitido criar novas Páginas, Grupos, Itens e Subitens, definindo a posição que o  mesmo será inserido.*

1. *Selecione o Tipo de Menu como customizado, e selecione o item de menu pai na TreeView conforme print abaixo:*
2. *Preencha os dados do item*  
     
   *Identificador: É o Identificador do item na arvore de menu.*  
   *Idenficicador do controller: É o identificador da classe que representa o menu.*  
   *Identificador do pai: É o identificador do pai do item que será criado na arvore de menu.*  
   *Caption: É o texto que será exibido no portal.*  
   *Descrição: Descrição do menu.*  
   *Link da imagem: Caminho interno do ícone do menu que será criado.*  
   *Tag de segurança: Tag de segurança do menu que será criado.*  
   *Action: Nome da action do menu que será criado.*  
   *NavigateURL: Link externo caso necessite de um menu que faça um redirecionamento para outras páginas.*
3. **Esse item será inserido conforme dados cadastrados.**  
     
   4. Após a criação de um item customizado que possua Tag de segurança, será criado no perfíl do módulo criado, a arvore de permissionamento do item customizado.

   Observação

   Itens customizados que não possuam filhos, que possuam Actions ou NavigateURL preencidos, não serão exibidos no Portal.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
