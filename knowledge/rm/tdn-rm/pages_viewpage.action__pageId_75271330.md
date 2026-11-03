---
content_hash: aa7028d45e62672358580fb9b272b1fc0065a36aadf3caf08981c28f8bf6522e
fetched_at: '2026-06-29T00:11:33.167877+00:00'
page_id: '75271330'
product: rm
source: tdn-rm
title: Criação de Categoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75271330
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.xx |
| **Processo** | **:** | Categoria |
| **Subprocesso** | **:** | Criação de Categoria |
| **Data da publicação** | **:** | 23/09/2013 |

Para realizar a importação dos cubos é necessário ter uma categoria associada ao seu perfil.

O primeiro passo que deverá ser feito é criar uma nova categoria para associar ao seu perfil. Caso não possua acesso ao RM Bis pelo executável é necessário realizá-lo através da nova MDI:  acesse o diretório "C:\totvs\CorporeRM\RM.Net" da máquina e clique no executável "RM.exe".

Depois que logar na nova MDI o sistema irá abrir a tela principal. Haverá um ícone da TOTVS, clique no mesmo e em seguida escolha a opção "Serviços Globais". Este é o local onde será concedida a permissão do seu usuário no RM Bis.

Selecione a guia "Segurança" e nos ícones da guia você irá clicar no ícone "Perfis". Escolha na opção "Sistema" a opção "Inteligência de Negócios". Em seguida selecione o perfil DBA e clique duas vezes no mesmo.

O sistema irá abrir a tela de permissões e configurações deste perfil. Neste formulário você deverá clicar na guia "Acesso a Menus". O sistema irá mostrar todos os menus que este perfil possui disponível.

Clique no botão "Recolher Tudo".   
   
   
   
 Em seguida clique no botão "Permitir Acesso". Desta forma você estará atribuindo acesso total a este perfil. Clique em salvar as alterações.

Depois de feita a atribuição de permissão para este perfil você irá clicar no ícone "Usuários" que fica ao lado do ícone perfil já citado. Escolha "Inteligência de Negócios" novamente na opção "Sistema". Selecione o seu usuário e atribua para o mesmo perfil que você acabou de atribuir permissão. No caso o Perfil DBA.   
   
   
   
   
 Depois de atribuído as permissões ao perfil e relacionado o perfil ao usuário faça logout na nova MDI. Para realizar o logout você deverá clicar novamente no ícone da Totvs e escolher a opção Logout/Login.

Depois de feito o login novamente você deverá clicar no ícone da Totvs e escolher a opção "Inteligência de Negócios".   
   
   
   
   
   
 O sistema irá modificar as opções de menu. Você deverá escolher a aba "Gestão Estratégica" e clicar no ícone "Categorias". Em seguida clique no ícone botão "Incluir Categoria".

Depois que você clicar no botão "Incluir" o sistema irá abrir a tela de cadastro de categoria. Atribua um novo nome a esta categoria e descrição.   
   
   
   
   
 Em seguida você irá clicar no botão "Incluir" na aba "Perfis autorizados".

Para facilitar a pesquisa clique no filtro e escolha "Cód. Sistema" e digite a letra "G". O sistema irá listar todos os perfis atribuídos existentes para "Inteligência de Negócios" (RM Bis). Depois de selecionado o perfil que atribuímos permissão total clique no botão OK.   
   
   
   
   
 Depois que você clicar em OK marque todas as opções da tela seguinte.

Repita a operação porem selecionando o perfil que o seu usuário está atribuído no RM Labore. Para facilitar a pesquisa digite a letra "P" tendo o filtro "Cód. Sistema". Selecione o Perfil mestre e em seguida atribua permissão total a este perfil para esta categoria. No final você verá a tela abaixo onde você deverá salvar e clicar em Ok depois.

Depois de criada a categoria, saia da nova MDI, acesse o RM Labore e faça o mesmo procedimento que já foi instruído nas interações anteriores.

Selecionando os cubos a serem importados.

Atribuindo a importação para todas as coligadas.

Porém diferente da primeira instrução quando você clicar na aba "Parâmetros" você irá pesquisar pela categoria ("RH") que criamos na nova MDI.

Depois de selecionada a categoria correta clique no botão "Executar" que a importação dos objetos será  concluída com sucesso.

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
