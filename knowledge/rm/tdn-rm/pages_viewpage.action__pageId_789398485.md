---
content_hash: a5db39bcfe70312e1c1c0dc834a4394032743839653e78cea0c4fcafc327bf7d
fetched_at: '2026-06-29T00:11:39.277746+00:00'
page_id: '789398485'
product: rm
source: tdn-rm
title: 01. Pré-requisitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789398485
version: 38
---

Para o perfeito funcionamento do Meu eduCONNECT é necessário que alguns pré-requisitos sejam atendidos. São eles: instalação e configuração do TOTVS Educa Mobile e TOTVS Educacional nas releases:

* **12.1.2402.297** ou superior,
* **12.1.2406.270** ou superior,
* **12.1.2410.222** ou superior,
* **12.1.2502.138** ou superior
* **12.1.2506.xxx** ou superiores (qualquer patch)

Versões mínimas de sistema operacional dos dispositivos móveis onde o Meu eduCONNECT será instalado. Veja a seguir mais detalhes nos itens 01.1 e 01.2.

O aplicativo já se encontra disponível para uso em Tablets (Android e IOS).

IMPORTANTE

A configuração do URL Rewrite é **OBRIGATÓRIA**, caso contrário, o usuário poderá ter um erro de falha de autenticação.  
Revise, caso seja necessário, a correta parametrização do URL Rewrite conforme descrito itens abaixo.

IMPORTANTE - Dispositivos iOS 14 ou superior

A partir da versão **08.2506.07**, para que o usuário consiga realizar o **check-in da aula**, é necessário conceder permissão ao recurso **App Tracking Transparency**, disponível a partir do **iOS 14** ou superior.

Após o login no aplicativo, será exibida a solicitação de permissão conforme a mensagem abaixo. O usuário deverá selecionar a opção **"Permitir" (Allow)** para prosseguir com o acesso.

OBS: Além disso, o usuário também deve conceder permissão de **acesso à localização** para que o **check-in da aula** funcione corretamente.

## **01.1 - INTEGRAÇÃO COM TOTVS EDUCA MOBILE**

Para acesso às informações acadêmicas e financeiras, o Meu eduCONNECT traz embarcado consigo o  TOTVS Educa Mobile. Portanto, para o perfeito funcionamento dessas funcionalidades dentro do aplicativo,  é necessário que o TOTVS Educa Mobile esteja devidamente instalado. Clique [aqui](http://tdn.totvs.com/x/n5ntEw) e consulte a documentação do TOTVS Educa Mobile.

## **01.2 - VERSÕES RECOMENDADAS DE SISTEMA OPERACIONAL**

As **versões recomendadas de sistema operacional**, que contam com **suporte da TOTVS para o correto funcionamento do Meu eduCONNECT**, estão alinhadas às versões que **oficialmente ainda recebem atualizações de segurança** pelos respectivos fabricantes (Android e Apple).

Atualmente, são suportadas as seguintes versões:

* **Android:** versões **Android 13.0 ou superiores**
* **iOS:** versões **iOS 15.8.x ou superiores**

Informações técnicas podem ser obtidas clicando [aqui](https://developer.android.com/distribute/best-practices/develop/target-sdk).

Aviso importante

O aplicativo Meu eduCONNECT **não funcionará** em dispositivos com o modo desenvolvedor habilitado ou que tenham sido submetidos a processo de jailbreak. Recomendamos desativar o modo desenvolvedor e evitar o jailbreak do seu dispositivo para garantir a estabilidade e segurança do aplicativo.

## **01.3 - CONFIGURAÇÃO DO ARR (Application Request Routing)**

A instalação deve ser realizada no servidor IIS do Educa Mobile a ser utilizado pelo Meu eduCONNECT.

**Link para download do ARR**:  <https://www.microsoft.com/en-us/download/details.aspx?id=47333> 

Apenas uma vez para cada IIS

**A instalação deve ser realizada apenas uma vez para cada IIS.**

Habilitar o proxy

Após finalizar a instalação **ARR (Application Request Routing),** deverá ser **habilitado** a propriedade **"Enable proxy"**

## **01.4 - CONFIGURAÇÃO DO URL Rewrite:**

URL Rewrite0.1Instalaçãofade

**1.**Acessar o IIS (como administrador) | Clicar na opção: "Obter Novos Componentes Web Plataform"

**2.**Em seguida, será habilitado uma tela, onde serão carregados as plataformas Web.

**3.**Pesquisar por “URL Rewrite” e clicar na opção: Add:

**4.**Após a Instalação, será criado um ícone: “URL Rewrite” no IIS

0.1Configuração do URL Rewritefade

**1.**Acessar o IIS -> Ir no aplicativo do EducaMobile -> URL Rewrite

**2.**Dar um duplo click no ícone URL Rewrite e em seguida clicar em: Adicionar uma *Rule* do tipo *Inboud Rule.*

## Inserir as informações:

**3.**No campo "**Name**" informar o endereço:  TOTVS\_API\_ReverseProxyInboundRule

**4.**Na opção: Match URL, no campo: "**Pattern"** inserir as infirmação: (.\*)

**5.**Na opção: "**Conditions"**, clicar no botão: Add. e inserir a informação:

{REQUEST\_URI}  /api/(.\*)

**6.**Na opção: "**Actions"**, no campo: Rewrite URL informar o link: <http://localhost:8052/{R:1>}

**Importante**:

* A URL a ser utilizada é a do servidor onde encontra-se instalado o Host, como exemplo, utilizamos o endereço [http://IPdoServidorHost:8052/{R:1](http://localhost:8052/{R:1)} 
  + Em alguns casos o servidor do Host é dirente do servidor Web, então neste caso, deve-se utilizar o endereço do servidor do Host.
* Verificar a porta configurada na tag ApiPort do arquivo de configuração do Host, como exemplo, utilizamos a porta 8052.

Verificar qual é a parte da URL {R:1} 

Utilizar o endereço [**http://EnderecodoServidorWeb/EducaMobile**](http://app.ibeu.org.br/EducaMobile/api/framework/v1/menus/dd6626a5aa1e3c2c2ad79198824f67a4?$filter=tagMenu)[/api/framework/v1/menus/dd6626a5aa1e3c2c2ad79198824f67a4?$filter=tagMenu](http://app.ibeu.org.br/EducaMobile/api/framework/v1/menus/dd6626a5aa1e3c2c2ad79198824f67a4?$filter=tagMenu) eq '808100759'&companyId=1

**7.**Em seguida, clicar no botão: Aplicar

Será apresentado a mensagem: As alterações foram salvas com êxito.

0.1Configuração do Configfade

* Acessar o RM.Host.Service.exe.config (Se o cliente utilizar o Host Service) ou  RM.Host.exe.config (Se o cliente utilizar o Host local)  na Pasta: Bin da versão e inserir as chaves:

<add key="ApiPort" value="Porta definida no Host" />  
<add key="DefaultDB" value="CorporeRM" />
