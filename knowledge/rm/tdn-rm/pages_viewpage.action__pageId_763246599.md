---
content_hash: b9a9648dc7342c162d245082710101c38986c23c3ad8885d36dc2db69c86b84a
fetched_at: '2026-06-29T00:11:33.942489+00:00'
page_id: '763246599'
product: rm
source: tdn-rm
title: 2.0 - Configuração Portal de Pesquisa pública
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=763246599
version: 16
---

## **01.****CONFIGURAÇÃO**

Após configurar o servidor conforme o item de [pré-requisito](https://tdn.totvs.com/x/0zzqMQ), é necessário configurar o arquivo de configuração no Portal da Pesquisa Pública. Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador do Portal da Pesquisa Pública. “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalBiblioteca\config\”.

No arquivo, as seguintes configurações são possíveis:

#### Parâmetro **apiServer**

Deve ser configurado com o mesmo endereço utilizado para acessar o portal. Essa configuração é utilizada para fazer o redirecionamento para a API que será feito pelo módulo URL Rewrite do IIS.

O endereço parametrizado deve conter o endereço público do portal. Exemplo: [http://instituicao.br/FrameHTML/web/app/edu/portalbiblioteca](http://instituicao.br/FrameHTML/web/app/edu/portaldoprofessor)

#### Parâmetro **basePath**

Deve ser configurado com o mesmo caminho relativo utilizado no portal conforme imagens abaixo.

#### Parâmetro **defaultAlias**

Deve ser configurado com o alias padrão utilizado para fazer o acesso a base de dados. Este alias deve estar cadastrado no arquivo alias.dat.

## **02.****CONFIGURAÇÃO PARA MULTI -TENANCY**

Otimizado o sistema para que seja possível configurar o portal de pesquisa pública para o Multi-Tenancy.

Para realizar a configuração, realizar os passos:

false10.11º - Configurar os Domínios no IISfade

1. Acessar o IIS | Sites | Default Web Site | Associações

O IIS, irá  abrir uma janela para que seja informado os alias e os domínios.

Informe o **alias.seu\_site** conforme a imagem abaixo.

Após realizar a configuração, reiniciar o IIS

0.12º - Configuração do Configfade

Após realizar o 1° passo, realizar a parametrização no RM.Host.

* Acessar o RM.Host.Service.exe.config (Se o cliente utilizar o Host Service) ou  RM.Host.exe.config (Se o cliente utilizar o Host local)  na Pasta: Totvs\RM.Net\Bin da versão e inserir as chaves:

      <add key="ApiPort" value="porta\_definida\_no\_rewrite (IIS)" />  
      <add key="DefaultDB" value="informe\_aqui\_o\_nome\_do\_alias" />  
      <add key="SubDomainMask" value="[ALIAS].domínio\_parametrizado\_no\_IIS" />

0.13º - Configuração do arquivo JSONfade

Após configurar o RM.Host,  é necessário configurar o arquivo de configuração no Portal de Pesquisa pública. Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador de Pesquisa pública. “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalBiblioteca\config\”.

No arquivo, as seguintes configurações são possíveis:

0.13º - URL do Portal de Pesquisa Públicafade

Após as configurações, acessar o novo portal através do link: [http://ALIAS.domínio\_parametrizado\_no\_IIS/FrameHTML/web/app/Edu/PortalBiblioteca/](http://localhost/FrameHTML/web/app/Edu/PortalDoProfessor/)[#/?c=*(InformarColigada)*&f=](http://localhost/FrameHTML/web/app/Edu/PortalBiblioteca/#/?c=1&f=1&b=5)*[(InformarFilial)&b=](http://localhost/FrameHTML/web/app/Edu/PortalBiblioteca/#/?c=1&f=1&b=5)**[(InformarIUnidadeBibliotecária)](http://localhost/FrameHTML/web/app/Edu/PortalBiblioteca/#/?c=1&f=1&b=5)*

Para mais informação sobre o Multitenant, clique [aqui](https://tdn.totvs.com/x/9XwcEQ).
