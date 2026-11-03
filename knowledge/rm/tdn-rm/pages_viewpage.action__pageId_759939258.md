---
content_hash: e113713a9d98b3040a9d03a3c132a6bd1c854f46763782a801d6092b41622939
fetched_at: '2026-06-29T00:11:33.437963+00:00'
page_id: '759939258'
product: rm
source: tdn-rm
title: Novo serviço do TOTVS Update
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=759939258
version: 37
---

# Índice

---

2.\*ndice

# Introdução

---

        A partir da versão 12.1.2402, foi disponibilizado um novo serviço externo para o TOTVS Update (Servidor de Atualização) que será responsável por fazer a atualização dos ambientes Smart de forma mais rápida e isolada do RM.Host. O novo serviço conta com uma melhor gerenciamento do download dos arquivos reduzindo a leitura em disco e é capaz de suportar mais conexões que o antigo proporcionando uma atualização mais rápida e eficiente.

# Distribuição

---

       Este novo serviço é instalado junto com o RM, porém é um aplicativo isolado do RM.Host, seu executável se encontra na pasta **rm-update**da instalação padrão.   
Ele pode ser utilizado  ou .

# Arquivo de configuraçãoconfig-file

---

Na pasta **rm-update** fica o arquivo **appsettings.json**, que define as configurações da aplicação.

Exemplo de arquivo:

appsettings.jsontrue

Propriedade de configuração:

* **UseCompression:** Ativa ou desativa a compactação de resposta. Ativado pode reduzir o tamanho da resposta e aumentar capacidade de performance do serviço.
* **Logging:** Propriedades de registro de Log padrão do .Net, Veja mais informações:   
  <https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-6.0>  
  <https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-6.0#llvl>
* **AllowedHosts:** Configuração de uma lista de Host permitidos para acessar o Totvs Update. Lista separada por ponto e vírgula de nomes de host sem número de porta.
* **UseSwagger:** Ativa ou desativa a página de documentação de APIs, [http://localhost:5000/swagger](http://localhost:5010/swagger/index.html)
* **Update**
  + **BasePath**: É o caminho para a pasta base do RM, de onde os arquivos de atualização serão obtidos.   
    Este é o local principal onde deverá ter a versão mais recente do RM, que será utilizada como base de atualização.
  + **CacheEnabled**: Ativa ou desativa o gerenciamento de cache do serviço de atualização. Ativado poderá reduzir a quantidade de leitura em disco e reduzir o tempo total de atualização.
  + **SubDomainMask**: responsável por realizar a tenantização dos serviços do RM detalhes [Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=851282781)
  + **ApiPort**: Porta utilizada para expor serviços de API do RM
* **Kestrel.Endpoints**
  + **Http**
    - **Url**: Configuração de endereço do Servidor de Atualização e porta http, não seguro. Como padrão, 5000 (*http*).
  + **Https**
    - **Url**: Configuração de endereço do Servidor de Atualização e porta https, seguro. Padrão, 5001 (*https*).

O ambiente configurado na propriedade **BasePath**, deve ser um ambiente isolado.  
Não pode ser um Host (Ambiente Server) e no seu arquivo **RM.Host.Service.exe.config**, não deve possuir a propriedade UpdateServerEnabled=true.

Atenção!

Também é importante deixar claro que a máquina ou diretório onde estará o "Servidor de Atualização", não pode ser um "Servidor de Aplicação" que também será atualizado. Ele deve ser um ambiente isolado dos demais servidores de aplicação e clientes.

# Configurando ambiente Client

---

      Para que o RM.exe utilize o novo serviço de atualização, seu endereço deverá ser configurado no RM.exe.config

Alterar a tag ***UpdateServer**,* no **RM.exe.config** com o endereço, seguindo este formato: *<protocolo>://<endereço-do-host>:<porta>*, ([http://localhost:500](http://localhost:5001)0), como no exemplo abaixo:

xmlRM.exe.configtrue
















]]>

      Essa configuração pode ser feita diretamente no *RM.exe.config* do Host "Servidor de Atualização", assim, na próxima atualização automática o arquivo *\*.config* será atualizado e as máquinas clientes já passarão a utilizar o novo endereço.

# Configurando ambiente Server

---

      Para que o RM Host em um ambiente server utilize o novo serviço de atualização, seu endereço deverá ser configurado no RM.Host.Service.exe.config

Alterar a tag ***UpdateServer**,* no **RM.Host.Service.exe.config** com o endereço, seguindo este formato: *<protocolo>://<endereço-do-host>:<porta>*, ([http://localhost:500](http://localhost:5001)0), como no exemplo abaixo:

xmlRM.Host.Service.exe.configtrue



















]]>

Este ambiente server não pode ser o mesmo que foi configurado no arquivo **appsettings.json,** pasta **rm-update**, na propriedade **BasePath**.  
E em seu arquivo **RM.Host.Service.exe.config**, deve possuir a propriedade UpdateServerEnabled=true para que seja gerado o arquivo \_Update.dat.

 

Atenção!

O arquivo *\_update.dat* foi evoluído para que o novo serviço também o utilize. Sendo assim, o novo serviço deve ser iniciado após a inicialização completa do RM.Host do ambiente utilizado como "Servidor de Atualização".

# Utilizando como aplicativoas-app

---

Ao executar "RM.UpdateManager.Runtime.exe" serão utilizadas as portas configuradas (os padrões são 5000 para *http* e 5001 para *https*).   
Estas portas, assim como a *url*, podem ser alteradas no arquivo de configuração, conforme a seção .

Quando o aplicativo executar será exibido um console, informando o nome do host configurado e exposto, como o exemplo abaixo:

# Utilizando como serviçoas-service

---

     O novo TOTVS Update pode ser utilizado em um sistema operacional Windows ou Linux, veja abaixo como configurar cada um.

## Serviço no Windows

Para subir o TOTVS Update como serviço no Windows, basta criar um serviço que aponta para o executável *RM.UpdateManager.Runtime.exe*.   
Exemplo de comando que pode ser utilizado:

powershell

Com o serviço criado, e as configurações corretas, basta iniciar o serviço:

Para que o serviço funcione corretamente, é necessário que o usuário do serviço possua permissões necessárias de acesso a disco, e caso seja utilizado o protocolo **HTTPS**, também tenha acesso ao certificado instalado na máquina. Caso contrário, o serviço não irá subir corretamente.

## Serviço no Linux

O TOTVS Update é compatível com sistemas operacionais baseados em Linux, permitindo uma aplicação eficiente e integrada a esta plataforma.

Para implementar o TOTVS Update Manager no Linux como um serviço, siga as instruções detalhadas abaixo. Este processo assegura que o serviço seja configurado corretamente e funcione de maneira otimizada.

     Criar o arquivo de serviço, utilizando o comando a seguir:

bash

     Neste arquivo criado, insira o conteúdo a seguir, modificando os parâmetros do serviço, especificamente o ****WorkingDirectory**** (diretório que contém o *RM.UpdateManager.Runtime*) e o **ExecStart** (caminho absoluto para o arquivo *RM.UpdateManager.Runtime*):

Pela diretiva do Linux, não é recomendado que arquivo de serviço fique em uma pasta a partir do diretório */home*, pois em muitas distribuições tal caminho não é permitido para a utilização como serviço.

updatemanager.service

Salve o arquivo utilizando as teclas: CTRL+X, Y para confirmar, e em seguida, pressione *Enter*.

Habilite e Inicie o Serviço:

bash

A partir deste momento, o serviço já está de pé e rodando.

### Comandos para manutenção do serviço no Linux

Para verificar o status do serviço, a qualquer momento o seguinte comando pode ser utilizado:

bash

E para visualizar os logs do serviço, o seguinte comando pode ser utilizado:

bash

Para atualizar o serviço:

bash

E para parar o serviço:

bashfalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2402 ou superiores

false

**Processo:** TOTVS Update

falsefalse

**Status:** Finalizado

false

**Data:** 28/11/2023

false

**Autores:**
