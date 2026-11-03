---
content_hash: a4b65d3a2c0c44823e80770f1c4cac1fcd821dda0f99fee0141b19491daede19
fetched_at: '2026-06-29T00:05:55.966098+00:00'
page_id: '147818073'
product: rm
source: tdn-rm
title: Alias default no RM Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/Alias+default+no+RM+Portal
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.XX |
| **Processo** | **:** | RM Portal - Web |
| **Subprocesso** | **:** | Definir alias default no login no RM Portal |
| **Data da publicação** | **:** |  |

Para remover a opção para selecionar o Alias no login no RM Portal, siga as orientações abaixo:

As tags utilizadas nesta configuração são:

<add key="HideAliasSelector" value="true"/> → Indica se o seletor de alias estará visível para o usuário. Esse recurso deve ser utilizado com a TAG DefaultAlias

<add key="DefaultAlias" value="CorporeRM"/>  → Informa o Alias padrão quando utilizada a opção HideAliasSelector. Esse recurso é complementar à utilização da TAG HideAliasSelector

**Exemplo do comportamento de ocultação de Alias na prática:**

Tela de login padrão, onde o Alias é apresentado:

**Ocultando o Alias:**

Acesse o arquivo Web.config (UNIDADE:\totvs\CorporeRM\Corpore.Net) e edite o mesmo.

No bloco <appSettings>, pesquise a tag HideAliasSelector. Para ocultar o Alias o valor da tag deve ser true = verdadeiro, ou seja, ocultar Alias, sim.

<add key="HideAliasSelector" value="true" />

Deve-se informar o Alias padrão quando utilizada a opção HideAliasSelector. Esse recurso é complementar à utilização da TAG HideAliasSelector

Logo abaixo da tag HideAliasSelector adicione a tag <add key="DefaultAlias" value="CorporeRM"/>, conforme exemplo no print abaixo e salve o arquivo:

Ao logar no RM Portal, a opção para selecionar o Alias não será apresentada e será utilizado o Alias padrão configurado:

Segue uma forma para que o RM Portal não apresente a opção de qual o Alias deseja utilizar.   
   
   
 Obs. Esse procedimento só é válido quando o acesso ao portal é realizado por dentro de outro site.

<http://localhost/Corpore.Net/Login.aspx?DefaultAlias=CorporeRM>   
   
 Assim a opção ficará inibida na tela de login, Sendo necessário informar somente Usuário e Senha.

Entretanto quando o usuário solicitar Sair do RM Portal.

A tela de login voltará a apresentar a  opção do alias.

Para que isso não ocorra, basta seguir as orientações abaixo.

No caminho "C:\totvs\CorporeRM\Corpore.Net"  editar o arquivo Web.config  e alterá-lo conforme exemplo abaixo.

Na tag abaixo deve ser inserido o link informando o Alias default.

  <add key="AfterLogoutPage" value="<http://localhost/Corpore.Net/Login.aspx?DefaultAlias=CorporeRM>"/>

Assim quando o usuário clicar em sair o RM Portal, ele irá direcionar para o link informado na tag.

No caso a página de login do RM Portal sem a opção do alias, mas poderia  ser o site da empresa por exemplo.

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
