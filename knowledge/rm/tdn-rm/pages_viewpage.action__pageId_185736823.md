---
content_hash: 19e4d36cf8a7d6aa06d7d1743437dd54df5018f3b0263ab096447cd732733929
fetched_at: '2026-06-29T00:05:58.152158+00:00'
page_id: '185736823'
product: rm
source: tdn-rm
title: Menu Esqueceu sua senha? RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185736823
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.xx |
| **Processo** | **:** | RM Portal - Gestão de Conteúdos |
| **Subprocesso** | **:** | Menu Esqueceu sua Senha? |
| **Data da publicação** | **:** | 03/03/2015 |

Caso o recurso "Esqueceu sua Senha?" no RM Portal (Corpore.Net) esteja apresentado alguma inconsistência, seguem abaixo algumas orientações para verificação.

Acesse o diretório C:\totvs\CorporeRM\Corpore.Net, localize o arquivo Web.config, abra-o no bloco de notas e confirme se a tag abaixo está com valor "True" :

<!--Informa se o controle "Esqueceu sua senha" estará visivel na página de login.-->  
 <add key="RecoverPassVisible" value="**true**" />

Acesse o Menu Opções -> Parâmetros Globais -> Aba Envio de E-mail e confirme se é possível enviar e-mail de teste, para coligada atual e coligada global:

Mais informações sobre o Envio de E-mail na linha RM disponíveis no Link abaixo:

Acesse o cadastro de coligadas e confirme se existe e-mail preenchido:

Confirme se o Browser utilizado está homologado, vide documento de Portabilidade e Arquitetura, conforme link abaixo:

Confirme se o Modo Server está iniciado. Acesse a nova MDI (RM.exe, localizado em C:\totvs\CorporeRM\RM.Net), Ambiente -> Cockpit:

Realize um teste enviando uma consulta SQL por e-mail para confirmar o funcionamento dos processos:

Menu Utilitários -> Consultas SQL:

Realizar a consulta sql abaixo e confirmar se existe o CODSERVICO "**RMEsqueciMinhaSenha**":

Acesse o Menu Opções -> Parâmetros Globais -> Aba Gerais e confirme se a URL de acesso ao portal está preenchida:

Mais informações em:

Na tela de login do RM Portal, após selecionado o Alias, clique no menu "Esqueceu sua Senha?". Será aberto um pop-up:

Neste pop-up existe um endereço. Confirme se o mesmo apresenta o nome do alias selecionado antes de solicitar recuperação da senha.

Exemplo: No print acima foi selecionado o Alias CocporeRM. No link abaixo o nome do Alias é CorporeRM:

<http://bhd000000301/corpore.net/SharedServices/LibPages/RecoverPassConfirmation.aspx?UserCaption=5LK%5c9F%5c3D%5c023%5c5B&ConfirmationCaption=%5c7B%5cFAbP%5c06%5c11Q%5c7C&RecoverContainerClassName=ASP.login_aspx,%20App_Web_gpluqekv,%20Version=0.0.0.0,%20Culture=neutral,%20PublicKeyToken=null&RecoverInitializeMethodName=GetRecoverPassServer&ServiceAlias=CorporeRM>

Neste exemplo, o nome do Alias selecionado foi CocporeRM (ServiceAlias=CorporeRM). 

Após essas validações, confirme o funcionamento do recurso "Esqueceu sua Senha?" no RM Portal. Sugerimos que todos os testes sejam realizados localmente, no Servidor de Portal. No Browser, informe:

[http://localhost/corpore.net/Login.aspx](http://bhd000000301/corpore.net/Login.aspx)

Caso obtenha sucesso, será apresentada a tela abaixo, informando o envio do e-mail:

Após receber o e-mail, clique no link e altere a senha conforme desejado:

* Para maiores informações:

  Icon

  Consulte o[Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

  **COMUNIDADE**[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

  **Canais de Atendimento:**

  **Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)
