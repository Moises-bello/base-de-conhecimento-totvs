---
content_hash: 18e822ff573bb6ce41efbb0262bcb14c33ecbafef668fbf1acc6f5c18e0f5645
fetched_at: '2026-06-29T00:11:56.717460+00:00'
page_id: '870392186'
product: rm
source: tdn-rm
title: 2- URL Rewrite - Portal Gestão educacional ( Sala de Atendimento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=870392186
version: 11
---

A instalação deve ser realizada no servidor do portal desejado

Atenção

**A partir da versão 12.1.2402**

É possível utilizar as api's do host diretamente, sem o uso do módulo do **URL** **Rewrite**. Para isso deve expor o host para a web e informar o endereço do host nos arquivos de config dos portais.

**Importante** ficar atento a questões de **segurança** ao expor o host para a web. A forma como será utilizado fica a critério da instituição.

0.1tempfadeInstalaçãofade

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do URL Rewrite**: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após a Instalação, será criado um ícone: “URL Rewrite” no IIS

Configuração Rewritefade

Deve ser necessário configurar **duas** regras para o **URL** **Rewrite***:*

* A 1º regra **(regra comum para todas as versões)** é utilizada para direcionamento de **API** onde não é necessário passar o alias selecionado;
* A 2º regra **(apenas para versões anteriores à 12.1.2402)** é utilizada para as **API** onde é necessário passar o alias selecionado.

Exclusivamente para os novos portais

A configuração deve ser realizada **exclusivamente** nos portais: **Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor** em: **Sites | Default Web Site | FrameHTML | Web | App |Edu | 'Pasta referente ao portal'.** Caso a configuração **não** seja realizada no caminho especificado anteriormente, o portal do Aluno poderá ser impactado.

A ordem das regras deve ser respeitada.

A ordem das regras deve ser respeitada.

Regra comum para todas as versões

**1.**Acessar o IIS -> Ir no aplicativo que está sendo configurado (Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor) -> URL *Rewrite*

**2.**Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule**.*

**3.**No campo "**Name**" informar um nome para a regra que está sendo criada

**4.**Na opção: Match URL, no campo: "**Pattern"** inserir as informação: api/(.\*)

**5.**Na opção*: "**Actions"**, no campo: Rewrite URL informar o link: [http://nome\_da\_maquina\_do\_host:porta/api/{R:1](http://localhost:8052/%7BR:1)}*

Regra adicional necessário para versões anteriores a 12.1.2402

**Para as versões anteriores à 12.1.2402** é necessário configurar uma nova regra

Atenção

A porta utilizada deve ser a mesma que está configurada na chave "ApiPort" no arquivo de host **RM.Host.Service.exe.config**.

**1.**Acessar o IIS -> Ir no aplicativo que está sendo configurado (**Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor**) -> URL *Rewrite*

**2.** Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule**.*

**3.** No campo "**Name**" informar um nome para a regra que está sendo criada

**4.** Na opção: Match URL, no campo: "**Pattern**" inserir as informação: aliasname\.(.\*)/api/(.\*)

**5.**Na opção*: "**Actions"**, no campo: Rewrite URL informar o link: [http://{R:1}.nome\_da\_maquina\_do\_host:porta/api/{R:](http://localhost:8052/%7BR:1)2}*

**6.**Marcar a opção*: "**Stop processing of subsequent rules"***

Configuração Rewrite TOTVS Educa Mobile (exibição das Salas no App)fade

Essa configuração é necessária para que as salas sejam exibidas no menu: Mensagens | Sala de Atendimento. Para mais detalhes [Parametrização da Sala de Atendimento no App: Meu eduCONNECT](https://tdn.totvs.com/x/7l3rJ)

false

**Para que a comunicação entre o Portal Gestão Educacional e o App: Meu eduCONNECT possa ocorrer normalmente, é necessário que a porta da API configuração do Rewrite do Portal Gestão Educacional e do TOTVS Educa Mobile estejam na mesma porta.**

**1.**Acessar o IIS -> Ir no aplicativo que está sendo configurado EducaMobile -> URL *Rewrite*

**2.**Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule***

**3.**No campo "**Name**" informar o endereço:  **TOTVS\_API\_ReverseProxyInboundRule**

**4.**Na opção: Match URL, no campo "**Pattern"** inserir a informação: **(.\*)**

**5.**Na opção: "**Conditions"**, clicar no botão: Add. e inserir a informação: **{REQUEST\_URI}  /api/(.\*)**

**6.**Na opção: "**Actions"**, no campo: Rewrite URL informar o link: **<http://localhost:8052/{R:1>}**

**Importante**:

* A URL a ser utilizada é a do servidor onde encontra-se instalado o Host, como exemplo, utilizamos o endereço <http://IPdoServidorHost:8052/{R:1>} 
  + Em alguns casos o servidor do Host é diferente do servidor Web, então neste caso, deve-se utilizar o endereço do servidor do Host.
* Verificar a porta configurada na tag ApiPort do arquivo de configuração do Host, como exemplo, utilizamos a porta 8052.
* Em alguns cliente a parte da URL {R:1} é substituído por {C:0}

Verificar qual é a parte da URL {R:1} ou {C:0}

Utilizar o endereço **<http://EndereçodoServidorWeb/EducaMobile>**/api/framework/v1/menus/dd6626a5aa1e3c2c2ad79198824f67a4?$filter=tagMenu eq '808100759'&companyId=1

**7.**Em seguida, clicar no botão: **Aplicar**
