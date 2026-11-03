---
content_hash: 2fd42be06a0591b119db224a91d5303ca001c2e5d34c75fa3859ed57114dc20c
fetched_at: '2026-06-29T00:11:33.937057+00:00'
page_id: '763246572'
product: rm
source: tdn-rm
title: 1.0 - Pré-requisito.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=763246572
version: 4
---

**O Portal de Pesquisa Pública do TOTVS Gestão Bibliotecária está disponível a partir da versão 12.1.2306**

O portal de pesquisa pública faz uso de api's para buscar e armazenar informações, o controle destas APIs é feito pelo host. Para que o portal funcione corretamente é necessário expor as APIs para web, desta maneira é necessário o uso do módulo URL Rewrite do IIS para que este módulo filtre as solicitações e encaminhe para o host as solicitações que sejam para a API.

É necessário instalar o URL Rewrite e o ARR (Application Request Routing) no IIS.

ARR (Application Request Routing)

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do ARR**:  <https://www.microsoft.com/en-us/download/details.aspx?id=47333> 

Avisos

1. **A instalação deve ser realizada apenas uma vez para cada IIS.**
2. **Após finalizar a instalação** ARR(Application Request Routing)**, deverá ser habilitado a propriedade "Enable proxy"**
URL Rewrite

A instalação deve ser realizada no servidor do portal desejado.

Atenção

**A partir da versão 12.1.2402: é** possível utilizar as api's do host diretamente, sem o uso do módulo do **URL** **Rewrite**. Para isso deve expor o host para a web e informar o endereço do host nos arquivos de config dos portais.

**Importante** ficar atento a questões de **segurança** ao expor o host para a web. A forma como será utilizado fica a critério da instituição.

0.1tempfadeInstalaçãofade

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do URL Rewrite**: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após a Instalação, será criado um ícone: “URL Rewrite” no IIS

Configuração Rewritefade

Deve ser necessário configurar **duas** regras para o **URL** **Rewrite***:*

* A 1º regra **(regra comum para todas as versões)** é utilizada para direcionamento de **API** onde não é necessário passar o alias selecionado;
* A 2º regra **(apenas para versões anteriores à 12.1.2402)** é utilizada para as **API** onde é necessário passar o alias selecionado.

Avisos

1. A ordem das regras deve ser respeitada.
2. A configuração deve ser realizada **exclusivamente** nos portais: **Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor** e em: **Sites | Default Web Site | FrameHTML | Web | App |Edu | 'Pasta referente ao portal'.** Caso a configuração **não** seja realizada no caminho especificado anteriormente, o portal do Aluno poderá ser impactado.
Regra comum para todas as versões

**1.**Acessar o IIS -> Ir no aplicativo que está sendo configurado (Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor) -> URL *Rewrite*

**2.** Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule**.*

**3.** No campo "**Name**" informar um nome para a regra que está sendo criada

**4.** Na opção: Match URL, no campo: "**Pattern"** inserir as informação: api/(.\*)

**5.** Na opção*: "**Actions"**, no campo: Rewrite URL informar o link: [http://nome\_da\_maquina\_do\_host:porta/api/{R:1](http://localhost:8052/%7BR:1)}*

Regra adicional necessário para versões anteriores a 12.1.2402

**Para as versões anteriores à 12.1.2402** é necessário configurar uma nova regra.

Atenção

A porta utilizada deve ser a mesma que está configurada na chave "ApiPort" no arquivo de host **RM.Host.Service.exe.config**.

**1.** Acessar o IIS -> Ir no aplicativo que está sendo configurado (**Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor**) -> URL *Rewrite*

**2.** Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule**.*

**3.** No campo "**Name**" informar um nome para a regra que está sendo criada

**4.** Na opção: Match URL, no campo: "**Pattern**" inserir as informação: aliasname\.(.\*)/api/(.\*)

**5.**Na opção*: "**Actions"**, no campo: Rewrite URL informar o link: [http://{R:1}.nome\_da\_maquina\_do\_host:porta/api/{R:](http://localhost:8052/%7BR:1)2}*

**6.**Marcar a opção*: "**Stop processing of subsequent rules"***
