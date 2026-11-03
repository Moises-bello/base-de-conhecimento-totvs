---
content_hash: 04f2cb795c3daa4da0e6ad133a11f549833b4de08084c6369bdd324804859b6f
fetched_at: '2026-06-29T00:11:10.253877+00:00'
page_id: '642951377'
product: rm
source: tdn-rm
title: 03 - Configuração no ambiente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642951377
version: 5
---

false1Configuração: Local21º - Configuração do arquivo JSON

Após configurar o IIS conforme o item de [01 - Pré-requisitos após a instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=642951326) é necessário ajustar o arquivo de configuração do Portal E-commerce de cursos.

Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador do Portal E-commerce de cursos:  “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalEcommerceCurso\config”.

No arquivo, alterar as informações a seguir:

* "apiServer": "[http://informe\_o\_nome\_do\_servidor\_onde\_esta\_configurado\_o\_IIS:i](http://localhost:8052)nforme\_a\_porta\_API",
* "defaultAlias": "infome\_o\_nome\_do\_Alias",
* "multitenant": false (Altera para TRUE, se utilizar MultiTenacy
* "subDomainMask": "[ALIAS].informe\_o\_nome\_do\_servidor",

##### Exemplo após a configuração

2º - URL do Portal Gestão Educacional

Após as configurações, acessar o novo portal através do link: [http://Local\_de\_Instalação/FrameHTML/web/app/Edu/PortalEcommerceCurso/#/home?c=1&f=1](http://Local_de_Instalação/FrameHTML/web/app/Edu/PortalGestaoEducacional/)

Configuração: Multi - Tenancy41º - Configurar os Domínios no IIS

1. Acessar o IIS | Sites | Default Web Site | Associações

O IIS, irá  abrir uma janela para que seja informado os alias e os domínios.

Informe o nome do host sendo **alias**.**seu\_site** conforme a imagem abaixo.

Após realizar a configuração, reiniciar o IIS

2º - Configuração do arquivo JSON

Após configurar o RM.Host,  é necessário configurar o arquivo de configuração no Portal do Professor. Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador do Portal do Professor. “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalGestãoEducacional\config\”.

No arquivo, alterar as informações a seguir:

Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador do Portal E-commerce de cursos:  “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalEcommerceCurso\config”.

No arquivo, alterar as informações a seguir:

* "apiServer": "[http://informe\_o\_domínio\_informado\_no\_IIS:](http://localhost:8052)Porta(API)\_definida\_no\_rewrite",
* "defaultAlias": "infome\_o\_nome\_do\_Alias",
* "multitenant": false (Altera para True)
* "subDomainMask": "[ALIAS][informe\_o\_domínio\_informado\_no\_IIS](http://localhost:8052)",

3º - URL do Portal Gestão Educacional

Após as configurações, acessar o novo portal através do link: [http://**Domínio\_parametrizado\_no\_IIS**/FrameHTML/web/app/Edu/PortalEcommerceCurso/#/home?c=1&f=1](http://localhost/FrameHTML/web/app/Edu/PortalDoProfessor/)
