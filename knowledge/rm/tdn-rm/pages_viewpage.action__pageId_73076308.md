---
content_hash: 0325a17c3d7791bea50cbb79414ba6465885d2ca895c4a7718b7fe71d1ee7f6b
fetched_at: '2026-06-29T00:11:28.353519+00:00'
page_id: '73076308'
product: rm
source: tdn-rm
title: Alterar a página principal do Portal Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73076308
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.xx |
| **Processo** | **:** | Portal Web |
| **Subprocesso** | **:** | Alterar a página principal do Portal Web |
| **Data da publicação** | **:** | 01/08/2013 |

É possível alterar a página principal do portal web, porém qualquer alteração efetuada nos códigos será de total responsabilidade do cliente. Recomendamos neste caso, um programador web para efetuar as alterações e / ou customizações necessárias.

Página Inicial

As imagens estão localizadas nos seguintes diretórios:

C:\totvs\CorporeRM\Corpore.Net\Images\login

C:\totvs\CorporeRM\Corpore.Net\Images\

Para alterar via código, deverá ter conhecimento nas extensões css. Como exemplo, para alterar ou redirecionar o "**moresocialmorebusiness"** localize o arquivo style.css (C:\totvs\CorporeRM\Corpore.Net\Styles).

Neste arquivo terá as informações das imagens e redirecionamento das mesmas.

.login .main .moresocialmorebusiness {  
[width:575px](http://width:575px);  
[height:79px](http://height:79px);  
background: url(../Images/login/moresocialmorebusiness.gif) no-repeat;  
[display:block](http://displayblock);  
[float:left](http://floatleft);  
text-indent:-9999px;  
[margin:5px](http://margin:5px) 0px 0 0;  
Página 2  
}  
.login .main .box-left {  
[width:575px](http://width:575px);  
}  
.login .main h2 {  
[width:350px](http://width:350px);  
[float:left](http://floatleft);  
color:#167CC3;  
[font-size:21px](http://font-size:21px);  
}  
.login .main a.thumb-video {  
width: 208px;  
[height:149px](http://height:149px);  
background: url(../Images/login/Frame\_Video\_Pequeno.jpg) no-repeat;  
display: block;  
[float:right](http://floatright);  
}  
.login .main h5 {  
[clear:left](http://clearleft);  
}  
.login a.entre-em-contato {  
width: 108px;  
[height:21px](http://height:21px);  
background: url(../Images/login/ico-contato.gif) no-repeat;  
display: block;  
font-size: 13px;  
[padding-left:30px](http://padding-left:30px);  
[margin:10px](http://margin:10px) 0 0 40px;

Para eliminar / retirar os links Currículo, Cotação On-line, Executor web e etc, será através do arquivo web.config (C:\totvs\CorporeRM\Corpore.Net) para as tags:

Valor falso irá retirar o link do portal.

\*\*Este procedimento continua o mesmo das versões anteriores

<!--Valor que informa se deve carregar o primeiro item do menu ao fazer login da aplicação-->

<add key="LoadDefaultMenuOnLogin" value="false"/>

<!--Informa se o link para o currículo está visível na página de login-->

<add key="LoginCurriculoVisible" value="true"/>

<!--Informa se o link para a cotação está visível na página de login-->

<add key="LoginCotacaoVisible" value="true"/>

<!--Informa se o link para o executor está visível na página de login-->

<add key="LoginExecutorVisible" value="true"/>

<!--Informa se o link para o processo seletivo está visível na página de login-->

<add key="LoginProcSeletivoVisible" value="true"/>

<!--Informa se o serviço de mensagens dentro dos controles está ativo.

Visualizamos as mensagens dentro de seletores de filtro, na caixa do localizar, etc.-->

<!--Informa se o controle "Esqueceu sua senha" estará visivel na página de login.-->

<add key="RecoverPassVisible" value="true"/>

Para retirar os itens como Perfil, segurança, Mobilidade e etc, será através do arquivo login.aspx (C:\totvs\CorporeRM\Corpore.Net) através do código.

Ex: <div class="box-destaques">  
 <div class="destaque-perfil" align="center">  
 <h3> Perfil</h3>  
 </div>  
 <div class="destaque-seguranca" align="center">  
 <h3> Segurança</h3>  
 </div>  
 <div class="destaque-mobilidade" align="center">  
 <h3> Mobilidade</h3>  
 </div>  
 <div class="destaque-produtividade" align="center">  
 <h3> Produtividade</h3>  
 </div>  
 <div class="destaque-integracao" align="center">  
 <h3> Integração</h3>  
 </div>  
 <div class="destaque-rede-de-empresas" align="center">  
 <h3>  
 Rede de empresas</h3>  
 </div>  
 <div style="width: 158px; padding: 35px 10px 10px 30px; float: left;  
 display: block">  
 <h5>  
 Quer saber mais sobre  
 <br />

Alerto novamente que os exemplos e / ou caminhos citados acima podem ser alterados, onde a total responsabilidade é do cliente, onde recomendamos um programador web ou TI da sua empresa. Qualquer erro apresentado nesta tela devido à alteração, o suporte irá solicitar a reinstalação do produto sem a obrigatoriedade de localizar ou acertar os códigos alterados.
