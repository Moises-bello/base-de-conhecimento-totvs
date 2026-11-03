---
content_hash: 70404c7fe645f7ce027401151495b7a6674556cb21bc9825df7738dce32ef46a
fetched_at: '2026-06-29T00:10:58.925291+00:00'
page_id: '607847121'
product: rm
source: tdn-rm
title: Nova tela de Login Totvs RM Portal - 12.1.32 ou Superiores
type: documentation
url: https://tdn.totvs.com/display/LRM/Nova+tela+de+Login+Totvs+RM+Portal+-+12.1.32+ou+Superiores
version: 3
---

**1. Acessando o Portal:**

Na máquina que está instalado o Portal, digite <http://localhost/Corpore.Net>

**2. Alteração das logomarcas**

A nova página de Login possui 2 logomarcas (**Cabeçalho** e **Rodapé**)

**2.1. Alterar logomarca do Cabeçalho**

   1- Abra a pasta UNIDADE:\CorporeRM\Corpore.Net\Nova\_Tela\_Login\img\  
   2- Substitua a imagem "logo.png" pela logo desejada.

**2.2. Alterar logomarca do Rodapé**

   1- Abra a pasta UNIDADE:\CorporeRM\Corpore.Net\Nova\_Tela\_Login\img\  
   2- Substitua a imagem "logo\_cinza.png" pela logo desejada.

**3. Alteração do ícone**

   1- Abra a pasta UNIDADE:\CorporeRM\Corpore.Net\Nova\_Tela\_Login\  
   2- Substitua o ícone "favicon.ico" pelo novo ícone.

**4. Remoção dos Links na página de Login**

Para alteração na página de Login, será necessário alterar o arquivo **WEB.CONFIG**.

Nas tags indicadas, colocar o valor "false" para remoção.

Para remoção do Alias:

Deve ser utilizado juntamente com o DefaultAlias→

<add key="HideAliasSelector" value="false"/>

Para remoção do Link Esqueceu sua senha?:

<add key="RecoverPassVisible" value="true"/>

<!--Informa se o controle "Esqueceu sua senha" estará visivel na página de login.–>

Para remoção do Link Currículo:

<!--Informa se o link para o currículo está visível na página de login-->

<add key="LoginCurriculoVisible" value="true"/>

Para remoção do Link Cotação On-line:

<!--Informa se o link para a cotação está visível na página de login-->

<add key="LoginCotacaoVisible" value="true"/>

Para remoção do Link Executor Web:

<!--Informa se o link para o executor está visível na página de login-->

<add key="LoginExecutorVisible" value="true"/>

Para remoção do Link Processo Seletivo:

<!--Informa se o link para processo seletivo está visível na página de login-->

<add key="LoginProcSeletivoVisible" value="fals"/>

Para remoção do Link Pesquisar Acervo:

<!--Informa se o link para Pesquisar acervo está visível na página de login-->

<add key="LoginPesquisaAcervoVisible" value="true"/>

Pesquisar acervo

Por exigência do MEC, o link "**Pesquisar acervo**" deve estar visível, pois qualquer pessoa deve poder fazer essa pesquisa na Instituição.

Para remoção do Link Forum:

<!--Informa se o link para o forum está visível na página de login-->

<add key="LoginForumVisible" value="true"/>

Para remoção do Link Certificador de Relatórios:

<!--Informa se o link para o Certificador de Relatórios está visível na página de login→

<add key="LoginReportsCertificateVisible" value="true"/>

**5.** **Alteração do CSS da página inicial**

Com as melhorias lançadas no release 12.1.32, agora é possível realizar alterações na tela de inicial do Portal RM através de configuração de estilos (css).

Importante

Recomendamos que a execução dos passos abaixo sejam realizadas por profissional com expertise em programação web (Front-end).

Para manipular a página de inicial através de CSS siga os passos abaixo:

1. Crie/Edite o arquivo UNIDADE:\TOTVS\CorporeRM\Corpore.Net\Nova\_Tela\_Login\css\**customizeLogin.css**
2. Através deste arquivo é possível customizar completamente a página de inicial sendo possível alterar cores, formatos, fontes, imagens entre outros.

**6.** **Bootstrap**

A partir da versão 12.1.32, o Bootstrap possui a versão atualizada 3.4.1. Em caso de lançamento de uma nova versão do bootstrap, a mesma pode ser verificada no site oficial [https://getbootstrap.com/docs/3.4/getting-started/](https://getbootstrap.com/docs/3.4/getting-started/ "Seguir link") ,e deve ser atualizada nos arquivos:

1. CorporeRM\Corpore.Net\Nova\_Tela\_Login\css\bootstrap.min.css
2. Corpore.Net\Nova\_Tela\_Login\js\bootstrap.min.js
