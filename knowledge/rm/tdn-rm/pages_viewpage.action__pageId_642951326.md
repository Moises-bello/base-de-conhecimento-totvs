---
content_hash: 0ecdbe8530dae151545b2b804acf6213de532e468fc7fbc7e1e25fe619b30009
fetched_at: '2026-06-29T00:11:10.245591+00:00'
page_id: '642951326'
product: rm
source: tdn-rm
title: 01 - Pré-requisitos após a instalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642951326
version: 3
---

false0.21fade1º - Instalar e configurar o Application Request Routing (ARR)

## 1° - Instalar e configurar o "Application Request Routing" (ARR)

**Caso tenha instalado e configurado o Application Request Routing (ARR) para o Novo Portal do professor ou Portal Gestão Educacional, não é necessário realizar esse processo.**

Realizar o download do ARR no link  <https://www.microsoft.com/en-us/download/details.aspx?id=47333>. 

1- Acessar o IIS, selecionar a Guia principal e dar um duplo click sobre o ícone: Application Request Routing (ARR)

Será habilitado a opção: **Ações | Abrir Proxy**

Será habilitado algumas opções, e clicar no link: **Proxy | Server Proxy Settings**

Marcar o Checkbbx: Enable proxy e em seguida, clicar em aplicar.

2º - Instalar e configurar o URL Rewrite

## 2° - Instalar e configurar o URL Rewrite

0.1tempfadeInstalaçãofade

**Caso tenha instalado o Rewrite para o Novo Portal do professor ou Portal Gestão Educacional, não é necessário realizar esse processo.  
Será necessário realizar apenas a configuração para o Portal Gestão Educacional (Ir para a Aba: Configuração Rewrite).**

**1.**Acessar o IIS (como administrador) | Clicar na opção: "Obter Novos Componentes Web Plataform"

**2.**Em seguida, será habilitado uma tela, onde serão carregados as plataformas Web.

**3.**Pesquisar por “URL Rewrite” e clicar na opção: Add:

**4.**Após a Instalação, será criado um ícone: “URL Rewrite” no IIS

Configuração Rewritefade

O Portal E-commerce de cursos utiliza três regras para o rewrite, onde a primeira é utilizada para direcionamento de api's onde não é necessário passar o alias selecionado, a segunda é utilizada para as api's onde é necessário passar o alias selecionado e a terceira regra, onde é utilizando a comunicação entre o Portal Gestão Educacional e o app Meu eduCONNECT .Segue a configuração das três regras:

#### 1- URL

* Campo: **Partten** : aliasname\.(.\*)/api/(.\*)
* Campo: **Rewrite UR**L: http://{R:1}.informe\_aqui\_o\_nome\_da\_máquina:informe\_a\_apiport/api/{R:2}

Exemplo: http://{R:1}.192.168.98.34:8052/api/{R:2}

#### 2- API

* Campo: **Partten** : api/(.\*)
* Campo: **Rewrite UR**L:  [http://informe\_aqui\_o\_nome\_da\_máquina:informe\_a\_apiport/api/{R:1](http://informe_aqui_o_nome_da_máquinaPorta_API)}

Exemplo: <http://192.168.98.34:8052/api/{R:1>}

Atenção

A porta utilizada deve ser a mesma que está configurada na chave "ApiPort" no arquivo de host (RM.Host.Service.exe.config, se utilizar o Host Service e RM.Host.exe.config, se utilizar o Host local). Ver a aba **Configurações do config.**A ordem das regras deverão ser respeitadas.

Configuração do configfade

* Acessar o RM.Host.Service.exe.config (Se o cliente utilizar o Host Service) ou  RM.Host.exe.config (Se o cliente utilizar o Host local)  na Pasta: Totvs\RM.Net\Bin da versão e inserir as chaves:

 <add key="ApiPort" value="porta\_definida\_no\_rewrite (IIS)" />

      <add key="DefaultDB" value="informe\_aqui\_o\_nome\_do\_alias" />

      <add key="SubDomainMask" value="[ALIAS].nome\_da\_máquina\_do\_host" />

Atenção

Para a opção "SubDomainMask", o nome da máquina deve ser inserido todo utilizando letras **minúsculas**. O texto [ALIAS] **não deve ser alterado**, deve ser inserido o texto desta forma, o que deve ser alterado é o "nomeDaMaquinaDoHost". Exemplo: a máquina do host possui o nome de ServerXYZ, desta forma, deve ser inserido o texto [ALIAS].serverxyz.

false

Em servidor publicado, na TAG: "SubDomainMask" utilizar o DNS.

false

Se utilizar do rm.host, atentar para executa-lo como administrador.

Se utilizar o host.service, o usuário associado ao serviço tem que ter permissão para acessar a porta da API definida no URL Rewrite.
