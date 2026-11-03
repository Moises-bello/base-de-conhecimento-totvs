---
content_hash: 6262d3c712d39aa61f2584100f796fc65a8736ac2f63a59486fe6e821124c4e6
fetched_at: '2026-06-29T00:11:16.492158+00:00'
page_id: '668648864'
product: rm
source: tdn-rm
title: 01.1 - Aplicação Externa (Sessão do Usuário)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668648864
version: 31
---

Essa funcionalidade tem como objetivo fornecer as informações do contexto do Educa Mobile à aplicação de terceiros, para que seja possível realizar algumas integrações através de uma chamada por dentro do Educa Mobile.

Para utilizar este recurso, é necessário realizar as parametrizações abaixo:

## **01. PARAMETRIZAÇÃO**

É necessário habilitar item de menu: **Aplicação Externa** dentro do arquivo **Menu.xml** do TOTVS Educa Mobile localizado em "C:\TOTVS\CorporeRM\EducaMobile\Areas\Educacional"

**1-** Localizar os seguintes itens referentes a **Aplicação Externa** para usuários do tipo **Aluno** e/ou **Professor**, retirando os comentários das tags MenuItem, conforme abaixo:

Item de menu referente ao acesso de alunos:

Item de menu referente ao acesso de professores:

**2-** Definir as permissões de acesso a estes itens de menu: Cada item de menu é exibido para o usuário logado no Educa Mobile conforme a sua permissão existente no **Perfil do usuário** correspondente ao seu usuário. Para que estas permissões não sejam validadas para a exibição de um item de menu, e todos os usuários tenham acesso ao item independente das suas permissões, basta deixar o conteúdo da tag **<Tag>0</Tag>** com o valor **0** no seu conteúdo. O valor 0 indica que não será feito nenhuma validação de permissão para este item.

Para exibir este item de menu conforme permissões do item "URL's externas" no cadastro de Perfil, defina os seguintes valores (que são valores fixos referente ao código do respectivo perfil:

ID de segurança do item "URL's externas" para **aluno**: **808100537**

ID de segurança do item "URL's externas" para o **professor**: **808100572**

**3-** A tag chamada **SetContext** especifica se antes do redirecionamento para o endereço especificado na tag **ExternalURL,** será aberto a tela de seleção de contexto para o usuário logado no Educa Mobile. 

1. Para especificar que o contexto deve ser aberto antes do redirecionamento, a tag **SetContext** deve conter o valor "S". A tela de seleção de contexto só será aberta se o aluno ou professor ainda não estiver selecionado nenhum contexto anteriormente, e as variáveis e sessions internas do Educa Mobile ainda não estiverem preenchidas.
2. Se o valor da tag **SetContexto** conter qualquer valor diferente de "S" ou até mesmo não existir, não será exibido a tela de seleção de contexto antes do redirecionamento. Se o contexto do aluno ou professor já tiver sido selecionado antes da utilização deste item de menu, o contexto não será alterado ou apagado.

**4-** O tipo de usuário deverá ser especificado corretamente através da tag **TipoUser** como sendo "A" para aluno e "P" para professor. O contexto que será exibido para o usuário será baseado nesta informação. Esta tag é obrigatória conforme os outros itens de menu.

**5-** Conceder as as devidas permissões no cadastro de perfil de aluno e professor, caso especificado no **item 2**:

**Aluno:** Educacional | Educacional (Portal) | Acadêmico | URL's externas

**Professor:** Educacional | Educacional (Portal) | Professor | URL's externas

**7-** Especificar a URL da aplicação externa, ou a URL da página intermediária na tag **ExternalURL**, conforme exemplo abaixo:

Menu Professor:

Menu Aluno:

Regras de validação

Nos casos em que for utilizado o WebService **GetSession** para recuperar a sessão do usuário, a aplicação que fará a requisição deve estar no mesmo **Site** do **IIS** onde o Educa Mobile foi instalado, conforme imagem abaixo. Caso seja outra tecnologia ou servidor web, sugerimos fazer uma página intermediária para fazer a requisição de coleta da sessão e depois redirecionar para a aplicação externa.

**8-** Acessar o IIS, clicar com o botão direito do mouse em Default Web Site, e clicar em adicionar aplicativo.

Nesta janela informa no campo Alias o nome da sua aplicação e no caminho físico informar o local onde está a pasta da aplicação externa.

Após informar os passos acima a sua aplicação vai ficar no mesmo **Site** do **IIS** onde o Educa Mobile foi instalado conforme print abaixo:

## **02. LOCALIZAR A SESSÃO DO USUÁRIO**

Acessar o arquivo **Web.config** em "C:\TOTVS\CorporeRM\EducaMobile" e incluir o portal (desejado) na tag: **<add key="DomainAccessSession" value="insira\_aqui\_a\_URL\_do\_portal" />**

## **03. EXEMPLO - LOCALIZAÇÃO DOS DADOS DOS USUÁRIOS**

Ao logar no portal TOTVS Educa Mobile e clicar no menu correspondente a **Aplicação Externa**, será apresentado a informação do contexto do usuário (logado) em formato JSON.

> Aluno

> Professor

Para formatar os dados no formato legível, poderá formatar de duas formas:

* Pelo link: <https://jsonformatter.org/> e colar a informação no campo a esquerda da tela e clicar em: Format/Beautify.

* Pelo POSTMAN: Acessar o Postaman, clicar em raw, em seguida selecionar a formatação JSON e clicar em Beautify.

Exemplo de uma 'Aplicação Externa'

<?xml version="1.0" encoding="UTF-8"?>  
<HTML>  
<title></title>  
 <head></head>  
 <body>  
  <h1>GetSession</h1>  
  <label id="lb"></label>    
  <script lang="javascript">  
    var xhr = new XMLHttpRequest();  
    xhr.open('GET', '[http://DOMININIO/EducaMobile/EduSessao/GetSession](http://192.168.13.50/EducaMobile/EduSessao/GetSession)');  
    xhr.responseType = 'json';  
    xhr.onload = function() {  
      if (xhr.status === 200) {  
          var jsonString = JSON.stringify(xhr.response);  
        document.getElementById("lb").innerHTML  = jsonString;  
      }  
    };  
    xhr.send();  
  </script>     
 </body>  
</HTML>
